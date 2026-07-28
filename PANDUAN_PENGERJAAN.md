## 🧩 Bagian 0 — Gambaran Umum & Arsitektur Proyek

Soal UAS mengharuskan pembangunan satu aplikasi interaktif berbasis **Streamlit** dengan arsitektur **Multi-Page Application**. Aplikasi ini mengintegrasikan dua pendekatan utama dalam Data Mining:

| Domain Proyek | Pendekatan Learning | Algoritma Utama | Output & Evaluasi |
| :--- | :--- | :--- | :--- |
| **Bagian A: Prediksi Diabetes** | Supervised Learning (Klasifikasi) | • K-Nearest Neighbors (KNN)<br>• Naïve Bayes (Gaussian)<br>• Decision Tree | • Benchmark Metrik Evaluasi (*Accuracy, Precision, Recall, F1-Score*)<br>• Interactive Heatmap Confusion Matrix<br>• Form Simulasi Prediksi Pasien Realtime |
| **Bagian B: Clustering Gerai Kopi** | Unsupervised Learning (Clustering) | K-Means Clustering | • Dynamic Cluster Selection ($K=2 \dots 8$)<br>• Interactive Spatial Scatter Plot (Koordinat X & Y)<br>• Automated Low-Activity Zone Detection ("Zona Sepi")<br>• Form Analisis Kelayakan Lokasi Baru |

---

## 📂 Struktur Direktori Repositori

Proyek ini terstruktur secara modular untuk memastikan keterbacaan kode (*code readability*) dan kemudahan penguji dalam mengevaluasi sistem:

```text
uas_data_mining/
│
├── 📁 data/                        # Direktori penyimpanan dataset utama
│   ├── diabetes.csv                # Dataset medis indikator kesehatan pasien
│   └── gerai_kopi.csv              # Dataset variabel demografi & lokasi bisnis
│
├── 📁 pages/                       # Multi-page views (Streamlit otomatis mendeteksi folder ini)
│   ├── 1_🩺_Klasifikasi.py         # Modul Supervised Learning (Diabetes)
│   └── 2_☕_Clustering.py          # Modul Unsupervised Learning (Gerai Kopi)
│
├── .gitignore                      # Konfigurasi pengabaian file cache Git/Python
├── Home.py                         # Entry point / Landing Page utama aplikasi
├── requirements.txt                # Dependensi pustaka Python untuk Streamlit Cloud
├── PANDUAN_PENGERJAAN.md           # Panduan teknis & teori komprehensif proyek
└── README.md                       # Dokumentasi resmi repositori GitHub

```

---

## 🧠 Bagian 1 — Pemahaman Konsep Teori & Materi Sidang

Sebelum melakukan presentasi atau pengumpulan, pahami alur kerja dan teori dasar yang diimplementasikan pada kode program berikut:

### 1. Preprocessing Data Medis (`diabetes.csv`)

* **Masalah:** Pada dataset medis, terdapat angka `0` pada atribut biologis seperti Glucose, BloodPressure, SkinThickness, Insulin, dan BMI. Secara medis, nilai `0` pada parameter ini tidak mungkin terjadi pada manusia hidup.
* **Solusi:** Nilai `0` diperlakukan sebagai *Missing Value* (data hilang) dan diimputasi menggunakan **Nilai Median** dari masing-masing kolom. Imputasi median dipilih agar tidak terpengaruh oleh *outlier* (pencilan) ekstrem.

### 2. Feature Scaling (StandardScaler)

* **Konsep:** Mentransformasikan data agar memiliki rata-rata ($\mu = 0$) dan standar deviasi ($\sigma = 1$).
* **Mengapa KNN butuh scaling?** KNN menghitung jarak antar titik data menggunakan rumus **Jarak Euclidean**:

$$d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}$$



