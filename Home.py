import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Data Mining Intelligence - UAS Project",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function Load Lottie Animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Animation JSON
lottie_ai = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_m64ro6zs.json")

# 2. Styling Kustom: Dark Luxe, Gradient Glow & Cards (Sidebar Disamakan)
st.markdown("""
<style>
    /* Background Gradient Utama */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #030712 100%);
        color: #f3f4f6;
    }

    /* Target khusus Sidebar (Dark Navy Persis Klasifikasi & Clustering) */
    section[data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 1px solid #1f2937 !important;
    }
    
    /* Warna teks dan label di sidebar */
    section[data-testid="stSidebar"] *, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] p {
        color: #9ca3af !important;
    }

    /* Target item navigasi Streamlit di sidebar */
    div[data-testid="stSidebarNav"] span {
        color: #d1d5db !important;
        font-weight: 500;
    }

    /* Active link / Menu aktif di sidebar */
    div[data-testid="stSidebarNav"] a[aria-selected="true"] {
        background-color: #1f2937 !important;
        border-radius: 8px;
    }
    div[data-testid="stSidebarNav"] a[aria-selected="true"] span {
        color: #ffffff !important;
        font-weight: 600;
    }
    
    /* Header Card Mewah */
    .hero-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
    }
    
    /* Gradien Teks Judul */
    .gradient-title {
        background: linear-gradient(90deg, #a855f7, #ec4899, #f59e0b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.8rem;
    }
    
    /* Badge Profil */
    .profile-badge {
        background: linear-gradient(90deg, rgba(168, 85, 247, 0.2), rgba(236, 72, 153, 0.2));
        border: 1px solid rgba(168, 85, 247, 0.4);
        padding: 8px 16px;
        border-radius: 30px;
        display: inline-block;
        font-weight: 600;
        color: #e9d5ff;
        margin-bottom: 15px;
    }
    
    /* Hover Card Feature */
    .feature-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 20px;
        transition: all 0.3s ease-in-out;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #a855f7;
        box-shadow: 0 10px 25px rgba(168, 85, 247, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Profile Info (Format & Avatar Disamakan)
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # URL Avatar
    img_url = "https://cdn-icons-png.flaticon.com/512/3135/3135789.png"
    
    st.markdown(f'''
        <div style="margin-bottom: 15px;">
            <img src="{img_url}" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 3px solid #ec4899; box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3); background-color: #f3f4f6;">
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("### 🎓 Informasi Mahasiswa")
    st.markdown("""
    **Nama:** Shella Salsabila  
    **NIM:** 23146051  
    **Mata Kuliah:** Data Mining (SIF304)  
    **Dosen:** Teuku Rizky Noviandy, S.Kom., M.Kom.
    """)
    st.markdown("---")
    st.info("💡 **Gunakan Sidebar** untuk berpindah antar modul klasifikasi dan clustering.")

# 4. Hero Section
col_hero1, col_hero2 = st.columns([2, 1])

with col_hero1:
    st.markdown('<div class="profile-badge">✨ UAS Data Mining (SIF304) Project</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="gradient-title">Data Mining Intelligence Portal</h1>', unsafe_allow_html=True)
    st.markdown("""
    Selamat datang di platform interaktif analisis data mining. Portal ini mengintegrasikan metode **Supervised Learning** untuk prediksi medis dan **Unsupervised Learning** untuk analisis spasial bisnis.
    """)

with col_hero2:
    if lottie_ai:
        st_lottie(lottie_ai, height=200, key="ai_anim")

st.markdown("---")

# 5. Fitur Modul (Dua Kolom Card)
st.markdown("### 📌 **Pilih Modul Analisis**")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🩺 Klasifikasi Diabetes</h3>
        <p style="color: #9ca3af;">Menganalisis indikator kesehatan pasien berbasis algoritma Machine Learning (KNN, Naïve Bayes, Decision Tree) untuk memprediksi risiko penyakit diabetes secara akurat.</p>
        <p><b>Fitur:</b> Metrics Evaluation, Confusion Matrix, & Live Prediction Form.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>☕ Clustering Gerai Kopi</h3>
        <p style="color: #9ca3af;">Pengelompokan titik spasial lokasi gerai kopi menggunakan K-Means Clustering untuk memetakan kepadatan serta mendeteksi <b>Zona Sepi</b> (area berisiko rendah konsumen).</p>
        <p><b>Fitur:</b> Interactive Map Box, K-Means Slider, & Location Evaluator.</p>
    </div>
    """, unsafe_allow_html=True)