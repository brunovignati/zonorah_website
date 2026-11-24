"""Textos del sitio de Zonorah en inglés, español e indonesio.

El DISEÑO no está aquí: vive en `build/plantilla.html`, que es la portada original sin tocar.
Este archivo solo trae los textos que `build.py` pone dentro de ella, página por página.

Cada fila es (inglés, español, indonesio). Una clave no puede faltar en un idioma.

Voz: frases cortas, verbos concretos, cifras y nombres. Sin eslóganes, sin simetrías del tipo
«no X, sino Y», sin listas de tres por costumbre. Cada idioma está escrito en ese idioma, no
traducido del inglés. Cada afirmación sale de la metodología publicada
(`~/Zonorah/zonorah/web/estaticos/metodologia.html` y `privacidad.html`), de `planes.py` o del
código del análisis. Nada de «24 horas», «audio guardado», «alerta en 3 minutos» ni «RGPD», y
nada que sugiera que Zonorah mide actividad cerebral. Si no se puede defender, no entra.
"""

EMAIL = "hola@zonorah.com"
SITE = "https://zonorah.com"
LAB_URL = "https://www.medianeuroscience.org/"
UPDATED = "2026-11-24"
CITA = "Zonorah (2026). Minutes on air per 100 hours recorded. Consulted [date], terms: [terms]. [link to the comparison]"

LANGS = ("en", "es", "id")
LOCALES = {"en": "en_US", "es": "es_PE", "id": "id_ID"}
NOMBRES = {"en": "English", "es": "Español", "id": "Bahasa Indonesia"}

# Páginas: una URL por tema e idioma. «home» es la raíz de cada idioma.
PAGINAS = ("home", "method", "research", "data", "studies", "privacy", "terms")
SLUGS = {
    "en": {"home": "", "method": "method", "research": "research", "data": "data", "studies": "studies", "privacy": "privacy", "terms": "terms"},
    "es": {"home": "", "method": "metodo", "research": "investigacion", "data": "datos-abiertos", "studies": "estudios", "privacy": "privacidad", "terms": "terminos"},
    "id": {"home": "", "method": "metode", "research": "riset", "data": "data", "studies": "studi", "privacy": "privasi", "terms": "ketentuan"},
}
PREFIJO = {"en": "", "es": "es/", "id": "id/"}


def ruta(lang: str, pagina: str) -> str:
    """Ruta absoluta de una página, p. ej. /es/metodo/ ."""
    s = SLUGS[lang][pagina]
    return "/" + PREFIJO[lang] + (s + "/" if s else "")


# Sectores de los estudios de muestra: (slug, en, es, id)
SECTORES = [
    ("alimentos-agroindustria", "Food and agribusiness", "Alimentos y agroindustria", "Pangan dan agroindustri"),
    ("banca-finanzas", "Banking and finance", "Banca y finanzas", "Perbankan dan keuangan"),
    ("construccion-infraestructura", "Construction and infrastructure", "Construcción e infraestructura", "Konstruksi dan infrastruktur"),
    ("energia-hidrocarburos", "Energy and hydrocarbons", "Energía e hidrocarburos", "Energi dan hidrokarbon"),
    ("medio-ambiente", "Environment", "Medio ambiente", "Lingkungan hidup"),
    ("mineria", "Mining", "Minería", "Pertambangan"),
    ("salud-medicina", "Health and medicine", "Salud y medicina", "Kesehatan dan kedokteran"),
    ("seguridad-ciudadana-defensa", "Public security and defence", "Seguridad ciudadana y defensa", "Keamanan publik dan pertahanan"),
    ("telecomunicaciones", "Telecommunications", "Telecomunicaciones", "Telekomunikasi"),
    ("transporte-movilidad", "Transport and mobility", "Transporte y movilidad", "Transportasi dan mobilitas"),
]

# Filas de cada página (prefijos de clave): se pintan con el diseño de las filas originales.
FILAS = {
    "home": ("hr1", "hr2", "hr3", "hr4"),
    "method": ("ml1", "ml2", "ml3", "ml4", "ml5", "ml6"),
    "research": ("rr1", "rr2", "rr3"),
    "data": ("dr1", "dr2", "dr3"),
    "privacy": ("pv1", "pv2", "pv3", "pv7", "pv8", "pv4", "pv5", "pv6"),
    "terms": ("tm1", "tm2", "tm3", "tm4", "tm5", "tm6", "tm7"),
}
# En portada cada fila es un enlace a su página.
ENLACE_FILA = {"hr1": "method", "hr2": "research", "hr3": "data", "hr4": "studies"}

