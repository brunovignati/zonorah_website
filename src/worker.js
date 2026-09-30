// zonorah.com/datos/… -> la app de datos de Zonorah (datos.zonorah.com).
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
    if (url.pathname === "/datos") {
      return Response.redirect(`${url.origin}/datos/${url.search}`, 301);
    }
    if (!url.pathname.startsWith("/datos/")) {
      return env.ASSETS.fetch(request);
    }
    const destino = new URL(url.pathname.slice("/datos".length) + url.search, ORIGEN);
    const peticion = new Request(destino, request);
    // La IP de quien pregunta, para los límites de uso de la app.
    const ip = request.headers.get("CF-Connecting-IP");
    if (ip) peticion.headers.set("X-Forwarded-For", ip);
    try {
      const r = await fetch(peticion, { redirect: "manual" });
      if (r.status >= 520) return fuera_de_linea();
      return r;
    } catch {
      return fuera_de_linea();
    }
  },
};

function fuera_de_linea() {
  return new Response(
    `<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Zonorah · Datos</title>
<body style="margin:0;background:#163300;color:#fff;font:17px/1.6 system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;padding:16px">
<div style="max-width:32em"><p style="color:#9FE870;font-weight:900;letter-spacing:.28em">ZONORAH</p>
<h1 style="font-size:26px">Los datos no están disponibles en este momento</h1>
<p style="color:#C3D9B4">El servicio de datos se está reiniciando o no tiene conexión. Vuelve a intentarlo en unos minutos.</p>
<p><a href="/" style="color:#9FE870">Volver a zonorah.com</a></p></div></body></html>`,
    { status: 503, headers: { "Content-Type": "text/html; charset=utf-8", "Retry-After": "120" } },
  );
}
