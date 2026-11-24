// zonorah.com/datos fue la dirección de la plataforma; ahora es zonorah.com/platform.
// Las páginas van con un 301 a la dirección nueva (enlaces viejos, favoritos). La API sigue
// pasando por aquí para que una pestaña que ya estaba abierta no se rompa a mitad de sesión.
import { proxy } from "../_app.js";

export async function onRequest({ request }) {
  const url = new URL(request.url);
  if (url.pathname.startsWith("/datos/api/")) return proxy(request, "/datos");
  const resto = url.pathname.slice("/datos".length);
  return Response.redirect(`${url.origin}/platform${resto || "/"}${url.search}`, 301);
}