# clave: (en, es, id)
T = {
    # ---- etiquetas de página (título del navegador, descripción y encabezado)
    "t_home": ("Zonorah · Media Neuroscience Lab: open media data",
               "Zonorah · Media Neuroscience Lab: datos abiertos de medios",
               "Zonorah · Media Neuroscience Lab: data media terbuka"),
    "d_home": ("Zonorah is a Media Neuroscience Lab. It writes down what radio, TV and YouTube broadcast and counts it. Open data and studies on commission.",
               "Zonorah es un Media Neuroscience Lab. Escribe lo que emiten la radio, la TV y YouTube y lo cuenta. Datos abiertos y estudios a medida.",
               "Zonorah adalah Media Neuroscience Lab. Menuliskan dan menghitung siaran radio, TV, dan YouTube. Data terbuka dan studi pesanan."),
    "t_method": ("Method: how Zonorah counts what media broadcast",
                 "Método: cómo cuenta Zonorah lo que emiten los medios",
                 "Metode: cara Zonorah menghitung siaran media"),
    "d_method": ("How Zonorah records, transcribes and counts radio, TV and YouTube, what the numbers cannot tell you, and how to cite them.",
                 "Cómo graba, transcribe y cuenta Zonorah la radio, la TV y YouTube, qué no dicen las cifras y cómo citarlas.",
                 "Cara Zonorah merekam, mentranskripsi, dan menghitung radio, TV, dan YouTube, batasan angkanya, dan cara mengutipnya."),
    "t_research": ("Research: open data and studies on commission | Zonorah",
                   "Investigación: datos abiertos y estudios a medida | Zonorah",
                   "Riset: data terbuka dan studi pesanan | Zonorah"),
    "d_research": ("Two lines of work on broadcast media: open data for science and journalism, and studies on commission for organisations.",
                   "Dos líneas de trabajo sobre los medios de comunicación: datos abiertos para la ciencia y el periodismo, y estudios a medida para organizaciones.",
                   "Dua lini kerja tentang media siaran: data terbuka untuk sains dan jurnalisme, serta studi pesanan untuk organisasi."),
    "t_data": ("Zonorah Data: compare words across radio and TV stations",
               "Zonorah Datos: compara palabras entre emisoras de radio y TV",
               "Zonorah Data: bandingkan kata antarstasiun radio dan TV"),
    "d_data": ("See how many minutes a word got on radio, TV and YouTube, download the table and ask the AI assistant. Free until 31 December 2026.",
               "Mira cuántos minutos tuvo una palabra en la radio, la TV y YouTube, descarga la tabla y pregunta al asistente de IA. Gratis hasta el 31 de diciembre de 2026.",
               "Lihat berapa menit sebuah kata tayang di radio, TV, dan YouTube, unduh tabelnya, dan tanya asisten AI. Gratis hingga 31 Desember 2026."),
    "t_studies": ("Sample studies: ten sector reports | Zonorah",
                  "Estudios de muestra: diez informes por sector | Zonorah",
                  "Studi contoh: sepuluh laporan sektor | Zonorah"),
    "d_studies": ("Ten PDF reports from one week of radio and TV in September 2026, one per sector. The reports are in Spanish.",
                  "Diez informes en PDF de una semana de radio y TV en septiembre de 2026, uno por sector.",
                  "Sepuluh laporan PDF dari satu minggu radio dan TV pada September 2026, satu per sektor. Laporan berbahasa Spanyol."),
    "t_privacy": ("Privacy | Zonorah", "Privacidad | Zonorah", "Privasi | Zonorah"),
    "d_privacy": ("What Zonorah stores, what it does not store and how to delete your account. No recordings are kept.",
                  "Qué guarda Zonorah, qué no guarda y cómo borrar tu cuenta. No se guardan grabaciones.",
                  "Apa yang disimpan Zonorah, apa yang tidak, dan cara menghapus akun Anda. Rekaman tidak disimpan."),
    "t_terms": ("Terms and refunds | Zonorah", "Términos y reembolsos | Zonorah", "Ketentuan dan pengembalian dana | Zonorah"),
    "d_terms": ("The terms of use, billing and refund rules for Zonorah plans. Draft pending legal review.",
                "Los términos de uso, la facturación y las reglas de reembolso de los planes de Zonorah. Borrador pendiente de revisión legal.",
                "Ketentuan penggunaan, penagihan, dan aturan pengembalian dana untuk paket Zonorah. Draf menunggu tinjauan hukum."),
    "og_title": ("Zonorah · Media Neuroscience Lab",) * 3,
    "pg_home": ("Home", "Inicio", "Beranda"),
    "pg_method": ("Method", "Método", "Metode"),
    "pg_research": ("Research", "Investigación", "Riset"),
    "pg_data": ("Zonorah Data", "Zonorah Datos", "Zonorah Data"),
    "pg_studies": ("Sample studies", "Estudios de muestra", "Studi contoh"),
    "pg_privacy": ("Privacy", "Privacidad", "Privasi"),
    "pg_terms": ("Terms and refunds", "Términos y reembolsos", "Ketentuan dan pengembalian dana"),
    "updated": ("Last updated", "Actualizado", "Diperbarui"),
    # ---- accesibilidad
    "aria_nav": ("Main navigation", "Navegación principal", "Navigasi utama"),
    "aria_lang": ("Change language", "Cambiar idioma", "Ganti bahasa"),
    "aria_menu": ("Menu", "Menú", "Menu"),
    "menu_open": ("Open menu", "Abrir menú", "Buka menu"),
    "menu_close": ("Close menu", "Cerrar menú", "Tutup menu"),
    "aria_logos": ("Source types we record", "Tipos de fuente que grabamos", "Jenis sumber yang kami rekam"),
    "loader_tuning": ("Tuning in", "Sintonizando", "Menyetel"),
    "fuentes": ("Radio · Television · YouTube · Podcasts · Streaming · News sites · Radio · Television · YouTube · Podcasts",
                "Radio · Televisión · YouTube · Podcasts · Streaming · Medios digitales · Radio · Televisión · YouTube · Podcasts",
                "Radio · Televisi · YouTube · Podcast · Streaming · Media daring · Radio · Televisi · YouTube · Podcast"),
    # ---- navegación (las páginas y dos accesos a la app)
    "n_learn": ("Learn", "Aprende", "Belajar"),
    "n_chat": ("Platform", "Plataforma", "Platform"),
    "n_login": ("Sign in / Sign up", "Iniciar sesión / Registrarse", "Masuk / Daftar"),
    "n_logout": ("Sign out", "Salir", "Keluar"),
    "n_tochat": (" · go to chat", " · ir al chat", " · ke chat"),
    "n_access": ("Get access", "Obtener acceso", "Dapatkan akses"),
    "cur_go": ("Go", "Ir", "Buka"), "cur_view": ("View", "Ver", "Lihat"),
    "cur_down": ("Down", "Bajar", "Turun"), "cur_pdf": ("Open PDF", "Abrir PDF", "Buka PDF"),
    # ---- portada: hero
    "h1a": ("Zonorah.",) * 3, "h1b": ("Media Neuroscience",) * 3, "h1c": ("Lab.",) * 3,
    "hero_lead": (
        "Zonorah is a computational media lab. We record radio, TV and YouTube, transcribe the audio and measure what is said: how many minutes, on which station and when. Open data for research, and studies on commission.",
        "Zonorah es un laboratorio computacional de medios. Grabamos radio, TV y YouTube, transcribimos el audio y medimos lo que se dice: cuántos minutos, en qué emisora y cuándo. Datos abiertos para investigar y estudios por encargo.",
        "Zonorah adalah laboratorium komputasi media. Kami merekam radio, TV, dan YouTube, mentranskripsi audionya, dan mengukur apa yang dikatakan: berapa menit, di stasiun mana, dan kapan. Data terbuka untuk riset dan studi berdasarkan pesanan."),
    "hero_cta1": ("Open the data", "Abrir los datos", "Buka data"),
    "hero_cta2": (
        "Method",
        "Método",
        "Metode"),
    # ---- portada: preguntas flotantes
    "q1": ("How many minutes did a topic get?", "¿Cuántos minutos tuvo un tema?", "Berapa menit sebuah topik tayang?"),
    "q2": ("On which stations?", "¿En qué emisoras?", "Di stasiun mana?"),
    "q3": ("At what hour?", "¿A qué hora?", "Pada jam berapa?"),
    "q4": ("Who was speaking?", "¿Quién hablaba?", "Siapa yang bicara?"),
    "q5": ("How was it put?", "¿Cómo lo planteaban?", "Bagaimana dibingkai?"),
    "q6": ("Evidence, or hearsay?", "¿Datos o rumores?", "Bukti, atau desas-desus?"),
    "q7": ("What changed since last week?", "¿Qué cambió desde la semana pasada?", "Apa yang berubah sejak minggu lalu?"),
    "problema_h": (
        "Questions the data can answer",
        "Preguntas que los datos pueden responder",
        "Pertanyaan yang dapat dijawab data"),
    # ---- portada: por dónde empezar
    "home_h": (
        "On this site",
        "En este sitio",
        "Di situs ini"),
    "home_lead": (
        "Zonorah is a Media Neuroscience Lab. It records and counts what media broadcast. Research on the brain is done separately and uses these counts.",
        "Zonorah es un Media Neuroscience Lab. Graba y cuenta lo que emiten los medios. La investigación sobre el cerebro se hace aparte y usa estos conteos.",
        "Zonorah adalah Media Neuroscience Lab. Ia merekam dan menghitung siaran media. Riset tentang otak dikerjakan terpisah dan memakai hitungan ini."),
    "hr1m": ("Method", "Método", "Metode"),
    "hr1h": (
        "Recording, transcribing and counting",
        "Grabación, transcripción y conteo",
        "Perekaman, transkripsi, dan penghitungan"),
    "hr1p": (
        "The procedure, the limits of the counts and how to cite them.",
        "El procedimiento, los límites de los conteos y cómo citarlos.",
        "Prosedur, batasan hitungan, dan cara mengutipnya."),
    "hr1x": (
        "Method →",
        "Método →",
        "Metode →"),
    "hr2m": ("Research", "Investigación", "Riset"),
    "hr2h": (
        "Open data and studies on commission",
        "Datos abiertos y estudios a medida",
        "Data terbuka dan studi pesanan"),
    "hr2p": (
        "Open data for researchers, teachers and journalists, and studies carried out for organisations.",
        "Datos abiertos para investigadores, docentes y periodistas, y estudios hechos para organizaciones.",
        "Data terbuka untuk peneliti, pengajar, dan jurnalis, serta studi yang dikerjakan untuk organisasi."),
    "hr2x": (
        "Research →",
        "Investigación →",
        "Riset →"),
    "hr3m": ("Zonorah Data", "Zonorah Datos", "Zonorah Data"),
    "hr3h": (
        "Comparator, downloads and assistant",
        "Comparador, descargas y asistente",
        "Pembanding, unduhan, dan asisten"),
    "hr3p": (
        "Compare words by station and day, download tables and charts, and ask the AI assistant.",
        "Compara palabras por emisora y día, descarga tablas y gráficos, y pregunta al asistente de IA.",
        "Bandingkan kata menurut stasiun dan hari, unduh tabel dan grafik, dan tanya asisten AI."),
    "hr3x": (
        "Zonorah Data →",
        "Zonorah Datos →",
        "Zonorah Data →"),
    "hr4m": ("Sample studies", "Estudios de muestra", "Studi contoh"),
    "hr4h": (
        "Ten reports, one per sector",
        "Diez informes, uno por sector",
        "Sepuluh laporan, satu per sektor"),
    "hr4p": (
        "PDF reports covering one week in September 2026. They are in Spanish.",
        "Informes en PDF de una semana de septiembre de 2026.",
        "Laporan PDF dari satu minggu pada September 2026. Berbahasa Spanyol."),
    "hr4x": (
        "Sample studies →",
        "Estudios de muestra →",
        "Studi contoh →"),
    # ---- método: los cuatro pasos
    "como_h": ("Method", "Método", "Metode"),
    "step": ("Step", "Paso", "Langkah"),
    "s1r": ("Live · station hours", "En directo · horario de cada emisora", "Langsung · jam tiap stasiun"),
    "s2r": ("Whisper · on our computer", "Whisper · en nuestro ordenador", "Whisper · di komputer kami"),
    "s3r": ("A fixed form for each passage", "Una ficha fija por pasaje", "Satu formulir tetap per kutipan"),
    "s4r": ("Table or PDF", "Tabla o PDF", "Tabel atau PDF"),
    "s1t": ("Record", "Grabar", "Rekam"),
    "s2t": ("Transcribe", "Transcribir", "Transkripsi"),
    "s3t": ("Code", "Codificar", "Kodekan"),
    "s4t": ("Report", "Informar", "Laporkan"),
    "s1p": ("Each station's live signal comes in over the internet. We record it during the hours of its schedule.",
            "La señal en directo de cada emisora llega por internet. La grabamos durante las horas de su programación.",
            "Sinyal langsung setiap stasiun masuk lewat internet. Kami merekamnya selama jam siarannya."),
    "s2p": ("A speech-recognition program on our own computer turns the audio into text, with a time for every sentence. Then the audio is deleted.",
            "Un programa de reconocimiento de voz, en nuestro propio ordenador, convierte el audio en texto con la hora de cada frase. Después se borra el audio.",
            "Program pengenalan suara di komputer kami sendiri mengubah audio menjadi teks, dengan waktu untuk setiap kalimat. Setelah itu audio dihapus."),
    "s3p": (
        "The text is searched for the words each study uses, including their variants. Every passage that matches is entered on a fixed form: who speaks, the role of the person or cause, topic, tone, framing, and whether the claim has evidence or is rumour.",
        "Se buscan en el texto las palabras que usa cada estudio, con sus variantes. Cada pasaje que coincide se anota en una ficha fija: quién habla, el papel de la persona o la causa, tema, tono, encuadre y si lo dicho tiene respaldo o es rumor.",
        "Teks dicari untuk kata-kata yang dipakai setiap studi, termasuk variannya. Setiap kutipan yang cocok dicatat pada formulir tetap: siapa yang bicara, peran orang atau isu, topik, nada, pembingkaian, dan apakah pernyataannya berbukti atau desas-desus."),
    "s4p": ("The public numbers are minutes on air per 100 hours recorded. Work done on commission arrives as a PDF by email, on the schedule you choose.",
            "Las cifras públicas son minutos al aire por cada 100 horas grabadas. El trabajo a medida llega en PDF por correo, en el horario que elijas.",
            "Angka publik berupa menit siaran per 100 jam rekaman. Pekerjaan pesanan tiba sebagai PDF lewat email, sesuai jadwal yang Anda pilih."),
    "s1g1": ("Radio", "Radio", "Radio"), "s1g2": ("TV", "TV", "TV"), "s1g3": ("YouTube",) * 3,
    "s1g4": ("Station hours", "Horario de la emisora", "Jam stasiun"),
    "s2g1": ("Time for each sentence", "Hora de cada frase", "Waktu tiap kalimat"),
    "s2g2": ("Our own computer", "Nuestro ordenador", "Komputer kami"),
    "s2g3": ("Audio deleted", "Audio borrado", "Audio dihapus"),
    "s3g1": ("Tone", "Tono", "Nada"), "s3g2": ("Speaker", "Quién habla", "Pembicara"),
    "s3g3": ("Topic", "Tema", "Topik"), "s3g4": ("Framing", "Encuadre", "Pembingkaian"),
    "s4g1": ("Minutes per 100 h", "Minutos por 100 h", "Menit per 100 jam"), "s4g2": ("PDF",) * 3,
    "s4g3": ("Email", "Correo", "Email"),
    # ejemplo ilustrativo del paso 3
    "v3a": ("Who speaks?", "¿Quién habla?", "Siapa yang bicara?"),
    "v3av": ("Municipal spokesperson", "Portavoz municipal", "Juru bicara pemkot"),
    "v3b": ("About what?", "¿De qué?", "Tentang apa?"),
    "v3bv": ("Tender · award", "Adjudicación · pliego", "Penetapan pemenang · tender"),
    "v3c": ("Tone?", "¿Tono?", "Nada?"),
    "v3cv": ("Negative", "Negativo", "Negatif"),
    "v3d": ("Evidence or rumour?", "¿Evidencia o rumor?", "Bukti atau rumor?"),
    "v3dv": ("Rumour", "Rumor", "Rumor"),
    # ejemplo ilustrativo del paso 4
    "v4t": ("Zonorah · Study report", "Zonorah · Informe del estudio", "Zonorah · Laporan studi"),
    "v4h": ("23 mentions, 2 urgent, 847 segments listened to",
            "23 menciones, 2 urgentes, 847 segmentos escuchados",
            "23 sebutan, 2 mendesak, 847 segmen didengarkan"),
    "v4p": ("Radio Norte opens with the tender; Canal 5 covers the suspended works; Radio Sur is positive about the cultural centre.",
            "Radio Norte abre con el pliego; Canal 5 recoge la suspensión de obras; Radio Sur, positiva con el centro cultural.",
            "Radio Norte membuka dengan isu tender; Canal 5 meliput penghentian proyek; Radio Sur, positif soal pusat budaya."),
    "v4r1": ("2 urgent", "2 urgentes", "2 mendesak"), "v4r2": ("4 sources", "4 fuentes", "4 sumber"),
    "v4r3": ("PDF",) * 3,
    # ---- método: lo que las cifras no dicen
    "limits_h": (
        "Limits",
        "Límites",
        "Batasan"),
    "limits_lead": (
        "These limits apply to every published figure.",
        "Estos límites valen para toda cifra publicada.",
        "Batasan ini berlaku untuk setiap angka yang dipublikasikan."),
    "ml1m": ("Limit 1", "Límite 1", "Batasan 1"),
    "ml1h": (
        "Transcription errors",
        "Errores de transcripción",
        "Kesalahan transkripsi"),
    "ml1p": (
        "The speech-recognition program mishears names, acronyms and brands. A misheard word is not counted, so figures tend to be low.",
        "El programa de reconocimiento de voz oye mal nombres, siglas y marcas. Una palabra mal oída no se cuenta, de modo que las cifras tienden a ser bajas.",
        "Program pengenalan suara salah dengar nama, singkatan, dan merek. Kata yang salah dengar tidak dihitung, sehingga angka cenderung rendah."),
    "ml1x": ("Try several spellings of the same name", "Prueba varias grafías del mismo nombre", "Coba beberapa ejaan untuk nama yang sama"),
    "ml2m": ("Limit 2", "Límite 2", "Batasan 2"),
    "ml2h": (
        "Recorded hours only",
        "Solo las horas grabadas",
        "Hanya jam yang direkam"),
    "ml2p": (
        "A station that was not recorded at some hour tells nothing about what it broadcast then. Absence from the recording does not mean it was not said.",
        "Una emisora que no se grabó a cierta hora no dice nada de lo que emitió entonces. Que no esté en la grabación no significa que no se dijera.",
        "Stasiun yang tidak direkam pada jam tertentu tidak menunjukkan apa yang disiarkannya saat itu. Tidak ada dalam rekaman tidak berarti tidak dikatakan."),
    "ml2x": ("The coverage table shows what is recorded", "La tabla de cobertura muestra qué hay grabado", "Tabel cakupan menunjukkan apa yang direkam"),
    "ml3m": ("Limit 3", "Límite 3", "Batasan 3"),
    "ml3h": (
        "Music and advertising",
        "Música y publicidad",
        "Musik dan iklan"),
    "ml3p": (
        "Recorded minutes include songs and adverts. A word inside an advert is counted.",
        "Los minutos grabados incluyen canciones y anuncios. Una palabra dentro de un anuncio se cuenta.",
        "Menit rekaman mencakup lagu dan iklan. Kata di dalam iklan dihitung."),
    "ml3x": ("", "", ""),
    "ml4m": ("Limit 4", "Límite 4", "Batasan 4"),
    "ml4h": ("Comparing stations", "Comparar emisoras", "Membandingkan stasiun"),
    "ml4p": (
        "A music station and a news station cannot be compared directly. Compare stations of the same type, or the same word over time.",
        "Una emisora musical y una informativa no se pueden comparar directamente. Compara emisoras del mismo tipo, o la misma palabra a lo largo del tiempo.",
        "Stasiun musik dan stasiun berita tidak dapat dibandingkan langsung. Bandingkan stasiun sejenis, atau satu kata dari waktu ke waktu."),
    "ml4x": ("", "", ""),
    "ml5m": ("Limit 5", "Límite 5", "Batasan 5"),
    "ml5h": ("Rounding and hidden figures", "Redondeo y cifras ocultas", "Pembulatan dan angka tersembunyi"),
    "ml5p": ("Public figures are rounded to multiples of 5 and hidden below 3 minutes. With exact low figures, someone could tell whether a named person was mentioned at a given moment. Totals may not add up exactly.",
             "Las cifras públicas se redondean a múltiplos de 5 y se ocultan por debajo de 3 minutos. Con cifras exactas y bajas se podría saber si se habló de una persona concreta en un momento concreto. Los totales pueden no sumar exactamente.",
             "Angka publik dibulatkan ke kelipatan 5 dan disembunyikan di bawah 3 menit. Dengan angka rendah yang persis, orang bisa mengetahui apakah seseorang disebut pada saat tertentu. Total bisa tidak persis sama."),
    "ml5x": ("", "", ""),
    "ml6m": ("Citing", "Citar", "Mengutip"),
    "ml6h": (
        "Citing a figure",
        "Citar una cifra",
        "Mengutip angka"),
    "ml6p": (
        "Cite the permanent link of the comparison and the date it was consulted. Figures change when recordings are added.",
        "Cita el enlace fijo de la comparación y la fecha de consulta. Las cifras cambian cuando se añaden grabaciones.",
        "Kutip tautan permanen perbandingan dan tanggal akses. Angka berubah saat rekaman ditambahkan."),
    "ml6x": (CITA,
             "Zonorah (2026). Minutos al aire por cada 100 horas grabadas. Consulta del [fecha], términos: [términos]. [enlace de la comparación]",
             "Zonorah (2026). Menit siaran per 100 jam rekaman. Diakses [tanggal], istilah: [istilah]. [tautan perbandingan]"),
    # ---- investigación
    "research_lead": (
        "Two lines of work share the same recordings: open data, and studies carried out on commission.",
        "Dos líneas de trabajo comparten las mismas grabaciones: datos abiertos y estudios hechos por encargo.",
        "Dua lini kerja memakai rekaman yang sama: data terbuka dan studi yang dikerjakan atas pesanan."),
    "rr1m": ("Scientific research", "Investigación científica", "Riset ilmiah"),
    "rr1h": ("Open data", "Datos abiertos", "Data terbuka"),
    "rr1p": ("For researchers, teachers and journalists. The comparator, the charts, the CSV files and the El Niño index follow rules that are published and fixed, so anyone can check them. An AI assistant answers from the transcripts and quotes short fragments with their station and time.",
             "Para investigadores, docentes y periodistas. El comparador, los gráficos, los CSV y el índice de El Niño siguen reglas publicadas y fijas, y cualquiera puede comprobarlas. Un asistente de IA responde a partir de las transcripciones y cita fragmentos breves con su emisora y su hora.",
             "Untuk peneliti, pengajar, dan jurnalis. Pembanding, grafik, berkas CSV, dan indeks El Niño mengikuti aturan yang dipublikasikan dan tetap, sehingga siapa pun bisa memeriksanya. Asisten AI menjawab dari transkrip dan mengutip potongan singkat beserta stasiun dan waktunya."),
    "rr1x": ("Every figure: minutes on air per 100 hours recorded", "Toda cifra: minutos al aire por cada 100 horas grabadas", "Setiap angka: menit siaran per 100 jam rekaman"),
    "rr2m": ("Commercial research", "Investigación comercial", "Riset komersial"),
    "rr2h": ("Studies on commission", "Estudios a medida", "Studi pesanan"),
    "rr2p": (
        "An organisation chooses the sources, keywords and rules. Each mention is entered on a fixed form, including risk and urgency, and a PDF is sent by email on the schedule the organisation chooses. The public data does not show who commissioned what.",
        "Una organización elige las fuentes, las palabras clave y las reglas. Cada mención se anota en una ficha fija, con su riesgo y su urgencia, y se envía un PDF por correo en el horario que la organización elija. Los datos públicos no muestran quién encargó qué.",
        "Sebuah organisasi memilih sumber, kata kunci, dan aturan. Setiap sebutan dicatat pada formulir tetap, termasuk risiko dan urgensinya, dan PDF dikirim lewat email sesuai jadwal yang dipilih organisasi. Data publik tidak menunjukkan siapa memesan apa."),
    "rr2x": ("Not tied to a country: the client picks the stations and their language. Reports in English, Spanish or Indonesian", "Sin atarse a un país: el cliente elige las emisoras y su idioma. Informes en inglés, español o indonesio", "Tidak terikat negara: klien memilih stasiun dan bahasanya. Laporan dalam bahasa Inggris, Spanyol, atau Indonesia"),
    "rr3m": ("Foundations", "Fundamentos", "Landasan"),
    "rr3h": (
        "Origin of the approach",
        "Origen del enfoque",
        "Asal pendekatan"),
    "rr3p": (
        "The Media Neuroscience Lab at UC Santa Barbara works, among other topics, on moral narratives in news and entertainment, text mining and large media datasets. Zonorah uses that computational approach. It does no brain imaging and runs no experiments with participants. Research on the brain is done separately and uses these figures.",
        "El Media Neuroscience Lab de la UC Santa Bárbara trabaja, entre otros temas, en narrativas morales en noticias y entretenimiento, minería de texto y grandes conjuntos de datos de medios. Zonorah usa ese enfoque computacional. No hace imágenes cerebrales ni experimentos con participantes. La investigación sobre el cerebro se hace aparte y usa estas cifras.",
        "Media Neuroscience Lab di UC Santa Barbara meneliti antara lain narasi moral dalam berita dan hiburan, penambangan teks, dan kumpulan data media berskala besar. Zonorah memakai pendekatan komputasional itu. Zonorah tidak melakukan pencitraan otak dan tidak menjalankan eksperimen dengan partisipan. Riset tentang otak dikerjakan terpisah dan memakai angka-angka ini."),
    "rr3x": ("medianeuroscience.org ↗", "medianeuroscience.org ↗", "medianeuroscience.org ↗"),
    # ---- datos
    "data_lead": (
        "How many minutes a word was on air, by station and by day.",
        "Cuántos minutos estuvo al aire una palabra, por emisora y por día.",
        "Berapa menit sebuah kata tayang, menurut stasiun dan hari."),
    "dr1m": ("Compare", "Comparar", "Bandingkan"),
    "dr1h": (
        "Comparator",
        "Comparador",
        "Pembanding"),
    "dr1p": (
        "Up to four words at once, grouped by station, day, hour, region or type of station. The search ignores capital letters and accents and includes variants.",
        "Hasta cuatro palabras a la vez, agrupadas por emisora, día, hora, región o tipo de emisora. La búsqueda ignora mayúsculas y tildes e incluye variantes.",
        "Hingga empat kata sekaligus, dikelompokkan menurut stasiun, hari, jam, wilayah, atau jenis stasiun. Pencarian mengabaikan huruf besar dan aksen serta mencakup variannya."),
    "dr1x": ("The coverage table shows which stations and hours are recorded", "La tabla de cobertura muestra qué emisoras y horas están grabadas", "Tabel cakupan menunjukkan stasiun dan jam yang direkam"),
    "dr2m": ("Download", "Descargar", "Unduh"),
    "dr2h": (
        "Downloads and charts",
        "Descargas y gráficos",
        "Unduhan dan grafik"),
    "dr2p": (
        "Each comparison downloads as a CSV file with the same columns as the table. The same comparison can be embedded in an article as a chart that shows its source.",
        "Cada comparación se descarga como CSV con las mismas columnas que la tabla. La misma comparación se puede insertar en una nota como gráfico que muestra su fuente.",
        "Setiap perbandingan diunduh sebagai berkas CSV dengan kolom yang sama dengan tabel. Perbandingan yang sama dapat disematkan di artikel sebagai grafik yang menampilkan sumbernya."),
    "dr2x": ("", "", ""),
    "dr3m": ("Ask", "Preguntar", "Tanya"),
    "dr3h": (
        "AI assistant",
        "Asistente de IA",
        "Asisten AI"),
    "dr3p": (
        "It summarises the transcripts and quotes short fragments with station and time. It does not give names or data of private individuals. Transcripts are automatic, so a summary can contain mistakes.",
        "Resume las transcripciones y cita fragmentos breves con emisora y hora. No da nombres ni datos de personas privadas. Las transcripciones son automáticas, así que un resumen puede tener errores.",
        "Ia merangkum transkrip dan mengutip potongan singkat beserta stasiun dan waktu. Ia tidak memberikan nama atau data orang pribadi. Transkrip dibuat otomatis, jadi ringkasan bisa mengandung kesalahan."),
    "dr3x": ("", "", ""),
    "access_h": ("Access", "Acceso", "Akses"),
    # ---- estudios de muestra
    "studies_lead": (
        "One report per sector, from the week of 2 to 8 September 2026. They are in Spanish.",
        "Un informe por sector, de la semana del 2 al 8 de septiembre de 2026.",
        "Satu laporan per sektor, dari minggu 2 sampai 8 September 2026. Berbahasa Spanyol."),
    "inf_h": ("Sample studies", "Estudios de muestra", "Studi contoh"),
    "inf_meta": (
        "2 to 8 September 2026 · 29 radio and TV stations · 296 hours of audio · reports in Spanish",
        "2 al 8 de septiembre de 2026 · 29 emisoras de radio y TV · 296 horas de audio",
        "2 sampai 8 September 2026 · 29 stasiun radio dan TV · 296 jam audio · berbahasa Spanyol"),
    "inf_data": ("{n} mentions · {p} pp · PDF", "{n} menciones · {p} págs · PDF", "{n} sebutan · {p} hlm · PDF"),
    "inf_dl": ("Download PDF", "Descargar PDF", "Unduh PDF"),
    "inf_alt": ("Cover of the study {name}", "Portada del estudio {name}", "Sampul studi {name}"),
    # ---- acceso y precios
    "precios_h": ("Access", "Acceso", "Akses"),
    "precios_lead": ("All plans are free until 31 December 2026. No payment details.",
                     "Todos los planes son gratis hasta el 31 de diciembre de 2026. Sin datos de pago.",
                     "Semua paket gratis hingga 31 Desember 2026. Tanpa data pembayaran."),
    "p1n": ("Professional", "Profesional", "Profesional"), "p2n": ("Intensive", "Intensivo", "Intensif"),
    "p3n": ("Newsroom", "Redacción", "Redaksi"),
    "p_pop": ("Most chosen", "Más elegido", "Paling banyak dipilih"),
    "p1b": ("For journalists, teachers and researchers.", "Para periodistas, docentes e investigadores.", "Untuk jurnalis, pengajar, dan peneliti."),
    "p2b": ("For people who use the data every day.", "Para quien usa los datos cada día.", "Untuk yang memakai data setiap hari."),
    "p3b": ("For newsrooms, research teams and agencies.", "Para redacciones, equipos de investigación y agencias.", "Untuk redaksi, tim riset, dan agensi."),
    "p1l1": ("100 AI questions a day", "100 preguntas a la IA al día", "100 pertanyaan AI per hari"),
    "p1l2": ("Comparator and embeddable charts", "Comparador y gráficos para insertar", "Pembanding dan grafik yang dapat disematkan"),
    "p1l3": ("CSV downloads", "Descargas CSV", "Unduhan CSV"),
    "p1l4": ("Statistics laboratory", "Laboratorio de estadística", "Laboratorium statistik"),
    "p2l1": ("500 AI questions a day", "500 preguntas a la IA al día", "500 pertanyaan AI per hari"),
    "p2l2": ("Everything in Professional", "Todo lo de Profesional", "Semua fitur Profesional"),
    "p2l3": ("5 times more questions", "5 veces más consultas", "Pertanyaan 5 kali lebih banyak"),
    "p2l4": ("Free until 31/12", "Gratis hasta el 31/12", "Gratis hingga 31/12"),
    "p3l1": ("2,000 AI questions a day", "2.000 preguntas a la IA al día", "2.000 pertanyaan AI per hari"),
    "p3l2": ("Everything in Intensive", "Todo lo de Intensivo", "Semua fitur Intensif"),
    "p3l3": ("20 times more questions", "20 veces más consultas", "Pertanyaan 20 kali lebih banyak"),
    "p3l4": ("Free until 31/12", "Gratis hasta el 31/12", "Gratis hingga 31/12"),
    # ---- plan gratis: una escucha
    "free_h": ("Free plan", "Plan gratis", "Paket gratis"),
    "free_p": ("One source and 1 hour of listening a week. No card. If you use it up, wait 7 days for it to come back, or subscribe to keep listening.",
               "Un medio y 1 hora de escucha por semana. Sin tarjeta. Si la gastas, esperas 7 días a que se restablezca o te suscribes para seguir.",
               "Satu sumber dan 1 jam pemantauan per minggu. Tanpa kartu. Jika habis, tunggu 7 hari agar kembali, atau berlangganan untuk melanjutkan."),
    "free_cta": ("Start free", "Empezar gratis", "Mulai gratis"),
    "free_hero": ("Free plan · one source · 1 hour of listening a week · no card",
                  "Plan gratis · un medio · 1 hora de escucha por semana · sin tarjeta",
                  "Paket gratis · satu sumber · 1 jam pemantauan per minggu · tanpa kartu"),
    "p_cta": ("Activate for free", "Activar gratis", "Aktifkan gratis"),
    "p_foot": ("Prices are per month, in US dollars (USD). Want a study for your organisation? ",
               "Los precios son al mes, en dólares estadounidenses (USD). ¿Quieres un estudio para tu organización? ",
               "Harga per bulan, dalam dolar AS (USD). Ingin studi untuk organisasi Anda? "),
    "p_foot_a": ("Write to us", "Escríbenos", "Hubungi kami"),
    "mail_subject": ("Study on commission", "Estudio a medida", "Studi pesanan"),
    # ---- términos y reembolsos (borrador pendiente de revisión legal)
    "terms_lead": (
        "How the service, billing and refunds work. It is a draft pending legal review.",
        "Cómo funcionan el servicio, el cobro y los reembolsos. Es un borrador pendiente de revisión legal.",
        "Cara kerja layanan, penagihan, dan pengembalian dana. Ini adalah draf yang menunggu tinjauan hukum."),
    "tm1m": ('Service', 'Servicio', 'Layanan'),
    "tm1h": ('What Zonorah is', 'Qué es Zonorah', 'Apa itu Zonorah'),
    "tm1p": ('Zonorah listens to public radio, television and streaming broadcasts, turns the audio into text and analyses it. You use it through an account. The transcripts and analyses are tools to help you read the media; they are not legal, medical or financial advice.', 'Zonorah escucha emisiones públicas de radio, televisión y streaming, convierte el audio en texto y lo analiza. Se usa con una cuenta. Las transcripciones y los análisis son una ayuda para leer los medios; no son asesoramiento legal, médico ni financiero.', 'Zonorah mendengarkan siaran publik radio, televisi, dan streaming, mengubah audio menjadi teks, lalu menganalisisnya. Layanan digunakan melalui sebuah akun. Transkrip dan analisis adalah alat bantu membaca media; bukan nasihat hukum, medis, atau keuangan.'),
    "tm1x": ("", "", ""),
    "tm2m": ('Plans', 'Planes', 'Paket'),
    "tm2h": ('Free and paid plans', 'Plan gratis y planes de pago', 'Paket gratis dan berbayar'),
    "tm2p": ('The free plan gives one source and 1 hour of listening a week, with no card. When the hour is used up you wait 7 days for it to come back, or you subscribe. Paid plans are monthly, priced in US dollars, and are listed on the plans page.', 'El plan gratis da un medio y 1 hora de escucha por semana, sin tarjeta. Cuando se gasta la hora, esperas 7 días a que vuelva o te suscribes. Los planes de pago son mensuales, en dólares estadounidenses, y están en la página de planes.', 'Paket gratis memberi satu sumber dan 1 jam pemantauan per minggu, tanpa kartu. Setelah jam itu habis, Anda menunggu 7 hari agar kembali, atau berlangganan. Paket berbayar bersifat bulanan, dalam dolar AS, dan tercantum di halaman paket.'),
    "tm2x": ("", "", ""),
    "tm3m": ('Billing', 'Cobro', 'Penagihan'),
    "tm3h": ('Trial, renewal and cancelling', 'Prueba, renovación y cancelación', 'Uji coba, perpanjangan, dan pembatalan'),
    "tm3p": ('Paid plans start with a 7-day free trial that needs a card. There is one trial per account and per card. If you do not cancel before the trial ends, the card is charged and the plan renews every month until you cancel. You can cancel at any time from the billing portal; access continues until the end of the period already paid. Payments are handled by Stripe; Zonorah never sees your card number.', 'Los planes de pago empiezan con 7 días de prueba gratis que piden tarjeta. Hay una prueba por cuenta y por tarjeta. Si no cancelas antes de que termine la prueba, se cobra la tarjeta y el plan se renueva cada mes hasta que canceles. Puedes cancelar cuando quieras desde el portal de facturación; el acceso sigue hasta el final del periodo ya pagado. Los pagos los gestiona Stripe; Zonorah nunca ve el número de tu tarjeta.', 'Paket berbayar dimulai dengan uji coba gratis 7 hari yang memerlukan kartu. Ada satu uji coba per akun dan per kartu. Jika Anda tidak membatalkan sebelum uji coba berakhir, kartu akan ditagih dan paket diperpanjang setiap bulan sampai Anda membatalkan. Anda dapat membatalkan kapan saja dari portal penagihan; akses berlanjut hingga akhir periode yang sudah dibayar. Pembayaran ditangani Stripe; Zonorah tidak pernah melihat nomor kartu Anda.'),
    "tm3x": ("", "", ""),
    "tm4m": ('Refunds', 'Reembolsos', 'Pengembalian dana'),
    "tm4h": ('When money is returned', 'Cuándo se devuelve el dinero', 'Kapan uang dikembalikan'),
    "tm4p": ('Cancelling stops the next charge; it does not return the month already started. If you were charged by mistake, or you cancelled inside the trial and were charged anyway, write to info@zonorah.com within 14 days and the charge will be returned. Where the law of your country gives you a right to a refund, that right applies.', 'Cancelar detiene el siguiente cobro; no devuelve el mes ya empezado. Si te cobraron por error, o cancelaste dentro de la prueba y te cobraron igual, escribe a info@zonorah.com en un plazo de 14 días y se te devolverá el cobro. Si la ley de tu país te da derecho a un reembolso, ese derecho se aplica.', 'Pembatalan menghentikan penagihan berikutnya; tidak mengembalikan bulan yang sudah berjalan. Jika Anda ditagih karena kesalahan, atau membatalkan dalam masa uji coba tetapi tetap ditagih, tulis ke info@zonorah.com dalam 14 hari dan tagihan akan dikembalikan. Jika hukum negara Anda memberi hak pengembalian dana, hak itu berlaku.'),
    "tm4x": ("", "", ""),
    "tm5m": ('Use', 'Uso', 'Penggunaan'),
    "tm5h": ('What you agree not to do', 'Qué te comprometes a no hacer', 'Yang Anda setujui untuk tidak dilakukan'),
    "tm5p": ('Use Zonorah only to follow public broadcasts. Do not try to get around the free-plan limits with repeated accounts, do not resell access, and do not use the reports to harass or to profile private individuals. We may suspend an account that does.', 'Usa Zonorah solo para seguir emisiones públicas. No intentes saltarte los límites del plan gratis con cuentas repetidas, no revendas el acceso y no uses los informes para acosar ni para perfilar a personas privadas. Podemos suspender una cuenta que lo haga.', 'Gunakan Zonorah hanya untuk mengikuti siaran publik. Jangan mencoba menghindari batas paket gratis dengan akun berulang, jangan menjual kembali akses, dan jangan menggunakan laporan untuk melecehkan atau memprofil individu pribadi. Kami dapat menangguhkan akun yang melakukannya.'),
    "tm5x": ("", "", ""),
    "tm6m": ('Accuracy', 'Exactitud', 'Akurasi'),
    "tm6h": ('Automatic transcripts can be wrong', 'Las transcripciones automáticas pueden fallar', 'Transkrip otomatis bisa salah'),
    "tm6p": ('Speech recognition and AI analysis make mistakes: a name can be misheard, a word missed, a tone misread. Check any quote against the source before you publish or act on it. Zonorah gives no guarantee that every mention is found.', 'El reconocimiento de voz y el análisis con IA se equivocan: un nombre puede oírse mal, una palabra perderse, un tono leerse mal. Comprueba cualquier cita con la fuente antes de publicarla o actuar. Zonorah no garantiza que se encuentre cada mención.', 'Pengenalan suara dan analisis AI bisa salah: nama bisa terdengar keliru, kata terlewat, nada disalahbaca. Periksa setiap kutipan dengan sumbernya sebelum menerbitkan atau bertindak. Zonorah tidak menjamin setiap sebutan ditemukan.'),
    "tm6x": ("", "", ""),
    "tm7m": ('Changes', 'Cambios', 'Perubahan'),
    "tm7h": ('Changes and contact', 'Cambios y contacto', 'Perubahan dan kontak'),
    "tm7p": ('These terms are a draft pending legal review and may change; the date at the foot of the page shows the last update. The governing law and the court that decides disputes will be fixed after that review. Questions: info@zonorah.com.', 'Estos términos son un borrador pendiente de revisión legal y pueden cambiar; la fecha al pie de la página indica la última actualización. La ley aplicable y el tribunal que resuelve las disputas se fijarán tras esa revisión. Preguntas: info@zonorah.com.', 'Ketentuan ini adalah draf yang menunggu tinjauan hukum dan dapat berubah; tanggal di bagian bawah halaman menunjukkan pembaruan terakhir. Hukum yang berlaku dan pengadilan yang memutus sengketa akan ditetapkan setelah tinjauan itu. Pertanyaan: info@zonorah.com.'),
    "tm7x": ("", "", ""),
    # ---- privacidad
    "privacy_lead": (
        "No recordings are kept. This page says what is kept about people who sign in. It is a draft pending legal review.",
        "No se guardan grabaciones. Esta página dice qué se guarda de quien inicia sesión. Es un borrador pendiente de revisión legal.",
        "Rekaman tidak disimpan. Halaman ini menjelaskan apa yang disimpan tentang orang yang masuk. Ini adalah draf yang menunggu tinjauan hukum."),
    "pv1m": ("Recordings", "Grabaciones", "Rekaman"),
    "pv1h": ("None are kept", "No se guarda ninguna", "Tidak ada yang disimpan"),
    "pv1p": ("The audio is deleted as soon as it has been turned into text. Only the text stays.",
             "El audio se borra en cuanto se convierte en texto. Solo queda el texto.",
             "Audio dihapus segera setelah menjadi teks. Hanya teksnya yang tersisa."),
    "pv1x": ("", "", ""),
    "pv2m": ("Your account", "Tu cuenta", "Akun Anda"),
    "pv2h": ("What is stored if you sign in with Google", "Qué se guarda si entras con Google", "Apa yang disimpan jika Anda masuk dengan Google"),
    "pv2p": ("Your email and name as Google gives them, the date you joined and the date of your last visit, how many questions you ask each day, and which sector reports you download.",
             "Tu correo y tu nombre tal como los da Google, la fecha de alta y la del último acceso, cuántas preguntas haces cada día y qué informes sectoriales descargas.",
             "Email dan nama Anda sebagaimana diberikan Google, tanggal Anda bergabung dan kunjungan terakhir, berapa pertanyaan yang Anda ajukan setiap hari, dan laporan sektor mana yang Anda unduh."),
    "pv2x": ("The password is handled by Google. It is not stored here.", "La contraseña la gestiona Google. Aquí no se guarda.", "Kata sandi dikelola Google. Tidak disimpan di sini."),
    "pv3m": ("Your questions", "Tus preguntas", "Pertanyaan Anda"),
    "pv3h": ("They go to an AI service", "Van a un servicio de IA", "Dikirim ke layanan AI"),
    "pv3p": ("A question is sent to an AI service (Groq, in the United States) without your email or name. The text of your questions is not kept with your account. Please do not write personal data in a question.",
             "Una pregunta se envía a un servicio de IA (Groq, en Estados Unidos) sin tu correo ni tu nombre. El texto de tus preguntas no se guarda junto a tu cuenta. No escribas datos personales en las preguntas.",
             "Sebuah pertanyaan dikirim ke layanan AI (Groq, di Amerika Serikat) tanpa email dan nama Anda. Teks pertanyaan Anda tidak disimpan bersama akun Anda. Jangan menulis data pribadi dalam pertanyaan."),
    "pv3x": ("", "", ""),
    "pv7m": ("Payments", "Pagos", "Pembayaran"),
    "pv7h": ("Stripe handles the card", "La tarjeta la gestiona Stripe", "Stripe mengelola kartu"),
    "pv7p": ("Card payments are processed by Stripe. Zonorah never sees or stores your card number. It keeps your Stripe customer reference, your plan, the status of the subscription and its dates, and a card fingerprint, an identifier Stripe assigns that is not the number, to apply the rule of one free trial per card.",
             "Los pagos con tarjeta los procesa Stripe. Zonorah nunca ve ni guarda el número de tu tarjeta. Guarda tu referencia de cliente en Stripe, tu plan, el estado de la suscripción y sus fechas, y una huella de la tarjeta, un identificador que asigna Stripe y que no es el número, para aplicar la regla de una prueba gratuita por tarjeta.",
             "Pembayaran kartu diproses oleh Stripe. Zonorah tidak pernah melihat atau menyimpan nomor kartu Anda. Zonorah menyimpan referensi pelanggan Stripe Anda, paket, status langganan beserta tanggalnya, dan sidik kartu, pengenal yang diberikan Stripe dan bukan nomornya, untuk menerapkan aturan satu uji coba gratis per kartu."),
    "pv7x": ("Stripe keeps payment records for as long as the law requires.", "Stripe conserva los registros de pago el tiempo que exija la ley.", "Stripe menyimpan catatan pembayaran selama yang diwajibkan hukum."),
    "pv8m": ("Your monitors", "Tus monitoreos", "Pemantauan Anda"),
    "pv8h": ("Saved with your account", "Se guardan con tu cuenta", "Disimpan bersama akun Anda"),
    "pv8p": ("The searches and monitoring requests you save in the platform (keywords, sources, schedules and languages) belong to your account. When you delete the account, the monitors stop and those data are deleted, including the transcripts and reports made for them. The one thing that can stay is a one-way fingerprint of your email, not the email itself, and only while free listening time you already used or a wait for it to come back is still running: it stops deleting and re-creating the account from resetting the free time.",
             "Las búsquedas y las solicitudes de monitoreo que guardas en la plataforma (palabras clave, medios, horarios e idiomas) pertenecen a tu cuenta. Al borrar la cuenta, los monitoreos se detienen y esos datos se borran, incluidas las transcripciones y los informes hechos para ellos. Lo único que puede quedar es una huella de un solo sentido de tu correo, no el correo, y solo mientras siga corriendo tiempo de escucha gratis ya gastado o la espera para recuperarlo: evita que borrar y volver a crear la cuenta restablezca el tiempo gratis.",
             "Pencarian dan permintaan pemantauan yang Anda simpan di platform (kata kunci, sumber, jadwal, dan bahasa) milik akun Anda. Saat Anda menghapus akun, pemantauan berhenti dan data itu dihapus, termasuk transkrip dan laporan yang dibuat untuknya. Satu-satunya yang bisa tersisa adalah sidik satu arah dari email Anda, bukan emailnya, dan hanya selama waktu pemantauan gratis yang sudah terpakai atau masa tunggu untuk memulihkannya masih berjalan: ini mencegah penghapusan dan pembuatan ulang akun mengatur ulang waktu gratis."),
    "pv8x": ("", "", ""),
    "pv4m": ("How long", "Cuánto tiempo", "Berapa lama"),
    "pv4h": ("Until you delete the account", "Hasta que borres la cuenta", "Sampai Anda menghapus akun"),
    "pv4p": ("A session lasts 30 days. Your data stays while the account exists. You can delete the account whenever you want, and everything goes: email, name, sessions and question count.",
             "Una sesión dura 30 días. Tus datos se guardan mientras exista la cuenta. Puedes borrarla cuando quieras y se borra todo: correo, nombre, sesiones y recuento de preguntas.",
             "Satu sesi berlaku 30 hari. Data Anda tersimpan selama akun ada. Anda dapat menghapus akun kapan saja dan semuanya hilang: email, nama, sesi, dan jumlah pertanyaan."),
    "pv4x": ("", "", ""),
    "pv5m": ("Your rights", "Tus derechos", "Hak Anda"),
    "pv5h": ("Access, correction, deletion", "Acceso, rectificación, supresión", "Akses, perbaikan, penghapusan"),
    "pv5p": ("You can ask for access to your data, for it to be corrected or for it to be deleted by writing to " + EMAIL + ".",
             "Puedes pedir acceso a tus datos, que se rectifiquen o que se supriman escribiendo a " + EMAIL + ".",
             "Anda dapat meminta akses ke data Anda, perbaikan, atau penghapusan dengan menulis ke " + EMAIL + "."),
    "pv5x": ("", "", ""),
    "pv6m": ("Status", "Estado", "Status"),
    "pv6h": ("Draft pending legal review", "Borrador pendiente de revisión legal", "Draf menunggu tinjauan hukum"),
    "pv6p": ("The wording may change after the review. Companies that order studies are covered by their own agreement, not by this page.",
             "El texto puede cambiar tras la revisión. Las organizaciones que encargan estudios se rigen por su propio acuerdo, no por esta página.",
             "Teksnya dapat berubah setelah tinjauan. Organisasi yang memesan studi tunduk pada perjanjiannya sendiri, bukan halaman ini."),
    "pv6x": ("", "", ""),
    # ---- contacto (cierra todas las páginas)
    "demo_h": (
        "Contact",
        "Contacto",
        "Kontak"),
    "demo_lead": (
        "To commission a study or ask for access, write with the topics, stations or sources and the language of the report. Researchers working on the brain side can write too.",
        "Para encargar un estudio o pedir acceso, escribe con los temas, emisoras o fuentes y el idioma del informe. Los investigadores que trabajan el lado del cerebro también pueden escribir.",
        "Untuk memesan studi atau meminta akses, tulislah dengan topik, stasiun, atau sumber dan bahasa laporan. Peneliti yang menggarap sisi otak juga boleh menulis."),
    "demo_prices": ("Get access", "Obtener acceso", "Dapatkan akses"),
    "demo_label": ("Your email", "Tu correo", "Email Anda"),
    "demo_ph": ("you@organisation.org", "tu@organizacion.org", "anda@organisasi.org"),
    "demo_send": ("Send", "Enviar", "Kirim"),
    "demo_note": ("Or write to " + EMAIL, "O escribe a " + EMAIL, "Atau tulis ke " + EMAIL),
    # ---- pie
    "f_tag": (
        "Media Neuroscience Lab. Radio, TV and YouTube, recorded, transcribed and counted.",
        "Media Neuroscience Lab. Radio, TV y YouTube, grabados, transcritos y contados.",
        "Media Neuroscience Lab. Radio, TV, dan YouTube, direkam, ditranskripsi, dan dihitung."),
    "f_lab": ("The lab", "El laboratorio", "Laboratorium"), "f_contact": ("Contact", "Contacto", "Kontak"),
    "f_legal": ("Legal", "Legal", "Hukum"),
    "f_up": ("Back to top ↑", "Volver arriba ↑", "Kembali ke atas ↑"),
}


