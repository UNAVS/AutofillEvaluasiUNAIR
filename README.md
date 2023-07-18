
# Autofill Kuesioner Evaluasi UNAIR

Dalam dunia perkuliahan Universitas Airlangga (UNAIR), mahasiswa diharuskan untuk mengisi form evaluasi melalui Sistem Informasi Penjamin Mutu UNAIR (https://qa.unair.ac.id/qa/gate/login). Apabila belum mengisi form evaluasi ini, mahasiswa tidak dapat melihat hasil nilai akhir pada e-learning.
Mengisi kuesioner tersebut dapat menjadi suatu hal yang melelahkan dan memakan waktu. Untuk itulah autofill ini diciptakan. Apabila mahasiswa tidak memiliki keluhan terkait pengalaman semesternya, mahasiswa dapat menggunakan autofill ini untuk mengisi kuesioner secara otomatis. Autofill ini memanfaatkan library Selenium untuk menelusuri elemen dan mengisi halaman login, dropdown, radio buttons, dsb.
## Installation

Library yang dibutuhkan dalam autofill ini adalah:
```bash
  pip install time
  pip install selenium
```
    
## Versions

- Versi 1: Fungsi utama autofill dan halaman login telah tercapai melalui versi 1. Rencana selanjutnya adalah membuat kode lebih bisa digunakan user secara langsung tanpa perlu mengotak-atik kode. Misalnya request input halaman login, pemberian pilihan evaluasi yang lebih spesifik, dsb.