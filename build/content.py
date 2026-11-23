"""Contenido de la portada de Zonorah en tres idiomas.

Regla de redacción: cada afirmación de aquí sale de la metodología publicada
(`~/Zonorah/zonorah/web/estaticos/metodologia.html`), de `planes.py` o del
código del análisis. Nada de lo que no esté respaldado: ni «24 horas», ni
«audio guardado», ni cifras que envejecen. Si una frase no se puede defender,
no entra.

Las claves son las mismas en los tres idiomas; `build.py` falla si falta una.
"""

EMAIL = "hola@zonorah.com"
SITE = "https://zonorah.com"
LAB_URL = "https://www.medianeuroscience.org/"

# Precios de lista en soles, de planes.py (PLANES_POR_OMISION).
PLANES = [
    ("profesional", 89, 100),
    ("intensivo", 229, 500),
    ("redaccion", 429, 2000),
]
CITA = ("Zonorah (2026). Memoria de los medios del Perú: minutos al aire por "
        "cada 100 horas grabadas.")

EN = {
    "lang": "en", "locale": "en_US", "dir_name": "English",
    "title": "Zonorah · Media Neuroscience Lab",
    "description": ("Zonorah is a Media Neuroscience Lab. We listen to Peruvian radio, TV and "
                    "YouTube and measure what is said: open data for scientific research, "
                    "custom research for business."),
    "og_alt": "Zonorah, Media Neuroscience Lab",
    "skip": "Skip to content",
    "nav": [("lab", "The lab"), ("method", "How it works"), ("research", "Research"),
            ("data", "Zonorah Data"), ("faq", "FAQ"), ("contact", "Contact")],
    "nav_cta": "Open Zonorah Data",
    "nav_label": "Main", "lang_label": "Language",
    "eyebrow": "Media Neuroscience Lab",
    "h1_a": "Zonorah", "h1_b": "Media Neuroscience Lab",
    "lead": ("We listen to radio, television and YouTube in Peru, transcribe what is said and "
             "measure how much each topic is discussed, where, when and by whom. One system, two "
             "fronts: scientific research and commercial research."),
    "cta1": "Explore Zonorah Data", "cta2": "Commission research",
    "facts": [
        ("Live listening", "Peruvian radio stations, TV channels and YouTube broadcasts, recorded in the time windows of their schedules."),
        ("Minutes, not mentions", "Every public figure is minutes on air per 100 hours recorded, so stations can be compared fairly."),
        ("No recordings kept", "Audio is deleted as soon as it has been transcribed."),
    ],
    "lab_h": "What Zonorah is",
    "lab_p": [
        "Zonorah is a Media Neuroscience Lab. Our research links media and the brain. The Zonorah computational tool takes care of the media side: it listens to Peruvian radio, television and YouTube, transcribes what is said and measures how much, when, by whom and how each topic is framed.",
        "The tool is software and does not record brain activity. Our research on the brain side is separate, and it draws on the tool's data about what was actually broadcast.",
    ],
    "method_h": "How it works",
    "steps": [
        ("Capture", "We receive each station's live signal over the internet and record it in the time windows of its schedule."),
        ("Transcribe", "A speech-recognition model (Whisper) runs locally and transcribes the audio with a timestamp for every sentence. The audio is deleted as soon as it is transcribed."),
        ("Analyse", "Terms are searched in the transcript, ignoring case and accents and including variants. Each relevant passage is classified in closed fields: who is speaking, the role of the subject, topic, tone, framing, and whether a claim rests on verifiable evidence or on rumour."),
        ("Measure", "Public figures are minutes on air in which a term was said, per 100 hours recorded. Stations recorded for different lengths of time stay comparable."),
    ],
    "step_word": "Step",
    "research_h": "Two fronts, one system",
    "sci_h": "Scientific research",
    "sci_for": "For journalists, teachers and researchers.",
    "sci_li": [
        "Published, literal rules that do not depend on any AI. The El Niño index, for example, does not count a bare “niño”, so the phenomenon is not confused with a minor.",
        "Aggregate public figures, rounded to multiples of 5 and hidden below 3 minutes, so no one can tell whether a specific person was mentioned at a specific moment.",
        "A comparator, embeddable charts, CSV downloads and a statistics laboratory.",
        "An AI chat that answers from the transcripts and quotes short fragments with their station and time.",
    ],
    "sci_cta": "Open Zonorah Data",
    "com_h": "Commercial research",
    "com_for": "For organisations, agencies and brands.",
    "com_li": [
        "You define the sources, keywords and rules. Zonorah listens and delivers a report on the schedule you choose.",
        "Each mention is analysed: speaker, topic, tone, framing, evidence or rumour, reputational risk and urgency.",
        "Reports go out as PDF by email, in English, Spanish or Indonesian.",
        "Your commission is private: public data never reveals who asked for a follow-up or what was followed.",
    ],
    "com_cta": "Commission research",
    "com_subject": "Commissioned research",
    "q_h": "Questions our data can answer",
    "q_li": [
        "How much is a topic discussed on air, where and at what times?",
        "Who has the voice: officials, companies, affected communities, experts, listeners?",
        "How is the same event framed: as an environmental problem, an economic cost or a public-order issue?",
        "Which claims rest on verifiable evidence, and which on opinion, rumour or denial?",
    ],
    "found_h": "Foundations",
    "found_p": [
        ("Zonorah takes the computational side of media neuroscience: measuring media messages at scale. "
         "The Media Neuroscience Lab at UC Santa Barbara, directed by René Weber, works, among other "
         "topics, on computational analysis of moral narratives and moral conflict in news and "
         "entertainment, text mining and large media datasets."),
        ("What the Zonorah tool does not do: brain imaging, experiments with participants, or any claim about what media do to a person's brain. It supplies the media-side data that research on the brain needs."),
    ],
    "found_link": "Media Neuroscience Lab, UC Santa Barbara",
    "data_h": "Zonorah Data",
    "data_p": ("The open instrument of the lab. Compare any term across stations, days and regions, "
               "download the numbers, embed the charts and ask the AI questions that it answers from the "
               "transcripts."),
    "plans_note": "All plans are free until 31 December 2026. No payment details are needed.",
    "plans": {
        "profesional": ("Professional", ["100 AI questions a day", "Comparator and embeddable charts", "Statistics laboratory and CSV downloads", "For journalists, teachers and researchers"]),
        "intensivo": ("Intensive", ["Everything in Professional", "5 times more questions: 500 a day", "For people who work with the data daily"]),
        "redaccion": ("Newsroom", ["Everything in Intensive", "20 times more questions: 2,000 a day", "For newsrooms, research teams and agencies"]),
    },
    "list_price": "list price per month (soles, PEN)", "plans_cta": "Activate for free",
    "pop": "Most chosen",
    "limits_h": "Limits you should know",
    "limits": [
        ("Speech-recognition errors.", "Transcription is automatic. A badly transcribed term is not counted, so figures tend to fall short, especially for proper names, acronyms and brands."),
        ("Coverage.", "Only what was recorded is measured. “Not recorded” is not the same as “not said”."),
        ("Music and advertising.", "Recorded minutes include songs and adverts. A term in an advert also counts."),
        ("Comparing stations.", "A music station and a news station are not directly comparable. Compare stations of the same type, or the same term over time."),
        ("Rounding.", "Figures are rounded, so adding groups may not give exactly the total. AI summaries come from automatic transcripts and can contain errors."),
    ],
    "privacy_h": "Privacy",
    "privacy": [
        "No recordings are kept: the audio is deleted once it is transcribed.",
        "If you sign in with Google we store your email and name, your sign-up and last-visit dates, and how many questions you ask each day. We do not store the text of your questions with your account.",
        "Your question is sent to an AI service (Groq, United States) without your email or name. Do not write personal data in your questions.",
        "You can delete your account and all your data at any time, or ask for access or correction by writing to " + EMAIL + ".",
    ],
    "cite_h": "How to cite",
    "cite_p": "Use the permanent link of each comparison and state the date you consulted it, because figures can change when new recordings are added.",
    "cite_fmt": CITA + " Consulted [date], terms: [terms]. [link to the comparison]",
    "faq_h": "Questions",
    "faq": [
        ("What is Zonorah?", "Zonorah is a Media Neuroscience Lab. It listens to Peruvian radio, television and YouTube, transcribes what is said and measures how much each topic is discussed, where, when and by whom. It offers open data for scientific research and custom research for organisations."),
        ("What does Zonorah measure?", "Minutes on air in which a term was said, per 100 hours recorded. Minutes, not mentions: a three-minute item that repeats a term ten times counts as three minutes."),
        ("Does Zonorah measure brain activity?", "No. Zonorah is a computational tool and does not record brain activity. It measures the media side: what is broadcast, how much, when, by whom and how it is framed. Our research on the brain side is separate and draws on that data."),
        ("Does Zonorah keep recordings?", "No. The audio is deleted as soon as it has been transcribed."),
        ("How accurate is it?", "Transcription is automatic and makes errors, mostly with proper names, acronyms and brands, so figures tend to fall short. Each figure is published together with the hours recorded."),
        ("How much does it cost?", "Zonorah Data has three plans from S/ 89 a month at list price. All plans are free until 31 December 2026 and need no payment details."),
        ("How do I commission research?", "Write to " + EMAIL + " saying which topics, stations or sources you need and the language of the report."),
    ],
    "contact_h": "Commission research, or ask for access",
    "contact_p": "For commissioned research, quotations and context for journalistic verification, or to report an error.",
    "footer_tag": "Media Neuroscience Lab",
    "foot_links": [("Methodology", "/datos/metodologia"), ("Privacy", "/datos/privacidad"), ("Zonorah Data", "/datos/")],
    "rights": "© 2026 Zonorah",
}

