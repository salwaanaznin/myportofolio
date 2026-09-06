Tutorial 0 
Nama : Salwa Alyani Naznin
NPM : 2506622802
Kelas : PBP A

### Tugas 1

1. Penggunaan Elemen Semantik HTML5:
   saya menggunakan elemen semantik HTML5 seperti <section>, <article>, dan <header>. Elemen-elemen ini sangat membantu dalam menyusun struktur web agar lebih terorganisir. Selain itu, penggunaannya dapat mempermudah penerapan styling CSS yang spesifik tanpa perlu bergantung sepenuhnya pada elemen <div>.

2. Tantangan Responsivitas CSS & Evaluasi Tata Letak:
   Tantangan utama saat mengatur responsivitas adalah menyesuaikan elemen berformat baris (horizontal layout/grid) pada layar desktop agar tidak bertumpukan dan tetap bagus dilihat saat dibuka di layar mobile yang sempit. Saya menggunakan prioritas visual dengan mengarahkan orientasi dari samping-ke-samping menjadi tumpukan vertical dan menyesuaikan ukuran font dan padding. Selain itu, saya juga menggunakan Media Query @media (max-width: 768px) pada CSS digunakan untuk menyesuaikan tata letak komponen tetap stabil saat dibuka melalui perangkat mobile.

3. Batasan Static Web & Fungsionalitas Dinamis yang Ingin Ditambahkan:
   Batasan utama dari static web murni adalah seluruh konten bersifat statis/hardcoded sehingga untuk memperbarui data berarti saya harus mengubah kode HTML secara manual. Selain itu, web juga belum bisa menerima input interaktif pengguna. Fungsionalitas dinamis yang paling ingin saya tambahkan adalah integrasi basis data (MVT Django) untuk mengelola data portofolio secara terpusat, fitur formulir kontak yang dapat langsung mengirim pesan dan juga admin dashboard untuk memperbarui konten tanpa mengedit kode HTML.


***Log Prompting Penggunaan AI**
Saya menggunakan Gemini AI sebagai tools pembantu untuk beberapa bagian spesifik berikut terkait pengerjaan Tugas 1.
### 1. Design tampilan web di mobile
*Prompt:*
- ini design css web aku untuk bagian education, kenapa pas dibuka di hp dia jadi gak stabil sih layout nya di education section
*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Log%20AI%20Tugas%201/chat-no1.jpeg) (arahkan kursor ke link)
- Gunakan Media Query (@media) untuk memisahkan aturan tata letak desktop dan mobile.
- Ubah Arah Flexbox menjadi Vertikal pada Mobile: Mengubah flex-direction: row menjadi column pada layar kecil agar elemen tahun berada di bawah nama instansi secara alami.


### 2. Pembuatan elemen pills pada Section skills
*Prompt:* 
- aku pengen nambahin section skill dan pake elemen kayak buletan kecil/pills gitu dan dituliskan skillsnya, 
bantuin dan arahkan cara bikin elemennya aja dong

*Hasil dari AI:*
**Notes: Kode ai hanya berupa contoh implementasi untuk design tersebut, yang saya gunakan di kode tugas saya sudah dimodifikasi sedikit untuk menyesuaikan isi teks dari "skills" dan sedikit penyesuaian lainnya.**
Screenshoot chat bisa diakses ![disini](Log%20AI%20Tugas%201/chat-no2.png) (arahkan kursor ke link)
- Gunakan tag <section> sebagai wadah utama dan daftar <span> di dalam pembungkus Flexbox (.skills-container):
- Gunakan properti flex-wrap: wrap agar jika daftar keahlian cukup banyak, elemen pill otomatis berpindah ke baris baru tanpa memicu horizontal scrollbar.


### 3. Merancang pembuatan section timeline di experience berbentuk dots
*Prompt:*
- gmn styling css aku pengen bikin experience tp model design nya aku pengen bentuk dots dan tiap experience dihubungkan oleh garis dan dots tsb gimana arahin aja

*Hasil dari AI:*  
**Notes: Hasil ai hanya berupa contoh implementasi kode untuk design tersebut, yang saya gunakan di kode tugas saya sudah dimodifikasi sedikit untuk menyesuaikan isi dari html dan sedikit penyesuaian lainnya.**
Screenshoot chat bisa diakses ![disini](Log%20AI%20Tugas%201/chat-no3.jpeg) (arahkan kursor ke link)
- menggunakan position: relative pada container utama dan position: absolute untuk menggambar garis serta titiknya secara tepat.
- Membedakan warna .timeline-dot pada peran aktif (#d95d39) dan peran lampau (#f4a28c) memberikan scannability yang baik bagi perekrut/pengunjung untuk langsung mengenali posisi kamu saat ini secara cepat.