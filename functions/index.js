// Cloudflare Pages Function para la portada (/).
//
// La portada siempre se sirve: antes redirigía a /datos/ a quien tenía sesión,
// y eso hacía que la app pareciera otro sitio. Ahora zonorah.com y la app
// comparten menú y se puede ir de una a otra sin que nada redirija solo.
export async function onRequestGet({ next }) {
  return next();
}
