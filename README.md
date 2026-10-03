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
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%201/chat-no1.jpeg) (arahkan kursor ke link)
- Gunakan Media Query (@media) untuk memisahkan aturan tata letak desktop dan mobile.
- Ubah Arah Flexbox menjadi Vertikal pada Mobile: Mengubah flex-direction: row menjadi column pada layar kecil agar elemen tahun berada di bawah nama instansi secara alami.


### 2. Pembuatan elemen pills pada Section skills
*Prompt:*
- aku pengen nambahin section skill dan pake elemen kayak buletan kecil/pills gitu dan dituliskan skillsnya,
bantuin dan arahkan cara bikin elemennya aja dong

*Hasil dari AI:*
**Notes: Kode ai hanya berupa contoh implementasi untuk design tersebut, yang saya gunakan di kode tugas saya sudah dimodifikasi sedikit untuk menyesuaikan isi teks dari "skills" dan sedikit penyesuaian lainnya. (warna, ukuran)**
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%201/chat-no2.PNG) (arahkan kursor ke link)
- Gunakan tag <section> sebagai wadah utama dan daftar <span> di dalam pembungkus Flexbox (.skills-container):
- Gunakan properti flex-wrap: wrap agar jika daftar keahlian cukup banyak, elemen pill otomatis berpindah ke baris baru tanpa memicu horizontal scrollbar.


### 3. Merancang pembuatan section timeline di experience berbentuk dots
*Prompt:*
- gmn styling css aku pengen bikin experience tp model design nya aku pengen bentuk dots dan tiap experience dihubungkan oleh garis dan dots tsb gimana arahin aja

*Hasil dari AI:*
**Notes: Hasil ai hanya berupa contoh implementasi kode untuk design tersebut, yang saya gunakan di kode tugas saya sudah dimodifikasi sedikit untuk menyesuaikan isi dari html dan sedikit penyesuaian lainnya.**
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%201/chat-no3.jpeg) (arahkan kursor ke link)
- menggunakan position: relative pada container utama dan position: absolute untuk menggambar garis serta titiknya secara tepat.
- Membedakan warna .timeline-dot pada peran aktif (#d95d39) dan peran lampau (#f4a28c) memberikan scannability yang baik bagi perekrut/pengunjung untuk langsung mengenali posisi kamu saat ini secara cepat.



### Tugas 2

*1. Alur Permintaan di Django*
- Browser mengirimkan permintaan HTTP ke server Django.
- Permintaan pertama kali diterima oleh urls.py tingkat proyek (myportofolio/urls.py), yang bertugas mencocokkan pola URL utama dan mengarahkan (routing) ke urls.py aplikasi (main/urls.py).
- Berkas urls.py di dalam aplikasi main mencocokkan sisa pola URL dan menentukan fungsi view spesifik yang akan dipanggil.
- Fungsi atau kelas view menerima permintaan tersebut. View bertindak sebagai otak pengolah data dan berinteraksi dengan Model untuk mengambil atau memanipulasi data
- Model merepresentasi struktur tabel database. Model mengambil data yang diminta oleh view dari database.
- Setelah data didapatkan oleh view, data tersebut dikemas ke dalam sebuah context dan dikirim ke Template. Template bertugas merender data tersebut menjadi tampilan visual yang rapi.
- Django mengirimkan hasil HTML akhir kembali ke browser pengguna untuk ditampilkan.

*2. Alasan Data Disimpan pada Model, Bukan Ditulis Langsung di Template*
Data portofolio yang dibuat sebaiknya disimpan dalam model karena alasan kemudahan pemeliharaan. Jika data ditulis langsung di template, setiap kali ada penambahan riwayat kerja atau pendidikan baru, kita harus membuka dan mengubah kode HTML secara manual. Dengan model, data dapat dikelola secara dinamis melalui halaman Django Admin tanpa menyentuh kode program sama sekali.

*3. Perbedaan makemigrations dan migrate*I
- **Makemigrations** berfungsi untuk mencatat atau membuat draf file migrasi baru berdasarkan perubahan apa saja yang kamu lakukan pada file models.py. Perintah ini sebenernya belum menyentuh atau mengubah struktur database langsung.
- **Migrate** berfungsi untuk mengeksekusi file migrasi yang telah dibuat sebelumnya ke dalam database fisik sehingga tabel di database benar-benar terbentuk atau diperbarui sesuai model.


***Log Prompting Penggunaan AI**
Saya menggunakan Gemini AI sebagai tools pembantu untuk beberapa bagian spesifik berikut terkait pengerjaan Tugas 2.
### 1. Diskusi pembuatan main models untuk section Education
*Prompt:*
- buat nambahin main models di views ini buat education harus bikin file baru apa bs lanjut dr sini??
*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%202/no-1.jpeg) (arahkan kursor ke link)
- Bisa langsung dilanjutkan di file main/views.py yang sama tanpa perlu membuat file baru
- Tinggal import model Education dan tambahkan fungsi view baru untuk menangani halaman education