ES = {
    "lang": "es", "locale": "es_PE", "dir_name": "Español",
    "title": "Zonorah · Media Neuroscience Lab",
    "description": ("Zonorah es un Media Neuroscience Lab. Escuchamos radio, TV y YouTube del Perú y "
                    "medimos lo que se dice: datos abiertos para la ciencia e investigación a medida."),
    "og_alt": "Zonorah, Media Neuroscience Lab",
    "skip": "Saltar al contenido",
    "nav": [("lab", "El laboratorio"), ("method", "Cómo funciona"), ("research", "Investigación"),
            ("data", "Zonorah Datos"), ("faq", "Preguntas"), ("contact", "Contacto")],
    "nav_cta": "Abrir Zonorah Datos",
    "nav_label": "Principal", "lang_label": "Idioma",
    "eyebrow": "Media Neuroscience Lab",
    "h1_a": "Zonorah", "h1_b": "Media Neuroscience Lab",
    "lead": ("Escuchamos radio, televisión y YouTube en el Perú, transcribimos lo que se dice y medimos "
             "cuánto se habla de cada tema, dónde, cuándo y quién. Un solo sistema, dos frentes: "
             "investigación científica e investigación comercial."),
    "cta1": "Explorar Zonorah Datos", "cta2": "Encargar una investigación",
    "facts": [
        ("Escucha en directo", "Emisoras de radio, canales de televisión y transmisiones de YouTube del Perú, grabados en las franjas horarias de su parrilla."),
        ("Minutos, no menciones", "Toda cifra pública son minutos al aire por cada 100 horas grabadas, para comparar emisoras con justicia."),
        ("No guardamos grabaciones", "El audio se borra en cuanto se transcribe."),
    ],
    "lab_h": "Qué es Zonorah",
    "lab_p": [
        "Zonorah es un Media Neuroscience Lab. Nuestra investigación une los medios y el cerebro. La herramienta computacional de Zonorah se encarga del lado de los medios: escucha radio, televisión y YouTube del Perú, transcribe lo que se dice y mide cuánto, cuándo, quién lo dice y con qué encuadre se trata cada tema.",
        "La herramienta es software y no registra actividad cerebral. Nuestra investigación sobre el cerebro es aparte y se apoya en los datos de la herramienta sobre lo que realmente se emitió.",
    ],
    "method_h": "Cómo funciona",
    "steps": [
        ("Captura", "Recibimos la señal en directo de cada emisora por internet y la grabamos en las franjas horarias de su parrilla."),
        ("Transcripción", "Un modelo de reconocimiento de voz (Whisper) corre en local y transcribe el audio con la marca de tiempo de cada frase. El audio se borra en cuanto se transcribe."),
        ("Análisis", "Se buscan los términos en la transcripción, sin distinguir mayúsculas ni tildes e incluyendo variantes. Cada pasaje relevante se clasifica en campos cerrados: quién habla, el papel del sujeto, tema, tono, encuadre y si una afirmación se apoya en evidencia verificable o en rumor."),
        ("Medida", "Las cifras públicas son los minutos al aire en que se dijo un término, por cada 100 horas grabadas. Emisoras grabadas durante tiempos distintos siguen siendo comparables."),
    ],
    "step_word": "Paso",
    "research_h": "Dos frentes, un sistema",
    "sci_h": "Investigación científica",
    "sci_for": "Para periodistas, docentes e investigadores.",
    "sci_li": [
        "Reglas literales y publicadas que no dependen de ninguna IA. El índice de El Niño, por ejemplo, no cuenta el «niño» suelto, para no confundir el fenómeno con un menor de edad.",
        "Cifras públicas agregadas, redondeadas a múltiplos de 5 y ocultas por debajo de 3 minutos, para que nadie pueda saber si se habló de una persona concreta en un momento concreto.",
        "Comparador, gráficos para insertar, descargas CSV y un laboratorio de estadística.",
        "Un chat con IA que responde a partir de las transcripciones y cita fragmentos breves con su emisora y su hora.",
    ],
    "sci_cta": "Abrir Zonorah Datos",
    "com_h": "Investigación comercial",
    "com_for": "Para organizaciones, agencias y marcas.",
    "com_li": [
        "Tú defines las fuentes, las palabras clave y las reglas. Zonorah escucha y entrega un informe en el horario que elijas.",
        "Cada mención se analiza: quién habla, tema, tono, encuadre, evidencia o rumor, riesgo reputacional y urgencia.",
        "Los informes salen en PDF por correo, en español, inglés o indonesio.",
        "Tu encargo es privado: los datos públicos nunca revelan quién pidió un seguimiento ni qué se seguía.",
    ],
    "com_cta": "Encargar una investigación",
    "com_subject": "Investigación a medida",
    "q_h": "Preguntas que nuestros datos pueden responder",
    "q_li": [
        "¿Cuánto se habla de un tema en el aire, dónde y a qué horas?",
        "¿Quién tiene la voz: autoridades, empresas, comunidades afectadas, expertos, oyentes?",
        "¿Cómo se enmarca el mismo hecho: como problema ambiental, coste económico o asunto de orden público?",
        "¿Qué afirmaciones se apoyan en evidencia verificable y cuáles en opinión, rumor o negación?",
    ],
    "found_h": "Fundamentos",
    "found_p": [
        ("Zonorah toma el lado computacional de la neurociencia de los medios: medir mensajes mediáticos "
         "a gran escala. El Media Neuroscience Lab de la UC Santa Bárbara, dirigido por René Weber, "
         "trabaja, entre otros temas, en el análisis computacional de narrativas y conflictos morales en "
         "noticias y entretenimiento, la minería de texto y los grandes conjuntos de datos de medios."),
        ("Lo que la herramienta de Zonorah no hace: imágenes cerebrales, experimentos con participantes ni afirmaciones sobre lo que los medios hacen al cerebro de una persona. Aporta los datos del lado de los medios que necesita la investigación sobre el cerebro."),
    ],
    "found_link": "Media Neuroscience Lab, UC Santa Bárbara",
    "data_h": "Zonorah Datos",
    "data_p": ("El instrumento abierto del laboratorio. Compara cualquier término entre emisoras, días y "
               "regiones, descarga las cifras, inserta los gráficos y hazle a la IA preguntas que responde "
               "a partir de las transcripciones."),
    "plans_note": "Todos los planes son gratis hasta el 31 de diciembre de 2026. No hacen falta datos de pago.",
    "plans": {
        "profesional": ("Profesional", ["100 preguntas a la IA al día", "Comparador y gráficos para insertar", "Laboratorio de estadística y descargas CSV", "Para periodistas, docentes e investigadores"]),
        "intensivo": ("Intensivo", ["Todo lo de Profesional", "5 veces más preguntas: 500 al día", "Para quien trabaja con los datos a diario"]),
        "redaccion": ("Redacción", ["Todo lo de Intensivo", "20 veces más preguntas: 2.000 al día", "Para redacciones, equipos de investigación y agencias"]),
    },
    "list_price": "precio de lista al mes (soles, PEN)", "plans_cta": "Activar gratis",
    "pop": "Más elegido",
    "limits_h": "Límites que hay que conocer",
    "limits": [
        ("Errores de reconocimiento de voz.", "La transcripción es automática. Un término mal transcrito no se cuenta, así que las cifras tienden a quedarse cortas, sobre todo con nombres propios, siglas y marcas."),
        ("Cobertura.", "Solo se mide lo que se grabó. «No se grabó» no es lo mismo que «no se dijo»."),
        ("Música y publicidad.", "Los minutos grabados incluyen canciones y anuncios. Un término que aparece en una cuña publicitaria también cuenta."),
        ("Comparaciones entre emisoras.", "Una emisora musical y una informativa no son comparables sin más. Compara emisoras del mismo tipo, o el mismo término a lo largo del tiempo."),
        ("Redondeo.", "Las cifras se redondean, así que sumar grupos puede no dar exactamente el total. Los resúmenes de la IA salen de transcripciones automáticas y pueden tener errores."),
    ],
    "privacy_h": "Privacidad",
    "privacy": [
        "No se guardan grabaciones: el audio se borra en cuanto se transcribe.",
        "Si entras con Google guardamos tu correo y tu nombre, la fecha de alta y la del último acceso, y cuántas preguntas haces cada día. No guardamos el texto de tus preguntas junto a tu cuenta.",
        "Tu pregunta se envía a un servicio de IA (Groq, en Estados Unidos) sin tu correo ni tu nombre. No escribas datos personales en las preguntas.",
        "Puedes borrar tu cuenta y todos tus datos cuando quieras, o pedir acceso o rectificación escribiendo a " + EMAIL + ".",
    ],
    "cite_h": "Cómo citar",
    "cite_p": "Usa el enlace fijo de cada comparación e indica la fecha de consulta, porque las cifras pueden cambiar cuando se añaden nuevas grabaciones.",
    "cite_fmt": CITA + " Consulta del [fecha], términos: [términos]. [enlace de la comparación]",
    "faq_h": "Preguntas",
    "faq": [
        ("¿Qué es Zonorah?", "Zonorah es un Media Neuroscience Lab. Escucha radio, televisión y YouTube del Perú, transcribe lo que se dice y mide cuánto se habla de cada tema, dónde, cuándo y quién. Ofrece datos abiertos para investigación científica e investigación a medida para organizaciones."),
        ("¿Qué mide Zonorah?", "Minutos al aire en que se dijo un término, por cada 100 horas grabadas. Minutos, no menciones: una nota de tres minutos que repite el término diez veces cuenta tres minutos."),
        ("¿Mide Zonorah la actividad cerebral?", "No. Zonorah es una herramienta computacional y no registra actividad cerebral. Mide el lado de los medios: qué se emite, cuánto, cuándo, quién lo dice y con qué encuadre. Nuestra investigación sobre el cerebro es aparte y se apoya en esos datos."),
        ("¿Zonorah guarda las grabaciones?", "No. El audio se borra en cuanto se transcribe."),
        ("¿Qué tan preciso es?", "La transcripción es automática y comete errores, sobre todo con nombres propios, siglas y marcas, así que las cifras tienden a quedarse cortas. Cada cifra se publica junto a sus horas grabadas."),
        ("¿Cuánto cuesta?", "Zonorah Datos tiene tres planes desde S/ 89 al mes a precio de lista. Todos son gratis hasta el 31 de diciembre de 2026 y no piden datos de pago."),
        ("¿Cómo encargo una investigación?", "Escribe a " + EMAIL + " indicando qué temas, emisoras o fuentes necesitas y el idioma del informe."),
    ],
    "contact_h": "Encarga una investigación o pide acceso",
    "contact_p": "Para investigación a medida, acceso a citas y contexto con fines de verificación periodística, o para señalar un error.",
    "footer_tag": "Media Neuroscience Lab",
    "foot_links": [("Metodología", "/datos/metodologia"), ("Privacidad", "/datos/privacidad"), ("Zonorah Datos", "/datos/")],
    "rights": "© 2026 Zonorah",
}

