import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Clustering Gerai Kopi - UAS Data Mining",
    page_icon="☕",
    layout="wide"
)

# 2. CUSTOM STYLING CSS (DISAMAKAN PERSIS DENGAN MENU KLASIFIKASI)
st.markdown("""
    <style>
    /* 1. Background Utama */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0b0f19 !important;
        color: #f3f4f6 !important;
    }

    /* 2. Sidebar / Menu Samping (Dark Navy Persis Klasifikasi) */
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

    /* Custom Title & Labels */
    h1, h2, h3, h4, h5, h6, label {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    /* Card Container Estetis */
    .control-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 18px 22px;
        margin-bottom: 20px;
    }
    
    /* Metric Box */
    .metric-box {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border: 1px solid #1f2937;
        padding: 12px 15px;
        border-radius: 10px;
        text-align: center;
    }
    .metric-val {
        font-size: 22px;
        font-weight: bold;
        color: #38bdf8;
    }
    .metric-lbl {
        font-size: 12px;
        color: #9ca3af;
    }
    
    /* Styling Slider & Radio */
    div[data-baseweb="slider"] * {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: ELEMEN INFORMASI MAHASISWA & AVATAR ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # URL Ikon Wanita yang Anda berikan
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

# 3. HEADER BANNER UTAMA (HERO CARD STYLE KLASIFIKASI)
st.markdown("""
<div style="background-color: #111827; border: 1px solid #1f2937; padding: 24px; border-radius: 12px; margin-bottom: 24px;">
    <span style="background: linear-gradient(135deg, rgba(147, 51, 234, 0.25), rgba(79, 70, 229, 0.25)); border: 1px solid rgba(168, 85, 247, 0.4); color: #d8b4fe; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; display: inline-block; margin-bottom: 12px;">
        ✨ Modul Unsupervised Learning
    </span>
    <h2 style="margin-top: 5px; margin-bottom: 8px; color: #ffffff; font-size: 2.1rem; font-weight: 800;">☕ Analisis Klaster Gerai Kopi & Spatial Mapping</h2>
    <p style="color: #9ca3af; margin: 0; font-size: 0.95rem;">
        Pengelompokan posisi pemetaan gerai kopi menggunakan algoritma <b>K-Means Clustering</b> untuk analisis spasial bisnis.
    </p>
</div>
""", unsafe_allow_html=True)

# 4. LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("data/gerai_kopi.csv")
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_cols) < 2:
        st.error("File CSV kurang dari 2 kolom angka. Mohon periksa kembali ketersediaan data.")
    else:
        # 5. KONTROL PARAMETER DENGAN CARA BARU (ESTETIS & JELAS)
        col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([1.5, 1, 1])
        
        with col_ctrl1:
            st.markdown("##### 🎛️ Pilih Jumlah Klaster (K)")
            k = st.radio(
                label="Pilih Klaster",
                options=[2, 3, 4, 5, 6],
                index=1, # Default 3
                horizontal=True,
                label_visibility="collapsed"
            )
            
        with col_ctrl2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-lbl">Total Dataset Gerai</div>
                <div class="metric-val">{len(df):,}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with col_ctrl3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-lbl">Status Klaster Aktif</div>
                <div class="metric-val" style="color: #ec4899;">{k} Klaster</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 6. K-MEANS CLUSTERING ENGINE
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        df['Cluster_ID'] = kmeans.fit_predict(df[numeric_cols])
        df['Cluster'] = "Klaster " + (df['Cluster_ID'] + 1).astype(str)

        # 7. VISUALISASI GRAFIK HD & MODERN
        col_graph, col_info = st.columns([2.3, 1])

        x_col = numeric_cols[0]
        y_col = numeric_cols[1]

        # Warna Terang High-Contrast
        vibrant_colors = ['#FF0055', '#00E5FF', '#7600FF', '#00FF66', '#FFB703', '#FB8500', '#E63946']

        with col_graph:
            st.subheader("🗺️ Visualisasi Persebaran Klaster")
            
            fig_map = px.scatter(
                df,
                x=x_col,
                y=y_col,
                color='Cluster',
                hover_data=df.columns,
                color_discrete_sequence=vibrant_colors
            )
            
            fig_map.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="#111827",
                font=dict(family="Sans-Serif", color="#f3f4f6"),
                xaxis=dict(
                    gridcolor="#1f2937", 
                    zerolinecolor="#374151", 
                    title=f"Koordinat X ({x_col})"
                ),
                yaxis=dict(
                    gridcolor="#1f2937", 
                    zerolinecolor="#374151", 
                    title=f"Koordinat Y ({y_col})"
                ),
                margin=dict(l=10, r=10, t=20, b=10),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    title=None
                )
            )
            
            fig_map.update_traces(
                marker=dict(
                    size=8,
                    opacity=0.85,
                    line=dict(width=0.4, color='#ffffff')
                )
            )
            
            st.plotly_chart(fig_map, use_container_width=True)

        with col_info:
            st.subheader("📊 Distribusi Data")
            
            cluster_summary = df.groupby('Cluster').size().reset_index(name='Jumlah Gerai')
            cluster_summary['Persentase'] = ((cluster_summary['Jumlah Gerai'] / len(df)) * 100).round(1).astype(str) + '%'
            
            st.dataframe(
                cluster_summary,
                column_config={
                    "Cluster": "Nama Klaster",
                    "Jumlah Gerai": st.column_config.NumberColumn("Jumlah", format="%d"),
                    "Persentase": "Proporsi"
                },
                hide_index=True,
                use_container_width=True
            )

        # 8. TABEL DATA DETAIL
        st.markdown("---")
        with st.expander("📋 Data Hasil Clustering Lengkap"):
            st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Terjadi kesalahan teknis: {e}")