### 2. Memperbaiki kode HTML untuk education
*Prompt:*
- eh tolong highlight mana aja yg hrs diubah untuk mencapai itu dr kode education yg aku kasih

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%202/no-2.jpeg) (arahkan kursor ke link)


### 3. CSS bermasalah dan konsistensi ukuran logo/gambar yang diletakkan di section education
*Prompt:*
- ini gak kena design css ya.. terus ini size logo nya beda beda antara high school sama univ

*Hasil dari AI:*
**Notes: Hasil ai hanya berupa contoh implementasi kode untuk design tersebut, yang saya gunakan di kode tugas saya sudah dimodifikasi sedikit untuk menyesuaikan isi dari html dan sedikit penyesuaian lainnya.**
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%202/no-3.jpeg) (arahkan kursor ke link)
- Ternyata CSS belum terhubung dengan template HTML yang saya buat
- Perombakan width, height, object

### Tugas 3

*1. Mengapa menggunakan ModelForm dan menambahkan csrf_token?*
ModelForm digunakan untuk membuat form berdasarkan model Django yang sudah ada. Dengan ModelForm, saya tidak perlu mendefinisikan ulang seluruh field dan aturan validasinya secara manual.
Pada proyek ini, saya membuat EducationForm dengan field title, description, major, degree, dan thumbnail dan digunakan untuk menambahkan dan mengedit data pendidikan. Ketika sedang mengedit, saya menggunakan instance=education agar perubahan disimpan ke objek yang sudah ada. ModelForm tetap membutuhkan template HTML untuk mengatur tampilannya. Manfaat utamanya adalah membantu pembentukan field, validasi, dan penyimpanan data melalui is_valid() dan save(). Tag {% csrf_token %} ditambahkan pada form POST sebagai bagian dari perlindungan terhadap Cross-Site Request Forgery (CSRF). Serangan ini dapat membuat browser pengguna mengirim permintaan perubahan data dari situs lain tanpa kehendak pengguna. Django memeriksa token yang dikirim bersama form melalui middleware CSRF.

*2. Mengapa JSON lebih disukai dibandingkan XML dalam pengembangan web modern?*
JSON banyak digunakan karena strukturnya ringkas dan sesuai dengan bentuk data yang umum dipakai aplikasi, seperti objek, array, string, dan angka. Dibandingkan XML yang memakai tag pembuka dan penutup, JSON biasanya membutuhkan lebih sedikit teks untuk merepresentasikan data sederhana yang sama. Pada proyek portofolio ini, JSON cocok untuk menyajikan daftar Education dan Project beserta atributnya. Namun, JSON tidak selalu lebih baik untuk semua kebutuhan. XML tetap berguna untuk data dokumen yang memerlukan atribut, namespace, atau struktur markup yang lebih kompleks.

