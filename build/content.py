"""Copy de la portada de Zonorah en inglés, español e indonesio.

El DISEÑO no está aquí: vive en `build/plantilla.html`, que es la portada original
sin tocar. Este archivo solo trae los textos que `build.py` pone dentro de ella.

Cada fila es (inglés, español, indonesio): una clave no puede faltar en un idioma.

Voz: un Media Neuroscience Lab. Zonorah es su INSTRUMENTO computacional (transcribe, codifica y
mide los medios); la investigación sobre el cerebro es aparte y se apoya en esos datos. El
vocabulario es de laboratorio (método, corpus, codificación, estudio, datos abiertos), pero cada
afirmación sale de la metodología publicada (`~/Zonorah/zonorah/web/estaticos/metodologia.html`),
de `planes.py` o del código del análisis. Nada de «24 horas», «audio guardado», «alerta en 3
minutos» ni «RGPD», y nada que sugiera que Zonorah mide actividad cerebral. Si no se puede
defender, no entra.
"""

EMAIL = "hola@zonorah.com"
SITE = "https://zonorah.com"
LAB_URL = "https://www.medianeuroscience.org/"
UPDATED = "2026-11-24"
CITA = ("Zonorah (2026). Memoria de los medios del Perú: minutos al aire por "
        "cada 100 horas grabadas.")

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