Jika satu variabel memiliki rentang angka ratusan (seperti Insulin) dan variabel lain hanya angka puluhan (seperti BMI), maka variabel Insulin akan mendominasi perhitungan jarak.
* **Mengapa Decision Tree tidak butuh scaling?** Decision Tree membuat keputusan berdasarkan pembagian nilai ambang batas (*threshold split*) menggunakan algoritma seperti **Gini Impurity** atau **Entropy**. Skala relatif angka tidak mengubah urutan pemisahan fitur.

### 3. Pemodelan Klasifikasi & Metrik Evaluasi

* **Accuracy:** Persentase prediksi benar dari total keseluruhan data.
* **Precision:** Tingkat ketepatan model dari seluruh hasil yang diprediksi positif ($TP / (TP + FP)$).
* **Recall (Sensitivity):** Kemampuan model menemukan kembali seluruh kasus positif yang sebenarnya ($TP / (TP + FN)$). Sangat krusial pada domain medis untuk menghindari *False Negative* (pasien sakit tapi terprediksi sehat).
* **F1-Score:** Rata-rata harmonik antara Precision dan Recall.

### 4. K-Means Clustering & Detection Zone (`gerai_kopi.csv`)

* **Penentuan Centroid:** Parameter `random_state=42` ditetapkan pada algoritma K-Means untuk menjaga konsistensi pengelompokan (*reproducibility*) setiap kali aplikasi dimuat ulang.
* **Skor Potensi Lokasi (Formula Zona Sepi):** Untuk mendeteksi klaster mana yang merupakan "Zona Sepi", sistem menghitung rata-rata rasio aktivitas berdasarkan rumus:

$$\text{Activity Score} = (\text{Kepadatan Penduduk} + \text{Lalu Lintas}) - (2 \times \text{Jumlah Kompetitor})$$



Klaster dengan nilai rata-rata *Activity Score* paling rendah secara otomatis ditandai sebagai **Zona Sepi / Risiko Tinggi**.

---

## 💻 Bagian 2 — Panduan Pengujian Aplikasi Secara Lokal

Gunakan perintah terminal berikut untuk menjalankan aplikasi di lingkungan komputer lokal kamu:

1. **Buka Terminal / Command Prompt**, navigasi ke folder proyek:
```bash
cd uas_data_mining

```


2. **Buat & Aktifkan Virtual Environment (Disarankan):**
```bash
# Di Windows
python -m venv venv
venv\Scripts\activate

# Di macOS/Linux
python3 -m venv venv
source venv/bin/activate

```


3. **Install Pustaka yang Dibutuhkan:**
```bash
pip install -r requirements.txt

```


4. **Jalankan Aplikasi Streamlit:**
```bash
streamlit run Home.py

```


5. **Pengujian Fitur:**
* Buka browser pada alamat `http://localhost:8501`.
* Pindah ke halaman **1_🩺_Klasifikasi.py**, pilih algoritma, dan coba masukkan input simulasi medis baru.
* Pindah ke halaman **2_☕_Clustering.py**, geser slider jumlah klaster ($K$), dan amati perubahan visual scatter plot serta zona sepi.



---

## 🐙 Bagian 3 — Sintaks & Perintah Git untuk GitHub

Untuk mengunggah seluruh perubahan dari lokal ke repositori GitHub milikmu (`shella183/uas_data_mining`), jalankan perintah Git berikut:

```bash
# 1. Inisialisasi repositori Git (jika belum)
git init

# 2. Menambahkan seluruh file ke staging area
git add .

# 3. Simpan perubahan dengan pesan commit yang jelas
git commit -m "feat: Update dokumentasi lengkap UAS Data Mining Shella Salsabila (23146051)"

# 4. Atur branch utama ke main
git branch -M main

# 5. Menghubungkan ke repositori GitHub milikmu
git remote add origin [https://github.com/shella183/uas_data_mining.git](https://github.com/shella183/uas_data_mining.git)

# 6. Upload seluruh kode ke GitHub
git push -u origin main --force

```

---

## ☁️ Bagian 4 — Panduan Deploy ke Streamlit Cloud