*3. Bagaimana alur pengembalian data portofolio dalam JSON dan mengapa serialization diperlukan?*
- Ketika pengguna mengakses /api/education/, Django mencocokkan URL tersebut melalui konfigurasi URL proyek dan aplikasi. Rute tersebut kemudian menjalankan view get_education_json.
- View mengambil data menggunakan Education.objects.all(), lalu mengubahnya menjadi JSON dengan serializers.serialize("json", education). Hasilnya dikembalikan melalui HttpResponse
- Serialization diperlukan karena hasil query Django berupa QuerySet yang berisi objek model Python, bukan data JSON yang bisa langsung dibaca oleh aplikasi lain. Serializer mengubah objek tersebut menjadi representasi JSON yang memuat identitas model, primary key, dan nilai field. Serializer juga menangani tipe seperti UUID
- Untuk halaman /education/, view show_education memanggil get_education_json secara langsung, membaca isi responsnya, lalu menjalankan serializers.deserialize. Objek hasil deserialisasi diambil melalui atribut .object dan dimasukkan ke context sebagai education_list. Template kemudian menampilkan daftar tersebut menggunakan perulangan Django Template Language.
- Alur JSON dan deserialisasi ini saya gunakan untuk memenuhi ketentuan tugas. Pemanggilan fungsi view tersebut berlangsung di server, tanpa mengirim permintaan HTTP tambahan ke endpoint sendiri.


***Screenshoot Prompting Penggunaan AI**
Saya menggunakan ChatGpt OpenAI sebagai tools pembantu untuk beberapa bagian spesifik berikut terkait pengerjaan Tugas 3.
### 1. Memeriksa bagian yang salah di bagian menambahkan ModelForm baru.
*Prompt:*
- aku mau nambahin education sebagai ModelForms baru, ini knp ya kok masih salah
*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%203/No_1.jpeg) (arahkan kursor ke link)
- AI tidak menemukan kesalahan logika yang pasti dari potongan kode tersebut, tetapi menunjukkan kemungkinan masalah indentasi


### 2. Memperbaiki EducationForm
*Prompt:*
- form buat education ini aku adaptasi dari ProjectForm. coba cek in apakah masih ada judul, action, atau link yang salah mengarah ke file project

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%203/No_2.jpeg) (arahkan kursor ke link)
- Ada satu bagian yang perlu disesuaikan: class pada section masih project-section.


### 3. Unit Test
*Prompt:*
- aku kan ada tambahan fitur ya di modelsform juga, jadinya test nya ada yg gagal gitu, coba kurang apa ya ini

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%203/No_3.jpeg) (arahkan kursor ke link)
- data pendidikan tetap tampil tanpa keterangan periode, sesuai perubahan kode saya yang mana tidak mencantumkan started at dan ended at sebagai timestamp


***Screenshoot Prompting Penggunaan AI**
Saya menggunakan ChatGpt sebagai tools pembantu untuk beberapa bagian spesifik berikut terkait pengerjaan Tugas 4.
### 1. Sembunyikan tombol create/edit/delete berdasarkan berbagai macam role 
*Prompt:*
- aku mau hide tombol create/edit/delete berdasarkan role gimana yaa? harusnya edit education_star.html kan
*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%204/no-1.jpeg) (arahkan kursor ke link)
AI menjelaskan bahwa penyembunyian tombol Create, Edit, dan Delete seharusnya dilakukan di education.html, bukan education_star.html. AI juga memberikan kondisi template berdasarkan role.AI juga mengingatkan bahwa variabel is_editor perlu dikirim dari show_education() melalui context. 

*Tindak lanjut saya:*
Saya mengikuti saran tersebut dengan menambahkan kondisi {% if %} pada education.html dan menambahkan status is_editor ke context di show_education(). Saya juga tetap mempertahankan pengecekan authorization di sisi server menggunakan @login_required dan PermissionDenied


