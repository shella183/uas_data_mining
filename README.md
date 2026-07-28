<div align="center">

  <!-- Header Banner Animasi -->
  <img src="https://capsule-render.vercel.app/render?type=waving&color=gradient&customColorList=10,12,24,20&height=230&section=header&text=UAS%20DATA%20MINING%20(SIF304)&fontSize=42&fontColor=ffffff&animation=twinkling&fontAlignY=38" width="100%" />

  <!-- Shields / Badges Status -->
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
    <img src="https://img.shields.io/badge/Plotly-5.18%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
    <img src="https://img.shields.io/badge/Pandas-2.1%2B-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  </p>

  <h3>🩺 Klasifikasi Diabetes (Supervised) & ☕ Clustering Gerai Kopi (Unsupervised)</h3>
  <p><i>Aplikasi Web Machine Learning End-to-End dengan UI Dark Mode Modern & Interactive Analytics</i></p>

</div>

---

## 🎓 Identitas Mahasiswa

<table>
  <tr>
    <td width="180px" align="center">
      <img src="https://cdn-icons-png.flaticon.com/512/3135/3135789.png" width="120px" style="border-radius: 50%;" />
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

Aplikasi ini telah di-deploy dan dapat diakses secara publik melalui tautan berikut:  
👉 **[Buka Aplikasi Streamlit Live Demo](https://uasdatamining-shella.streamlit.app/)**

---

## 📌 Deskripsi & Fitur Utama Proyek

Aplikasi ini dirancang untuk menyelesaikan dua permasalahan data mining utama menggunakan pendekatan **Supervised Learning** dan **Unsupervised Learning**:

### 1. 🩺 Modul Klasifikasi Risk Level Diabetes (Supervised)
* **Tujuan:** Memprediksi apakah seorang pasien berisiko mengidap penyakit diabetes berdasarkan indikator medis.
* **Algoritma yang Digunakan:**
  * K-Nearest Neighbors (KNN)
  * Naïve Bayes (GaussianNB)
  * Decision Tree Classifier
* **Fitur Unggulan:**
  * 📈 **Evaluasi Performa Model:** Menampilkan *Accuracy*, *Precision*, *Recall*, dan *F1-Score* secara *real-time*.
  * 🎯 **Confusion Matrix Visual:** Plot matriks interaktif menggunakan Plotly.
  * 🧪 **Form Prediksi Pasien:** Input parameter medis interaktif untuk melakukan simulasi diagnosis langsung.

### 2. ☕ Modul Clustering Lokasi Gerai Kopi (Unsupervised)
* **Tujuan:** Pengelompokan spasial & pemetaan lokasi gerai kopi untuk analisis kelayakan tempat/bisnis.
* **Algoritma yang Digunakan:** K-Means Clustering.
* **Fitur Unggulan:**
  * 🎛️ **Dinamis K-Selection:** Pemilihan jumlah klaster ($K=2$ hingga $K=6$) secara interaktif.
  * 🗺️ **Spatial Scatter Plot:** Visualisasi titik koordinat lokasi gerai beresolusi tinggi dengan skema warna kontras.
  * 📊 **Ringkasan Distribusi Data:** Tabel proporsi dan jumlah gerai pada masing-masing klaster.

---

## 📊 Ringkasan Dataset

| Modul | Dataset | Jumlah Sampel | Atribut / Fitur Utama | Target Output |
| :--- | :--- | :---: | :--- | :--- |
| **Klasifikasi** | `diabetes.csv` | 768 Data | Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigree, Age | Outcome (`0`: Sehat, `1`: Diabetes) |
| **Clustering** | `gerai_kopi.csv` | 200+ Data | Koordinat X, Koordinat Y, Kepadatan Penduduk, Arus Lalu Lintas, Jumlah Kompetitor | Cluster ID (`Klaster 1`, `Klaster 2`, dst.) |

---

## 📂 Struktur Repositori

```text
uas_data_mining/
│
├── 📁 data/                        # Directory dataset
│   ├── diabetes.csv                # Dataset medis pasien diabetes
│   └── gerai_kopi.csv              # Dataset lokasi & demografi gerai kopi
│
├── 📁 pages/                       # Multi-page Streamlit views
│   ├── 1_🩺_Klasifikasi.py         # Modul Klasifikasi Diabetes
│   └── 2_☕_Clustering.py          # Modul Clustering Gerai Kopi
│
├── .gitignore                      # Pengabaian file cache & environment Git
├── Home.py                         # Landing page utama aplikasi
├── PANDUAN_PENGERJAAN.md           # Panduan pengerjaan & modul teori proyek
├── requirements.txt                # Dependensi pustaka Python
└── README.md                       # Dokumentasi resmi proyek

```

---

## 🛠️ Teknologi yang Digunakan

Aplikasi ini dibangun menggunakan *tech stack* modern untuk memastikan pemrosesan data presisi dan performa antarmuka yang cepat:

* **Bahasa Pemrograman:** `Python 3.11+`
* **Web Framework & UI:** `Streamlit 1.28+`
* **Machine Learning & Preprocessing:** `Scikit-Learn` (KNN, GaussianNB, DecisionTreeClassifier, KMeans, StandardScaler)
* **Pengolahan & Analisis Data:** `Pandas`, `NumPy`
* **Visualisasi Data Interaktif:** `Plotly Express`, `Plotly Graph Objects`
* **Deployment & Hosting:** `Streamlit Community Cloud`

---

## 🚀 Cara Menjalankan Aplikasi Secara Lokal

Ingin mencoba dan menjalankan aplikasi ini langsung di komputer lokal kamu? Ikuti panduan langkah demi langkah berikut:

### 1. Prasyarat

Pastikan kamu sudah menginstal **Python 3.9** atau versi yang lebih baru di komputermu.

### 2. Clone Repositori

Buka Terminal / Command Prompt, lalu jalankan perintah:

```bash
git clone [https://github.com/shella183/uas_data_mining.git](https://github.com/shella183/uas_data_mining.git)
cd uas_data_mining

```

### 3. Buat & Aktifkan Virtual Environment (Opsional tapi Disarankan)

```bash
# Untuk Windows:
python -m venv venv
venv\Scripts\activate

# Untuk macOS / Linux:
python3 -m venv venv
source venv/bin/activate

```

### 4. Install Seluruh Dependensi

Jalankan perintah berikut untuk mengunduh pustaka/library yang dibutuhkan:

```bash
pip install -r requirements.txt

```

### 5. Jalankan Aplikasi Streamlit

Setelah instalasi selesai, jalankan perintah utama berikut:

```bash
streamlit run Home.py

```

Aplikasi akan secara otomatis terbuka di browser kamu pada alamat `http://localhost:8501`.

---
