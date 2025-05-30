import streamlit as st
import random

# --- Sidebar untuk memilih game ---
st.sidebar.title("🎮 Pilih Game")
selected_game = st.sidebar.radio("Pilih Game", ["-- Pilih Game --", "Kuis Tabel Periodik", "Kuis Senyawa Organik"])

# --- Styling umum font ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# --- Styling background berdasarkan halaman ---
if selected_game == "-- Pilih Game --":
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                    url("https://i.imgur.com/06z4doi.jpeg") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f8cdda, #1d2b64);
        background-attachment: fixed;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Styling komponen lainnya (selalu aktif) ---
st.markdown("""
    <style>
    .question-card {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 20px;
        box-shadow: 4px 4px 30px rgba(0,0,0,0.2);
        margin-bottom: 25px;
        animation: fadeIn 1s ease-in-out;
        color: #fff;
    }
    .score-box {
        background: rgba(0,0,0,0.25);
        backdrop-filter: blur(10px);
        padding: 15px; border-radius: 12px;
        font-size: 18px; font-weight: 600;
        text-align: center; color: white;
        margin-top: 10px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; padding: 10px 24px;
        border-radius: 10px; border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        filter: brightness(1.1); transform: scale(1.03);
    }
    .stTextInput>div>div>input {
        background-color: #fff !important;
        color: #000 !important;
        border: 1px solid #ccc; border-radius: 10px;
    }
    @keyframes fadeIn {
        from {opacity:0; transform:translateY(20px);}
        to {opacity:1; transform:translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# --- Halaman Selamat Datang ---
if selected_game == "-- Pilih Game --":
    st.markdown("""
    <div style='padding: 30px; background-color: rgba(255,255,255,0.05); border-radius: 20px; text-align: center;'>
        <h1 style='color: #ffffff; font-size: 48px; text-shadow: 0 0 10px #ffffff, 0 0 20px #00e6e6;'>Selamat datang di QChems</h1>
        <h3 style='color: #f0f0f0; text-shadow: 0 0 5px #00ffff;'>Aplikasi kuis interaktif seputar Tabel Periodik & Senyawa Organik.</h3>
        <p style='color: #dddddd;'>Silakan pilih game dari menu di sebelah kiri untuk memulai.</p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# === GAME 1: Kuis Tabel Periodik ===
if selected_game == "Kuis Tabel Periodik":
    if "pt_started" not in st.session_state:
        st.session_state.pt_started = False

    if not st.session_state.pt_started:
        st.title("🧪 Kuis Tabel Periodik Unsur")
        st.image("https://i.imgur.com/Kcgjoc5.png", caption="Tabel Periodik Unsur", use_container_width=True)
        if st.button("Mulai Kuis"):
            st.session_state.pt_started = True
        st.stop()

    NUM_PT = 5
    periodic_table = [
        {"name":"hidrogen","symbol":"H","number":1,"group":1,"period":1},
        {"name":"helium","symbol":"He","number":2,"group":18,"period":1},
        {"name":"litium","symbol":"Li","number":3,"group":1,"period":2},
        {"name":"berilium","symbol":"Be","number":4,"group":2,"period":2},
        {"name":"karbon","symbol":"C","number":6,"group":14,"period":2},
        {"name":"oksigen","symbol":"O","number":8,"group":16,"period":2},
        {"name":"natrium","symbol":"Na","number":11,"group":1,"period":3},
        {"name":"kalsium","symbol":"Ca","number":20,"group":2,"period":4},
        {"name":"nitrogen","symbol":"N","number":7,"group":15,"period":2},
        {"name":"magnesium","symbol":"Mg","number":12,"group":2,"period":3},
        {"name":"aluminium","symbol":"Al","number":13,"group":13,"period":3},
        {"name":"klorin","symbol":"Cl","number":17,"group":17,"period":3},
        {"name":"fosfor","symbol":"P","number":15,"group":15,"period":3},
        {"name":"argon","symbol":"Ar","number":18,"group":18,"period":3},
        {"name":"kalium","symbol":"K","number":19,"group":1,"period":4},
        {"name":"mangan","symbol":"Mn","number":25,"group":7,"period":4},
        {"name":"besi","symbol":"Fe","number":26,"group":8,"period":4},
        {"name":"tembaga","symbol":"Cu","number":29,"group":11,"period":4},
        {"name":"zinc","symbol":"Zn","number":30,"group":12,"period":4},
        {"name":"fluorin","symbol":"F","number":9,"group":17,"period":2},
        {"name":"neon","symbol":"Ne","number":10,"group":18,"period":2},
        {"name":"silikon","symbol":"Si","number":14,"group":14,"period":3},
        {"name":"nikel","symbol":"Ni","number":28,"group":10,"period":4},
    ]

    group_to_iupac = {
        1: "1A", 2: "2A", 3: "3B", 4: "4B", 5: "5B", 6: "6B", 7: "7B",
        8: "8B", 9: "8B", 10: "8B", 11: "1B", 12: "2B", 13: "3A", 14: "4A",
        15: "5A", 16: "6A", 17: "7A", 18: "8A"
    }

    if "pt_score" not in st.session_state:
        st.session_state.pt_score = 0
        st.session_state.pt_index = 0
        st.session_state.pt_q = None
        st.session_state.pt_feedback = ""
        st.session_state.pt_answered = False

    st.progress(st.session_state.pt_index / NUM_PT)

    def new_pt_q():
        el = random.choice(periodic_table)
        typ = random.choice(["symbol", "number", "group", "period"])
        return {"el": el, "type": typ}

    if st.session_state.pt_index < NUM_PT:
        if st.session_state.pt_q is None:
            st.session_state.pt_q = new_pt_q()
            st.session_state.pt_answered = False

        q = st.session_state.pt_q
        e = q["el"]
        if q["type"] == "symbol":
            text = f"🧪 Apa simbol dari unsur {e['name'].capitalize()}?"
            ans = e["symbol"]
            correct = lambda u: u.strip().lower() == ans.lower()
        elif q["type"] == "number":
            text = f"🔢 Berapa nomor atom dari {e['name'].capitalize()}?"
            ans = str(e["number"])
            correct = lambda u: u.strip() == ans
        elif q["type"] == "group":
            text = f"📚 Golongan berapa unsur {e['name'].capitalize()}?"
            ans = str(e["group"])
            alt_ans = group_to_iupac.get(e["group"], "")
            correct = lambda u: u.strip().lower() in [ans.lower(), alt_ans.lower()]
        else:
            text = f"🕏 Periode berapa unsur {e['name'].capitalize()}?"
            ans = str(e["period"])
            correct = lambda u: u.strip() == ans

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.pt_index+1} dari {NUM_PT}")
        user = st.text_input(text, key=f"pt_in_{st.session_state.pt_index}")

        if st.button("Kirim Jawaban", key=f"pt_sub_{st.session_state.pt_index}") and not st.session_state.pt_answered:
            if correct(user):
                st.session_state.pt_score += 1
                st.session_state.pt_feedback = "✅ Jawaban Benar!"
                st.balloons()
            else:
                feedback = f"❌ Salah. Jawaban benar: {ans}"
                if q["type"] == "group" and alt_ans:
                    feedback += f" (atau {alt_ans})"
                st.session_state.pt_feedback = feedback
            st.session_state.pt_answered = True

        st.write(st.session_state.pt_feedback)

        if st.session_state.pt_answered:
            if st.button("➡ Soal Berikutnya", key=f"pt_next_{st.session_state.pt_index}"):
                st.session_state.pt_index += 1
                st.session_state.pt_q = None
                st.session_state.pt_feedback = ""
                st.session_state.pt_answered = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>🌟 Skor: {st.session_state.pt_score}/{NUM_PT}</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.pt_score}/{NUM_PT}")
        if st.button("🔁 Ulangi Kuis"):
            for k in ["pt_score", "pt_index", "pt_q", "pt_feedback", "pt_answered", "pt_started"]:
                del st.session_state[k]