### 2. Pesan Error 404 atau 403 saat bagian authorization 
*Prompt:*
- aku lagi mengetes authorization akses edit buat user reguler tp dapet 404, padahal seharusnya 403? kenapa yaa apakah kode aku ada yg salah di url nya 

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%204/no-2.jpeg) (arahkan kursor ke link)
AI menyarankan menggunakan UUID Education yang valid untuk menguji authorization. Setelah memeriksa urutan pemeriksaan pada kode, saya memahami bahwa respons juga bergantung pada tahap penolakan request. UUID dengan format tidak valid menghasilkan 404 karena tidak cocok dengan route. Pada update_education(), pengguna biasa menerima 403 sebelum pencarian objek dilakukan. Sementara itu, pengguna yang memiliki izin menerima 404 apabila UUID valid secara format tetapi objek tidak ditemukan.

*Tindak lanjut saya:*
Saya mengambil UUID Education yang valid dari endpoint /api/education/ lalu menguji kembali URL edit menggunakan akun regular user. Setelah menggunakan UUID yang benar, server mengembalikan 403 Forbidden sesuai requirement. Karena itu, masalahnya ternyata berasal dari URL pengujian yang salah.


### 3.Evaluasi Implementasi is_editor()
*Prompt:*
- aku sudah punya fungsi is_editor(user). mending dipanggil dari view atau query group langsung di show_education? jelasin penggunannya

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%204/no-3.jpeg) (arahkan kursor ke link)
AI menyarankan untuk memakai helper is_editor(user) secara konsisten daripada menulis query Group secara langsung di beberapa tempat. Helper tersebut dapat dipakai baik di show_education() untuk mengirim status Editor ke template maupun di update_education() untuk pengecekan authorization. Menurut AI, pendekatan ini mengurangi duplikasi kode dan membuat logika role lebih mudah dirawat.

*Tindak lanjut saya:*
Saya menggunakan helper is_editor(user) pada show_education() untuk mengirim status Editor ke template dan pada update_education() untuk pemeriksaan authorization. Helper juga memeriksa is_authenticated. Dengan demikian, logika keanggotaan Group Editor tidak perlu ditulis ulang pada kedua view tersebut.



## Tugas 5

### 1. Apa itu debouncing dan mengapa penting pada pencarian AJAX?
Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan suatu aksi selama beberapa waktu tertentu.

Pada fitur pencarian AJAX, debouncing penting karena tanpa teknik ini setiap karakter yang diketik pengguna dapat langsung mengirim request baru ke server. Hal tersebut dapat menyebabkan terlalu banyak request dalam waktu singkat.

Pada implementasi saya, pencarian Education menggunakan delay 300 ms. Request baru dikirim setelah pengguna berhenti mengetik selama 300 ms. Dengan cara ini, pencarian menjadi lebih efisien dan server tidak menerima request yang sebenarnya belum diperlukan.

### 2. Apa fungsi `await` ketika menggunakan `fetch()`? Apa yang terjadi jika tidak menggunakan `await`?
- `fetch()` merupakan operasi asynchronous yang mengembalikan sebuah `Promise`.
- Keyword `await` digunakan agar JavaScript menunggu sampai Promise tersebut selesai sebelum melanjutkan ke proses berikutnya. 

### 3. Apa itu XSS dan mengapa data AJAX lebih rentan dibanding template Django?
Cross-Site Scripting atau XSS adalah serangan ketika input berbahaya berhasil dimasukkan ke halaman web dan kemudian dieksekusi sebagai kode JavaScript oleh browser.
Template Django secara default memiliki mekanisme auto-escaping terhadap data yang ditampilkan menggunakan template variable. Namun, pada implementasi AJAX, data dari server diterima dalam bentuk JSON dan kemudian dimasukkan ke halaman menggunakan JavaScript.

Pada kasus ini, saya menggunakan innerHTML untuk membentuk card Education. Karena data dimasukkan melalui JavaScript, perlindungan auto-escaping dari template Django tidak secara otomatis diterapkan.

Oleh karena itu, saya menggunakan fungsi escapeHtml() untuk mengubah karakter khusus seperti <, >, ", ', dan & menjadi HTML entity sebelum data dimasukkan ke innerHTML.
Selain perlindungan di sisi client, saya juga menggunakan strip_tags() pada EducationForm untuk membersihkan input dari tag HTML di sisi server.


