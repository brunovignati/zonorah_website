// Cloudflare Pages Function para la portada (/).
//
// Como en las apps con «sitio» y «app» separados: quien ya entró con su
// cuenta no ve la portada, va directo a la app (/datos/: chat y aprende).
// La sesión es la cookie que pone la app de datos al entrar con Google por
// zonorah.com/datos; aquí solo se pregunta a la app si sigue viva. Si la app
// no responde, se sirve la portada como siempre.
const APP = "https://datos.zonorah.com/api/sesion";

export async function onRequestGet({ request, next }) {
  const galleta = request.headers.get("Cookie") || "";
  if (/(?:^|;\s*)zonorah_sesion=[^;]+/.test(galleta)) {
    try {
      const r = await fetch(APP, { headers: { Cookie: galleta } });
      if (r.ok && (await r.json()).usuario) {
        return new Response(null, {
          status: 302,
          headers: { Location: new URL("/datos/", request.url).toString(), "Cache-Control": "no-store" },
        });
      }
    } catch { /* la app no responde: portada */ }
  }
  return next();
}
