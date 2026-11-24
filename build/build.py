#!/usr/bin/env python3
"""Genera el sitio de Zonorah: 6 páginas en 3 idiomas, una URL por tema e idioma.

    python3 build/build.py

El DISEÑO es el de la portada original: `build/plantilla.html` (su CSS, sus animaciones GSAP, su
estructura y sus clases, intactos). Este script solo cambia el TEXTO y lo que hace falta para el SEO.
Cada reemplazo comprueba que el fragmento original existe, así que si la plantilla cambia falla en
voz alta en vez de dejar texto colado. Las páginas se arman con las secciones de la plantilla.

Páginas (ver `content.PAGINAS` y `content.SLUGS`):
    /  /method/  /research/  /data/  /studies/  /privacy/            (inglés)
    /es/  /es/metodo/  /es/investigacion/  /es/datos-abiertos/  …    (español)
    /id/  /id/metode/  /id/riset/  /id/data/  …                      (indonesio)
más 404.html, sitemap.xml, robots.txt, llms.txt y llms-full.txt.

No hay traducción en el navegador: cada página trae su idioma ya puesto. Solo biblioteca estándar.
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import (CITA, EMAIL, ENLACE_FILA, FILAS, LAB_URL, LANGS, LOCALES, NOMBRES, PAGINAS,  # noqa: E402
                     SECTORES, SITE, UPDATED, comprobar, ruta, textos)

RAIZ = Path(__file__).resolve().parent.parent
PUBLIC = RAIZ / "public"
PLANTILLA = (Path(__file__).parent / "plantilla.html").read_text(encoding="utf-8")
e = html.escape
MESES = {
    "en": "January February March April May June July August September October November December".split(),
    "es": "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split(),
    "id": "Januari Februari Maret April Mei Juni Juli Agustus September Oktober November Desember".split(),
}


def fecha_larga(lang: str) -> str:
    a, m, d = UPDATED.split("-")
    mes = MESES[lang][int(m) - 1]
    return f"{int(d)} de {mes} de {a}" if lang == "es" else f"{int(d)} {mes} {a}"


def url(lang: str, pg: str) -> str:
    return SITE + ruta(lang, pg)


class Plantilla:
    """La plantilla original con reemplazos que comprueban que el original existe."""

    def __init__(self, s: str):
        self.s = s

    def rp(self, old: str, new: str, n: int | None = None):
        c = self.s.count(old)
        if c == 0 or (n is not None and c != n):
            raise SystemExit(f"[plantilla] se esperaba {n or '≥1'} vez «{old[:80]}» y hay {c}")
        self.s = self.s.replace(old, new)

    def re_sub(self, patron: str, nuevo, n: int | None = None, flags=re.S):
        res, c = re.subn(patron, nuevo, self.s, flags=flags)
        if c == 0 or (n is not None and c != n):
            raise SystemExit(f"[plantilla] patrón {patron[:70]!r}: se esperaba {n or '≥1'} y hay {c}")
        self.s = res


# ---------------------------------------------------------------- cabecera del documento
def head_nuevo(lang: str, pg: str, x: dict) -> str:
    titulo, desc = x[f"t_{pg}"], x[f"d_{pg}"]
    alt = "\n".join(f'<meta property="og:locale:alternate" content="{LOCALES[o]}">' for o in LANGS if o != lang)
    hreflang = "".join(f'<link rel="alternate" hreflang="{o}" href="{url(o, pg)}">\n' for o in LANGS)
    org = {"@type": ["Organization", "ResearchOrganization"], "@id": SITE + "/#org", "name": "Zonorah",
           "alternateName": "Zonorah Media Neuroscience Lab", "url": SITE + "/", "email": EMAIL,
           "description": x["d_home"],
           "logo": {"@type": "ImageObject", "url": SITE + "/logo.png", "width": 512, "height": 512},
           "image": SITE + "/og.png",
           "knowsAbout": ["media monitoring", "content analysis", "speech transcription",
                          "media framing", "open media data"]}
    web = {"@type": "WebSite", "@id": SITE + "/#web", "url": SITE + "/", "name": "Zonorah",
           "inLanguage": list(LANGS), "publisher": {"@id": SITE + "/#org"}}
    page = {"@type": "WebPage", "@id": url(lang, pg) + "#page", "url": url(lang, pg), "name": titulo,
            "description": desc, "inLanguage": lang, "isPartOf": {"@id": SITE + "/#web"},
            "about": {"@id": SITE + "/#org"}, "dateModified": UPDATED, "datePublished": "2026-11-23",
            "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/og.png", "width": 1200, "height": 630}}
    grafo = [org, web, page]
    if pg != "home":
        page["breadcrumb"] = {"@id": url(lang, pg) + "#crumbs"}
        grafo.append({"@type": "BreadcrumbList", "@id": url(lang, pg) + "#crumbs", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": x["pg_home"], "item": url(lang, "home")},
            {"@type": "ListItem", "position": 2, "name": x[f"pg_{pg}"], "item": url(lang, pg)}]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=1)
    return f"""<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{url(lang, pg)}">
{hreflang}<link rel="alternate" hreflang="x-default" href="{url("en", pg)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Zonorah">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(lang, pg)}">
<meta property="og:locale" content="{LOCALES[lang]}">
{alt}
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(x["og_title"])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(titulo)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/og.png">
<meta name="theme-color" content="#0b1f00">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">
{ld}
</script>"""


def script_idioma(lang: str, x: dict) -> str:
    """Sustituye al traductor del navegador: fija el idioma, da `zt` al script de la cuenta y
    guarda la cookie `zonorah_lang`, que es la que lee la app de datos."""
    d = {"Salir": x["n_logout"], "Iniciar sesión / Registrarse": x["n_login"], " · ir al chat": x["n_tochat"]}
    return ("<script>\nwindow.ZLANG=" + json.dumps(lang) + ";\n(function(){var T=" + json.dumps(d, ensure_ascii=False)
            + ";window.zt=function(s){return Object.prototype.hasOwnProperty.call(T,s)?T[s]:s};\n"
            "try{document.cookie=\"zonorah_lang=" + lang + "; path=/; max-age=31536000; SameSite=Lax\"}catch(e){}})();\n</script>")


# ---------------------------------------------------------------- piezas que se arman por página
def filas(lang: str, x: dict, pg: str) -> str:
    """Las filas (`.caso`) de la plantilla original: etiqueta, título y texto, y una línea pequeña."""
    out = []
    for pre in FILAS[pg]:
        tag, h, txt, ex = x[pre + "m"], x[pre + "h"], x[pre + "p"], x.get(pre + "x", "")
        enlace = ENLACE_FILA.get(pre)
        if enlace:
            href = ruta(lang, enlace)
            h_html = f'<a href="{href}">{e(h)}</a>'
            ex_html = f'<span class="ex"><a href="{href}">{e(ex)}</a></span>' if ex else ""
        else:
            h_html = e(h)
            if pre == "rr3":
                ex_html = f'<span class="ex"><a href="{LAB_URL}" target="_blank" rel="noopener noreferrer">{e(ex)}</a></span>'
            else:
                ex_html = f'<span class="ex">{e(ex)}</span>' if ex else ""
        out.append(f'<article class="caso" data-cursor="Ver">\n          <span class="mono">{e(tag)}</span>\n'
                   f'          <h3>{h_html}</h3>\n          <div><p>{e(txt)}</p>{ex_html}</div>\n        </article>')
    return "\n        ".join(out)


def seccion_filas(titulo: str, lead: str, cuerpo: str, h1: bool) -> str:
    """Una sección `casos` de la plantilla (encabezado + filas) con el título que se pida."""
    t = "h1" if h1 else "h2"
    # El título de arriba de una página interior ya está a la vista al cargar y el efecto de líneas
    # (SplitText + ScrollTrigger) no se dispara solo ahí: usa el de aparición, que sí. Los demás títulos
    # siguen con el efecto original, que se activa con el scroll.
    efecto = "data-reveal" if h1 else "data-split"
    return (f'<section class="casos is-light" id="casos" data-theme="light" data-sec="04" aria-labelledby="casosTitle">\n'
            f'    <div class="container">\n      <div class="sec-head">\n'
            f'        <{t} class="display h-xl" id="casosTitle" {efecto}>{e(titulo)}</{t}>\n'
            f'        <p class="lead" data-reveal>{e(lead)}</p>\n      </div>\n'
            f'      <div class="casos-list" data-stagger>\n        {cuerpo}\n      </div>\n    </div>\n  </section>')


def a_h1(seccion: str, ident: str) -> str:
    """El título de la primera sección de una página interior pasa de h2 a h1 (una página, un h1)."""
    nuevo, n = re.subn(r'<h2 (class="display h-xl" id="%s") data-split>(.*?)</h2>' % ident, r"<h1 \1 data-reveal>\2</h1>", seccion, flags=re.S)
    if n != 1:
        raise SystemExit(f"[plantilla] no hay un h2 «{ident}» que pasar a h1")
    return nuevo


# ---------------------------------------------------------------- la página
def pagina(lang: str, pg: str) -> str:
    x = textos(lang)
    p = Plantilla(PLANTILLA)
    rp, rs = p.rp, p.re_sub
    ll = f"lang={lang}"
    app = lambda r: r + ("&" if "?" in r else "?") + ll  # noqa: E731
    data_precios = ruta(lang, "data") + "#precios"

    # ---- documento
    rp('<html lang="es">', f'<html lang="{lang}">', 1)
    # El comentario de edición empieza ANTES de <title> y lo nombra en su texto: hay que partir de su apertura.
    rs(r"<!--\s*═+\s*ZONA EDITABLE Nº 1 ·.*?FIN DE LA ZONA EDITABLE Nº 1 ═+ -->", lambda m: head_nuevo(lang, pg, x), 1)
    rs(r"<!-- ═+ IDIOMA \(ES / ID\) ═+.*?</script>", lambda m: script_idioma(lang, x), 1)
    rs(r"<script>\s*/\* ── Idioma: traduce textos y atributos antes de las animaciones ── \*/.*?</script>", "", 1)

    # ---- cabecera y menú: ahora enlazan a páginas
    rp('aria-label="Canales y emisoras que sintonizamos"', f'aria-label="{e(x["aria_logos"])}"', 1)

    def enlaces(menu: bool) -> str:
        items = []
        for destino in ("method", "research", "data", "studies"):
            act = ' class="active" aria-current="page"' if destino == pg else ""
            items.append(f'<a href="{ruta(lang, destino)}"{act}>{e(x["pg_" + destino])}</a>')
        items.append(f'<a href="{app("/datos/")}">{e(x["n_chat"])}</a>')
        return "\n    ".join(items) + "\n"
    rs(r'(<nav class="nav-links" aria-label=")[^"]*(">).*?(</nav>)',
       lambda m: m.group(1) + e(x["aria_nav"]) + m.group(2) + "\n    " + enlaces(False) + "  " + m.group(3), 1)
    rs(r'(<nav class="menu-links" aria-label=")[^"]*(">).*?(</nav>)',
       lambda m: m.group(1) + e(x["aria_menu"]) + m.group(2) + "\n    " + enlaces(True)
       + f'    <a href="{app("/datos/")}" id="menuCuenta" hidden>{e(x["n_login"])}</a>\n  ' + m.group(3), 1)
    switch = "".join(
        f'<a href="{ruta(o, pg)}" hreflang="{o}" lang="{o}" data-lang="{o}" aria-current="{str(o == lang).lower()}">{o.upper()}</a>'
        for o in LANGS)
    rs(r'<span class="lang" role="group" aria-label="[^"]*">.*?</span>',
       f'<span class="lang" role="group" aria-label="{e(x["aria_lang"])}">{switch}</span>', 1)
    rp('id="navPlanes" class="btn btn-lime btn-nav magnetic" href="/datos/planes" data-cursor="Ir">Ver planes</a>',
       f'id="navPlanes" class="btn btn-lime btn-nav magnetic" href="{data_precios}" data-cursor="Ir">{e(x["n_access"])}</a>', 1)
    rp('aria-label="Abrir menú"', f'aria-label="{e(x["menu_open"])}"', 1)
    rp("'Cerrar menú'", "'" + x["menu_close"].replace("'", "\\'") + "'", 1)
    rp("'Abrir menú'", "'" + x["menu_open"].replace("'", "\\'") + "'", 1)
    # El enlace «Entrar al panel» apuntaba a dashboard.zonorah.com, que no existe: se quita.
    rp('<div class="menu-foot"><a href="https://dashboard.zonorah.com" target="_blank" rel="noopener">Entrar al panel</a><span>hola@zonorah.com</span></div>',
       f'<div class="menu-foot"><span>{EMAIL}</span></div>', 1)

    # ---- hero (solo en la portada)
    rp('<span class="line-inner">Radio, TV<br class="br-m"> e internet.</span>', f'<span class="line-inner">{e(x["h1a"])}</span>', 1)
    rp('<span class="line-inner">Sintonizados</span>', f'<span class="line-inner">{e(x["h1b"])}</span>', 1)
    rp('<span class="line-inner"><em>las 24 horas.</em></span>', f'<span class="line-inner"><em>{e(x["h1c"])}</em></span>', 1)
    # La frase va ENCIMA del bloque de botones (dentro de él se aplastaba al lado de los botones en móvil).
    rp('<div class="hero-bottom">', f'<p class="lead hero-lead" data-reveal>{e(x["hero_lead"])}</p>\n      <div class="hero-bottom">', 1)
    rp('href="/datos/planes" data-cursor="Ir">Empieza gratis', f'href="{app("/datos/")}" data-cursor="Ir">{e(x["hero_cta1"])}', 1)
    rp('href="#como" data-scroll data-cursor="Bajar">Cómo funciona', f'href="{ruta(lang, "method")}" data-cursor="Ir">{e(x["hero_cta2"])}', 1)

    # ---- preguntas flotantes
    citas = ["“Me enteré por un cliente, no por mi equipo.”", "“Grabamos la radio a mano cada mañana.”",
             "“La emisora local no sale en ningún informe.”", "“Lo vimos tres días tarde.”",
             "“Nadie escucha los fines de semana.”", "“El clipping llega en PDF y sin audio.”",
             "“Pagamos por menciones que no nos interesan.”"]
    for i, viejo in enumerate(citas, 1):
        rp(f">{viejo}<", f">{e(x[f'q{i}'])}<", 1)
    rp("Enterarte de lo tuyo no debería ser un turno de guardia.", e(x["problema_h"]), 1)

    # ---- método: los cuatro pasos
    rp('data-split>Cómo funciona</h2>', f'data-split>{e(x["como_h"])}</h2>', 1)
    for n, viejo, nuevo in (("1", "24 h · en continuo", "s1r"), ("2", "Whisper · español", "s2r"),
                            ("3", "Análisis · IA", "s3r"), ("4", "07:00 · o en &lt;3 min", "s4r")):
        rp(f"<span>Paso 0{n}</span><span>{viejo}</span>", f'<span>{e(x["step"])} 0{n}</span><span>{e(x[nuevo])}</span>', 1)
    for viejo, k in (("Captura", "s1t"), ("Transcripción", "s2t"), ("Análisis", "s3t"), ("Entrega", "s4t")):
        rp(f"<h3>{viejo}</h3>", f"<h3>{e(x[k])}</h3>", 1)
    for viejo, k in (
            ("Grabamos la emisión completa de cada fuente que elijas. Si una cae, reconectamos.", "s1p"),
            ("Audio a texto con marcas de tiempo. Locución rápida y acentos locales incluidos.", "s2p"),
            ("Por cada mención: quién habla, de qué, en qué tono y si es urgente según tus reglas.", "s3p"),
            ("Informe diario a la hora que elijas. Si algo es crítico, alerta en menos de 3 minutos.", "s4p")):
        rp(f"<p>{viejo}</p>", f"<p>{e(x[k])}</p>", 1)
    tags = [[x["s1g1"], x["s1g2"], x["s1g3"], x["s1g4"]], [x["s2g1"], x["s2g2"], x["s2g3"]],
            [x["s3g1"], x["s3g2"], x["s3g3"], x["s3g4"]], [x["s4g1"], x["s4g2"], x["s4g3"]]]
    it = iter(tags)
    rs(r'<ul class="step-tags">.*?</ul>',
       lambda m: '<ul class="step-tags">' + "".join(f"<li>{e(t)}</li>" for t in next(it)) + "</ul>", 4)
    rs(r'<div class="vis-tags">.*?</div>',
       f'<div class="vis-tags"><span>{e(x["v3a"])}<b>{e(x["v3av"])}</b></span><span>{e(x["v3b"])}<b>{e(x["v3bv"])}</b></span>'
       f'<span>{e(x["v3c"])}<b>{e(x["v3cv"])}</b></span><span class="hot">{e(x["v3d"])}<b>{e(x["v3dv"])}</b></span></div>', 1)
    rs(r'<div class="vis-mail">.*?<div class="row">.*?</div>\s*</div>',
       f'<div class="vis-mail"><div class="mono"><span>{e(x["v4t"])}</span><span>07:00</span></div>'
       f'<strong>{e(x["v4h"])}</strong>{e(x["v4p"])}<div class="row"><span class="neg">{e(x["v4r1"])}</span>'
       f'<span>{e(x["v4r2"])}</span><span>{e(x["v4r3"])}</span></div></div>', 1)

    # ---- estudios de muestra
    rp('data-split>Informes</h2>', f'data-split>{e(x["inf_h"])}</h2>', 1)
    rs(r'(<p class="mono inf-meta" data-reveal>).*?(</p>)', lambda m: m.group(1) + e(x["inf_meta"]) + m.group(2), 1)
    rp('src="informes/', 'src="/informes/' + ("id/" if lang == "id" else ""), None)
    for slug, en, es, idn in SECTORES:
        nombre = {"en": en, "es": es, "id": idn}[lang]

        def tarjeta(m, nombre=nombre, nombre_es=es):
            b = m.group(0)
            n, pg_ = re.search(r"(\d+) menciones · (\d+) págs · PDF", b).groups()
            b = b.replace(f"Portada del informe {nombre_es}", x["inf_alt"].format(name=nombre))
            b = b.replace(f'<span class="inf-cover-t">{nombre_es}</span>', f'<span class="inf-cover-t">{e(nombre)}</span>')
            b = b.replace(f"<h3>{nombre_es}</h3>", f"<h3>{e(nombre)}</h3>")
            b = re.sub(r"\d+ menciones · \d+ págs · PDF", x["inf_data"].format(n=n, p=pg_), b)
            return b.replace("Descargar PDF</span>", e(x["inf_dl"]) + "</span>")
        rs(r'<a class="inf" href="/datos/informes/' + re.escape(slug) + r'".*?</a>', tarjeta, 1)

    # ---- acceso y precios
    rp('data-split>Precios</h2>', f'data-split>{e(x["precios_h"])}</h2>', 1)
    rp("Todos los planes, gratis hasta el 31 de diciembre de 2026. Sin datos de pago.", e(x["precios_lead"]), 1)
    for viejo, k in (("Profesional", "p1n"), ("Intensivo", "p2n"), ("Redacción", "p3n")):
        rp(f"<div class=\"mono\"><span>{viejo}</span>", f'<div class="mono"><span>{e(x[k])}</span>', 1)
    rp('<span class="tag">Más elegido</span>', f'<span class="tag">{e(x["p_pop"])}</span>', 1)
    for viejo, k in (("Para periodistas, docentes e investigadores.", "p1b"), ("Para quien trabaja con los datos a diario.", "p2b"),
                     ("Para redacciones, equipos de investigación y agencias.", "p3b")):
        rp(f'<p class="body">{viejo}</p>', f'<p class="body">{e(x[k])}</p>', 1)
    for viejo, k in (("100 preguntas a la IA al día", "p1l1"), ("Comparador y gráficos para insertar", "p1l2"),
                     ("Descargas CSV sin límite", "p1l3"), ("Laboratorio de estadística", "p1l4"),
                     ("500 preguntas a la IA al día", "p2l1"), ("Todo lo de Profesional", "p2l2"),
                     ("5 veces más consultas", "p2l3"), ("2.000 preguntas a la IA al día", "p3l1"),
                     ("Todo lo de Intensivo", "p3l2"), ("20 veces más consultas", "p3l3")):
        rp(f"</svg>{viejo}</li>", f"</svg>{e(x[k])}</li>", 1)
    rp("</svg>Gratis hasta el 31/12</li>", f'</svg>{e(x["p2l4"])}</li>', 2)
    rp("Activar gratis", e(x["p_cta"]), 3)
    rs(r'(<p class="lead" style="margin-top:48px" data-reveal>).*?(</p>)',
       lambda m: m.group(1) + e(x["p_foot"]) + f'<a href="mailto:{EMAIL}?subject={e(x["mail_subject"]).replace(" ", "%20")}" style="text-decoration:underline">'
       + e(x["p_foot_a"]) + "</a>." + m.group(2), 1)

    # ---- preguntas frecuentes: se borra la sección
    rs(r"<!-- ═+ FAQ ═+ -->\s*<section class=\"faq.*?</section>", "", 1)

    # ---- contacto (cierra todas las páginas)
    rp("Deja de enterarte tarde.", e(x["demo_h"]), 1)
    rp("Te enseñamos el panel con tus propias fuentes en 15 minutos. Si encaja, tu primer informe llega mañana.", e(x["demo_lead"]), 1)
    rp('href="/datos/planes" data-cursor="Ir">Ver planes<svg', f'href="{app("/datos/")}" data-cursor="Ir">{e(x["hero_cta1"])}<svg', 1)
    rp('href="#precios" data-scroll>Ver precios', f'href="{data_precios}">{e(x["demo_prices"])}', 1)
    rp('for="demoEmail">Tu correo</label>', f'for="demoEmail">{e(x["demo_label"])}</label>', 1)
    rp('placeholder="tu@organizacion.es"', f'placeholder="{e(x["demo_ph"])}"', 1)
    rp(">Enviar</button>", f'>{e(x["demo_send"])}</button>', 1)
    rp("O escríbenos y te llamamos hoy mismo", e(x["demo_note"]), 1)
    rp('action="mailto:hola@zonorah.com"', f'action="mailto:{EMAIL}"', 1)

    # ---- pie
    rp("<p>Radio, televisión y streaming escuchados con IA, las 24 horas.</p>", f'<p>{e(x["f_tag"])}</p>', 1)
    cols = iter([
        f'<div class="foot-col"><h4>{e(x["f_lab"])}</h4>'
        + "".join(f'<a href="{ruta(lang, d)}">{e(x["pg_" + d])}</a>' for d in ("method", "research", "data", "studies")) + "</div>",
        f'<div class="foot-col"><h4>{e(x["f_contact"])}</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div>',
        f'<div class="foot-col"><h4>{e(x["f_legal"])}</h4><a href="{ruta(lang, "privacy")}">{e(x["pg_privacy"])}</a></div>'])
    rs(r'<div class="foot-col">.*?</div>', lambda m: next(cols), 3)
    rp("Volver arriba ↑", e(x["f_up"]), 1)
    rp("<span>© 2026 Zonorah</span>", f'<span>© 2026 Zonorah · <time datetime="{UPDATED}">{e(x["updated"])} {fecha_larga(lang)}</time></span>', 1)

    # ---- armar la página con las secciones de la plantilla
    def sec(nombre: str) -> str:
        m = re.search(r'<section class="%s\b.*?</section>' % nombre, p.s, re.S)
        if not m:
            raise SystemExit(f"[plantilla] no encuentro la sección «{nombre}»")
        return m.group(0)
    demo = sec("demo")
    if pg == "home":
        cuerpo = [sec("hero"), sec("problema"),
                  seccion_filas(x["home_h"], x["home_lead"], filas(lang, x, "home"), h1=False), demo]
    elif pg == "method":
        cuerpo = [a_h1(sec("como"), "comoTitle"),
                  seccion_filas(x["limits_h"], x["limits_lead"], filas(lang, x, "method"), h1=False), demo]
    elif pg == "research":
        cuerpo = [seccion_filas(x["pg_research"], x["research_lead"], filas(lang, x, "research"), h1=True), demo]
    elif pg == "data":
        cuerpo = [seccion_filas(x["pg_data"], x["data_lead"], filas(lang, x, "data"), h1=True), sec("precios"), demo]
    elif pg == "studies":
        cuerpo = [a_h1(sec("informes"), "infTitle"), demo]
    elif pg == "privacy":
        cuerpo = [seccion_filas(x["pg_privacy"], x["privacy_lead"], filas(lang, x, "privacy"), h1=True), demo]
    else:
        raise SystemExit(f"página desconocida: {pg}")
    main = '<main id="top">\n' + "\n".join(cuerpo) + "\n</main>"
    rs(r'<main id="top">.*?</main>', lambda m: main, 1)

    # Scroll nativo: el scroll virtual de ScrollSmoother falla con rueda, trackpad y anclas.
    # El resto de la animación (pines, revelados) no depende de él.
    rp("if (window.ScrollSmoother && !reduce) {", "if (false) {", 1)
    # ---- cursor y enlaces a la app
    cur = {"Ir": x["cur_go"], "Ver": x["cur_view"], "Bajar": x["cur_down"], "Abrir PDF": x["cur_pdf"]}
    rs(r'data-cursor="([^"]*)"', lambda m: f'data-cursor="{e(cur[m.group(1)])}"')
    # toda ruta de la app lleva el idioma, para que se abra en el mismo que se está leyendo
    rs(r'href="(/datos[^"#?]*)(\?[^"#]*)?"',
       lambda m: m.group(0) if "lang=" in (m.group(2) or "") else f'href="{m.group(1)}{(m.group(2) + "&amp;") if m.group(2) else "?"}{ll}"')
    # Los comentarios de edición de la plantilla (en español) no tienen sentido en la página servida.
    rs(r"<!--.*?-->", "")
    # Red de seguridad: un reemplazo que se coma media página debe fallar, no publicarse.
    for etiqueta in ("<style", "</style>", "<body", "</body>", "<main", "</main>", "<header", "<footer", "</html>"):
        if etiqueta not in p.s:
            raise SystemExit(f"[{lang}/{pg}] la página generada perdió «{etiqueta}»")
    if p.s.count("<style") != PLANTILLA.count("<style"):
        raise SystemExit(f"[{lang}/{pg}] cambió el número de bloques <style>")
    if p.s.count("<h1") != 1:
        raise SystemExit(f"[{lang}/{pg}] debe tener exactamente un h1 y tiene {p.s.count('<h1')}")
    return p.s


PALABRAS_ES = re.compile(r"[áéíóúñ¿¡]|\b(el|la|los|las|de|del|para|con|por|una|que|es|se|su|tu|sus|y|o|en|al|más|sin|cada|todo|gratis|planes|precios|empieza|cómo)\b", re.I)
REF_PAIS = re.compile(r"per[uú]|peruan|senamhi", re.I)


def texto_visible(s: str) -> str:
    t = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", s, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", "\n", t))


def revisar(s: str, lang: str) -> list:
    t = texto_visible(s)
    avisos = [f"país: «{l.strip()[:70]}»" for l in t.split("\n") if REF_PAIS.search(l)]
    if lang != "es":
        avisos += [f"español: «{l.strip()[:70]}»" for l in t.split("\n") if len(l.strip()) > 2 and PALABRAS_ES.search(l)]
    return avisos


NO_ENCONTRADA = {
    "en": ("Page not found", "The page you are looking for does not exist or has moved.", "Go to the home page"),
    "es": ("Página no encontrada", "La página que buscas no existe o ha cambiado de sitio.", "Ir a la portada"),
    "id": ("Halaman tidak ditemukan", "Halaman yang Anda cari tidak ada atau telah dipindahkan.", "Ke beranda"),
}


def pagina_404() -> str:
    """Una URL que no existe debe responder 404, no la portada con un 200 (Cloudflare Pages
    trata un sitio sin `404.html` como una app de una sola página y devuelve `index.html`)."""
    bloques = "".join(
        f'<section lang="{l}"><h2>{e(t)}</h2><p>{e(d)}</p><p><a href="{ruta(l, "home")}">{e(a)} →</a></p></section>'
        for l, (t, d, a) in NO_ENCONTRADA.items())
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>404 · Zonorah</title>
<meta name="robots" content="noindex,follow">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">
<style>body{{margin:0;background:#0b1f00;color:#eaf7dc;font:400 18px/1.6 'Archivo',system-ui,sans-serif;padding:clamp(32px,8vw,96px) clamp(20px,6vw,80px)}}
p.k{{font:500 13px ui-monospace,Menlo,monospace;letter-spacing:.16em;text-transform:uppercase;color:#9fe870;margin:0 0 28px}}
section{{margin:0 0 40px}}h2{{font-size:clamp(28px,5vw,48px);line-height:1.1;margin:0 0 8px;font-stretch:90%}}
p{{margin:0 0 12px;color:#cfe3bd}}a{{color:#9fe870;font-weight:700}}</style>
</head>
<body><p class="k">404 · Zonorah</p>{bloques}</body>
</html>
"""


