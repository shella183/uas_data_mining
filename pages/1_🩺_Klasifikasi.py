import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

st.set_page_config(page_title="Klasifikasi Diabetes", page_icon="🩺", layout="wide")

# --- Custom Styling CSS (Menyamakan Sidebar & Layout Gelap + Fix Label Terang) ---
st.markdown("""
    <style>
    /* 1. Background Utama */
    .stApp {
        background-color: #0b0f19 !important;
        color: #f3f4f6 !important;
    }

    /* 2. Sidebar / Menu Samping (Dark Navy) */
    section[data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 1px solid #1f2937 !important;
    }
    
    /* Warna teks dan link di sidebar */
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

    /* Active link di sidebar */
    div[data-testid="stSidebarNav"] a[aria-selected="true"] {
        background-color: #1f2937 !important;
        border-radius: 8px;
    }
    div[data-testid="stSidebarNav"] a[aria-selected="true"] span {
        color: #ffffff !important;
        font-weight: 600;
    }

    /* 3. Hero / Header Card Container */
    .hero-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 24px;
    }

    .badge-header {
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.25), rgba(79, 70, 229, 0.25));
        border: 1px solid rgba(168, 85, 247, 0.4);
        color: #d8b4fe !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
    }

    .main-title {
        color: #ffffff !important;
        font-size: 2.1rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .sub-title {
        color: #9ca3af !important;
        font-size: 0.95rem;
        margin-bottom: 0;
    }

    /* 4. Metric Box Styling */
    div[data-testid="stMetricValue"] {
        color: #38bdf8 !important; /* Warna cyan cerah kontras */
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #9ca3af !important;
        font-weight: 600 !important;
    }

    /* ------------------------------------------------------------- */
    /* FIX UTAMA: MEMBUAT LABEL WIDGET & FORM BERWARNA PUTIH TERANG */
    /* ------------------------------------------------------------- */
    div[data-testid="stWidgetLabel"] p, 
    div[data-testid="stWidgetLabel"] label,
    label[data-testid="stWidgetLabel"],
    .stNumberInput label, 
    .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        opacity: 1 !important;
    }

    /* Teks Tab (Evaluasi Model & Form Prediksi Pasien) */
    button[data-baseweb="tab"] div p {
        color: #d1d5db !important;
        font-weight: 600 !important;
    }
    button[aria-selected="true"][data-baseweb="tab"] div p {
        color: #ec4899 !important; /* Warna aksen pink saat tab aktif */
    }

    /* Subtitle Caption */
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #9ca3af !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Elemen Tambahan di Sidebar (Profil Mahasiswa) ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # URL Ikon Wanita dari Flaticon
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

# --- Header Section ---
st.markdown("""
<div class="hero-card">
    <div class="badge-header">✨ Modul Supervised Learning</div>
    <div class="main-title">🩺 Klasifikasi Diabetes Pasien</div>
    <div class="sub-title">Menganalisis indikator kesehatan pasien berbasis algoritma Machine Learning (KNN, Naïve Bayes, Decision Tree) untuk memprediksi risiko penyakit diabetes secara akurat.</div>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("data/diabetes.csv")

df = load_data()
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tab1, tab2 = st.tabs(["📊 Evaluasi Model", "🧪 Form Prediksi Pasien"])

with tab1:
    col_sel, _ = st.columns([1, 2])
    with col_sel:
        algo = st.selectbox("Pilih Algoritma Model:", ["K-Nearest Neighbors (KNN)", "Naïve Bayes", "Decision Tree"])
    
    if algo == "K-Nearest Neighbors (KNN)":
        model = KNeighborsClassifier(n_neighbors=5)
    elif algo == "Naïve Bayes":
        model = GaussianNB()
    else:
        model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.2%}")
    c2.metric("Precision", f"{precision_score(y_test, y_pred):.2%}")
    c3.metric("Recall", f"{recall_score(y_test, y_pred):.2%}")
    c4.metric("F1-Score", f"{f1_score(y_test, y_pred):.2%}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 🎯 Confusion Matrix")
    
    cm = confusion_matrix(y_test, y_pred)
    
    fig = px.imshow(
        cm, 
        text_auto=True, 
        x=['Non-Diabetes', 'Diabetes'], 
        y=['Non-Diabetes', 'Diabetes'], 
        color_continuous_scale=['#0f172a', '#6b21a8', '#ec4899']
    )
    fig.update_layout(
        template="plotly_dark", 
        height=380,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("### 📝 Input Data Medis Pasien")
    st.caption("Isi nilai variabel medis di bawah ini untuk mensimulasikan hasil analisis prediksi.")
    
    c1, c2, c3 = st.columns(3)
    preg = c1.number_input("Pregnancies (Jumlah Kehamilan)", 0, 20, 1)
    gluc = c2.number_input("Glucose (Kadar Gula Darah)", 0, 300, 120)
    bp = c3.number_input("Blood Pressure (Tekanan Darah)", 0, 150, 70)

    c4, c5, c6 = st.columns(3)
    skin = c4.number_input("Skin Thickness (Ketebalan Kulit)", 0, 100, 20)
    ins = c5.number_input("Insulin", 0, 900, 79)
    bmi = c6.number_input("BMI (Indeks Massa Tubuh)", 0.0, 70.0, 25.0)

    c7, c8 = st.columns(2)
    dpf = c7.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.47)
    age = c8.number_input("Age (Usia)", 1, 120, 30)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔍 Jalankan Analisis Prediksi", use_container_width=True):
        res = model.predict([[preg, gluc, bp, skin, ins, bmi, dpf, age]])[0]
        if res == 1:
            st.error("⚠️ **Hasil Prediksi:** Pasien **BERISIKO MENGIDAP DIABETES**.")
        else:
            st.success("✅ **Hasil Prediksi:** Pasien Diprediksi **SEHAT (NON-DIABETES)**.")