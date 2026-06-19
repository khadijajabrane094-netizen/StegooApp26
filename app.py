from PIL import Image
import streamlit as st
import time

st.set_page_config(
    page_title="🛡️ StegoApp Premium",
    page_icon="🔒",
    layout="centered"
)

# ============================================================
# ===== BACKGROUND PHOTO =====
# ============================================================

background_url = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1920"

st.markdown(f"""
<style>
.stApp {{
    background: url("{background_url}") no-repeat center center fixed !important;
    background-size: cover !important;
}}

.stApp::before {{
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5) !important;
    z-index: 0;
    pointer-events: none;
}}

.stApp > div {{
    position: relative;
    z-index: 1;
}}

.block-container {{
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(25px) !important;
    -webkit-backdrop-filter: blur(25px) !important;
    border-radius: 40px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding: 35px !important;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4) !important;
    margin: 25px auto !important;
    max-width: 800px !important;
}}

/* ===== HEADER ===== */
h1 {{
    font-size: 32px !important;
    font-weight: 800 !important;
    text-align: center !important;
    background: linear-gradient(135deg, #00d4ff, #00ff88) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}}

/* ===== TABS ===== */
.stTabs [data-baseweb="tab-list"] {{
    gap: 12px;
    background: rgba(255,255,255,0.03);
    border-radius: 16px;
    padding: 6px;
    border: 1px solid rgba(255,255,255,0.03);
}}

.stTabs [data-baseweb="tab"] {{
    color: rgba(255, 255, 255, 0.6) !important;
    border-radius: 12px !important;
    padding: 10px 24px !important;
    font-weight: 600 !important;
}}

.stTabs [data-baseweb="tab"][aria-selected="true"] {{
    background: linear-gradient(135deg, #00d4ff, #00ff88) !important;
    color: #000000 !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}}

/* ===== BOUTONS ===== */
.stButton button {{
    background: linear-gradient(135deg, #00d4ff, #00ff88) !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 14px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    box-shadow: 0 4px 30px rgba(0, 212, 255, 0.15) !important;
    transition: all 0.3s ease !important;
}}

.stButton button:hover {{
    transform: scale(1.02) !important;
    box-shadow: 0 8px 40px rgba(0, 212, 255, 0.25) !important;
}}

/* ===== FILE UPLOADER ===== */
.stFileUploader {{
    border: 2px dashed rgba(0, 212, 255, 0.15) !important;
    border-radius: 20px !important;
    background: rgba(255,255,255,0.02) !important;
    transition: all 0.3s ease !important;
}}

.stFileUploader:hover {{
    border-color: rgba(0, 212, 255, 0.3) !important;
    background: rgba(0, 212, 255, 0.02) !important;
}}

/* ===== TEXTE UPLOADER EN NOIR ===== */
.stFileUploader div {{
    color: #000000 !important;
    opacity: 0.8 !important;
}}

.stFileUploader div span {{
    color: #000000 !important;
    opacity: 0.8 !important;
}}

.stFileUploader div small {{
    color: #000000 !important;
    opacity: 0.6 !important;
}}

/* ===== IMAGES ===== */
.stImage img {{
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.04) !important;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3) !important;
}}

/* ===== TEXT AREA ===== */
.stTextArea textarea {{
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 16px !important;
    color: #ffffff !important;
}}

.stTextArea textarea::placeholder {{
    color: rgba(255, 255, 255, 0.3) !important;
}}

.stTextArea textarea:focus {{
    border-color: rgba(0, 212, 255, 0.2) !important;
    box-shadow: 0 0 30px rgba(0, 212, 255, 0.02) !important;
}}

/* ===== MESSAGES ===== */
.stSuccess {{
    background: rgba(0, 212, 255, 0.08) !important;
    border-left: 4px solid #00d4ff !important;
    border-radius: 12px !important;
    backdrop-filter: blur(10px) !important;
}}

.stSuccess p {{
    color: #ffffff !important;
}}

.stError {{
    background: rgba(255, 68, 68, 0.08) !important;
    border-left: 4px solid #ff4444 !important;
    border-radius: 12px !important;
    backdrop-filter: blur(10px) !important;
}}

.stError p {{
    color: #ffffff !important;
}}

.stWarning {{
    background: rgba(255, 200, 0, 0.08) !important;
    border-left: 4px solid #ffcc00 !important;
    border-radius: 12px !important;
    backdrop-filter: blur(10px) !important;
}}

.stWarning p {{
    color: #ffffff !important;
}}

/* ===== METRIC ===== */
.stMetric label {{
    color: rgba(255, 255, 255, 0.5) !important;
}}

.stMetric div {{
    color: #ffffff !important;
}}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: rgba(255,255,255,0.02); border-radius: 10px; }}
::-webkit-scrollbar-thumb {{ background: linear-gradient(180deg, #00d4ff, #00ff88); border-radius: 10px; }}

/* ===== HIDE ===== */
#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
header {{ visibility: hidden; }}

/* ===== RESPONSIVE ===== */
@media (max-width: 600px) {{
    .block-container {{ padding: 20px !important; }}
}}
</style>
""", unsafe_allow_html=True)

# ============================================================
# ===== HEADER =====
# ============================================================