def escribir(r: Path, texto: str):
    r.parent.mkdir(parents=True, exist_ok=True)
    r.write_text(texto, encoding="utf-8")


def destino(lang: str, pg: str) -> Path:
    return PUBLIC / ruta(lang, pg).strip("/") / "index.html" if ruta(lang, pg) != "/" else PUBLIC / "index.html"


def llms_full() -> str:
    x = textos("en")
    pl = ("- Professional: S/ 89 per month at list price, 100 AI questions a day.\n"
          "- Intensive: S/ 229 per month at list price, 500 AI questions a day.\n"
          "- Newsroom: S/ 429 per month at list price, 2,000 AI questions a day.\n")

    def bloque(pg):
        out = f"## {x['pg_' + pg]}\n\n{url('en', pg)}\n\n"
        lead = {"home": x["home_lead"], "method": x["limits_lead"], "research": x["research_lead"],
                "data": x["data_lead"], "studies": x["studies_lead"], "privacy": x["privacy_lead"]}[pg]
        out += lead + "\n\n"
        for pre in FILAS.get(pg, ()):
            out += f"### {x[pre + 'm']}: {x[pre + 'h']}\n\n{x[pre + 'p']}\n\n"
            if x.get(pre + "x"):
                out += f"{x[pre + 'x']}\n\n"
        return out
    pasos = "".join(f"{i}. {x[f's{i}t']}. {x[f's{i}p']}\n" for i in range(1, 5))
    return (f"# Zonorah, Media Neuroscience Lab\n\n> {x['d_home']}\n\nLast updated: {UPDATED}\n\n{x['hero_lead']}\n\n"
            f"{x['problema_h']}\n\n" + bloque("home") + f"## How the numbers are made\n\n{pasos}\n"
            + "".join(bloque(p) for p in ("method", "research", "data")) + f"### Access\n\n{x['precios_lead']}\n\n{pl}\n"
            + bloque("studies") + bloque("privacy") + f"Contact: {EMAIL}\n\n## Other languages\n\n"
            + "".join(f"- {NOMBRES[l]}: {url(l, 'home')}\n" for l in ("es", "id")))


