// Cloudflare Pages Function: zonorah.com/platform y /platform/… -> la plataforma de Zonorah.
// Sin ella, Pages respondería con la portada a cualquier ruta que no existe como archivo.
import { proxy } from "../_app.js";

export async function onRequest({ request }) {
  return proxy(request, "/platform");
}