st.markdown("""
<div style="text-align:center; padding:10px 0 20px 0;">
    <span style="font-size:50px;">🛡️</span>
    <h1>StegoApp Premium</h1>
    <p style="color:rgba(255,255,255,0.4); font-size:14px; letter-spacing:2px;">
        ⚡ Système de Stéganographie LSB
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ===== FONCTIONS =====
# ============================================================

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary_data):
    parts = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    text = ""
    for part in parts:
        if len(part) == 8:
            text += chr(int(part, 2))
    return text

def encode_image(pil_img, secret_text):
    img = pil_img.convert('RGB')
    pixels = img.load()
    binary_secret = text_to_binary(secret_text + "$$$")
    data_index = 0
    data_len = len(binary_secret)
    width, height = img.size
    
    max_chars = (width * height * 3) // 8 - 3
    if len(secret_text) > max_chars:
        raise ValueError(f"⚠️ Message trop long! Max: {max_chars} caractères")
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if data_index < data_len:
                r = (r & 254) | int(binary_secret[data_index])
                data_index += 1
            if data_index < data_len:
                g = (g & 254) | int(binary_secret[data_index])
                data_index += 1
            if data_index < data_len:
                b = (b & 254) | int(binary_secret[data_index])
                data_index += 1
            pixels[x, y] = (r, g, b)
            if data_index >= data_len:
                break
        if data_index >= data_len:
            break
    return img

def decode_image(pil_img):
    pixels = pil_img.load()
    binary_data = ""
    width, height = pil_img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
    full_text = binary_to_text(binary_data)
    if "$$$" in full_text:
        return full_text.split("$$$")[0]
    return None

# ============================================================
# ===== INTERFACE =====
# ============================================================

tab1, tab2 = st.tabs(["🔒 Cacher un Message", "🔓 Extraire un Message"])

with tab1:
    # CARD BLANCHE
    st.markdown("""
    <div style="background:rgba(255,255,255,0.9); backdrop-filter:blur(10px); border-radius:20px; padding:20px; margin-bottom:15px; border:1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <p style="color:#000000; font-weight:700; font-size:16px; margin:0;">
            📤 Téléchargez votre image (JPG, JPEG, PNG)
        </p>
        <p style="color:#000000; opacity:0.6; font-size:13px; margin:5px 0 0 0;">
            200MB per file • JPG, PNG
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    fichier = st.file_uploader("", type=["jpg", "jpeg", "png"], key="enc", label_visibility="collapsed")
    
    if fichier:
        img = Image.open(fichier)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(img, width=200)
        with col2:
            st.markdown(f"<p style='color:rgba(255,255,255,0.8);'>📐 Dimensions: {img.size[0]} x {img.size[1]}</p>", unsafe_allow_html=True)
            max_car = (img.size[0] * img.size[1] * 3) // 8 - 3
            st.markdown(f"<p style='color:rgba(255,255,255,0.8);'>✏️ Capacité max: {max_car} caractères</p>", unsafe_allow_html=True)
        
        texte = st.text_area("💬 Message secret:", placeholder="Tapez votre message ici...")
        
        if st.button("🔒 Cacher le message", use_container_width=True):
            if texte:
                try:
                    with st.spinner("⏳ Encodage en cours..."):
                        img_encoded = encode_image(img, texte)
                        img_encoded.save("stego_output.png", "PNG")
                    st.success("✅ Message caché avec succès!")
                    with open("stego_output.png", "rb") as f:
                        st.download_button(
                            "📥 Télécharger l'image",
                            data=f,
                            file_name="stego_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                except Exception as e:
                    st.error(str(e))
            else:
                st.warning("⚠️ Entrez un message!")

with tab2:
    # CARD BLANCHE
    st.markdown("""
    <div style="background:rgba(255,255,255,0.9); backdrop-filter:blur(10px); border-radius:20px; padding:20px; margin-bottom:15px; border:1px solid rgba(255,255,255,0.2); box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        <p style="color:#000000; font-weight:700; font-size:16px; margin:0;">
            🔍 Téléchargez l'image stéganographiée (PNG)
        </p>
        <p style="color:#000000; opacity:0.6; font-size:13px; margin:5px 0 0 0;">
            200MB per file • PNG
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    fichier_stego = st.file_uploader("", type=["png"], key="dec", label_visibility="collapsed")
    
    if fichier_stego:
        img_stego = Image.open(fichier_stego)
        st.image(img_stego, width=200)
        
        if st.button("🔓 Extraire le message", use_container_width=True):
            with st.spinner("⏳ Extraction..."):
                time.sleep(0.5)
                result = decode_image(img_stego)
                if result:
                    st.success(f"📩 Message: **{result}**")
                else:
                    st.error("❌ Aucun message caché trouvé!")

# ============================================================
# ===== FOOTER =====
# ============================================================

st.markdown("""
<div style="text-align:center; color:rgba(255,255,255,0.2); font-size:12px; padding-top:25px; margin-top:20px; border-top:1px solid rgba(255,255,255,0.02); letter-spacing:1px;">
    🛡️ StegoApp Premium v3.0 — Projet de Soutenance 2026
</div>
""", unsafe_allow_html=True)