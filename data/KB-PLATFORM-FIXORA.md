# Fixora — Tentang Platform

## Apa Itu Fixora?

Fixora adalah platform open source untuk melacak akuntabilitas jangka panjang terhadap infrastruktur publik yang dibiarkan rusak di kota-kota besar Indonesia, khususnya wilayah Jabodetabek (Jakarta, Bogor, Depok, Tangerang, Bekasi). Fixora bukan sekadar tempat melapor seperti LAPOR! atau Qlue — Fixora secara aktif mencari masalah infrastruktur dari berita media menggunakan AI, melacak berapa lama masalah dibiarkan, dan menyediakan verifikasi berlapis agar data yang ditampilkan kredibel.

Fixora memiliki dua sumber data utama yang berjalan paralel:
1. **Laporan manual warga** — warga mengunggah foto kerusakan infrastruktur, AI otomatis menganalisis foto tersebut untuk menghasilkan draft laporan (kategori, tingkat keparahan, lokasi).
2. **Deteksi otomatis dari berita media (AI News Crawler)** — sistem secara berkala mengambil berita infrastruktur dari media online, mengekstrak informasi terstruktur, dan menampilkannya di peta.

Kedua jenis data ditampilkan di peta interaktif yang sama, dibedakan lewat badge sumber data: "Laporan Warga" untuk laporan manual, dan "Terdeteksi AI (Media)" untuk hasil crawling berita.

---

## Cara Melapor di Fixora

### Langkah 1: Upload Foto

Warga cukup mengunggah satu foto masalah infrastruktur yang diambil menggunakan aplikasi kamera timestamp (kamera yang menampilkan tanggal dan waktu di foto). Foto wajib menunjukkan kerusakan infrastruktur nyata dan memiliki stempel tanggal/waktu yang tercetak di gambar. Foto tanpa stempel timestamp akan ditolak oleh sistem.

### Langkah 2: AI Menganalisis Foto

Setelah foto diunggah, AI secara otomatis menganalisis foto dan menghasilkan draft laporan berisi:
- **Judul** laporan
- **Deskripsi** kerusakan
- **Kategori** masalah (Jalan Rusak, Jembatan Rusak, Sampah, atau Bangunan Terbengkalai)
- **Tingkat keparahan** (Ringan, Sedang, atau Parah)
- **Lokasi** yang terbaca dari foto

Jika foto tidak relevan (bukan kerusakan infrastruktur, tidak ada stempel timestamp, lokasi tidak terbaca, atau kategori tidak dikenali), sistem akan memberitahu alasan penolakan dan meminta foto yang lebih sesuai.

### Langkah 3: Review dan Koreksi Draft

Warga dapat mereview draft yang dihasilkan AI dan mengoreksi field yang kurang tepat — misalnya mengganti kategori, memperbarui deskripsi, atau menggeser pin lokasi di peta. AI memberikan draft awal, tapi keputusan akhir tetap di tangan pelapor.

### Langkah 4: Submit Laporan

Setelah data sudah sesuai, warga menekan tombol submit. Laporan akan masuk dengan status "Menunggu Verifikasi" dan diproses oleh sistem verifikasi otomatis di latar belakang. Warga tidak perlu membuat akun atau login — pelaporan bersifat anonim. Email bersifat opsional, hanya untuk yang ingin mendapat update status laporan di kemudian hari.

### Langkah 5: Verifikasi dan Penayangan

Laporan warga diverifikasi secara otomatis oleh sistem multi-agent AI (3 agent yang berdebat untuk memastikan laporan valid). Jika lolos verifikasi, laporan tayang di peta publik. Jika ditolak, alasan penolakan akan dicatat.

---

## Syarat Foto yang Diterima

Foto yang diunggah ke Fixora harus memenuhi semua syarat berikut:

1. **Wajib ada stempel tanggal dan waktu** yang tercetak langsung di gambar (overlay teks dari aplikasi kamera timestamp, CCTV, atau dashcam). Screenshot, foto dari galeri lama, atau foto tanpa stempel waktu akan ditolak.
2. **Menunjukkan kerusakan infrastruktur publik nyata** — bukan foto interior rumah pribadi, bukan foto orang, bukan foto pemandangan tanpa kerusakan.
3. **Masuk salah satu dari 4 kategori** yang didukung Fixora: Jalan Rusak, Jembatan Rusak, Sampah, atau Bangunan Terbengkalai.
4. **Lokasi harus terbaca** — ada teks lokasi atau koordinat yang tercetak di foto, atau lokasi bisa diidentifikasi dari konteks foto.

---

## Status Laporan

Setiap laporan di Fixora memiliki salah satu status berikut:

- **Menunggu Verifikasi (pending_verification)**: Laporan baru saja disubmit dan sedang dalam antrian verifikasi otomatis. Belum tayang di peta publik.
- **Terverifikasi (verified)**: Laporan telah lolos verifikasi dan tayang di peta publik. Data ini dianggap valid dan bisa dilihat semua pengguna.
- **Ditolak (rejected)**: Laporan tidak lolos verifikasi. Alasan penolakan tersedia di detail laporan. Laporan yang ditolak tidak ditampilkan di peta publik.

Laporan dari sumber AI News Crawler dan Data Pemerintah langsung berstatus "Terverifikasi" tanpa melalui proses verifikasi multi-agent, karena sumbernya sudah terpercaya (media resmi dan data pemerintah).

---

## Tingkat Keparahan (Severity)

Fixora mengklasifikasikan tingkat keparahan masalah infrastruktur menjadi tiga level:

- **Ringan**: Kerusakan minor yang belum membahayakan namun perlu perhatian. Contoh: lubang kecil di jalan, retakan ringan pada trotoar, sampah berserakan dalam jumlah kecil, cat mengelupas pada fasilitas umum.
- **Sedang**: Kerusakan yang sudah mengganggu kenyamanan dan berpotensi membahayakan jika tidak segera ditangani. Contoh: lubang jalan berdiameter sedang, tumpukan sampah yang mulai menggunung, retakan signifikan pada jembatan, saluran air tersumbat sebagian.
- **Parah**: Kerusakan berat yang membahayakan keselamatan publik dan membutuhkan penanganan segera. Contoh: jalan ambles atau berlubang besar, jembatan rawan roboh, bangunan runtuh sebagian, tumpukan sampah masif yang menimbulkan bau dan penyakit.

---

## Konfirmasi "Masih Begini"

Pengguna Fixora dapat mengkonfirmasi bahwa suatu titik masalah masih dalam kondisi rusak dengan menekan tombol "Masih Begini" pada halaman detail laporan. Fitur ini penting untuk:

1. Memperbarui data kapan terakhir kali masalah dikonfirmasi masih ada, sehingga durasi mangkrak terus terhitung akurat.
2. Meningkatkan kepercayaan (confidence score) terhadap data laporan.
3. Menunjukkan bahwa masyarakat masih memperhatikan dan peduli terhadap masalah tersebut.

Setiap pengguna hanya dapat mengkonfirmasi satu kali per 24 jam untuk mencegah spam.

---

## Durasi Mangkrak

Salah satu fitur utama Fixora adalah menampilkan berapa lama suatu masalah infrastruktur dibiarkan tanpa penanganan. Durasi dihitung dari tanggal pertama kali masalah dilaporkan atau terdeteksi (first_reported_at) hingga saat ini. Semakin lama durasi mangkrak, semakin tinggi urgensi penanganan.

---

## Proses Verifikasi Multi-Agent

Setiap laporan dari warga melewati proses verifikasi otomatis yang melibatkan 3 agent AI yang bekerja secara sekuensial:

1. **Advocate Agent**: Bertugas memberikan argumen mendukung validitas laporan. Agent ini mencari bukti dari foto, deskripsi, dan metadata yang menunjukkan bahwa laporan ini memang benar menunjukkan masalah infrastruktur nyata.

2. **Skeptic Agent**: Bertugas memberikan argumen yang mempertanyakan validitas laporan. Agent ini mencari kejanggalan, inkonsistensi, atau alasan mengapa laporan mungkin tidak valid.

3. **Manager Agent**: Bertugas sebagai penengah yang menimbang argumen kedua agent di atas dan membuat keputusan akhir apakah laporan diterima atau ditolak. Manager agent hanya dipanggil jika advocate dan skeptic tidak mencapai konsensus (keduanya tidak sepakat dengan tingkat kepercayaan tinggi).

Jika advocate dan skeptic setuju dengan tingkat kepercayaan di atas 80%, keputusan langsung diambil tanpa perlu manager agent.

---

## Sumber Data Laporan

Fixora menampilkan data dari tiga jenis sumber:

### 1. Laporan Warga (user_report)
Laporan yang disubmit langsung oleh warga melalui platform Fixora. Warga mengunggah foto kerusakan infrastruktur, AI menganalisis dan menghasilkan draft, lalu warga mereview dan submit. Laporan ini melewati proses verifikasi multi-agent sebelum tayang di peta.

### 2. Deteksi AI dari Media (ai_news)
Entry yang dihasilkan secara otomatis oleh AI News Crawler. Sistem secara berkala (setiap 2 jam) mencari berita infrastruktur dari Google News RSS, mengekstrak informasi terstruktur (judul, kategori, lokasi, tingkat keparahan), dan membuat entry laporan otomatis. Data dari media langsung berstatus terverifikasi karena sumbernya sudah terpercaya (media massa).

### 3. Data Pemerintah (gov_data)
Entry yang berasal dari sinkronisasi data open government (seperti SatuData Jakarta). Fitur ini masih dalam tahap perencanaan dan belum tersedia di versi saat ini.