***Screenshoot Prompting Penggunaan AI**
Saya menggunakan ChatGpt sebagai tools pembantu untuk beberapa bagian spesifik berikut terkait pengerjaan Tugas 5. 
### 1. Validasi Keamanan XSS 
*Prompt:*
- buat keamanan xss, aku udah pake escapehtml() terus kurang apalagi buat validasi

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%205/no-1.jpeg) (arahkan kursor ke link)
AI menjelaskan bahwa escapeHtml() di frontend berfungsi sebagai output encoding, yaitu mengubah karakter khusus seperti <, >, ", ', dan & menjadi bentuk HTML entity agar data yang dimasukkan melalui innerHTML tidak dieksekusi sebagai HTML atau JavaScript.
Namun, escapeHtml() saja belum cukup karena perlindungan hanya terjadi saat data ditampilkan. Oleh karena itu, backend tetap perlu melakukan sanitasi dan validasi input. Pada Django Form, strip_tags() dapat digunakan untuk menghapus tag HTML sebelum data disimpan, sedangkan ValidationError dapat digunakan jika setelah dibersihkan nilai menjadi kosong atau tidak valid.

*Tindak lanjut saya:*
Saya memeriksa kembali implementasi EducationForm dan memastikan bahwa field title, description, dan major dibersihkan menggunakan strip_tags().
Pada field title, saya juga menambahkan pengecekan agar input yang hanya berisi tag HTML ditolak menggunakan ValidationError. Di sisi frontend, saya tetap menggunakan escapeHtml() sebelum memasukkan data Education ke innerHTML.

### 2. Penggunaan await pada fetch() dan response.json()
*Prompt:*
- knp perlu await di fetch() dan response.json()? kalau misalkan salah satu dihapus aja gapapa kah

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%205/no-2.jpeg) (arahkan kursor ke link)
AI menjelaskan bahwa `fetch()` dan `response.json()` sama-sama menghasilkan `Promise`, tetapi keduanya menunggu proses yang berbeda.
`await fetch(url)` digunakan untuk menunggu response HTTP dari server sampai objek `Response` tersedia. Setelah itu, `await response.json()` digunakan untuk menunggu body response selesai dibaca dan dikonversi menjadi data JavaScript. Jika `await` pada `fetch()` dihapus, variabel `response` masih berupa Promise sehingga method seperti `response.json()` belum dapat digunakan secara langsung.

*Tindak lanjut saya:*
Setelah memahami penjelasan tersebut, saya memeriksa kembali fungsi AJAX pada halaman Education dan memastikan bahwa proses pengambilan data menggunakan:
***javascript
const response = await fetch(url);
const educationData = await response.json();***


### 3.Final check implementasi Tugas 5 terhadap seluruh requirement
*Prompt:*
- boleh final check in seluruh commit aku di git branch tugas-5 ini sebelum aku nulis readme gak, jadi kayak double check semua requirements minimal yg hrs diselesaiin di tugas 5 ini udh terpenuhi di kode yg tercommit blmnya

*Hasil dari AI:*
Screenshoot chat bisa diakses ![disini](Dokumentasi%20AI%20Tugas%205/no-3.jpeg) (arahkan kursor ke link)
AI membantu melakukan pemeriksaan akhir terhadap implementasi Tugas 5 dengan membandingkan kode yang sudah dibuat dengan requirement tugas.
Dari pengecekan tersebut, AI menemukan dua hal yang masih perlu diperbaiki. Pertama, fungsi get_education_json() sudah membaca parameter title_query, tetapi belum menggunakan parameter tersebut untuk memfilter data Education. Hal ini menyebabkan fitur pencarian AJAX belum benar-benar memfilter hasil dari backend.

*Tindak lanjut saya:*
Saya Menambahkan .filter(title__icontains=title_query), menghapus route duplikat, lalu menguji ulang AJAX search sampai hasil dapat tersaring tanpa reload.