# ---- cobro con Stripe
# Mientras sea False, el sitio dice lo de siempre: gratis hasta el 31 de diciembre, sin datos de pago.
# El día que Stripe esté conectado en la app (bloque `stripe:` de config.yaml), se pone True, se ejecuta
# `python3 build/build.py` y se publica: los precios dejan de ir tachados y el sitio habla de la prueba con tarjeta.
COBRO_ACTIVO = True
PRUEBA_DIAS = 7            # el mismo número que `stripe.prueba_dias` en la app

T_COBRO = {
    "precios_lead": (
        f"Every paid plan starts with a {PRUEBA_DIAS}-day free trial, once per person. A card is required: it is charged when the trial ends unless you cancel before.",
        f"Todos los planes de pago empiezan con {PRUEBA_DIAS} días de prueba gratis, una sola vez por persona. Hace falta tarjeta: se cobra al terminar la prueba si no cancelas antes.",
        f"Setiap paket berbayar dimulai dengan uji coba gratis {PRUEBA_DIAS} hari, hanya sekali per orang. Perlu kartu: ditagih saat uji coba berakhir kecuali Anda membatalkan sebelumnya."),
    "p2l4": (f"{PRUEBA_DIAS}-day free trial", f"{PRUEBA_DIAS} días de prueba gratis", f"Uji coba gratis {PRUEBA_DIAS} hari"),
    "p3l4": (f"{PRUEBA_DIAS}-day free trial", f"{PRUEBA_DIAS} días de prueba gratis", f"Uji coba gratis {PRUEBA_DIAS} hari"),
    "p_cta": ("Start free trial", "Empezar la prueba gratis", "Mulai uji coba gratis"),
    "d_data": (
        "See how many minutes a word got on radio, TV and YouTube, download the table and ask the AI assistant.",
        "Mira cuántos minutos tuvo una palabra en la radio, la TV y YouTube, descarga la tabla y pregunta al asistente de IA.",
        "Lihat berapa menit sebuah kata tayang di radio, TV, dan YouTube, unduh tabelnya, dan tanya asisten AI."),
}


def textos(lang: str) -> dict:
    i = LANGS.index(lang)
    base = {**T, **T_COBRO} if COBRO_ACTIVO else T
    return {k: v[i] for k, v in base.items()}


def comprobar():
    for k, v in T_COBRO.items():
        if k not in T or len(v) != 3 or not all(v):
            raise SystemExit(f"[content] T_COBRO «{k}» no existe en T o no tiene tres textos")
    for k, v in T.items():
        if len(v) != 3 or not all(isinstance(x, str) for x in v):
            raise SystemExit(f"[content] «{k}» necesita exactamente tres textos")
        if not k.endswith("x") and not all(v):
            raise SystemExit(f"[content] «{k}» tiene un texto vacío")
    for p, prefs in FILAS.items():
        for pre in prefs:
            for suf in "mhp":
                if pre + suf not in T:
                    raise SystemExit(f"[content] falta {pre}{suf} de la página «{p}»")
    for lang in LANGS:
        slugs = list(SLUGS[lang].values())
        if len(set(slugs)) != len(slugs):
            raise SystemExit(f"[content] slugs repetidos en {lang}")
