"""Copy de la portada de Zonorah en inglés, español e indonesio.

El DISEÑO no está aquí: vive en `build/plantilla.html`, que es la portada original
sin tocar. Este archivo solo trae los textos que `build.py` pone dentro de ella.

Cada fila es (inglés, español, indonesio): una clave no puede faltar en un idioma.

Regla de redacción: cada afirmación sale de la metodología publicada
(`~/Zonorah/zonorah/web/estaticos/metodologia.html`), de `planes.py` o del código del
análisis. Nada de «24 horas», «audio guardado», «alerta en 3 minutos» ni «RGPD», que la
metodología desmiente o que nadie ha medido. Si no se puede defender, no entra.
"""

EMAIL = "hola@zonorah.com"
SITE = "https://zonorah.com"
LAB_URL = "https://www.medianeuroscience.org/"
UPDATED = "2026-11-24"
CITA = ("Zonorah (2026). Memoria de los medios del Perú: minutos al aire por "
        "cada 100 horas grabadas.")

# Sectores de los informes de muestra: (slug, en, es, id)
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
        "Zonorah is a Media Neuroscience Lab. We listen to Peruvian radio, TV and YouTube and measure what is said: open data for science, research for business.",
        "Zonorah es un Media Neuroscience Lab. Escuchamos radio, TV y YouTube del Perú y medimos lo que se dice: datos abiertos para la ciencia e investigación a medida.",
        "Zonorah adalah Media Neuroscience Lab. Kami memantau radio, TV, dan YouTube Peru dan mengukur apa yang dikatakan: data terbuka untuk sains, riset untuk bisnis."),
    "updated": ("Last updated", "Actualizado", "Diperbarui"),
    # ---- accesibilidad
    "aria_nav": ("Main navigation", "Navegación principal", "Navigasi utama"),
    "aria_lang": ("Change language", "Cambiar idioma", "Ganti bahasa"),
    "aria_menu": ("Menu", "Menú", "Menu"),
    "menu_open": ("Open menu", "Abrir menú", "Buka menu"),
    "menu_close": ("Close menu", "Cerrar menú", "Tutup menu"),
    "aria_logos": ("Channels and stations we listen to", "Canales y emisoras que sintonizamos", "Kanal dan stasiun yang kami pantau"),
    # ---- navegación
    "n_how": ("How it works", "Cómo funciona", "Cara kerja"),
    "n_research": ("Research", "Investigación", "Riset"),
    "n_chat": ("Chat", "Chat", "Chat"),
    "n_learn": ("Learn", "Aprende", "Belajar"),
    "n_plans": ("Plans", "Planes", "Paket"),
    "n_seeplans": ("See plans", "Ver planes", "Lihat paket"),
    "n_dash": ("Client dashboard", "Panel de clientes", "Dasbor klien"),
    "n_login": ("Sign in / Sign up", "Iniciar sesión / Registrarse", "Masuk / Daftar"),
    "n_logout": ("Sign out", "Salir", "Keluar"),
    "n_tochat": (" · go to chat", " · ir al chat", " · ke chat"),
    "cur_go": ("Go", "Ir", "Buka"), "cur_view": ("View", "Ver", "Lihat"),
    "cur_down": ("Down", "Bajar", "Turun"), "cur_pdf": ("Open PDF", "Abrir PDF", "Buka PDF"),
    # ---- hero
    "h1a": ("Zonorah.",) * 3, "h1b": ("Media Neuroscience",) * 3, "h1c": ("Lab.",) * 3,
    "hero_lead": (
        "We listen to Peruvian radio, television and YouTube and measure what is said: how much, where, when and by whom.",
        "Escuchamos radio, televisión y YouTube del Perú y medimos lo que se dice: cuánto, dónde, cuándo y quién.",
        "Kami memantau radio, televisi, dan YouTube Peru dan mengukur apa yang dikatakan: seberapa banyak, di mana, kapan, dan oleh siapa."),
    "hero_cta1": ("Explore Zonorah Data", "Explorar Zonorah Datos", "Jelajahi Zonorah Data"),
    "hero_cta2": ("How it works", "Cómo funciona", "Cara kerja"),
    # ---- el problema (citas flotantes = preguntas de investigación)
    "q1": ("How much is a topic discussed on air?", "¿Cuánto se habla de un tema en el aire?", "Seberapa banyak topik dibahas di udara?"),
    "q2": ("Which stations talk about it?", "¿Qué emisoras hablan de él?", "Stasiun mana yang membahasnya?"),
    "q3": ("At what times does it enter the day?", "¿A qué horas entra en el día?", "Pada jam berapa topik itu muncul?"),
    "q4": ("Who has the voice?", "¿Quién tiene la voz?", "Siapa yang memegang suara?"),
    "q5": ("How is the same event framed?", "¿Cómo se enmarca el mismo hecho?", "Bagaimana peristiwa yang sama dibingkai?"),
    "q6": ("Evidence, or rumour?", "¿Evidencia o rumor?", "Bukti, atau rumor?"),
    "q7": ("What was said last week?", "¿Qué se dijo la semana pasada?", "Apa yang dikatakan minggu lalu?"),
    "problema_h": (
        "Before asking what media do to the brain, measure what the media say.",
        "Antes de preguntar qué hacen los medios al cerebro, mide lo que dicen los medios.",
        "Sebelum bertanya apa yang dilakukan media terhadap otak, ukur apa yang dikatakan media."),
    # ---- cómo funciona
    "como_h": ("How it works", "Cómo funciona", "Cara kerja"),
    "step": ("Step", "Paso", "Langkah"),
    "s1r": ("Live · by schedule windows", "En directo · por franjas", "Langsung · per jam siaran"),
    "s2r": ("Whisper · local", "Whisper · en local", "Whisper · lokal"),
    "s3r": ("Analysis · closed fields", "Análisis · campos cerrados", "Analisis · kolom tertutup"),
    "s4r": ("Your schedule", "Tu horario", "Jadwal Anda"),
    "s1t": ("Capture", "Captura", "Perekaman"),
    "s2t": ("Transcribe", "Transcripción", "Transkripsi"),
    "s3t": ("Analyse", "Análisis", "Analisis"),
    "s4t": ("Deliver", "Entrega", "Pengiriman"),
    "s1p": ("We receive each station's live signal over the internet and record it in the time windows of its schedule.",
            "Recibimos la señal en directo de cada emisora por internet y la grabamos en las franjas horarias de su parrilla.",
            "Kami menerima sinyal langsung setiap stasiun melalui internet dan merekamnya pada jam-jam sesuai jadwal siarannya."),
    "s2p": ("A speech-recognition model runs locally and transcribes the audio with a timestamp for every sentence. The audio is deleted as soon as it is transcribed.",
            "Un modelo de reconocimiento de voz corre en local y transcribe el audio con la marca de tiempo de cada frase. El audio se borra en cuanto se transcribe.",
            "Model pengenalan suara berjalan secara lokal dan mentranskripsi audio dengan penanda waktu untuk setiap kalimat. Audio dihapus segera setelah ditranskripsi."),
    "s3p": ("Terms are searched in the transcript, with variants. Each relevant passage is classified in closed fields: who speaks, role of the subject, topic, tone, framing, and evidence or rumour.",
            "Se buscan los términos en la transcripción, con sus variantes. Cada pasaje relevante se clasifica en campos cerrados: quién habla, papel del sujeto, tema, tono, encuadre y evidencia o rumor.",
            "Istilah dicari dalam transkrip, termasuk variannya. Setiap bagian yang relevan diklasifikasikan dalam kolom tertutup: siapa yang bicara, peran subjek, topik, nada, pembingkaian, serta bukti atau rumor."),
    "s4p": ("Commissioned research arrives as a PDF by email on the schedule you choose. Public figures go to Zonorah Data as minutes on air per 100 hours recorded.",
            "La investigación a medida llega en PDF por correo en el horario que elijas. Las cifras públicas van a Zonorah Datos como minutos al aire por cada 100 horas grabadas.",
            "Riset pesanan tiba sebagai PDF melalui email sesuai jadwal yang Anda pilih. Angka publik masuk ke Zonorah Data sebagai menit siaran per 100 jam rekaman."),
    "s1g1": ("Radio", "Radio", "Radio"), "s1g2": ("TV", "TV", "TV"), "s1g3": ("YouTube",) * 3,
    "s1g4": ("Schedules", "Franjas", "Jadwal"),
    "s2g1": ("Timestamps", "Marcas de tiempo", "Penanda waktu"),
    "s2g2": ("Local model", "Modelo local", "Model lokal"),
    "s2g3": ("Audio deleted after transcribing", "Audio borrado al transcribir", "Audio dihapus setelah transkripsi"),
    "s3g1": ("Tone", "Tono", "Nada"), "s3g2": ("Speaker", "Actor", "Pembicara"),
    "s3g3": ("Topic", "Tema", "Topik"), "s3g4": ("Framing", "Encuadre", "Pembingkaian"),
    "s4g1": ("Email", "Correo", "Email"), "s4g2": ("PDF",) * 3,
    "s4g3": ("Open data", "Datos abiertos", "Data terbuka"),
    # visual del paso 3 (ejemplo ilustrativo)
    "v3a": ("Who speaks?", "¿Quién habla?", "Siapa yang bicara?"),
    "v3av": ("Municipal spokesperson", "Portavoz municipal", "Juru bicara pemkot"),
    "v3b": ("About what?", "¿De qué?", "Tentang apa?"),
    "v3bv": ("Tender · award", "Adjudicación · pliego", "Penetapan pemenang · tender"),
    "v3c": ("Tone?", "¿Tono?", "Nada?"),
    "v3cv": ("Negative", "Negativo", "Negatif"),
    "v3d": ("Evidence or rumour?", "¿Evidencia o rumor?", "Bukti atau rumor?"),
    "v3dv": ("Rumour", "Rumor", "Rumor"),
    # visual del paso 4 (parte de ejemplo)
    "v4t": ("Zonorah · Daily report", "Zonorah · Parte diario", "Zonorah · Laporan harian"),
    "v4h": ("23 mentions, 2 urgent, 847 segments listened to",
            "23 menciones, 2 urgentes, 847 segmentos escuchados",
            "23 sebutan, 2 mendesak, 847 segmen didengarkan"),
    "v4p": ("Radio Norte opens with the tender; Canal 5 covers the suspended works; RPP, positive about the cultural centre.",
            "Radio Norte abre con el pliego; Canal 5 recoge la suspensión de obras; RPP, positivo con el centro cultural.",
            "Radio Norte membuka dengan isu tender; Canal 5 meliput penghentian proyek; RPP, positif soal pusat budaya."),
    "v4r1": ("2 urgent", "2 urgentes", "2 mendesak"), "v4r2": ("4 sources", "4 fuentes", "4 sumber"),
    "v4r3": ("PDF",) * 3,
    # ---- investigación: dos frentes (+ límites, privacidad, fundamentos)
    "casos_h": ("Two fronts, one system", "Dos frentes, un sistema", "Dua lini, satu sistem"),
    "casos_lead": (
        "Zonorah is a Media Neuroscience Lab. Its computational tool takes care of the media side; our research on the brain side is separate and draws on that data.",
        "Zonorah es un Media Neuroscience Lab. Su herramienta computacional se encarga del lado de los medios; nuestra investigación sobre el cerebro es aparte y se apoya en esos datos.",
        "Zonorah adalah Media Neuroscience Lab. Alat komputasionalnya menangani sisi media; riset kami di sisi otak berjalan terpisah dan memanfaatkan data tersebut."),
    "c1m": ("Scientific research", "Investigación científica", "Riset ilmiah"),
    "c1h": ("The media side of the question", "El lado de los medios de la pregunta", "Sisi media dari pertanyaannya"),
    "c1p": ("Published, literal rules and open data for journalists, teachers and researchers: a comparator, embeddable charts, CSV downloads and an AI chat that quotes short fragments with their station and time.",
            "Reglas literales y publicadas, y datos abiertos para periodistas, docentes e investigadores: comparador, gráficos para insertar, descargas CSV y un chat con IA que cita fragmentos breves con su emisora y su hora.",
            "Aturan harfiah yang dipublikasikan dan data terbuka untuk jurnalis, pengajar, dan peneliti: pembanding, grafik yang dapat disematkan, unduhan CSV, dan obrolan AI yang mengutip potongan singkat beserta stasiun dan waktunya."),
    "c1x": ("Every figure: minutes on air per 100 hours recorded",
            "Toda cifra: minutos al aire por cada 100 horas grabadas",
            "Setiap angka: menit siaran per 100 jam rekaman"),
    "c2m": ("Commercial research", "Investigación comercial", "Riset komersial"),
    "c2h": ("Custom research for organisations", "Investigación a medida para organizaciones", "Riset pesanan untuk organisasi"),
    "c2p": ("You define the sources, keywords and rules. Each mention is analysed for speaker, topic, tone, framing, evidence or rumour, risk and urgency, and delivered as a PDF report by email.",
            "Tú defines las fuentes, las palabras clave y las reglas. Cada mención se analiza: quién habla, tema, tono, encuadre, evidencia o rumor, riesgo y urgencia, y se entrega en un informe PDF por correo.",
            "Anda menentukan sumber, kata kunci, dan aturan. Setiap sebutan dianalisis: pembicara, topik, nada, pembingkaian, bukti atau rumor, risiko, dan urgensi, lalu dikirim sebagai laporan PDF melalui email."),
    "c2x": ("Your commission is private: public data never reveals who asked for what",
            "Tu encargo es privado: los datos públicos nunca revelan quién pidió qué",
            "Pesanan Anda bersifat privat: data publik tidak pernah mengungkap siapa yang meminta apa"),
    "c3m": ("Zonorah Data", "Zonorah Datos", "Zonorah Data"),
    "c3h": ("The open instrument", "El instrumento abierto", "Instrumen terbuka"),
    "c3p": ("Compare any term across stations, days and regions. To cite a figure, use the permanent link of the comparison and the date you consulted it.",
            "Compara cualquier término entre emisoras, días y regiones. Para citar una cifra, usa el enlace fijo de la comparación y la fecha de consulta.",
            "Bandingkan istilah apa pun antarstasiun, hari, dan wilayah. Untuk mengutip angka, gunakan tautan permanen perbandingan dan tanggal akses."),
    "c3x": ("Cite as: " + CITA, "Cita así: " + CITA, "Kutip sebagai: " + CITA),
    "c4m": ("Limits", "Límites", "Batasan"),
    "c4h": ("What the figures do not say", "Lo que las cifras no dicen", "Yang tidak dikatakan angka"),
    "c4p": ("Transcription is automatic and errs on names, acronyms and brands, so figures tend to fall short. Only what was recorded is measured, music and adverts count, and figures are rounded.",
            "La transcripción es automática y falla con nombres, siglas y marcas, así que las cifras tienden a quedarse cortas. Solo se mide lo que se grabó, la música y la publicidad cuentan, y las cifras se redondean.",
            "Transkripsi dilakukan otomatis dan keliru pada nama, singkatan, dan merek, sehingga angka cenderung lebih rendah. Hanya yang direkam yang diukur, musik dan iklan ikut dihitung, dan angka dibulatkan."),
    "c4x": ("“Not recorded” is not the same as “not said”", "«No se grabó» no es lo mismo que «no se dijo»", "«Tidak direkam» tidak sama dengan «tidak dikatakan»"),
    "c5m": ("Privacy", "Privacidad", "Privasi"),
    "c5h": ("No recordings kept", "No guardamos grabaciones", "Rekaman tidak disimpan"),
    "c5p": ("Audio is deleted as soon as it is transcribed. Your AI questions go to an AI service (Groq, United States) without your email or name. You can delete your account and data at any time.",
            "El audio se borra en cuanto se transcribe. Tus preguntas a la IA van a un servicio de IA (Groq, Estados Unidos) sin tu correo ni tu nombre. Puedes borrar tu cuenta y tus datos cuando quieras.",
            "Audio dihapus segera setelah ditranskripsi. Pertanyaan AI Anda dikirim ke layanan AI (Groq, Amerika Serikat) tanpa email dan nama Anda. Anda dapat menghapus akun dan data Anda kapan saja."),
    "c5x": ("Access, correction or deletion: " + EMAIL, "Acceso, rectificación o supresión: " + EMAIL, "Akses, perbaikan, atau penghapusan: " + EMAIL),
    "c6m": ("Foundations", "Fundamentos", "Landasan"),
    "c6h": ("Computational media neuroscience", "Neurociencia de los medios computacional", "Neurosains media komputasional"),
    "c6p": ("Zonorah takes the computational side of media neuroscience, such as the work of the Media Neuroscience Lab at UC Santa Barbara on moral narratives, text mining and large media datasets. The tool does not do brain imaging or experiments with participants.",
            "Zonorah toma el lado computacional de la neurociencia de los medios, como el trabajo del Media Neuroscience Lab de la UC Santa Bárbara sobre narrativas morales, minería de texto y grandes conjuntos de datos de medios. La herramienta no hace imágenes cerebrales ni experimentos con participantes.",
            "Zonorah mengambil sisi komputasional dari neurosains media, seperti karya Media Neuroscience Lab di UC Santa Barbara tentang narasi moral, penambangan teks, dan kumpulan data media berskala besar. Alat ini tidak melakukan pencitraan otak atau eksperimen dengan partisipan."),
    # ---- informes de muestra
    "inf_h": ("Reports", "Informes", "Laporan"),
    "inf_meta": (
        "Peru · 2 to 8 September 2026 · 29 radio and TV stations · 296 hours of audio · sample reports, in Spanish",
        "Perú · 2 al 8 de septiembre de 2026 · 29 emisoras de radio y TV · 296 horas de audio · informes de muestra",
        "Peru · 2 sampai 8 September 2026 · 29 stasiun radio dan TV · 296 jam audio · laporan contoh"),
    "inf_data": ("{n} mentions · {p} pp · PDF", "{n} menciones · {p} págs · PDF", "{n} sebutan · {p} hlm · PDF"),
    "inf_dl": ("Download PDF", "Descargar PDF", "Unduh PDF"),
    "inf_alt": ("Cover of the report {name}", "Portada del informe {name}", "Sampul laporan {name}"),
    # ---- precios
    "precios_h": ("Prices", "Precios", "Harga"),
    "precios_lead": ("All plans are free until 31 December 2026. No payment details.",
                     "Todos los planes, gratis hasta el 31 de diciembre de 2026. Sin datos de pago.",
                     "Semua paket gratis hingga 31 Desember 2026. Tanpa data pembayaran."),
    "p1n": ("Professional", "Profesional", "Profesional"), "p2n": ("Intensive", "Intensivo", "Intensif"),
    "p3n": ("Newsroom", "Redacción", "Redaksi"),
    "p_pop": ("Most chosen", "Más elegido", "Paling banyak dipilih"),
    "p1b": ("For journalists, teachers and researchers.", "Para periodistas, docentes e investigadores.", "Untuk jurnalis, pengajar, dan peneliti."),
    "p2b": ("For people who work with the data daily.", "Para quien trabaja con los datos a diario.", "Untuk Anda yang bekerja dengan data setiap hari."),
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
    "p_foot": ("Prices per month, in soles (PEN). Custom research for your organisation? ",
               "Precios al mes, en soles. ¿Investigación a medida para tu organización? ",
               "Harga per bulan, dalam sol Peru (PEN). Riset pesanan untuk organisasi Anda? "),
    "p_foot_a": ("Write to us", "Escríbenos", "Hubungi kami"),
    "mail_subject": ("Commissioned research", "Investigación a medida", "Riset pesanan"),
    # ---- contacto
    "demo_h": ("Commission research, or ask for access.", "Encarga una investigación o pide acceso.", "Pesan riset, atau minta akses."),
    "demo_lead": ("Tell us which topics, stations or sources you need and the language of the report.",
                  "Cuéntanos qué temas, emisoras o fuentes necesitas y el idioma del informe.",
                  "Beri tahu kami topik, stasiun, atau sumber yang Anda butuhkan serta bahasa laporan."),
    "demo_prices": ("See prices", "Ver precios", "Lihat harga"),
    "demo_label": ("Your email", "Tu correo", "Email Anda"),
    "demo_ph": ("you@organisation.org", "tu@organizacion.org", "anda@organisasi.org"),
    "demo_send": ("Send", "Enviar", "Kirim"),
    "demo_note": ("Or write to " + EMAIL, "O escribe a " + EMAIL, "Atau tulis ke " + EMAIL),
    # ---- pie
    "f_tag": ("Media Neuroscience Lab. Peruvian radio, TV and YouTube, listened to and measured.",
              "Media Neuroscience Lab. Radio, TV y YouTube del Perú, escuchados y medidos.",
              "Media Neuroscience Lab. Radio, TV, dan YouTube Peru, dipantau dan diukur."),
    "f_product": ("Product", "Producto", "Produk"), "f_contact": ("Contact", "Contacto", "Kontak"),
    "f_legal": ("Legal", "Legal", "Hukum"),
    "f_reports": ("Reports", "Informes", "Laporan"), "f_prices": ("Prices", "Precios", "Harga"),
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