ID = {
    "lang": "id", "locale": "id_ID", "dir_name": "Bahasa Indonesia",
    "title": "Zonorah · Media Neuroscience Lab",
    "description": ("Zonorah adalah Media Neuroscience Lab. Kami memantau radio, TV, dan YouTube Peru "
                    "dan mengukur apa yang dikatakan: data terbuka untuk riset ilmiah, riset "
                    "pesanan untuk bisnis."),
    "og_alt": "Zonorah, Media Neuroscience Lab",
    "skip": "Lewati ke konten",
    "nav": [("lab", "Laboratorium"), ("method", "Cara kerja"), ("research", "Riset"),
            ("data", "Zonorah Data"), ("faq", "Tanya jawab"), ("contact", "Kontak")],
    "nav_cta": "Buka Zonorah Data",
    "nav_label": "Utama", "lang_label": "Bahasa",
    "eyebrow": "Media Neuroscience Lab",
    "h1_a": "Zonorah", "h1_b": "Media Neuroscience Lab",
    "lead": ("Kami memantau radio, televisi, dan YouTube di Peru, mentranskripsi apa yang dikatakan, "
             "dan mengukur seberapa banyak setiap topik dibahas, di mana, kapan, dan oleh siapa. Satu "
             "sistem, dua lini: riset ilmiah dan riset komersial."),
    "cta1": "Jelajahi Zonorah Data", "cta2": "Pesan riset",
    "facts": [
        ("Pemantauan langsung", "Stasiun radio, kanal televisi, dan siaran YouTube di Peru, direkam pada jam-jam sesuai jadwal siarannya."),
        ("Menit, bukan sebutan", "Setiap angka publik adalah menit siaran per 100 jam rekaman, sehingga stasiun dapat dibandingkan secara adil."),
        ("Rekaman tidak disimpan", "Audio dihapus segera setelah ditranskripsi."),
    ],
    "lab_h": "Apa itu Zonorah",
    "lab_p": [
        "Zonorah adalah Media Neuroscience Lab. Riset kami menghubungkan media dan otak. Alat komputasional Zonorah menangani sisi media: memantau radio, televisi, dan YouTube di Peru, mentranskripsi apa yang dikatakan, dan mengukur seberapa banyak, kapan, oleh siapa, dan bagaimana setiap topik dibingkai.",
        "Alat ini adalah perangkat lunak dan tidak merekam aktivitas otak. Riset kami di sisi otak berjalan terpisah dan memanfaatkan data alat tersebut tentang apa yang benar-benar disiarkan.",
    ],
    "method_h": "Cara kerja",
    "steps": [
        ("Perekaman", "Kami menerima sinyal langsung setiap stasiun melalui internet dan merekamnya pada jam-jam sesuai jadwal siarannya."),
        ("Transkripsi", "Model pengenalan suara (Whisper) berjalan secara lokal dan mentranskripsi audio dengan penanda waktu untuk setiap kalimat. Audio dihapus segera setelah ditranskripsi."),
        ("Analisis", "Istilah dicari dalam transkrip tanpa membedakan huruf besar-kecil dan tanda aksen, termasuk variannya. Setiap bagian yang relevan diklasifikasikan dalam kolom tertutup: siapa yang berbicara, peran subjek, topik, nada, pembingkaian, dan apakah suatu pernyataan bertumpu pada bukti yang dapat diverifikasi atau pada rumor."),
        ("Pengukuran", "Angka publik adalah menit siaran saat suatu istilah diucapkan, per 100 jam rekaman. Stasiun yang direkam dengan durasi berbeda tetap dapat dibandingkan."),
    ],
    "step_word": "Langkah",
    "research_h": "Dua lini, satu sistem",
    "sci_h": "Riset ilmiah",
    "sci_for": "Untuk jurnalis, pengajar, dan peneliti.",
    "sci_li": [
        "Aturan harfiah yang dipublikasikan dan tidak bergantung pada AI mana pun. Indeks El Niño, misalnya, tidak menghitung kata «niño» yang berdiri sendiri, agar fenomena itu tidak tertukar dengan anak di bawah umur.",
        "Angka publik agregat, dibulatkan ke kelipatan 5 dan disembunyikan di bawah 3 menit, sehingga tidak ada yang dapat mengetahui apakah seseorang tertentu disebut pada saat tertentu.",
        "Pembanding, grafik yang dapat disematkan, unduhan CSV, dan laboratorium statistik.",
        "Obrolan dengan AI yang menjawab berdasarkan transkrip dan mengutip potongan singkat beserta stasiun dan waktunya.",
    ],
    "sci_cta": "Buka Zonorah Data",
    "com_h": "Riset komersial",
    "com_for": "Untuk organisasi, agensi, dan merek.",
    "com_li": [
        "Anda menentukan sumber, kata kunci, dan aturan. Zonorah memantau dan mengirim laporan sesuai jadwal yang Anda pilih.",
        "Setiap sebutan dianalisis: pembicara, topik, nada, pembingkaian, bukti atau rumor, risiko reputasi, dan urgensi.",
        "Laporan dikirim sebagai PDF melalui email, dalam bahasa Inggris, Spanyol, atau Indonesia.",
        "Pesanan Anda bersifat privat: data publik tidak pernah mengungkap siapa yang meminta pemantauan atau apa yang dipantau.",
    ],
    "com_cta": "Pesan riset",
    "com_subject": "Riset pesanan",
    "q_h": "Pertanyaan yang dapat dijawab data kami",
    "q_li": [
        "Seberapa banyak sebuah topik dibahas di udara, di mana, dan pada jam berapa?",
        "Siapa yang memegang suara: pejabat, perusahaan, komunitas terdampak, pakar, pendengar?",
        "Bagaimana peristiwa yang sama dibingkai: sebagai masalah lingkungan, biaya ekonomi, atau persoalan ketertiban umum?",
        "Pernyataan mana yang bertumpu pada bukti yang dapat diverifikasi, dan mana pada opini, rumor, atau penyangkalan?",
    ],
    "found_h": "Landasan",
    "found_p": [
        ("Zonorah mengambil sisi komputasional dari neurosains media: mengukur pesan media dalam skala "
         "besar. Media Neuroscience Lab di UC Santa Barbara, yang dipimpin René Weber, antara lain "
         "meneliti analisis komputasional narasi dan konflik moral dalam berita dan hiburan, penambangan "
         "teks, serta kumpulan data media berskala besar."),
        ("Yang tidak dilakukan alat Zonorah: pencitraan otak, eksperimen dengan partisipan, atau klaim apa pun tentang apa yang dilakukan media terhadap otak seseorang. Alat ini menyediakan data sisi media yang dibutuhkan riset tentang otak."),
    ],
    "found_link": "Media Neuroscience Lab, UC Santa Barbara",
    "data_h": "Zonorah Data",
    "data_p": ("Instrumen terbuka laboratorium ini. Bandingkan istilah apa pun antarstasiun, hari, dan "
               "wilayah, unduh angkanya, sematkan grafiknya, dan ajukan pertanyaan kepada AI yang "
               "menjawab berdasarkan transkrip."),
    "plans_note": "Semua paket gratis hingga 31 Desember 2026. Tidak perlu data pembayaran.",
    "plans": {
        "profesional": ("Profesional", ["100 pertanyaan AI per hari", "Pembanding dan grafik yang dapat disematkan", "Laboratorium statistik dan unduhan CSV", "Untuk jurnalis, pengajar, dan peneliti"]),
        "intensivo": ("Intensif", ["Semua fitur Profesional", "Pertanyaan 5 kali lebih banyak: 500 per hari", "Untuk Anda yang bekerja dengan data setiap hari"]),
        "redaccion": ("Redaksi", ["Semua fitur Intensif", "Pertanyaan 20 kali lebih banyak: 2.000 per hari", "Untuk redaksi, tim riset, dan agensi"]),
    },
    "list_price": "harga daftar per bulan (sol Peru, PEN)", "plans_cta": "Aktifkan gratis",
    "pop": "Paling dipilih",
    "limits_h": "Batasan yang perlu diketahui",
    "limits": [
        ("Kesalahan pengenalan suara.", "Transkripsi dilakukan otomatis. Istilah yang salah ditranskripsi tidak dihitung, sehingga angka cenderung lebih rendah, terutama untuk nama diri, singkatan, dan merek."),
        ("Cakupan.", "Hanya yang direkam yang diukur. «Tidak direkam» tidak sama dengan «tidak dikatakan»."),
        ("Musik dan iklan.", "Menit rekaman mencakup lagu dan iklan. Istilah yang muncul dalam iklan juga dihitung."),
        ("Membandingkan stasiun.", "Stasiun musik dan stasiun berita tidak dapat dibandingkan begitu saja. Bandingkan stasiun sejenis, atau istilah yang sama dari waktu ke waktu."),
        ("Pembulatan.", "Angka dibulatkan, sehingga penjumlahan kelompok bisa tidak persis sama dengan totalnya. Ringkasan AI berasal dari transkrip otomatis dan dapat mengandung kesalahan."),
    ],
    "privacy_h": "Privasi",
    "privacy": [
        "Rekaman tidak disimpan: audio dihapus segera setelah ditranskripsi.",
        "Jika Anda masuk dengan Google, kami menyimpan email dan nama Anda, tanggal pendaftaran dan kunjungan terakhir, serta jumlah pertanyaan yang Anda ajukan setiap hari. Kami tidak menyimpan teks pertanyaan Anda bersama akun Anda.",
        "Pertanyaan Anda dikirim ke layanan AI (Groq, Amerika Serikat) tanpa email dan nama Anda. Jangan menulis data pribadi dalam pertanyaan.",
        "Anda dapat menghapus akun dan seluruh data Anda kapan saja, atau meminta akses atau perbaikan dengan menulis ke " + EMAIL + ".",
    ],
    "cite_h": "Cara mengutip",
    "cite_p": "Gunakan tautan permanen setiap perbandingan dan cantumkan tanggal akses, karena angka dapat berubah saat rekaman baru ditambahkan.",
    "cite_fmt": CITA + " Diakses [tanggal], istilah: [istilah]. [tautan perbandingan]",
    "faq_h": "Tanya jawab",
    "faq": [
        ("Apa itu Zonorah?", "Zonorah adalah Media Neuroscience Lab. Zonorah memantau radio, televisi, dan YouTube Peru, mentranskripsi apa yang dikatakan, dan mengukur seberapa banyak setiap topik dibahas, di mana, kapan, dan oleh siapa. Zonorah menyediakan data terbuka untuk riset ilmiah dan riset pesanan untuk organisasi."),
        ("Apa yang diukur Zonorah?", "Menit siaran saat suatu istilah diucapkan, per 100 jam rekaman. Menit, bukan sebutan: berita tiga menit yang mengulang istilah sepuluh kali dihitung tiga menit."),
        ("Apakah Zonorah mengukur aktivitas otak?", "Tidak. Zonorah adalah alat komputasional dan tidak merekam aktivitas otak. Alat ini mengukur sisi media: apa yang disiarkan, seberapa banyak, kapan, oleh siapa, dan bagaimana pembingkaiannya. Riset kami di sisi otak berjalan terpisah dan memanfaatkan data tersebut."),
        ("Apakah Zonorah menyimpan rekaman?", "Tidak. Audio dihapus segera setelah ditranskripsi."),
        ("Seberapa akurat?", "Transkripsi dilakukan otomatis dan bisa salah, terutama pada nama diri, singkatan, dan merek, sehingga angka cenderung lebih rendah. Setiap angka dipublikasikan bersama jam rekamannya."),
        ("Berapa biayanya?", "Zonorah Data memiliki tiga paket mulai dari S/ 89 per bulan pada harga daftar. Semua gratis hingga 31 Desember 2026 dan tidak memerlukan data pembayaran."),
        ("Bagaimana cara memesan riset?", "Tulis ke " + EMAIL + " dengan menyebutkan topik, stasiun, atau sumber yang Anda butuhkan serta bahasa laporan."),
    ],
    "contact_h": "Pesan riset, atau minta akses",
    "contact_p": "Untuk riset pesanan, akses ke kutipan dan konteks untuk verifikasi jurnalistik, atau untuk melaporkan kesalahan.",
    "footer_tag": "Media Neuroscience Lab",
    "foot_links": [("Metodologi", "/datos/metodologia"), ("Privasi", "/datos/privacidad"), ("Zonorah Data", "/datos/")],
    "rights": "© 2026 Zonorah",
}

IDIOMAS = {"en": EN, "es": ES, "id": ID}
RUTAS = {"en": "/", "es": "/es/", "id": "/id/"}