# clave: (en, es, id)
T = {
    # ---- cabecera del documento
    "title": ("Zonorah · Media Neuroscience Lab: open media data from Peru",
              "Zonorah · Media Neuroscience Lab: datos abiertos de medios",
              "Zonorah · Media Neuroscience Lab: data media terbuka dari Peru"),
    "og_title": ("Zonorah · Media Neuroscience Lab",) * 3,
    "description": (
        "Zonorah is a Media Neuroscience Lab. Our instrument transcribes Peruvian radio, TV and YouTube and measures what is said: open data and applied studies.",
        "Zonorah es un Media Neuroscience Lab. Nuestro instrumento transcribe radio, TV y YouTube del Perú y mide lo que se dice: datos abiertos y estudios aplicados.",
        "Zonorah adalah Media Neuroscience Lab. Instrumen kami mentranskripsi radio, TV, YouTube Peru dan mengukur apa yang dikatakan: data terbuka dan studi terapan."),
    "updated": ("Last updated", "Actualizado", "Diperbarui"),
    # ---- accesibilidad
    "aria_nav": ("Main navigation", "Navegación principal", "Navigasi utama"),
    "aria_lang": ("Change language", "Cambiar idioma", "Ganti bahasa"),
    "aria_menu": ("Menu", "Menú", "Menu"),
    "menu_open": ("Open menu", "Abrir menú", "Buka menu"),
    "menu_close": ("Close menu", "Cerrar menú", "Tutup menu"),
    "aria_logos": ("Stations and channels in the corpus", "Emisoras y canales del corpus", "Stasiun dan kanal dalam korpus"),
    # ---- navegación
    "n_how": ("Method", "Método", "Metode"),
    "n_research": ("Research", "Investigación", "Riset"),
    "n_chat": ("Ask the corpus", "Pregunta al corpus", "Tanya korpus"),
    "n_learn": ("Learn", "Aprende", "Belajar"),
    "n_plans": ("Access", "Acceso", "Akses"),
    "n_seeplans": ("Access plans", "Planes de acceso", "Paket akses"),
    "n_dash": ("Client dashboard", "Panel de clientes", "Dasbor klien"),
    "n_login": ("Sign in / Sign up", "Iniciar sesión / Registrarse", "Masuk / Daftar"),
    "n_logout": ("Sign out", "Salir", "Keluar"),
    "n_tochat": (" · go to chat", " · ir al chat", " · ke chat"),
    "cur_go": ("Go", "Ir", "Buka"), "cur_view": ("View", "Ver", "Lihat"),
    "cur_down": ("Down", "Bajar", "Turun"), "cur_pdf": ("Open PDF", "Abrir PDF", "Buka PDF"),
    # ---- hero
    "h1a": ("Zonorah.",) * 3, "h1b": ("Media Neuroscience",) * 3, "h1c": ("Lab.",) * 3,
    "hero_lead": (
        "Research on media and the brain. Our computational instrument transcribes Peruvian radio, television and YouTube into a corpus and measures what is said: how much, where, when, by whom and how it is framed.",
        "Investigación sobre los medios y el cerebro. Nuestro instrumento computacional transcribe radio, televisión y YouTube del Perú en un corpus y mide lo que se dice: cuánto, dónde, cuándo, quién y con qué encuadre.",
        "Riset tentang media dan otak. Instrumen komputasional kami mentranskripsi radio, televisi, dan YouTube Peru menjadi korpus dan mengukur apa yang dikatakan: seberapa banyak, di mana, kapan, oleh siapa, dan bagaimana pembingkaiannya."),
    "hero_cta1": ("Explore the open data", "Explorar los datos abiertos", "Jelajahi data terbuka"),
    "hero_cta2": ("Our method", "Nuestro método", "Metode kami"),
    # ---- la pregunta (citas flotantes = preguntas de investigación)
    "q1": ("How much airtime does a topic get?", "¿Cuánto tiempo al aire recibe un tema?", "Berapa lama sebuah topik tayang di udara?"),
    "q2": ("Which stations carry it?", "¿Qué emisoras lo tratan?", "Stasiun mana yang menyiarkannya?"),
    "q3": ("At what hours does it enter the day?", "¿A qué horas entra en el día?", "Pada jam berapa topik itu muncul?"),
    "q4": ("Whose voice frames it?", "¿Qué voz lo enmarca?", "Suara siapa yang membingkainya?"),
    "q5": ("How is the same event framed?", "¿Cómo se enmarca el mismo hecho?", "Bagaimana peristiwa yang sama dibingkai?"),
    "q6": ("Evidence, or rumour?", "¿Evidencia o rumor?", "Bukti, atau rumor?"),
    "q7": ("What changed since last week?", "¿Qué cambió desde la semana pasada?", "Apa yang berubah sejak minggu lalu?"),
    "problema_h": (
        "Before asking what media do to the brain, measure what the media say.",
        "Antes de preguntar qué hacen los medios al cerebro, mide lo que dicen los medios.",
        "Sebelum bertanya apa yang dilakukan media terhadap otak, ukur apa yang dikatakan media."),
    # ---- método
    "como_h": ("Method", "Método", "Metode"),
    "step": ("Step", "Paso", "Langkah"),
    "s1r": ("Live · schedule windows", "En directo · franjas", "Langsung · jam siaran"),
    "s2r": ("Whisper · local", "Whisper · en local", "Whisper · lokal"),
    "s3r": ("Coding · closed fields", "Codificación · campos cerrados", "Pengodean · kolom tertutup"),
    "s4r": ("Open data · reports", "Datos abiertos · informes", "Data terbuka · laporan"),
    "s1t": ("Acquisition", "Adquisición", "Akuisisi"),
    "s2t": ("Transcription", "Transcripción", "Transkripsi"),
    "s3t": ("Coding", "Codificación", "Pengodean"),
    "s4t": ("Output", "Resultados", "Keluaran"),
    "s1p": ("We receive each station's live signal over the internet and record it in the time windows of its schedule.",
            "Recibimos la señal en directo de cada emisora por internet y la grabamos en las franjas horarias de su parrilla.",
            "Kami menerima sinyal langsung setiap stasiun melalui internet dan merekamnya pada jam-jam sesuai jadwal siarannya."),
    "s2p": ("A speech-recognition model runs locally and turns audio into timestamped text. Audio is deleted as soon as it is transcribed, so the corpus is text only.",
            "Un modelo de reconocimiento de voz corre en local y convierte el audio en texto con marca de tiempo. El audio se borra en cuanto se transcribe: el corpus es solo texto.",
            "Model pengenalan suara berjalan secara lokal dan mengubah audio menjadi teks berpenanda waktu. Audio dihapus segera setelah ditranskripsi, sehingga korpus hanya berupa teks."),
    "s3p": ("Terms are searched with their variants. Each relevant passage is coded in closed fields: speaker, role of the subject, topic, tone, framing, and evidence or rumour.",
            "Se buscan los términos con sus variantes. Cada pasaje relevante se codifica en campos cerrados: quién habla, papel del sujeto, tema, tono, encuadre y evidencia o rumor.",
            "Istilah dicari beserta variannya. Setiap bagian yang relevan dikodekan dalam kolom tertutup: pembicara, peran subjek, topik, nada, pembingkaian, serta bukti atau rumor."),
    "s4p": ("Figures go to Zonorah Data as minutes on air per 100 hours recorded. Commissioned studies arrive as a PDF by email on the schedule you choose.",
            "Las cifras van a Zonorah Datos como minutos al aire por cada 100 horas grabadas. Los estudios a medida llegan en PDF por correo en el horario que elijas.",
            "Angka masuk ke Zonorah Data sebagai menit siaran per 100 jam rekaman. Studi pesanan tiba sebagai PDF melalui email sesuai jadwal yang Anda pilih."),
    "s1g1": ("Radio", "Radio", "Radio"), "s1g2": ("TV", "TV", "TV"), "s1g3": ("YouTube",) * 3,
    "s1g4": ("Schedules", "Franjas", "Jadwal"),
    "s2g1": ("Timestamps", "Marcas de tiempo", "Penanda waktu"),
    "s2g2": ("Local model", "Modelo local", "Model lokal"),
    "s2g3": ("Text-only corpus", "Corpus solo de texto", "Korpus teks saja"),
    "s3g1": ("Tone", "Tono", "Nada"), "s3g2": ("Speaker", "Actor", "Pembicara"),
    "s3g3": ("Topic", "Tema", "Topik"), "s3g4": ("Framing", "Encuadre", "Pembingkaian"),
    "s4g1": ("Open data", "Datos abiertos", "Data terbuka"), "s4g2": ("PDF",) * 3,
    "s4g3": ("Email", "Correo", "Email"),
    # visual del paso 3 (ejemplo ilustrativo)
    "v3a": ("Who speaks?", "¿Quién habla?", "Siapa yang bicara?"),
    "v3av": ("Municipal spokesperson", "Portavoz municipal", "Juru bicara pemkot"),
    "v3b": ("About what?", "¿De qué?", "Tentang apa?"),
    "v3bv": ("Tender · award", "Adjudicación · pliego", "Penetapan pemenang · tender"),
    "v3c": ("Tone?", "¿Tono?", "Nada?"),
    "v3cv": ("Negative", "Negativo", "Negatif"),
    "v3d": ("Evidence or rumour?", "¿Evidencia o rumor?", "Bukti atau rumor?"),
    "v3dv": ("Rumour", "Rumor", "Rumor"),
    # visual del paso 4 (informe de ejemplo)
    "v4t": ("Zonorah · Study report", "Zonorah · Informe del estudio", "Zonorah · Laporan studi"),
    "v4h": ("23 mentions, 2 urgent, 847 segments listened to",
            "23 menciones, 2 urgentes, 847 segmentos escuchados",
            "23 sebutan, 2 mendesak, 847 segmen didengarkan"),
    "v4p": ("Radio Norte opens with the tender; Canal 5 covers the suspended works; RPP, positive about the cultural centre.",
            "Radio Norte abre con el pliego; Canal 5 recoge la suspensión de obras; RPP, positivo con el centro cultural.",
            "Radio Norte membuka dengan isu tender; Canal 5 meliput penghentian proyek; RPP, positif soal pusat budaya."),
    "v4r1": ("2 urgent", "2 urgentes", "2 mendesak"), "v4r2": ("4 sources", "4 fuentes", "4 sumber"),
    "v4r3": ("PDF",) * 3,
    # ---- investigación: dos frentes (+ límites, protección de datos, fundamentos)
    "casos_h": ("Two fronts, one instrument", "Dos frentes, un instrumento", "Dua lini, satu instrumen"),
    "casos_lead": (
        "Zonorah is a Media Neuroscience Lab. Its computational instrument measures the media side of the question; our research on the brain side is separate and builds on that data.",
        "Zonorah es un Media Neuroscience Lab. Su instrumento computacional mide el lado de los medios de la pregunta; nuestra investigación sobre el cerebro es aparte y se apoya en esos datos.",
        "Zonorah adalah Media Neuroscience Lab. Instrumen komputasionalnya mengukur sisi media dari pertanyaan; riset kami di sisi otak berjalan terpisah dan bertumpu pada data tersebut."),
    "c1m": ("Scientific research", "Investigación científica", "Riset ilmiah"),
    "c1h": ("Open data on the media side", "Datos abiertos del lado de los medios", "Data terbuka dari sisi media"),
    "c1p": (
        "Published, literal rules, such as the El Niño index, and aggregate open data for journalists, teachers and researchers: a comparator, embeddable charts, CSV downloads and an AI assistant that quotes short fragments with their station and time.",
        "Reglas literales y publicadas, como el índice de El Niño, y datos abiertos agregados para periodistas, docentes e investigadores: comparador, gráficos para insertar, descargas CSV y un asistente de IA que cita fragmentos breves con su emisora y su hora.",
        "Aturan harfiah yang dipublikasikan, seperti indeks El Niño, dan data terbuka agregat untuk jurnalis, pengajar, dan peneliti: pembanding, grafik yang dapat disematkan, unduhan CSV, dan asisten AI yang mengutip potongan singkat beserta stasiun dan waktunya."),
    "c1x": ("Every figure: minutes on air per 100 hours recorded",
            "Toda cifra: minutos al aire por cada 100 horas grabadas",
            "Setiap angka: menit siaran per 100 jam rekaman"),
    "c2m": ("Commercial research", "Investigación comercial", "Riset komersial"),
    "c2h": ("Applied media studies", "Estudios aplicados de medios", "Studi media terapan"),
    "c2p": (
        "Organisations define the sources, keywords and rules. Each mention is coded for speaker, topic, tone, framing, evidence or rumour, risk and urgency, and delivered as a PDF study by email.",
        "Las organizaciones definen las fuentes, las palabras clave y las reglas. Cada mención se codifica: quién habla, tema, tono, encuadre, evidencia o rumor, riesgo y urgencia, y se entrega como estudio en PDF por correo.",
        "Organisasi menentukan sumber, kata kunci, dan aturan. Setiap sebutan dikodekan: pembicara, topik, nada, pembingkaian, bukti atau rumor, risiko, dan urgensi, lalu dikirim sebagai studi PDF melalui email."),
    "c2x": (
        "A commission is private: public data never reveals who asked for what",
        "Un encargo es privado: los datos públicos nunca revelan quién pidió qué",
        "Pesanan bersifat privat: data publik tidak pernah mengungkap siapa yang meminta apa"),
    "c3m": ("Zonorah Data", "Zonorah Datos", "Zonorah Data"),
    "c3h": ("The lab's open instrument", "El instrumento abierto del laboratorio", "Instrumen terbuka laboratorium"),
    "c3p": (
        "The comparator contrasts any term across stations, days and regions. A figure is cited with the permanent link of its comparison and the date of consultation.",
        "El comparador contrasta cualquier término entre emisoras, días y regiones. Una cifra se cita con el enlace fijo de su comparación y la fecha de consulta.",
        "Pembanding membandingkan istilah apa pun antarstasiun, hari, dan wilayah. Angka dikutip dengan tautan permanen perbandingannya dan tanggal akses."),
    "c3x": ("Cite as: " + CITA, "Cita así: " + CITA, "Kutip sebagai: " + CITA),
    "c4m": ("Method limits", "Límites del método", "Batasan metode"),
    "c4h": ("What the figures do not say", "Lo que las cifras no dicen", "Yang tidak dikatakan angka"),
    "c4p": ("Transcription is automatic and errs on names, acronyms and brands, so figures tend to fall short. Only what was recorded is measured, music and adverts count, and figures are rounded.",
            "La transcripción es automática y falla con nombres, siglas y marcas, así que las cifras tienden a quedarse cortas. Solo se mide lo que se grabó, la música y la publicidad cuentan, y las cifras se redondean.",
            "Transkripsi dilakukan otomatis dan keliru pada nama, singkatan, dan merek, sehingga angka cenderung lebih rendah. Hanya yang direkam yang diukur, musik dan iklan ikut dihitung, dan angka dibulatkan."),
    "c4x": ("“Not recorded” is not the same as “not said”", "«No se grabó» no es lo mismo que «no se dijo»", "«Tidak direkam» tidak sama dengan «tidak dikatakan»"),
    "c5m": ("Data protection", "Protección de datos", "Perlindungan data"),
    "c5h": ("No recordings kept", "No guardamos grabaciones", "Rekaman tidak disimpan"),
    "c5p": (
        "Audio is deleted as soon as it is transcribed. Questions to the AI assistant go to an AI service (Groq, United States) without email or name. Accounts and their data can be deleted at any time.",
        "El audio se borra en cuanto se transcribe. Las preguntas al asistente de IA van a un servicio de IA (Groq, Estados Unidos) sin correo ni nombre. Las cuentas y sus datos se pueden borrar en cualquier momento.",
        "Audio dihapus segera setelah ditranskripsi. Pertanyaan kepada asisten AI dikirim ke layanan AI (Groq, Amerika Serikat) tanpa email dan nama. Akun beserta datanya dapat dihapus kapan saja."),
    "c5x": ("Access, correction or deletion: " + EMAIL, "Acceso, rectificación o supresión: " + EMAIL, "Akses, perbaikan, atau penghapusan: " + EMAIL),
    "c6m": ("Scientific foundations", "Fundamentos científicos", "Landasan ilmiah"),
    "c6h": ("Computational media neuroscience", "Neurociencia de los medios computacional", "Neurosains media komputasional"),
    "c6p": ("Zonorah takes the computational side of media neuroscience, such as the work of the Media Neuroscience Lab at UC Santa Barbara on moral narratives, text mining and large media datasets. The instrument does not do brain imaging or experiments with participants.",
            "Zonorah toma el lado computacional de la neurociencia de los medios, como el trabajo del Media Neuroscience Lab de la UC Santa Bárbara sobre narrativas morales, minería de texto y grandes conjuntos de datos de medios. El instrumento no hace imágenes cerebrales ni experimentos con participantes.",
            "Zonorah mengambil sisi komputasional dari neurosains media, seperti karya Media Neuroscience Lab di UC Santa Barbara tentang narasi moral, penambangan teks, dan kumpulan data media berskala besar. Instrumen ini tidak melakukan pencitraan otak atau eksperimen dengan partisipan."),
    # ---- estudios de muestra
    "inf_h": ("Sample studies", "Estudios de muestra", "Studi contoh"),
    "inf_meta": (
        "Peru · 2 to 8 September 2026 · 29 radio and TV stations · 296 hours of audio · sample studies, reports in Spanish",
        "Perú · 2 al 8 de septiembre de 2026 · 29 emisoras de radio y TV · 296 horas de audio · estudios de muestra",
        "Peru · 2 sampai 8 September 2026 · 29 stasiun radio dan TV · 296 jam audio · studi contoh"),
    "inf_data": ("{n} mentions · {p} pp · PDF", "{n} menciones · {p} págs · PDF", "{n} sebutan · {p} hlm · PDF"),
    "inf_dl": ("Download PDF", "Descargar PDF", "Unduh PDF"),
    "inf_alt": ("Cover of the study {name}", "Portada del estudio {name}", "Sampul studi {name}"),
    # ---- acceso y precios
    "precios_h": ("Access", "Acceso", "Akses"),
    "precios_lead": ("All access plans are free until 31 December 2026. No payment details.",
                     "Todos los planes de acceso, gratis hasta el 31 de diciembre de 2026. Sin datos de pago.",
                     "Semua paket akses gratis hingga 31 Desember 2026. Tanpa data pembayaran."),
    "p1n": ("Professional", "Profesional", "Profesional"), "p2n": ("Intensive", "Intensivo", "Intensif"),
    "p3n": ("Newsroom", "Redacción", "Redaksi"),
    "p_pop": ("Most chosen", "Más elegido", "Paling banyak dipilih"),
    "p1b": ("For journalists, teachers and researchers.", "Para periodistas, docentes e investigadores.", "Untuk jurnalis, pengajar, dan peneliti."),
    "p2b": ("For research that works with the data daily.", "Para investigación que trabaja con los datos a diario.", "Untuk riset yang bekerja dengan data setiap hari."),
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
    "p_cta": ("Activate for free", "Activar gratis", "Aktifkan gratis"),
    "p_foot": ("Prices per month, in soles (PEN). A study for your organisation? ",
               "Precios al mes, en soles. ¿Un estudio para tu organización? ",
               "Harga per bulan, dalam sol Peru (PEN). Studi untuk organisasi Anda? "),
    "p_foot_a": ("Write to us", "Escríbenos", "Hubungi kami"),
    "mail_subject": ("Commissioned study", "Estudio a medida", "Studi pesanan"),
    # ---- contacto
    "demo_h": ("Commission a study, or ask for access.", "Encarga un estudio o pide acceso.", "Pesan studi, atau minta akses."),
    "demo_lead": (
        "Researchers, media professionals and organisations are welcome: tell us your research question, the topics, stations or sources you need, and the language of the report.",
        "Investigadores, profesionales de los medios y organizaciones son bienvenidos: cuéntanos tu pregunta de investigación, los temas, emisoras o fuentes que necesitas y el idioma del informe.",
        "Peneliti, praktisi media, dan organisasi dipersilakan: beri tahu kami pertanyaan riset Anda, topik, stasiun, atau sumber yang dibutuhkan, serta bahasa laporan."),
    "demo_prices": ("Access plans", "Planes de acceso", "Paket akses"),
    "demo_label": ("Your email", "Tu correo", "Email Anda"),
    "demo_ph": ("you@organisation.org", "tu@organizacion.org", "anda@organisasi.org"),
    "demo_send": ("Send", "Enviar", "Kirim"),
    "demo_note": ("Or write to " + EMAIL, "O escribe a " + EMAIL, "Atau tulis ke " + EMAIL),
    # ---- pie
    "f_tag": ("Media Neuroscience Lab. Peruvian radio, TV and YouTube, transcribed and measured.",
              "Media Neuroscience Lab. Radio, TV y YouTube del Perú, transcritos y medidos.",
              "Media Neuroscience Lab. Radio, TV, dan YouTube Peru, ditranskripsi dan diukur."),
    "f_product": ("The lab", "El laboratorio", "Laboratorium"), "f_contact": ("Contact", "Contacto", "Kontak"),
    "f_legal": ("Legal", "Legal", "Hukum"),
    "f_reports": ("Sample studies", "Estudios de muestra", "Studi contoh"), "f_prices": ("Access", "Acceso", "Akses"),
    "f_dash": ("Dashboard", "Panel", "Dasbor"), "f_privacy": ("Privacy", "Privacidad", "Privasi"),
    "f_method": ("Methodology", "Metodología", "Metodologi"),
    "f_up": ("Back to top ↑", "Volver arriba ↑", "Kembali ke atas ↑"),
}

LANGS = ("en", "es", "id")
LOCALES = {"en": "en_US", "es": "es_PE", "id": "id_ID"}
NOMBRES = {"en": "English", "es": "Español", "id": "Bahasa Indonesia"}
RUTAS = {"en": "/", "es": "/es/", "id": "/id/"}


def textos(lang: str) -> dict:
    i = LANGS.index(lang)
    return {k: v[i] for k, v in T.items()}


def comprobar():
    for k, v in T.items():
        if len(v) != 3 or not all(isinstance(x, str) and x for x in v):
            raise SystemExit(f"[content] «{k}» necesita exactamente tres textos no vacíos")
