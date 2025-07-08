# ⚖️ Sistem Manajemen Kriminal (Crime Management System)

![Logo Polisi](./images/police_logo.jpg)

Aplikasi desktop yang dirancang untuk membantu aparat kepolisian dalam mengelola dan melacak data kriminal secara efisien.

---

## 🚀 Fitur

- **Login & Registrasi Pengguna:** Sistem otentikasi untuk memastikan hanya pengguna terotorisasi yang dapat mengakses data.
- **CRUD (Create, Read, Update, Delete):** Manajemen data kriminal secara lengkap, mulai dari penambahan data baru, melihat detail, memperbarui, hingga menghapus data.
- **Pencarian Cerdas:** Fitur pencarian untuk menemukan data kriminal dengan cepat berdasarkan berbagai kriteria seperti ID Kasus, No. Kriminal, atau Nama.
- **Tampilan Detail:** Menampilkan informasi lengkap seorang kriminal dalam jendela terpisah saat data di tabel di-klik dua kali.
- **Antarmuka Grafis (GUI):** Dibangun menggunakan Tkinter untuk kemudahan penggunaan.

---

## 💻 Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python
- **Library GUI:** Tkinter
- **Database:** MySQL
- **Konektor Database:** `mysql-connector-python`
- **Manipulasi Gambar:** Pillow (`PIL`)

---

## 📋 Syarat & Instalasi

Pastikan Anda telah memenuhi persyaratan berikut sebelum menjalankan aplikasi:

1.  **Python 3.x** terinstal di sistem Anda.
2.  **Server MySQL** aktif (bisa menggunakan XAMPP, Laragon, atau sejenisnya).

### Langkah-langkah Instalasi:

1.  **Clone repositori ini (jika ada) atau unduh file-filenya.**

2.  **Install dependensi yang dibutuhkan:**
    ```sh
    pip install mysql-connector-python pillow
    ```

3.  **Setup Database:**
    - Buat database baru di MySQL dengan nama `crime_management_db`.
    - Jalankan skrip SQL berikut untuk membuat tabel `criminal` dan `users`:
      ```sql
      CREATE TABLE criminal (
          Case_id VARCHAR(45) NOT NULL PRIMARY KEY,
          Criminal_no VARCHAR(45),
          Criminal_name VARCHAR(45),
          Nick_name VARCHAR(45),
          arrest_date VARCHAR(45),
          dateOfcrime VARCHAR(45),
          address VARCHAR(45),
          age VARCHAR(45),
          occupation VARCHAR(45),
          BirthMark VARCHAR(45),
          crimeType VARCHAR(45),
          fatherName VARCHAR(45),
          gender VARCHAR(45),
          wanted VARCHAR(45)
      );

      CREATE TABLE users (
          id INT AUTO_INCREMENT PRIMARY KEY,
          username VARCHAR(255) UNIQUE NOT NULL,
          password VARCHAR(255) NOT NULL
      );
      ```

4.  **Jalankan Aplikasi:**
    ```sh
    python criminal.py
    ```
    Aplikasi akan dimulai dengan jendela login. Silakan registrasi terlebih dahulu jika belum memiliki akun.

---

```

> criminal table will be like this

- criminal table

| Column Name   | Data Type   | Constraints           | Description                     |
| ------------- | ----------- | --------------------- | ------------------------------- |
| Case_id       | VARCHAR(45) | NOT NULL, PRIMARY KEY | Unique identifier for each case |
| Criminal_no   | VARCHAR(45) | NULL                  | Criminal number                 |
| Criminal_name | VARCHAR(45) | NULL                  | Name of the criminal            |
| Nick_name     | VARCHAR(45) | NULL                  | Nickname of the criminal        |
| arrest_date   | VARCHAR(45) | NULL                  | Date the criminal was arrested  |
| dateOfcrime   | VARCHAR(45) | NULL                  | Date of the crime               |
| address       | VARCHAR(45) | NULL                  | Address of the criminal         |
| age           | VARCHAR(45) | NULL                  | Age of the criminal             |
| occupation    | VARCHAR(45) | NULL                  | Occupation of the criminal      |
| BirthMark     | VARCHAR(45) | NULL                  | Birthmark of the criminal       |
| crimeType     | VARCHAR(45) | NULL                  | Type of crime committed         |
| fatherName    | VARCHAR(45) | NULL                  | Name of the criminal's father   |
| gender        | VARCHAR(45) | NULL                  | Gender of the criminal          |
| wanted        | VARCHAR(45) | NULL                  | Whether the criminal is wanted  |

- users Table

| Column Name | Data Type    | Constraints                 | Description                      |
| ----------- | ------------ | --------------------------- | -------------------------------- |
| id          | INT          | AUTO_INCREMENT, PRIMARY KEY | Unique identifier for each Users |
| username    | VARCHAR(255) | NOT NULL, UNIQUE            | Username for the user            |
| password    | VARCHAR(255) | NOT NULL                    | Password for the user            |

```

---

## 🔮 Potensi Pengembangan

- **Manajemen Peran Pengguna:** Menambahkan level akses yang berbeda (misalnya: Admin, Petugas Lapangan).
- **Fitur Pelaporan:** Membuat laporan statistik kriminal dalam format PDF atau Excel.
- **Pencarian Lanjutan:** Mengimplementasikan filter pencarian yang lebih kompleks (berdasarkan rentang tanggal, jenis kejahatan, dll.).
- **Integrasi Foto:** Memungkinkan unggah dan tampilkan foto kriminal langsung di aplikasi.
- **Peningkatan UI/UX:** Memodernisasi tampilan antarmuka agar lebih intuitif.