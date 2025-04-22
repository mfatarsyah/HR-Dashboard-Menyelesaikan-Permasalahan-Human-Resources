# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## 📘 Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di berbagai wilayah Indonesia. Selama dua dekade lebih beroperasi, perusahaan ini telah berkembang menjadi salah satu pemain utama di sektor industrinya. Namun, meskipun secara skala bisnis telah besar, perusahaan masih menghadapi tantangan signifikan dalam hal pengelolaan sumber daya manusia.

Salah satu indikator yang menunjukkan adanya masalah dalam manajemen SDM adalah tingginya tingkat attrition rate atau rasio jumlah karyawan yang keluar. Dalam beberapa periode terakhir, attrition rate perusahaan mencapai lebih dari 10%, yang berpotensi menurunkan produktivitas, meningkatkan biaya rekrutmen dan pelatihan, serta mengganggu kestabilan organisasi.

Untuk mengatasi permasalahan ini, departemen HR berinisiatif untuk mengadopsi pendekatan berbasis data (data-driven) guna mengidentifikasi faktor-faktor penyebab utama dari tingginya attrition rate dan menemukan solusi preventif yang tepat.

## ❓ Permasalahan Bisnis
Berikut adalah beberapa permasalahan bisnis utama yang ingin diselesaikan:

1. Apa saja faktor yang paling memengaruhi keputusan karyawan untuk keluar dari perusahaan?

2. Karakteristik seperti apa yang dimiliki karyawan yang cenderung keluar?

3. Bagaimana memanfaatkan data historis karyawan untuk memprediksi kemungkinan attrition di masa mendatang?

4. Apakah ada pola atau tren tertentu (misalnya berdasarkan departemen, level jabatan, atau jarak tempat tinggal) yang terkait dengan tingginya attrition rate?


## 🎯 Cakupan Proyek

- Melakukan eksplorasi data terhadap informasi karyawan (demografi, kompensasi, jabatan, performa, dll.)

- Mengidentifikasi faktor-faktor signifikan yang berhubungan dengan attrition menggunakan analisis statistik dan visualisasi.

- Membangun model prediksi machine learning untuk mengklasifikasikan kemungkinan karyawan keluar (attrition).

- Memberikan rekomendasi berbasis data kepada tim HR untuk strategi retensi karyawan.


## 📦 Persiapan
### Sumber Data