# === GAME 2: Kuis Senyawa Organik ===
elif selected_game == "Kuis Senyawa Organik":
    st.title("🧪 Kuis Senyawa Organik") 
    st.header("Pengantar Senyawa Organik")

    st.markdown("""
    ## I. Hidrokarbon

    Senyawa organik yang hanya mengandung atom karbon (C) dan hidrogen (H).

    **Contoh:**
    1. **Metana (CH₄):**  
       Hidrokarbon paling sederhana, termasuk golongan alkana. Gas utama dalam gas alam.  
    2. **Benzena (C₆H₆):**  
       Senyawa aromatik, memiliki cincin heksagonal dengan ikatan rangkap terkonjugasi.

    ## II. Gugus Fungsi dan Golongan Senyawa Organik

    Gugus fungsi adalah atom atau kelompok atom spesifik dalam molekul yang bertanggung jawab atas karakteristik reaksi kimia senyawa tersebut.

    ### A. Alkohol  
    Gugus Fungsi: Hidroksil (-OH)  
    Rumus Umum: R-OH (dimana R adalah gugus alkil)

    **Contoh:**  
    1. Etanol (C₂H₅OH): Alkohol yang umum ditemukan dalam minuman beralkohol.  
    2. Propanol (CH₃(CH₂)₂OH): Alkohol dengan 3 atom karbon.  
    3. Butanol (CH₃(CH₂)₃OH): Alkohol dengan 4 atom karbon.  
    4. Pentanol (C₅H₁₁OH): Alkohol dengan 5 atom karbon.

    ### B. Asam Karboksilat  
    Gugus Fungsi: Karboksil (-COOH)  
    Rumus Umum: R-COOH

    **Contoh:**  
    1. Asam Asetat (CH₃COOH): Asam yang memberikan rasa asam pada cuka.  
    2. Asam Propionat (CH₃CH₂COOH): Asam karboksilat dengan 3 atom karbon.  
    3. Asam Butirat (C₃H₇COOH): Asam karboksilat dengan 4 atom karbon.  
    4. Asam Metanoat (HCOOH): Asam format, asam karboksilat paling sederhana.

    ### C. Keton  
    Gugus Fungsi: Karbonil (>C=O) yang terikat pada dua gugus alkil.  
    Rumus Umum: R-CO-R'

    **Contoh:**  
    Aseton (CH₃COCH₃): Pelarut yang umum digunakan, contoh keton paling sederhana.

    ### D. Amina  
    Gugus Fungsi: Amino (-NH₂)  
    Rumus Umum: R-NH₂ (amina primer)

    **Contoh:**  
    1. Metilamina (CH₃NH₂): Amina primer paling sederhana.  
    2. Propilamina (CH₃(CH₂)₂NH₂): Amina primer dengan 3 atom karbon.

    ### E. Ester  
    Gugus Fungsi: Alkoksi-karbonil (-COOR')  
    Rumus Umum: R-COOR'

    **Contoh:**  
    Metil asetat (CH₃COOCH₃): Ester yang memberikan aroma buah-buahan.

    ### F. Amida  
    Gugus Fungsi: Karbonil yang terikat pada gugus amino (-CONH₂)  
    Rumus Umum: R-CONH₂

    **Contoh:**  
    Etanamida (CH₃CONH₂): Amida paling sederhana yang berasal dari asam asetat.

    ## III. Senyawa Turunan Halogen (Haloalkana)

    Definisi: Senyawa organik di mana satu atau lebih atom hidrogen digantikan oleh atom halogen (F, Cl, Br, I).

    **Contoh:**  
    Metilklorida (CH₃Cl): Turunan metana dengan satu atom hidrogen digantikan oleh klorin.

    ## IV. Senyawa Aromatik Terganti

    Definisi: Senyawa benzena di mana satu atau lebih atom hidrogen pada cincin benzena digantikan oleh gugus lain.

    **Contoh:**  
    Etilbenzena (C₆H₅CH₂CH₃ atau C₆H₅C₂H₅): Benzena dengan satu gugus etil (-CH₂CH₃) terikat.

    ## V. Karbohidrat (Contoh Umum)

    Definisi: Senyawa organik yang mengandung karbon, hidrogen, dan oksigen, biasanya dengan rumus umum (CH₂O)n. Sumber energi utama bagi makhluk hidup.

    **Contoh:**  
    Glukosa (C₆H₁₂O₆): Monosakarida, gula sederhana yang merupakan unit dasar banyak karbohidrat kompleks.

    ---

    **Referensi:**  
    Irawan, C., & Utami, A. (2024). *Pengantar kimia organik*. Yogyakarta: Deepublish.
    """)
    if st.button("Mulai Kuis"):
            st.session_state.pt_started = True
    st.stop()

    # Setelah ini baru panggil fungsi kuis atau tampilkan soal kuis

    organic_questions = [
        {"q":"Apa rumus molekul dari metana?","a":"CH4"},
        {"q":"Apa gugus fungsi dari alkohol?","a":"OH"},
        {"q":"Apa nama senyawa CH3COOH?","a":"Asam asetat"},
        {"q":"Apa nama senyawa dengan rumus C2H5OH?","a":"Etanol"},
        {"q":"Apa nama senyawa C6H6?","a":"Benzena"},
        {"q":"Apa nama senyawa CH3CH2COOH?","a":"Asam propionat"},
        {"q":"Apa nama senyawa dengan rumus C3H7OH?","a":"Propanol"},
        {"q":"Apa nama senyawa yang memiliki rumus C6H12O6?","a":"Glukosa"},
        {"q":"Apa nama senyawa C4H9OH?","a":"Butanol"},
        {"q":"Apa nama senyawa CH3NH2?","a":"Metilamina"},
        {"q":"Apa nama senyawa dengan rumus C5H10O?","a":"Pentanol"},
        {"q":"Apa nama senyawa CH3CH2COCH3?","a":"Aseton"},
        {"q":"Apa nama senyawa dengan rumus C7H8?","a":"Toluena"},
        {"q":"Apa nama senyawa C8H10?","a":"Etilbenzen"},
        {"q":"Apa nama senyawa C10H12O2?","a":"Asam benzoat metil ester"},
        {"q":"Apa nama senyawa dengan rumus C3H6O?","a":"Asetaldehida"},
        {"q":"Apa nama senyawa C4H8O2?","a":"Asam butirat"},
        {"q":"Apa nama senyawa CH3COOCH3?","a":"Metil asetat"},
        {"q":"Apa nama senyawa dengan rumus C2H4O2?","a":"Asam asetat"},
        {"q":"Apa nama senyawa C9H12O?","a":"Fenilpropanol"}
    ]

    if "org_score" not in st.session_state:
        st.session_state.org_score = 0
        st.session_state.org_index = 0
        st.session_state.org_feedback = ""
        st.session_state.org_answered = False
        st.session_state.org_questions = random.sample(organic_questions, 5)

    if st.session_state.org_index < len(st.session_state.org_questions):
        q = st.session_state.org_questions[st.session_state.org_index]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.subheader(f"Soal #{st.session_state.org_index+1} dari 5")
        ans_in = st.text_input(f"🔬 {q['q']}", key=f"org_in_{st.session_state.org_index}")

        if st.button("Kirim Jawaban", key=f"org_sub_{st.session_state.org_index}") and not st.session_state.org_answered:
            if ans_in.strip().lower() == q['a'].lower():
                st.session_state.org_score += 1
                st.session_state.org_feedback = "✅ Jawaban Benar!"
                st.balloons()
            else:
                st.session_state.org_feedback = f"❌ Salah. Jawaban benar: {q['a']}"
            st.session_state.org_answered = True

        st.write(st.session_state.org_feedback)

        if st.session_state.org_answered:
            if st.button("➡ Soal Berikutnya", key=f"org_next_{st.session_state.org_index}"):
                st.session_state.org_index += 1
                st.session_state.org_feedback = ""
                st.session_state.org_answered = False

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'>🌟 Skor: {st.session_state.org_score}/5</div>", unsafe_allow_html=True)

    else:
        st.success(f"🎉 Kuis selesai! Skor akhir: {st.session_state.org_score}/5")
        if st.button("🔁 Ulangi Kuis"):
            for k in ["org_score", "org_index", "org_feedback", "org_answered", "org_questions"]:
                del st.session_state[k]
