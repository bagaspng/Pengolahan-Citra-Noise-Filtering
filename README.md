# 🎨 Image Noise Reduction - Filter Comparison Tool

Program Python untuk **menambahkan noise** (Salt & Pepper dan Gaussian) pada citra, kemudian **membandingkan performa 4 metode filtering** (Min, Max, Mean, Median) untuk mengurangi noise tersebut.

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.19%2B-orange.svg)](https://numpy.org/)

---

## 📋 Deskripsi

Program ini dirancang untuk: 
1. ✅ **Menambahkan noise** pada citra (Salt & Pepper atau Gaussian)
2. ✅ **Menerapkan 4 filter** untuk mengurangi noise
3. ✅ **Menghitung MSE** (Mean Squared Error) untuk evaluasi kuantitatif
4. ✅ **Membuat visualisasi panel** perbandingan hasil filtering
5. ✅ **Mendukung mode Grayscale dan Color**

### 🔧 Metode Filtering yang Diimplementasikan

| Filter | Cara Kerja | Cocok Untuk |
|--------|------------|-------------|
| **Min Filter** | Mengambil nilai minimum dari window | Menghilangkan **salt noise** (titik putih) |
| **Max Filter** | Mengambil nilai maksimum dari window | Menghilangkan **pepper noise** (titik hitam) |
| **Mean Filter** | Rata-rata nilai dalam window | **Gaussian noise**, menghaluskan citra |
| **Median Filter** | Nilai tengah (median) dalam window | **Salt & pepper noise**, preservasi edge |

### 🎯 Jenis Noise yang Disimulasikan

| Noise Type | Parameter | Deskripsi |
|------------|-----------|-----------|
| **Salt & Pepper** | `prob` (0-1) | Noise impulsif - piksel random jadi putih (255) atau hitam (0) |
| **Gaussian** | `sigma` | Noise distribusi normal - menambahkan random value ke setiap piksel |

---

## 📦 Instalasi

### Requirements
- Python 3.7 atau lebih tinggi
- OpenCV (cv2)
- NumPy

### Langkah Instalasi

1. **Clone atau download repository**
   ```bash
   git clone <repository-url>
   cd image-noise-reduction
