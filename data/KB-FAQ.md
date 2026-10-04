# Fixora — FAQ (Pertanyaan yang Sering Ditanyakan)

---

## Tentang Platform

### Apa bedanya Fixora dengan LAPOR! atau Qlue?

Fixora berbeda dari platform pelaporan lain dalam tiga hal utama. Pertama, Fixora secara aktif mencari masalah infrastruktur dari berita media menggunakan AI, bukan hanya menunggu laporan warga. Kedua, Fixora melacak berapa lama masalah dibiarkan (durasi mangkrak), bukan sekadar mencatat satu laporan. Ketiga, Fixora menyediakan verifikasi berlapis menggunakan AI multi-agent untuk memastikan kredibilitas data.

### Apakah Fixora gratis?

Ya, Fixora sepenuhnya gratis dan open source. Siapa pun bisa menggunakan platform ini untuk melaporkan atau memantau kondisi infrastruktur publik tanpa biaya.

### Apakah saya harus membuat akun untuk melapor?

Tidak. Fixora tidak memerlukan registrasi atau login untuk membuat laporan. Pelaporan bersifat anonim. Email bersifat opsional — hanya untuk yang ingin mendapatkan notifikasi update status laporan di kemudian hari.

### Wilayah mana saja yang dicakup Fixora?

Saat ini Fixora difokuskan pada wilayah Jabodetabek (Jakarta, Bogor, Depok, Tangerang, Bekasi). Namun, laporan warga dari seluruh wilayah Indonesia tetap bisa diterima oleh sistem. Fitur AI News Crawler saat ini hanya mencari berita dari wilayah Jabodetabek.

### Apakah data di Fixora bisa dipercaya?

Fixora menerapkan beberapa mekanisme untuk menjaga kredibilitas data. Setiap laporan warga harus melewati verifikasi otomatis oleh 3 agent AI yang saling berdebat (advocate vs skeptic, dengan manager sebagai penengah). Foto wajib memiliki stempel tanggal/waktu untuk mencegah manipulasi foto lama. Laporan duplikat dideteksi otomatis dan digabungkan. Pengguna bisa mengkonfirmasi "masih begini" untuk menjaga data tetap terkini.

---

## Tentang Pelaporan

### Jenis masalah apa saja yang bisa dilaporkan?

Fixora saat ini menerima laporan untuk 4 kategori masalah infrastruktur publik:
1. Jalan Rusak — termasuk jalan berlubang, aspal rusak, trotoar amblas
2. Jembatan Rusak — termasuk retakan struktur, railing patah, jembatan miring
3. Sampah — termasuk sampah menumpuk, TPS liar, sampah di sungai
4. Bangunan Terbengkalai — termasuk proyek mangkrak, bangunan rawan roboh

### Apakah saya bisa melaporkan masalah selain 4 kategori di atas?

Saat ini Fixora hanya mendukung 4 kategori tersebut. Jika foto yang diunggah menunjukkan masalah di luar kategori yang didukung (misalnya drainase tersumbat, penerangan jalan mati, atau pohon tumbang), sistem akan menolak foto tersebut dengan keterangan "kategori tidak dikenali". Kami berencana menambah kategori di versi mendatang.

### Kenapa foto saya ditolak?

Foto bisa ditolak karena beberapa alasan:
- **Tidak ada stempel tanggal dan waktu** — gunakan aplikasi kamera timestamp yang menampilkan tanggal dan waktu langsung di foto.
- **Bukan kerusakan infrastruktur** — foto tidak menunjukkan masalah infrastruktur publik (misalnya foto makanan, selfie, atau pemandangan).
- **Kategori tidak dikenali** — masalah yang difoto tidak masuk dalam 4 kategori yang didukung.
- **Lokasi tidak terbaca** — tidak ada informasi lokasi yang bisa diidentifikasi dari foto.

### Berapa lama laporan saya diverifikasi?

Proses verifikasi otomatis biasanya memakan waktu beberapa menit hingga beberapa jam, tergantung antrian. Sistem verifikasi berjalan secara berkala (setiap 30 detik mengecek laporan yang perlu diverifikasi).

### Apakah laporan saya bisa ditolak setelah diverifikasi?

