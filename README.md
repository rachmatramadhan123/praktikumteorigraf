# Teori Graf - Implementasi Algoritma

Repository ini berisi implementasi dua algoritma penting dalam Teori Graf dan Dynamic Programming.

---

## 📋 Daftar Program

### 1. Knight's Tour (knights_tour.py)
### 2. Longest Monotonically Increasing Subsequence - LMIS (TGRAF2.py)

---

## 🐴 Knight's Tour

### Deskripsi
Program yang menyelesaikan masalah **Knight's Tour** menggunakan **Algoritma Warnsdorff**. Knight's Tour adalah masalah klasik di mana kuda catur harus mengunjungi setiap kotak pada papan catur 8×8 tepat satu kali.

### Fitur
- ✅ Input posisi awal kuda dengan format `xy` (x=horizontal, y=vertikal)
- ✅ Visualisasi papan catur ASCII dengan simbol kuda (♘)
- ✅ Algoritma Warnsdorff untuk menemukan jalur optimal
- ✅ Deteksi **CLOSED Tour** (kuda dapat kembali ke posisi awal) atau **OPEN Tour**
- ✅ Visualisasi grafik matplotlib dengan path lengkap
- ✅ Marker hijau untuk start, merah untuk end

### Cara Penggunaan

#### Instalasi Dependencies
```bash
pip install matplotlib
```

#### Menjalankan Program
```bash
python knights_tour.py
```

#### Format Input
- Input berformat **2 digit**: `xy`
  - `x` = posisi horizontal (1-8, dari kiri ke kanan)
  - `y` = posisi vertikal (1-8, dari bawah ke atas)

**Contoh Input:**
- `18` = kiri atas
- `88` = kanan atas
- `11` = kiri bawah
- `81` = kanan bawah
- `44` = tengah papan

#### Contoh Output
```
==================================================
KNIGHT'S TOUR - ALGORITMA WARNSDORFF
==================================================

  1 2 3 4 5 6 7 8
  ----------------
8|□ ■ □ ■ □ ■ □ ■ |8
7|■ □ ■ □ ■ □ ■ □ |7
...

Masukkan posisi awal kuda (xy): 18

✓ Kuda dimulai dari posisi x=1, y=8
⏳ Mencari rute Knight's Tour...

✓ Berhasil! Hasil: CLOSED Tour
  Total langkah: 64
  Kuda dapat kembali ke posisi awal!

📊 Menampilkan visualisasi...
```

### Algoritma
**Warnsdorff's Rule:**
- Pada setiap langkah, kuda bergerak ke kotak yang memiliki jumlah kemungkinan gerakan berikutnya paling sedikit
- Strategi greedy yang efisien untuk menemukan solusi Knight's Tour
- Kompleksitas waktu: O(N²) untuk papan N×N

### Output
1. **Console:** Papan catur ASCII + status tour (CLOSED/OPEN)
2. **Grafik:** Visualisasi matplotlib menampilkan jalur lengkap kuda dengan garis penghubung antar gerakan

---

## 📊 LMIS - Longest Monotonically Increasing Subsequence

### Deskripsi
Program yang mencari **subsequence terpanjang yang monoton naik** dari sebuah array menggunakan **Dynamic Programming**.

### Fitur
- ✅ Algoritma Dynamic Programming untuk mencari LMIS
- ✅ Menampilkan subsequence lengkap (bukan hanya panjangnya)
- ✅ Kompleksitas waktu: O(n²)
- ✅ Kompleksitas ruang: O(n²)

### Cara Penggunaan

#### Menjalankan Program
```bash
python TGRAF2.py
```

#### Contoh Input/Output
**Array:** `[4, 1, 13, 7, 0, 2, 8, 11, 3]`

**Output:** `[1, 2, 8, 11]`

**Penjelasan:**
- Subsequence `[1, 2, 8, 11]` adalah yang terpanjang dengan nilai monoton naik
- Panjang: 4 elemen

### Algoritma
**Dynamic Programming Approach:**
1. Buat array `dp[i]` yang menyimpan LMIS terpanjang yang berakhir di index `i`
2. Untuk setiap elemen `i`, cek semua elemen sebelumnya `j` (j < i)
3. Jika `arr[j] < arr[i]`, maka bisa extend subsequence dari `j` ke `i`
4. Pilih subsequence terpanjang dari semua kemungkinan

**Pseudocode:**
```
for i = 0 to n-1:
    dp[i] = [arr[i]]
    for j = 0 to i-1:
        if arr[j] < arr[i] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [arr[i]]
return max(dp, key=len)
```

### Modifikasi untuk Custom Input
Untuk mengubah input array, edit baris:
```python
arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
```

---

## 🛠️ Requirements

### Knight's Tour
- Python 3.6+
- matplotlib

### LMIS (TGRAF2)
- Python 3.6+ (tanpa dependencies eksternal)

---

## 📁 Struktur File

```
VSC/
├── knights_tour.py          # Program Knight's Tour
├── TGRAF2.py               # Program LMIS
└── README.md               # Dokumentasi (file ini)
```

---

## 🎓 Konsep Teori Graf

### Knight's Tour
- **Kategori:** Graph Traversal, Hamiltonian Path Problem
- **Representasi:** Graf tidak berarah dengan 64 node (kotak papan)
- **Edge:** Terhubung jika kuda dapat bergerak antar kotak dalam 1 langkah
- **Goal:** Temukan Hamiltonian Path (mengunjungi semua node tepat 1 kali)

### LMIS
- **Kategori:** Dynamic Programming, Optimization
- **Aplikasi:** Analisis data, pattern recognition, sequence alignment
- **Varian:** Longest Increasing Subsequence (LIS), Longest Common Subsequence (LCS)

---

## 📝 Catatan

### Knight's Tour
- Tidak semua posisi awal menghasilkan CLOSED Tour
- Posisi tengah papan (misal: `44`, `45`) cenderung menghasilkan CLOSED Tour
- Posisi sudut/tepi mungkin hanya menghasilkan OPEN Tour

### LMIS
- Algoritma ini menyimpan subsequence lengkap, bukan hanya panjangnya
- Untuk array besar, pertimbangkan optimasi ruang dengan hanya menyimpan panjang

---

## 👨‍💻 Author

**Tugas Teori Graf**  
Implementasi Algoritma: Knight's Tour & LMIS

---

## 📄 License

Educational Purpose - Free to use and modify

---

## 🔗 Referensi

### Knight's Tour
- [Wikipedia - Knight's Tour](https://en.wikipedia.org/wiki/Knight%27s_tour)
- [Warnsdorff's Rule](https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorff's_rule)

### LMIS/LIS
- [Wikipedia - Longest Increasing Subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)
- Dynamic Programming Fundamentals
