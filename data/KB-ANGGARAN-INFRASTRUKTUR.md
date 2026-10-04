# Fixora — Data Anggaran Infrastruktur (Placeholder)

> **Status: PLACEHOLDER.** File ini berisi struktur dan contoh template data anggaran infrastruktur pemerintah. Data aktual dari SatuData Jakarta atau sumber open data pemerintah lainnya belum dimasukkan. File ini berfungsi sebagai panduan format agar Python AI service mengetahui struktur data yang akan diisi nanti.

---

## Sumber Data Anggaran

### SatuData Jakarta (data.jakarta.go.id)
Portal open data resmi Pemerintah Provinsi DKI Jakarta. Dataset yang relevan untuk Fixora:
- Data kondisi jalan provinsi DKI Jakarta (persentase kondisi baik/sedang/rusak ringan/rusak berat per ruas).
- Realisasi anggaran Dinas Bina Marga DKI Jakarta per tahun.
- Data lelang proyek perbaikan infrastruktur melalui LPSE.
- Data kondisi jembatan dan JPO di DKI Jakarta.

### LKPJ (Laporan Keterangan Pertanggungjawaban)
Laporan tahunan kepala daerah kepada DPRD yang memuat realisasi program dan anggaran, termasuk sektor infrastruktur.

### E-budgeting / SIMRAL
Sistem informasi pengelolaan anggaran daerah yang mempublikasikan rencana dan realisasi anggaran per kegiatan.

---

## Struktur Data Anggaran (Template)

Berikut adalah format data yang direncanakan untuk disimpan dan di-index oleh RAG:

### Data Alokasi Anggaran Per Dinas

```
Tahun Anggaran: [2025/2026/...]
Provinsi/Kota: [DKI Jakarta / Kota Bekasi / ...]
Dinas: [Dinas Bina Marga / Dinas LH / Dinas PUPR / ...]
Program: [Pemeliharaan Jalan / Pembangunan Jembatan / ...]
Kegiatan: [Peningkatan Jalan ... / Rehabilitasi Jembatan ... / ...]
Pagu Anggaran: Rp [nominal]
Realisasi: Rp [nominal] ([persentase]%)
Lokasi: [nama jalan/kelurahan/kecamatan]
Status: [Selesai / Dalam Pelaksanaan / Belum Dimulai / Gagal Lelang]
Kontraktor: [nama perusahaan] (jika tersedia)
```

### Data Kondisi Infrastruktur Per Ruas

```
Tahun Survei: [2025/2026/...]
Provinsi/Kota: [DKI Jakarta / ...]
Jenis Infrastruktur: [Jalan / Jembatan / ...]
Nama Ruas / Lokasi: [Jl. Raya Kalimalang / Jembatan Kalibata / ...]
Panjang: [... km / ... meter]
Lebar: [... meter]
Kelas Jalan: [Nasional / Provinsi / Kota / Lingkungan]
Kondisi: [Baik / Sedang / Rusak Ringan / Rusak Berat]
Nilai Kondisi (IRI/PCI): [angka index, jika tersedia]
Tahun Terakhir Perbaikan: [tahun]
Catatan: [keterangan tambahan]
```

### Data Lelang Proyek (LPSE)

```
Nomor Paket: [...]
Nama Paket: [Rehabilitasi Jalan ...]
Pagu Anggaran: Rp [nominal]
HPS (Harga Perkiraan Sendiri): Rp [nominal]
Metode Pengadaan: [E-Tendering / Pengadaan Langsung / ...]
Tanggal Pengumuman: [tanggal]
Tanggal Penutupan: [tanggal]
Pemenang: [nama perusahaan]
Nilai Kontrak: Rp [nominal]
Lokasi Pekerjaan: [alamat/ruas]
Durasi Kontrak: [... hari kalender]
Status: [Pengumuman / Evaluasi / Kontrak / Pelaksanaan / Selesai]
```

---

## Contoh Data (Ilustratif — Bukan Data Asli)

> Data berikut hanya contoh format dan BUKAN data resmi. Data aktual harus diambil dari sumber resmi pemerintah.

### Contoh: Alokasi Anggaran Dinas Bina Marga DKI Jakarta 2025

| Program | Kegiatan | Pagu (Miliar Rp) | Realisasi | Lokasi |
|---------|----------|-------------------|-----------|--------|
| Pemeliharaan Jalan | Peningkatan Jl. Raya Bekasi (Cakung–Pulo Gadung) | 45,2 | 78% | Jakarta Timur |
| Pemeliharaan Jalan | Rehabilitasi Jl. Daan Mogot (Grogol–Cengkareng) | 38,7 | 92% | Jakarta Barat |
| Pemeliharaan Jembatan | Rehabilitasi Jembatan Kalibata | 12,5 | 100% | Jakarta Selatan |
| Drainase | Normalisasi Kali Ciliwung segmen Manggarai | 85,0 | 45% | Jakarta Pusat |

### Contoh: Kondisi Jalan Provinsi DKI Jakarta 2025

| Ruas Jalan | Panjang (km) | Kondisi | Tahun Terakhir Perbaikan |
|------------|-------------|---------|--------------------------|
| Jl. Jenderal Sudirman | 5,8 | Baik | 2024 |
| Jl. Raya Bekasi (Cakung) | 4,2 | Rusak Ringan | 2022 |
| Jl. Daan Mogot (segmen 3) | 3,1 | Rusak Berat | 2020 |
| Jl. Raya Bogor (Kramat Jati) | 6,5 | Sedang | 2023 |

---

## Catatan untuk Pipeline RAG

1. **Update berkala**: Data anggaran berubah setiap tahun (APBD). File ini harus di-update minimal setahun sekali setelah APBD disahkan (biasanya Desember–Januari).
2. **Chunking strategy**: Setiap blok data (per kegiatan / per ruas) sebaiknya di-chunk secara independen agar retrieval bisa spesifik per lokasi dan program.
3. **Metadata embedding**: Saat embedding, sertakan metadata tahun, lokasi (kecamatan/kota), dan jenis infrastruktur agar filtering hybrid (metadata + semantic) bisa dilakukan.
4. **Sumber data tambahan yang potensial**:
   - DJPK Kemenkeu (data transfer daerah/DAK): https://djpk.kemenkeu.go.id
   - LPSE Nasional (data lelang): https://lpse.lkpp.go.id
   - BPS (data kondisi infrastruktur survei): https://bps.go.id
   - Open Data Kota Bekasi, Depok, Tangerang (jika tersedia)
