// zonorah.com/platform/… -> la app de datos de Zonorah (datos.zonorah.com).
//
// El sitio sigue siendo estático: este Worker solo interviene en /datos
// (lo fija `run_worker_first` en wrangler.jsonc). Todo lo demás lo sirve
// Cloudflare desde ./public, como antes.
//
// La app de datos corre en el Mac de Zonorah y llega a Cloudflare por un
// túnel; aquí no hay datos, ni claves, ni lógica: solo el reenvío. Si el Mac
// está apagado, /datos responde con un aviso en vez de un error de Cloudflare.
const ORIGEN = "https://datos.zonorah.com";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/platform") {
      return Response.redirect(`${url.origin}/platform/${url.search}`, 301);
    }
    if (!url.pathname.startsWith("/platform/")) {
      return env.ASSETS.fetch(request);
    }
    const destino = new URL(url.pathname.slice("/platform".length) + url.search, ORIGEN);
    const peticion = new Request(destino, request);
    // La IP de quien pregunta, para los límites de uso de la app.
    const ip = request.headers.get("CF-Connecting-IP");
    if (ip) peticion.headers.set("X-Forwarded-For", ip);
    try {
      const r = await fetch(peticion, { redirect: "manual" });
      if (r.status >= 520) return fuera_de_linea(request);
      return conRobots(r);
    } catch {
      return fuera_de_linea(request);
    }
  },
};

// La app no se indexa: todo su contenido está en la portada (/, /es/, /id/). `noindex` evita
// copias duplicadas y versiones de idioma mezcladas (la app se traduce en el navegador);
// `follow` deja que se sigan sus enlaces.
function conRobots(r) {
  const h = new Headers(r.headers);
  h.set("X-Robots-Tag", "noindex, follow");
  return new Response(r.body, { status: r.status, statusText: r.statusText, headers: h });
}

const AVISO = {
  en: { t: "Data is not available right now", p: "The data service is restarting or has no connection. Please try again in a few minutes.", a: "Back to zonorah.com", h: "/" },
  es: { t: "Los datos no están disponibles en este momento", p: "El servicio de datos se está reiniciando o no tiene conexión. Vuelve a intentarlo en unos minutos.", a: "Volver a zonorah.com", h: "/es/" },
  id: { t: "Data tidak tersedia saat ini", p: "Layanan data sedang dimulai ulang atau tidak terhubung. Silakan coba lagi dalam beberapa menit.", a: "Kembali ke zonorah.com", h: "/id/" },
};

// Idioma del aviso: ?lang= > cookie zonorah_lang > inglés (el idioma por omisión).
function idiomaDe(request) {
  const url = new URL(request.url);
  const q = url.searchParams.get("lang");
  if (q in AVISO) return q;
  const c = /(?:^|;\s*)zonorah_lang=(en|es|id)/.exec(request.headers.get("Cookie") || "");
  return c ? c[1] : "en";
}

function fuera_de_linea(request) {
  const lang = idiomaDe(request);
  const a = AVISO[lang];
  return new Response(
    `<!doctype html><html lang="${lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Zonorah · Data</title>
<body style="margin:0;background:#163300;color:#fff;font:17px/1.6 system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;padding:16px">
<div style="max-width:32em"><p style="color:#9FE870;font-weight:900;letter-spacing:.28em">ZONORAH</p>
<h1 style="font-size:26px">${a.t}</h1>
<p style="color:#C3D9B4">${a.p}</p>
<p><a href="${a.h}" style="color:#9FE870">${a.a}</a></p></div></body></html>`,
    { status: 503, headers: { "Content-Type": "text/html; charset=utf-8", "Retry-After": "120" } },
  );
}
