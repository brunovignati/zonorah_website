# zonorah_website

Sitio público de **zonorah.com**. Cloudflare construye y sirve desde
este repositorio: cada `push` a `main` despliega la web.

## Estructura

| Ruta | Qué es |
|---|---|
| `build/content.py`, `build/build.py` | La fuente de la portada y su generador (ver «Idiomas») |
| `public/index.html`, `public/es/`, `public/id/` | Las portadas generadas (no editar a mano) |
| `public/og.png`, `sitemap.xml`, `llms.txt` | Imagen para redes y archivos para buscadores e IA |
| `public/_headers` | Cabeceras de seguridad y caché |
| `public/robots.txt` | Indexación abierta + referencia al sitemap |
| `wrangler.jsonc` | Configuración de Cloudflare: qué carpeta publicar y qué rutas pasan por el Worker |
| `functions/_app.js` | El proxy hacia la plataforma (datos.zonorah.com). Nada más |
| `functions/platform/[[ruta]].js` | Cloudflare Pages: `/platform/…` va a la plataforma |
| `functions/datos/[[ruta]].js` | La dirección antigua: las páginas redirigen (301) a `/platform`; `/datos/api/` sigue pasando |
| `src/worker.js` | Lo mismo que `/platform`, por si el sitio pasa de Pages a Workers |

Solo se publica el contenido de `public/`. Todo lo que esté fuera de esa
carpeta (este README, la configuración) no acaba en la web.

## Publicar un cambio

```bash
cd ~/zonorah-web
# editar public/index.html
git add -A && git commit -m "descripción del cambio" && git push
```

Cloudflare detecta el push y despliega en aproximadamente un minuto.

## Ver la web en local antes de subir

```bash
cd ~/zonorah-web/public && python3 -m http.server 8080
# abrir http://localhost:8080
```

## Sitio: seis páginas en tres idiomas

El DISEÑO es el de la portada original y no se toca: `build/plantilla.html` (CSS, animaciones GSAP,
estructura y clases). `build/build.py` cambia solo el TEXTO y lo necesario para SEO, y arma cada página
con las secciones de esa plantilla.

| Página | Inglés | Español | Indonesio |
|---|---|---|---|
| Portada | `/` | `/es/` | `/id/` |
| Método (pasos, límites, cómo citar) | `/method/` | `/es/metodo/` | `/id/metode/` |
| Investigación | `/research/` | `/es/investigacion/` | `/id/riset/` |
| Zonorah Data y acceso | `/data/` | `/es/datos-abiertos/` | `/id/data/` |
| Estudios de muestra | `/studies/` | `/es/estudios/` | `/id/studi/` |
| Privacidad | `/privacy/` | `/es/privacidad/` | `/id/privasi/` |

```bash
python3 build/build.py     # 18 páginas + 404.html, sitemap.xml, robots.txt, llms.txt y llms-full.txt
```

**Cambiar un texto:** edita `build/content.py` (cada fila trae inglés, español e indonesio) y vuelve a ejecutar
`build.py`. No edites los `index.html`: se sobrescriben. **Cambiar el diseño:** edita `build/plantilla.html`;
cada reemplazo de `build.py` comprueba que su fragmento original existe y la generación falla si una página
pierde el CSS, el cuerpo o su único `<h1>`.

**Voz del texto:** documentación, no publicidad. Títulos que son sustantivos, frases descriptivas, nada de
eslóganes, simetrías ni listas de tres por costumbre. Cada afirmación sale de la metodología publicada, de
`planes.py` o del código del análisis. Sin referencias a un país: Zonorah es global.

**SEO y GEO:** `hreflang` entre las tres versiones de cada página y `x-default` al inglés; datos estructurados
(Organization, WebSite, WebPage, BreadcrumbList); `og.png`; `sitemap.xml` con las 18 URLs y sus alternativas;
`llms.txt` y `llms-full.txt`; `robots.txt` que permite los rastreadores de IA y bloquea `/platform/api/`;
`404.html` (sin él, Cloudflare Pages responde 200 con la portada a cualquier ruta). La plataforma (`/platform` y
`datos.zonorah.com`) sale con `X-Robots-Tag: noindex`: todo el contenido está en estas páginas.

No hay traducción en el navegador. Un script mínimo guarda la cookie `zonorah_lang` para que la app abra en el
mismo idioma.

## zonorah.com/platform

La plataforma de Zonorah: tras el acceso con Google, el panel donde cada persona configura sus monitoreos y
sus búsquedas, con «Ask Zonorah» y «Learn» dentro. No vive en este repositorio: es la app de
`~/Zonorah/zonorah/web`, que corre en el Mac y sale a internet por un túnel de Cloudflare como
`datos.zonorah.com`. La función de `functions/platform/` solo reenvía `zonorah.com/platform/…` a esa
dirección. Si el Mac está apagado, `/platform` muestra un aviso en vez de un error de Cloudflare.

Todos los botones del sitio llevan a `/platform/` (alta o acceso con Google). `/datos` es la dirección
antigua y redirige.

Aquí no hay datos ni claves: la función no guarda nada.

## Cuando se conecte Stripe

El sitio dice «gratis hasta el 31 de diciembre, sin datos de pago» mientras `COBRO_ACTIVO = False` en
`build/content.py`. El día que el bloque `stripe:` esté en la configuración de la app (ver
`~/Zonorah/zonorah/web/pagos.py`):

1. `COBRO_ACTIVO = True` (y `PRUEBA_DIAS` igual que `stripe.prueba_dias` de la app).
2. `python3 build/build.py`: los precios dejan de ir tachados, los botones dicen «Empezar la prueba gratis»
   y el texto habla de la prueba con tarjeta, una por persona.
3. Publicar. No debe quedar ninguna página prometiendo «sin datos de pago» con el cobro activo.

## Reglas

- El HTML de la web va en `public/index.html`, **nunca** en el README.
  Un README es documentación; Cloudflare no lo sirve como página.
- Nunca meter claves ni `.env` aquí: este repositorio es público y su
  contenido acaba publicado.
- Este repositorio es **distinto** del sistema Zonorah (`~/zonorah`), que
  es privado y contiene la lógica de negocio y las palabras clave de los
  clientes. No mezclar los dos.
- Los repos borrados en GitHub solo se pueden restaurar durante 90 días.

## Historial

- **13-oct-2026** — Versión en indonesio con botón ES · ID en la cabecera.
- **30-sep-2026** — Enlace «Datos» y caso de periodismo de datos; `/datos`
  pasa por un Worker que reenvía a la app de datos.
- **25-ago-2026** — Repositorio reconstruido: la portada pasa de estar
  pegada en README.md a ser un `public/index.html` real, y se añade
  `wrangler.jsonc` para que Cloudflare pueda servirlo.
