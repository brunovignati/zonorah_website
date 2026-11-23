#!/usr/bin/env python3
"""Genera la portada de Zonorah en tres idiomas, una URL por idioma.

    python3 build/build.py

Escribe:
    public/index.html        inglés   (zonorah.com/)
    public/es/index.html     español  (zonorah.com/es/)
    public/id/index.html     indonesio (zonorah.com/id/)
    public/sitemap.xml  public/robots.txt  public/llms.txt

La fuente única es `build/content.py`. Cada página es HTML completo y legible
sin JavaScript: lo que ve un buscador o una IA es lo que ve una persona. No hay
traducción en el navegador. Solo biblioteca estándar.
"""
import html
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import (CITA, EMAIL, IDIOMAS, LAB_URL, PLANES, RUTAS, SITE)  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
PUBLIC = RAIZ / "public"
HOY = date.today().isoformat()
e = html.escape

CSS = """
:root{--noche:#0b1f00;--bosque:#163300;--lima:#9fe870;--rocio:#eaf7dc;--hueso:#f4f5ef;
--tinta:#0e1a08;--gris:#4f5849;--linea:#d9dccf;--w:1120px;--g:clamp(20px,4vw,48px);
--f:'Archivo','Helvetica Neue',Helvetica,Arial,sans-serif;--m:'IBM Plex Mono',ui-monospace,Menlo,Consolas,monospace}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:76px}
body{margin:0;font:400 17px/1.6 var(--f);color:var(--tinta);background:var(--hueso);-webkit-font-smoothing:antialiased}
a{color:inherit}img,svg{max-width:100%}
.skip{position:absolute;left:-999px;top:8px;background:var(--lima);color:var(--noche);padding:8px 14px;border-radius:6px;z-index:99}
.skip:focus{left:8px}
:focus-visible{outline:3px solid var(--lima);outline-offset:3px}
.wrap{max-width:var(--w);margin:0 auto;padding:0 var(--g)}
header.top{position:sticky;top:0;z-index:20;background:rgba(244,245,239,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--linea)}
.bar{display:flex;align-items:center;gap:20px;min-height:64px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:800;letter-spacing:.02em;font-size:19px}
.brand svg{width:22px;height:auto;flex:none}.brand span{white-space:nowrap}
nav.main{margin-left:auto;display:flex;gap:22px;align-items:center;font-size:15px}
nav.main a{text-decoration:none;color:var(--gris)}nav.main a:hover{color:var(--tinta)}
.langs{display:flex;gap:4px;font:500 13px var(--m)}
.langs a{padding:4px 8px;border-radius:5px;text-decoration:none;color:var(--gris);border:1px solid transparent}
.langs a[aria-current=true]{background:var(--bosque);color:var(--lima)}
.btn{display:inline-block;padding:12px 20px;border-radius:8px;font-weight:700;text-decoration:none;font-size:16px;border:2px solid var(--bosque)}
.btn.p{background:var(--lima);color:var(--noche);border-color:var(--lima)}.btn.p:hover{background:#b6f08e}
.btn.s{color:var(--rocio);border-color:#3f5a2a}.btn.s:hover{border-color:var(--lima)}
.btn.d{background:var(--bosque);color:var(--lima)}.btn.d:hover{background:var(--noche)}
.btn.o{background:transparent;color:var(--bosque)}.btn.o:hover{background:var(--rocio)}
.hero{background:var(--noche);color:var(--rocio);padding:clamp(56px,10vw,120px) 0 clamp(48px,8vw,88px)}
.eyebrow{font:500 13px var(--m);letter-spacing:.14em;text-transform:uppercase;color:var(--lima);margin:0 0 18px}
h1{font-weight:800;font-stretch:90%;line-height:1.02;letter-spacing:-.02em;margin:0 0 24px;font-size:clamp(42px,8vw,92px)}
h1 span{display:block;color:var(--lima)}
.lead{font-size:clamp(18px,2.2vw,23px);max-width:760px;margin:0 0 32px;color:#cfe3bd}
.cta{display:flex;flex-wrap:wrap;gap:12px}
.facts{background:var(--bosque);color:var(--rocio)}
.facts ul{list-style:none;margin:0;padding:28px 0;display:grid;gap:24px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.facts strong{display:block;color:var(--lima);font-size:18px;margin-bottom:4px}
.facts span{font-size:15px;color:#cfe3bd}
section{padding:clamp(56px,8vw,96px) 0;border-bottom:1px solid var(--linea)}
section.alt{background:#fff}
h2{font-size:clamp(28px,4vw,44px);line-height:1.1;letter-spacing:-.015em;margin:0 0 20px;font-stretch:92%}
h3{font-size:22px;line-height:1.2;margin:0 0 10px}
p{margin:0 0 16px;max-width:72ch}
.note{font-size:15px;color:var(--gris);border-left:3px solid var(--lima);padding-left:14px;max-width:72ch}
.grid{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.card{background:#fff;border:1px solid var(--linea);border-radius:12px;padding:26px}
section.alt .card{background:var(--hueso)}
.step b{font:500 12px var(--m);letter-spacing:.12em;text-transform:uppercase;color:var(--gris);display:block;margin-bottom:8px}
.two{display:grid;gap:24px;grid-template-columns:repeat(auto-fit,minmax(320px,1fr))}
.two .card{display:flex;flex-direction:column}
.two ul,.card ul,.list{margin:0 0 20px;padding-left:20px}.two li,.list li{margin-bottom:10px}
.two .card .btn{margin-top:auto;align-self:flex-start}
.tag{font-size:15px;color:var(--gris);margin-bottom:14px}
.plan.pop{border:2px solid var(--bosque)}
.plan .badge{font:500 12px var(--m);background:var(--lima);color:var(--noche);padding:3px 9px;border-radius:99px;display:inline-block;margin-bottom:10px}
.price{font-size:40px;font-weight:800;line-height:1;margin:6px 0}
.price small{display:block;font-size:13px;font-weight:400;color:var(--gris);margin-top:6px}
.plan ul{padding-left:18px;font-size:15px}
.limits dt{font-weight:700;margin-top:14px}.limits dd{margin:2px 0 0;color:var(--gris);max-width:72ch}
pre.cite{white-space:pre-wrap;background:var(--noche);color:var(--rocio);border-radius:10px;padding:18px;font:400 14px/1.6 var(--m);max-width:72ch}
details{border-bottom:1px solid var(--linea);padding:16px 0;max-width:820px}
summary{cursor:pointer;font-weight:700;font-size:18px;list-style:none}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";float:right;font-weight:400}details[open] summary::after{content:"–"}
details p{margin:12px 0 0;color:var(--gris)}
.contact{background:var(--bosque);color:var(--rocio);border:0}
.contact h2{color:#fff}.contact p{color:#cfe3bd}
.mail{font-size:clamp(22px,4vw,34px);font-weight:800;color:var(--lima);word-break:break-all}
footer{background:var(--noche);color:#9fb28c;padding:36px 0;font-size:14px}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px 28px;align-items:center}
footer a{color:#cfe3bd}footer .sp{margin-left:auto}
@media(max-width:860px){nav.main>a:not(.btn){display:none}nav.main{gap:12px}}
@media(max-width:560px){nav.main>a.btn{display:none}nav.main{margin-left:auto}.bar{gap:10px}.brand span{font-size:16px}.btn{padding:10px 14px;font-size:15px}nav.main{gap:8px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

LOGO = ('<svg viewBox="0 0 780 825" aria-hidden="true" focusable="false"><path fill="#163300" '
        'd="M138 0 L0 782 L380 162 L228 189 Z M780 36 L382 690 L679 649 L780 825 Z"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 780 825'%3E"
           "%3Crect width='780' height='825' fill='%23163300'/%3E%3Cpath d='M138 0 L0 782 L380 162 "
           "L228 189 Z M780 36 L382 690 L679 649 L780 825 Z' fill='%239fe870'/%3E%3C/svg%3E")


def app(ruta: str, lang: str) -> str:
    """Enlace a la app de datos en el mismo idioma que la página que se está leyendo.

    La app lee `?lang=` (y lo guarda en su cookie), así que quien cambia de idioma
    en la portada sigue en ese idioma al entrar: no hay un salto a otro idioma.
    """
    return ruta + ("&" if "?" in ruta else "?") + f"lang={lang}"


def url(lang: str) -> str:
    return SITE + RUTAS[lang]


def alternates(actual: str) -> str:
    t = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l)}">\n' for l in IDIOMAS)
    return t + f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'


def json_ld(c: dict) -> str:
    lang = c["lang"]
    org = {"@type": ["Organization", "ResearchOrganization"], "@id": SITE + "/#org",
           "name": "Zonorah", "alternateName": "Zonorah Media Neuroscience Lab", "url": SITE + "/",
           "email": EMAIL, "description": c["description"],
           "knowsAbout": ["media monitoring", "content analysis", "speech transcription",
                          "media framing", "open media data"]}
    web = {"@type": "WebSite", "@id": SITE + "/#web", "url": SITE + "/", "name": "Zonorah",
           "inLanguage": list(IDIOMAS), "publisher": {"@id": SITE + "/#org"}}
    page = {"@type": "WebPage", "@id": url(lang) + "#page", "url": url(lang), "name": c["title"],
            "description": c["description"], "inLanguage": lang, "isPartOf": {"@id": SITE + "/#web"},
            "about": {"@id": SITE + "/#org"}, "dateModified": HOY}
    faq = {"@type": "FAQPage", "@id": url(lang) + "#faq", "inLanguage": lang,
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
    return json.dumps({"@context": "https://schema.org", "@graph": [org, web, page, faq]},
                      ensure_ascii=False, indent=1)


def pagina(c: dict) -> str:
    lang = c["lang"]
    ruta = RUTAS[lang]
    mail = f"mailto:{EMAIL}"
    asunto = c["com_subject"].replace(" ", "%20")
    nav = "".join(f'<a href="#{i}"{" class=hide" if i in ("method", "faq") else ""}>{e(t)}</a>'
                  for i, t in c["nav"])
    langs = "".join(
        f'<a href="{RUTAS[l]}" hreflang="{l}" lang="{l}"{" aria-current=true" if l == lang else ""}>{l.upper()}</a>'
        for l in IDIOMAS)
    facts = "".join(f"<li><strong>{e(a)}</strong><span>{e(b)}</span></li>" for a, b in c["facts"])
    steps = "".join(f'<article class="card step"><b>{e(c["step_word"])} 0{i}</b><h3>{e(t)}</h3>'
                    f"<p>{e(d)}</p></article>" for i, (t, d) in enumerate(c["steps"], 1))
    li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)  # noqa: E731
    planes = ""
    for pid, precio, _ in PLANES:
        nombre, incl = c["plans"][pid]
        pop = pid == "intensivo"
        planes += (f'<article class="card plan{" pop" if pop else ""}">'
                   + (f'<span class="badge">{e(c["pop"])}</span>' if pop else "")
                   + f'<h3>{e(nombre)}</h3><div class="price">S/ {precio}<small>{e(c["list_price"])}</small></div>'
                   f"<ul>{li(incl)}</ul>"
                   f'<a class="btn d" href="{e(app("/datos/planes?plan=" + pid, lang))}">{e(c["plans_cta"])}</a></article>')
    limites = "".join(f"<dt>{e(a)}</dt><dd>{e(b)}</dd>" for a, b in c["limits"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    foot = "".join(f'<a href="{app(h, lang)}">{e(t)}</a>' for t, h in c["foot_links"])
    sec = lambda i: i  # noqa: E731
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(c["title"])}</title>
<meta name="description" content="{e(c["description"])}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{url(lang)}">
{alternates(lang)}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Zonorah">
<meta property="og:title" content="{e(c["title"])}">
<meta property="og:description" content="{e(c["description"])}">
<meta property="og:url" content="{url(lang)}">
<meta property="og:locale" content="{c["locale"]}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(c["og_alt"])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(c["title"])}">
<meta name="twitter:description" content="{e(c["description"])}">
<meta name="twitter:image" content="{SITE}/og.png">
<meta name="theme-color" content="#0b1f00">
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<script type="application/ld+json">
{json_ld(c)}
</script>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">{e(c["skip"])}</a>
<header class="top"><div class="wrap bar">
<a class="brand" href="{ruta}" aria-label="Zonorah">{LOGO}<span>ZONORAH</span></a>
<nav class="main" aria-label="{e(c["nav_label"])}">{nav}
<a class="btn d" href="{app("/datos/", lang)}">{e(c["nav_cta"])}</a>
<span class="langs" role="group" aria-label="{e(c["lang_label"])}">{langs}</span></nav>
</div></header>
<main id="main">
<section class="hero" aria-labelledby="t"><div class="wrap">
<p class="eyebrow">{e(c["eyebrow"])}</p>
<h1 id="t">{e(c["h1_a"])} <span>{e(c["h1_b"])}</span></h1>
<p class="lead">{e(c["lead"])}</p>
<div class="cta"><a class="btn p" href="{app("/datos/", lang)}">{e(c["cta1"])}</a>
<a class="btn s" href="{mail}?subject={asunto}">{e(c["cta2"])}</a></div>
</div></section>
<div class="facts"><div class="wrap"><ul>{facts}</ul></div></div>

<section id="lab" class="alt"><div class="wrap">
<h2>{e(c["lab_h"])}</h2>
{"".join(f"<p>{e(p)}</p>" for p in c["lab_p"])}
</div></section>

<section id="method"><div class="wrap">
<h2>{e(c["method_h"])}</h2>
<div class="grid">{steps}</div>
</div></section>

<section id="research" class="alt"><div class="wrap">
<h2>{e(c["research_h"])}</h2>
<div class="two">
<article class="card"><h3>{e(c["sci_h"])}</h3><p class="tag">{e(c["sci_for"])}</p>
<ul>{li(c["sci_li"])}</ul><a class="btn d" href="{app("/datos/", lang)}">{e(c["sci_cta"])}</a></article>
<article class="card"><h3>{e(c["com_h"])}</h3><p class="tag">{e(c["com_for"])}</p>
<ul>{li(c["com_li"])}</ul><a class="btn o" href="{mail}?subject={asunto}">{e(c["com_cta"])}</a></article>
</div>
<h3 style="margin-top:44px">{e(c["q_h"])}</h3>
<ul class="list">{li(c["q_li"])}</ul>
</div></section>

<section id="foundations"><div class="wrap">
<h2>{e(c["found_h"])}</h2>
{"".join(f"<p>{e(p)}</p>" for p in c["found_p"])}
<p><a href="{LAB_URL}" rel="noopener" target="_blank">{e(c["found_link"])} ↗</a></p>
</div></section>

<section id="data" class="alt"><div class="wrap">
<h2>{e(c["data_h"])}</h2>
<p>{e(c["data_p"])}</p>
<p class="note">{e(c["plans_note"])}</p>
<div class="grid" style="margin-top:28px">{planes}</div>
</div></section>

<section id="limits"><div class="wrap">
<h2>{e(c["limits_h"])}</h2>
<dl class="limits">{limites}</dl>
<h3 style="margin-top:44px">{e(c["privacy_h"])}</h3>
<ul class="list">{li(c["privacy"])}</ul>
<h3 style="margin-top:44px">{e(c["cite_h"])}</h3>
<p>{e(c["cite_p"])}</p>
<pre class="cite">{e(c["cite_fmt"])}</pre>
</div></section>

<section id="faq" class="alt"><div class="wrap">
<h2>{e(c["faq_h"])}</h2>
{faq}
</div></section>

<section id="contact" class="contact"><div class="wrap">
<h2>{e(c["contact_h"])}</h2>
<p>{e(c["contact_p"])}</p>
<p><a class="mail" href="{mail}">{EMAIL}</a></p>
</div></section>
</main>
<footer><div class="wrap"><strong>ZONORAH</strong><span>{e(c["footer_tag"])}</span>{foot}
<span class="sp">{e(c["rights"])}</span></div></footer>
</body>
</html>
"""