Ya. Jika agent AI penengah (manager) memutuskan bahwa bukti yang ada tidak cukup untuk memverifikasi laporan, laporan akan ditolak dengan alasan yang spesifik. Warga bisa mengambil foto yang lebih jelas dan melaporkan ulang.

### Apa yang terjadi jika ada laporan serupa dengan saya?

Fixora memiliki sistem deteksi duplikat otomatis yang membandingkan foto (menggunakan perceptual hash) dan lokasi (radius 100 meter) dari setiap laporan baru dengan laporan yang sudah ada. Jika terdeteksi sebagai duplikat, laporan akan digabung (merge) ke laporan induk, bukan dihapus. Hal ini memastikan semua data tetap tercatat dan menambah kekuatan bukti pada laporan induk.

---

## Tentang Data dan Privasi

### Apakah identitas pelapor ditampilkan secara publik?

Tidak. Identitas pelapor (email) tidak ditampilkan di mana pun secara publik. Hanya foto, lokasi, deskripsi, dan metadata laporan yang ditampilkan di peta publik. Email yang diisi saat pelaporan hanya digunakan untuk keperluan internal (notifikasi update status di kemudian hari, jika fitur ini sudah tersedia).

### Apakah lokasi saya dilacak?

Fixora tidak melacak lokasi pengguna secara terus-menerus. Koordinat lokasi hanya digunakan saat proses pelaporan untuk menentukan posisi masalah infrastruktur di peta. Lokasi ini berasal dari informasi yang tercetak di foto atau dari pin yang diletakkan pengguna secara manual di peta.

### Siapa yang bisa melihat laporan saya?

Setelah lolos verifikasi, laporan tayang di peta publik dan bisa dilihat oleh siapa saja yang mengakses Fixora. Laporan yang masih dalam status "menunggu verifikasi" atau yang ditolak tidak ditampilkan di peta publik.

---

## Tentang Peta dan Eksplorasi Data

### Bagaimana cara melihat masalah di sekitar saya?

Buka peta Fixora, lalu navigasi atau zoom ke area yang ingin Anda lihat. Setiap titik masalah ditampilkan sebagai marker yang bisa diklik untuk melihat detail. Anda bisa memfilter berdasarkan kategori, tingkat keparahan, status, atau sumber data.

### Apa arti badge "Laporan Warga" dan "Terdeteksi AI (Media)"?

Badge ini menunjukkan sumber data laporan. "Laporan Warga" berarti data berasal dari warga yang mengunggah foto langsung ke Fixora. "Terdeteksi AI (Media)" berarti data diekstrak secara otomatis oleh AI dari berita media online.

### Bagaimana cara mengetahui sudah berapa lama masalah dibiarkan?

Pada halaman detail setiap titik masalah, terdapat informasi "Tanggal Pertama Dilaporkan" dan "Tanggal Terakhir Dikonfirmasi". Selisih antara tanggal pertama dilaporkan hingga hari ini menunjukkan durasi mangkrak.

---

## Tentang Tindak Lanjut

### Apakah Fixora bisa memperbaiki infrastruktur yang rusak?

Tidak. Fixora adalah platform dokumentasi dan transparansi, bukan kontraktor perbaikan. Fixora menyediakan data yang terverifikasi dan terdokumentasi agar masyarakat, media, dan pemerintah bisa menggunakan data tersebut untuk mendorong tindakan nyata.

### Bagaimana saya bisa mendorong perbaikan setelah melaporkan di Fixora?

Selain melapor di Fixora, Anda juga bisa meneruskan laporan ke saluran resmi pemerintah seperti LAPOR! (https://lapor.go.id) atau CRM Jakarta (https://crm.jakarta.go.id) untuk DKI Jakarta. Data yang sudah terdokumentasi di Fixora (foto, lokasi, durasi mangkrak) bisa menjadi bukti pendukung yang kuat saat mengajukan laporan resmi. Anda juga bisa membagikan data Fixora ke media sosial atau media massa untuk meningkatkan visibilitas masalah.

### Apakah Fixora terhubung langsung dengan pemerintah?

Saat ini Fixora belum terhubung langsung dengan sistem pemerintah. Di masa depan, Fixora berencana menghubungkan data laporan dengan data anggaran resmi pemerintah (APBD) melalui fitur cross-reference, sehingga masyarakat bisa mengetahui apakah suatu titik kerusakan sudah dianggarkan untuk perbaikan atau belum.