Dataset: [Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Format data : CSV

Ukuran: 1.470 entri dan 35 fitur

### Setup Environment:
- Bahasa: Python

- Tools: [Google Colab](https://colab.research.google.com)

- Setup conda environment:
```
  conda create --name proyek-human-resources python==3.9.15
```

- Install requirements:
  
```
pip install -r requirements.txt
```
- Install Library : 

```
!pip install pandas matplotlib seaborn scikit-learn
```

## Menjalankan file predict.py
  1. Buka Google Colab
  2. Jalankan code ```pip install -r requirements.txt ```
  3. Buka file predict.py
  4. Pastikan model ```attrition_model.pkl```
  5. Jalankan file predict.py
  6. Tunggu hasil output
  7. Selesai

## Business Dashboard

Link: [Dashboard Tableau](https://public.tableau.com/views/HRAnalyticDashboard_17449921513130/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

![alt text](https://github.com/mfatarsyah/HR-Dashboard/blob/main/fatarsyah_26%20-%20Dashboard.png)

Dashboard ini dirancang untuk memberikan gambaran menyeluruh mengenai tingkat attrition atau keluar-masuk karyawan di perusahaan. Dengan total 1.470 karyawan, tercatat 179 orang mengalami attrition, menghasilkan attrition rate sebesar 12,18%. Ini merupakan indikator penting bagi tim Human Resource dalam mengevaluasi strategi retensi.

Melalui segmentasi usia, terlihat bahwa kelompok usia produktif antara 30 hingga 36 tahun memiliki jumlah karyawan tertinggi sekaligus menyumbang angka attrition yang signifikan. Hal ini mengindikasikan perlunya pendekatan retensi yang lebih adaptif pada kelompok usia tersebut.

Faktor lembur (overtime) juga terbukti berdampak besar terhadap attrition. Sebanyak 98 karyawan yang keluar tercatat rutin melakukan lembur, lebih tinggi dibandingkan dengan yang tidak lembur. Ini menguatkan asumsi bahwa beban kerja yang tinggi dapat mendorong niat resign karyawan.

Analisis berdasarkan Job Role dan Job Satisfaction mengungkap bahwa meskipun mayoritas karyawan berada pada level kepuasan kerja yang cukup tinggi (tingkat 3 dan 4), posisi seperti Sales Executive dan Research Scientist tetap menunjukkan volume attrition yang besar. Maka, peningkatan kepuasan kerja saja tidak cukup tanpa keseimbangan beban kerja dan peluang karier yang jelas.

Pada sisi lain, rata-rata lama bekerja (Years at Company) juga memperlihatkan perbedaan signifikan antar posisi. Misalnya, Research Scientist cenderung bertahan lebih lama dibanding posisi seperti Human Resources atau Sales Representative. Ini bisa dijadikan dasar dalam menyusun kebijakan promosi dan loyalitas karyawan.

Terakhir, visualisasi attrition berdasarkan departemen menunjukkan bahwa departemen Sales menjadi kontributor terbesar terhadap angka attrition, yang perlu mendapat perhatian khusus dari sisi manajerial maupun strategi HR.

Dashboard ini juga dilengkapi fitur filter berdasarkan Education Field, yang memungkinkan analisis lebih spesifik terhadap latar belakang pendidikan karyawan. Dengan filter ini, perusahaan dapat mengevaluasi apakah latar belakang pendidikan tertentu memiliki korelasi terhadap kecenderungan keluar dari perusahaan.

Secara keseluruhan, dashboard ini menjadi alat bantu strategis bagi manajemen dan HR dalam memahami faktor-faktor utama yang memengaruhi attrition, serta mendukung pengambilan keputusan berbasis data untuk meningkatkan retensi dan efisiensi organisasi.

## ✅ Conclusion
Berdasarkan analisis data historis karyawan di perusahaan Jaya Jaya Maju, ditemukan beberapa faktor utama yang berkontribusi terhadap tingginya tingkat attrition (keluarnya karyawan):

1. Jam kerja lembur (OverTime) adalah faktor paling signifikan yang memengaruhi keputusan karyawan untuk keluar. Karyawan yang sering lembur menunjukkan kemungkinan lebih tinggi untuk resign.

2. Jarak tempat tinggal (DistanceFromHome) juga menunjukkan hubungan positif terhadap attrition. Semakin jauh jarak rumah ke kantor, semakin besar kemungkinan karyawan untuk keluar.

3. Masa kerja (YearsAtCompany) memperlihatkan bahwa karyawan baru atau dengan masa kerja pendek lebih rentan terhadap attrition.

4. Terdapat perbedaan attrition berdasarkan departemen, yang mengindikasikan bahwa beban kerja atau kepuasan kerja bisa berbeda-beda antar divisi.

5. Model machine learning yang telah dibangun menunjukkan bahwa data historis karyawan dapat dimanfaatkan untuk memprediksi kemungkinan attrition secara cukup akurat, yang bisa menjadi dasar strategi retensi karyawan ke depan.

## 💡 Rekomendasi Action Items
1. **Tinjau dan atur ulang sistem kerja lembur.**

   Karyawan yang sering lembur memiliki risiko tinggi untuk keluar. Pertimbangkan memberikan kompensasi yang sesuai, mengatur beban kerja, atau menerapkan kebijakan batas lembur.

2. **Buat program onboarding dan mentorship untuk karyawan baru.**

   Karena karyawan dengan masa kerja singkat lebih sering keluar, penting untuk memberikan dukungan pada fase awal masa kerja mereka.

3. **Evaluasi ulang fleksibilitas lokasi kerja.**

    Bagi karyawan dengan jarak tempat tinggal jauh, perusahaan bisa mempertimbangkan opsi kerja hybrid atau fleksibel agar meningkatkan kenyamanan dan produktivitas.

4. **Perkuat manajemen SDM di departemen dengan attrition tinggi.**

    Lakukan survei internal untuk memahami kepuasan kerja antar divisi, terutama pada departemen dengan tingkat attrition yang tinggi.

5. **Manfaatkan sistem prediktif untuk mengidentifikasi karyawan berisiko tinggi.**

    Gunakan model prediktif secara reguler untuk mendeteksi karyawan dengan potensi resign tinggi dan ambil tindakan preventif lebih dini.