def comprobar():
    base = set(IDIOMAS["en"])
    for l, c in IDIOMAS.items():
        faltan, sobran = base - set(c), set(c) - base
        if faltan or sobran:
            sys.exit(f"[{l}] claves distintas: faltan {sorted(faltan)} sobran {sorted(sobran)}")
        for k in ("facts", "steps", "sci_li", "com_li", "q_li", "limits", "privacy", "faq", "nav"):
            if len(c[k]) != len(IDIOMAS["en"][k]):
                sys.exit(f"[{l}] «{k}» tiene {len(c[k])} elementos y en inglés {len(IDIOMAS['en'][k])}")
        if len(c["description"]) > 175:
            print(f"[{l}] aviso: description de {len(c['description'])} caracteres")


def escribir(ruta: Path, texto: str):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto, encoding="utf-8")
    print(f"  {ruta.relative_to(RAIZ)}  {len(texto.encode()) / 1024:.0f} KB")


def main():
    comprobar()
    for l, c in IDIOMAS.items():
        destino = PUBLIC / "index.html" if l == "en" else PUBLIC / l / "index.html"
        escribir(destino, pagina(c))
    urls = "".join(
        f"<url><loc>{url(l)}</loc><lastmod>{HOY}</lastmod>"
        + "".join(f'<xhtml:link rel="alternate" hreflang="{m}" href="{url(m)}"/>' for m in IDIOMAS)
        + f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en")}"/></url>\n'
        for l in IDIOMAS)
    escribir(PUBLIC / "sitemap.xml",
             '<?xml version="1.0" encoding="UTF-8"?>\n<urlset '
             'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot"]
    escribir(PUBLIC / "robots.txt",
             "# Zonorah publica su metodología y sus cifras para que se citen: se permite a todos los\n"
             "# rastreadores, incluidos los de buscadores con IA. /datos es la aplicación.\n"
             "User-agent: *\nAllow: /\n\n"
             + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)
             + f"Sitemap: {SITE}/sitemap.xml\n")
    en = IDIOMAS["en"]
    escribir(PUBLIC / "llms.txt",
             f"# Zonorah, Media Neuroscience Lab\n\n> {en['description']}\n\n"
             + "".join(f"{p}\n\n" for p in en["lab_p"])
             + "## Key facts\n\n"
             + "".join(f"- {a}: {b}\n" for a, b in en["facts"])
             + "\n## Pages\n\n"
             + "".join(f"- [{IDIOMAS[l]['dir_name']}]({url(l)}): home page in {IDIOMAS[l]['dir_name']}\n"
                       for l in IDIOMAS)
             + f"- [Methodology]({SITE}/datos/metodologia): how figures are measured, limits and how to cite\n"
             + f"- [Zonorah Data]({SITE}/datos/): comparator, charts, CSV downloads and AI chat\n"
             + "\n## Limits\n\n" + "".join(f"- {a} {b}\n" for a, b in en["limits"])
             + f"\n## Cite\n\n{en['cite_fmt']}\n\n## Contact\n\n{EMAIL}\n")


if __name__ == "__main__":
    main()