def main():
    comprobar()
    total = 0
    for lang in LANGS:
        for pg in PAGINAS:
            s = pagina(lang, pg)
            escribir(destino(lang, pg), s)
            total += 1
            avisos = revisar(s, lang)
            # Residuos legítimos: nombres de emisoras, la cita literal en español de la muestra y «El Niño».
            if avisos:
                print(f"  [{lang}/{pg}] {len(avisos)} aviso(s): " + " | ".join(avisos[:8]))
    print(f"  {total} páginas")
    escribir(PUBLIC / "404.html", pagina_404())
    urls = "".join(
        f"<url><loc>{url(l, pg)}</loc><lastmod>{UPDATED}</lastmod>"
        + "".join(f'<xhtml:link rel="alternate" hreflang="{m}" href="{url(m, pg)}"/>' for m in LANGS)
        + f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en", pg)}"/></url>\n'
        for pg in PAGINAS for l in LANGS)
    escribir(PUBLIC / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot"]
    grupo = lambda ua: f"User-agent: {ua}\nAllow: /\nDisallow: /datos/api/\n\n"  # noqa: E731
    escribir(PUBLIC / "robots.txt",
             "# Zonorah publica su metodología y sus cifras para que se citen: se permite a todos los rastreadores,\n"
             "# incluidos los de buscadores con IA. /datos es la aplicación: sus páginas llevan noindex y su API se bloquea.\n"
             + grupo("*") + "".join(grupo(b) for b in bots) + f"Sitemap: {SITE}/sitemap.xml\n")
    x = textos("en")
    escribir(PUBLIC / "llms.txt",
             f"# Zonorah, Media Neuroscience Lab\n\n> {x['d_home']}\n\n{x['home_lead']}\n\n## Pages\n\n"
             + "".join(f"- [{x['pg_' + pg]}]({url('en', pg)}): {x['d_' + pg]}\n" for pg in PAGINAS)
             + "\n## Other languages\n\n" + "".join(f"- [{NOMBRES[l]}]({url(l, 'home')})\n" for l in ("es", "id"))
             + f"\n## More\n\n- [Full content as plain text]({SITE}/llms-full.txt)\n"
             + f"- [Zonorah Data]({SITE}/datos/): the application (comparator, charts, CSV downloads, AI assistant)\n"
             + f"\n## Cite\n\n{CITA}\n\n## Contact\n\n{EMAIL}\n")
    escribir(PUBLIC / "llms-full.txt", llms_full())
    print("  404.html  sitemap.xml  robots.txt  llms.txt  llms-full.txt")


if __name__ == "__main__":
    main()