1. Masuk ke dashboard **[Streamlit Community Cloud](https://share.streamlit.io/)** menggunakan akun GitHub kamu.
2. Klik tombol **New app** di sudut kanan atas.
3. Isikan form pendaftaran aplikasi sesuai data berikut:
* **Repository:** `shella183/uas_data_mining`
* **Branch:** `main`
* **Main file path:** `Home.py`
* **App URL (Custom):** `uasdatamining-shella` *(opsional jika masih tersedia)*


4. Klik **Deploy!**
5. Tunggu proses instalasi pustaka dari `requirements.txt` selesai hingga dashboard live kamu muncul.
6. Catat URL aplikasi yang berhasil di-deploy (misal: `https://uasdatamining-shella.streamlit.app/`).

---

## 📄 Bagian 5 — Panduan Penyusunan Laporan PDF (Format Nilai Maksimal)

Laporan PDF diketik menggunakan format kertas A4, margin standar (2.5 cm), font Times New Roman / Calibri, dengan susunan bab sebagai berikut:

### 1. Halaman Cover

* Judul Laporan: *Laporan Akhir Semester Data Mining (SIF304) — Sistem Klasifikasi Kesehatan & Analisis Spasial Bisnis*
* Nama Lengkap: **Shella Salsabila**
* NIM: **23146051**
* Program Studi: Sistem Informasi
* Dosen Pengampu: **Teuku Rizky Noviandy, S.Kom., M.Kom.**
* Tautan Utama: Link Repository GitHub & Link Streamlit Cloud Live Demo.

### 2. Bab I — Pendahuluan & Identifikasi Masalah

* Latar belakang pentingnya Machine Learning untuk prediksi risiko kesehatan (Diabetes) dan pengambilan keputusan lokasi usaha (Gerai Kopi).
* Tujuan pembuatan aplikasi web berbasis Streamlit.

### 3. Bab II — Bagian A: Klasifikasi Diabetes

* **Metodologi Data:** Penjelasan jumlah dataset (768 data) dan teknik penanganan *missing values* (imputasi median).
* **Hasil Evaluasi Model:** Lampirkan tabel perbandingan performa (*Accuracy, Precision, Recall, F1-Score*) untuk ketiga algoritma (KNN, Naïve Bayes, Decision Tree).
* **Analisis Perbandingan:** Penjelasan algoritma mana yang paling unggul beserta alasannya.
* **Tampilan Antarmuka:** Screenshot Confusion Matrix dan Form Prediksi Pasien Baru dari aplikasi live.

### 4. Bab III — Bagian B: Clustering Gerai Kopi

* **Metodologi K-Means:** Penjelasan penentuan jumlah klaster $K$ dan teknik *scaling* variabel spasial.
* **Analisis Klaster & Zona Sepi:** Lampirkan grafik *Spatial Scatter Plot* dan jelaskan ciri-ciri klaster yang teridentifikasi sebagai zona sepi/potensi rendah.
* **Tampilan Antarmuka:** Screenshot pemetaan klaster dan form pengujian lokasi bisnis baru.

### 5. Bab IV — Kesimpulan & Saran

* Ringkasan temuan analisis dari modul klasifikasi dan clustering.
* Tautan lampiran publik.

---

## 📋 Checklist Akhir Sebelum Submisi Tugas

* [x] Kode program berjalan tanpa error secara lokal (`streamlit run Home.py`).
* [x] Identitas Nama (Shella Salsabila) dan NIM (23146051) terpasang di `Home.py` dan `README.md`.
* [x] Repositori GitHub tersetting **Public** dan memiliki struktur file yang rapi.
* [x] File `.gitignore`, `requirements.txt`, dan `PANDUAN_PENGERJAAN.md` tersedia di repositori.
* [x] Aplikasi berhasil tayang di Streamlit Cloud dan seluruh fiturnya dapat diakses.
* [x] Laporan PDF sudah di-export dan siap dikirimkan sesuai petunjuk pengumpulan.

```

```
