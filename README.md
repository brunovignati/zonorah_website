# zonorah_website

Sitio público de **zonorah.com**. Cloudflare construye y sirve desde
este repositorio: cada `push` a `main` despliega la web.

## Estructura

| Ruta | Qué es |
|---|---|
| `public/index.html` | La portada completa: HTML, CSS y JS en un solo archivo |
| `public/_headers` | Cabeceras de seguridad y caché |
| `public/robots.txt` | Indexación abierta + referencia al sitemap |
| `wrangler.jsonc` | Configuración de Cloudflare: qué carpeta publicar y qué rutas pasan por el Worker |
| `src/worker.js` | Reenvía `/datos/…` a la app de datos (datos.zonorah.com). Nada más |

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

## zonorah.com/datos

La memoria de los medios en cifras. No vive en este repositorio: es la app
de datos de Zonorah (`~/Zonorah/zonorah/web`), que corre en el Mac y sale a
internet por un túnel de Cloudflare como `datos.zonorah.com`. El Worker de
`src/worker.js` solo reenvía `zonorah.com/datos/…` a esa dirección, así que
la misma app se ve en las dos. Si el Mac está apagado, `/datos` muestra un
aviso en vez de un error de Cloudflare.

Aquí no hay datos ni claves: el Worker no guarda nada.

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

- **30-sep-2026** — Enlace «Datos» y caso de periodismo de datos; `/datos`
  pasa por un Worker que reenvía a la app de datos.
- **25-ago-2026** — Repositorio reconstruido: la portada pasa de estar
  pegada en README.md a ser un `public/index.html` real, y se añade
  `wrangler.jsonc` para que Cloudflare pueda servirlo.
