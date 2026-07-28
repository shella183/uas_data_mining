<div align="center">

  <!-- Header Banner Animasi (Fixed) -->
  <img src="https://capsule-render.vercel.app/render?type=waving&color=auto&height=220&section=header&text=UAS%20DATA%20MINING%20(SIF304)&fontSize=40&fontColor=ffffff&animation=twinkling&fontAlignY=38" width="100%" />

  <!-- Status & Interactive Badges -->
  <p align="center">
    <a href="https://uasdatamining-shella.streamlit.app/">
      <img src="https://img.shields.io/badge/Live_Demo-Streamlit_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
    </a>
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
    <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
  </p>

  <h3>🩺 Prediksi Diabetes (Supervised) & ☕ Clustering Gerai Kopi (Unsupervised)</h3>
  <p><i>Aplikasi Web Machine Learning End-to-End dengan UI Dark Mode Modern & Dashboard Analisis Interaktif</i></p>

</div>

---

## 🎓 Informasi Mahasiswa & Pengampu

<table>
  <tr>
    <td width="150px" align="center">
      <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" width="110px" style="border-radius: 50%;" />
    </td>
    <td>
      <ul>
        <li><b>Nama Lengkap:</b> Shella Salsabila</li>
        <li><b>NIM:</b> <code>23146051</code></li>
        <li><b>Mata Kuliah:</b> Data Mining (SIF304)</li>
        <li><b>Dosen Pengampu:</b> Teuku Rizky Noviandy, S.Kom., M.Kom.</li>
        <li><b>Program Studi:</b> Sistem Informasi</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🌐 Live Demo Application

Aplikasi ini dapat diakses secara publik dan realtime melalui tautan berikut:  
👉 **[https://uasdatamining-shella.streamlit.app/](https://uasdatamining-shella.streamlit.app/)**

---

## 📌 Fitur Unggulan Proyek (Nilai Tambah)

Aplikasi ini tidak hanya menyajikan prediksi dasar, tetapi dilengkapi fitur analitis canggih:

### 🩺 Modul Klasifikasi Diabetes (Supervised Learning)
* **Multi-Model Benchmark:** Membandingkan 3 algoritma sekaligus (**KNN**, **Naïve Bayes**, **Decision Tree**).
* **Evaluasi Komprehensif:** Metrik otomatis mencakup *Accuracy*, *Precision*, *Recall*, dan *F1-Score*.
* **Visualisasi Matrix:** *Confusion Matrix* interaktif menggunakan skema warna heatmap dark-mode.
* **Simulasi Prediksi Pasien:** Form input data medis langsung (*Pregnancies, Glucose, BP, BMI, Age*, dll) dengan *real-time alert Output*.

### ☕ Modul Clustering Gerai Kopi (Unsupervised Learning)
* **K-Means Clustering:** Pengelompokan lokasi bisnis berbasis pemodelan spasial.
* **Dynamic Elbow & K-Selection:** Fleksibilitas menentukan jumlah klaster ($K=2$ hingga $K=6$).
* **Pemetaan Visual:** Interactive Scatter Plot menggunakan Plotly Express untuk analisis zona kompetisi & potensi pasar.

---

## 📊 Detail Dataset & Pemodelan

| Parameter | Modul Klasifikasi | Modul Clustering |
| :--- | :--- | :--- |
| **Dataset** | `diabetes.csv` | `gerai_kopi.csv` |
| **Metode/Algoritma** | KNN, Naïve Bayes, Decision Tree | K-Means Clustering |
| **Tipe Pembelajaran** | Supervised Learning | Unsupervised Learning |
| **Jumlah Fitur/Atribut** | 8 Variabel Medis | 5 Variabel Spasial & Demografi |
| **Output Utama** | Klasifikasi Risiko (`Sehat` / `Diabetes`) | Klaster Pemetaan Lokasi Strategis |

---

## 📂 Arsitektur Repositori

```text
uas_data_mining/
│
├── 📁 data/                        # File Dataset CSV
│   ├── diabetes.csv                # Dataset Medis Pasien
│   └── gerai_kopi.csv              # Dataset Demografi & Lokasi Gerai
│
├── 📁 pages/                       # Multi-page Views Streamlit
│   ├── 1_🩺_Klasifikasi.py         # Modul Supervised Learning
│   └── 2_☕_Clustering.py          # Modul Unsupervised Learning
│
├── .gitignore                      # File konfig pengabaian cache Git
├── Home.py                         # Landing Page Utama Aplikasi
├── requirements.txt                # Dependensi Pustaka Python
└── README.md                       # Dokumentasi Resmi Proyek
