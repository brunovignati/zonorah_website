// Cloudflare Pages Function: zonorah.com/datos y /datos/… -> datos.zonorah.com.
//
// El sitio se sirve con Cloudflare Pages, que no usa el Worker de src/ (ese
// queda por si el sitio pasa a Workers). Pages ejecuta esta función para
// cualquier ruta bajo /datos; el resto del sitio sigue siendo estático.
// Sin ella, /datos devolvía la portada: Pages responde con index.html a
// cualquier ruta que no existe.
const ORIGEN = "https://datos.zonorah.com";

export async function onRequest({ request }) {
  const url = new URL(request.url);
  if (url.pathname === "/datos") {
    return Response.redirect(`${url.origin}/datos/${url.search}`, 301);
  }
  const destino = new URL(url.pathname.slice("/datos".length) + url.search, ORIGEN);
  const peticion = new Request(destino, request);
  const ip = request.headers.get("CF-Connecting-IP");
  if (ip) peticion.headers.set("X-Forwarded-For", ip);
  try {
    const r = await fetch(peticion, { redirect: "manual" });
    if (r.status >= 520) return fueraDeLinea();
    return r;
  } catch {
    return fueraDeLinea();
  }
}

function fueraDeLinea() {
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
