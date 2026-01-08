# 🎨 Image Noise Reduction - Filter Comparison Tool

Program Python komprehensif untuk **menambahkan noise** (Salt & Pepper dan Gaussian) pada citra, kemudian **membandingkan performa 4 metode filtering** (Min, Max, Mean, Median) untuk mengurangi noise tersebut.

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.19%2B-orange.svg)](https://numpy.org/)


---

## 📑 Table of Contents

- [Deskripsi](#-deskripsi)
- [Fitur Utama](#-fitur-utama)
- [Instalasi](#-instalasi)
- [Quick Start](#-quick-start)
- [Cara Penggunaan](#️-cara-penggunaan)
- [Struktur Output](#-struktur-output)
- [Analisis Hasil](#-analisis-hasil)
- [Teori & Algoritma](#-teori--algoritma)
- [Kustomisasi](#-kustomisasi)
- [Studi Kasus](#-studi-kasus)
- [Benchmark & Performance](#-benchmark--performance)
- [Troubleshooting](#️-troubleshooting)
- [FAQ](#-faq)
- [API Reference](#-api-reference)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [License](#-license)

---

## 📋 Deskripsi

Program ini dirancang untuk penelitian, pembelajaran, dan evaluasi metode **noise reduction** dalam pengolahan citra digital. Cocok untuk: 

- 🎓 **Mahasiswa** - Tugas kuliah Image Processing
- 🔬 **Researcher** - Evaluasi metode denoising
- 💼 **Developer** - Preprocessing untuk Computer Vision
- 📚 **Educator** - Material ajar pengolahan citra

### 🔧 Metode Filtering yang Diimplementasikan

| Filter | Complexity | Cara Kerja | Cocok Untuk | Kelebihan | Kekurangan |
|--------|------------|------------|-------------|-----------|------------|
| **Min Filter** | O(n²) | Mengambil nilai minimum dari window | Menghilangkan **salt noise** (titik putih) | Efektif untuk bright outliers | Citra jadi lebih gelap |
| **Max Filter** | O(n²) | Mengambil nilai maksimum dari window | Menghilangkan **pepper noise** (titik hitam) | Efektif untuk dark outliers | Citra jadi lebih terang |
| **Mean Filter** | O(n²) | Rata-rata nilai dalam window | **Gaussian noise** | Smoothing bagus | Blur edge |
| **Median Filter** | O(n² log n) | Nilai tengah (median) dalam window | **Salt & pepper noise** | Preservasi edge | Lebih lambat |

### 🎯 Jenis Noise yang Disimulasikan

| Noise Type | Parameter | Formula | Karakteristik | Real-world Example |
|------------|-----------|---------|---------------|-------------------|
| **Salt & Pepper** | `prob` (0-1) | P(x) = white if rand < prob/2<br>P(x) = black if rand > 1-prob/2 | Noise impulsif - piksel random jadi putih (255) atau hitam (0) | Dead pixels pada sensor kamera |
| **Gaussian** | `sigma` (σ) | N(0, σ²) | Noise distribusi normal - menambahkan random value ke setiap piksel | Low-light photography noise |

### 🌟 Yang Membedakan Program Ini

- ✅ **Manual Implementation** - Konvolusi tanpa library filtering (educational purpose)
- ✅ **Dual Mode Processing** - Support grayscale & color images
- ✅ **Quantitative Evaluation** - MSE metrics untuk objektif comparison
- ✅ **Visual Comparison** - Auto-generate comparison panels
- ✅ **Flexible Parameters** - Customizable noise levels dan filter size
- ✅ **Production Ready** - Error handling dan logging lengkap

---

## 🚀 Fitur Utama

### 1. **Noise Generation**
- **Salt & Pepper Noise**
  - Adjustable probability (0-100%)
  - Uniform random distribution
  - Support grayscale & RGB
  
- **Gaussian Noise**
  - Adjustable sigma (standard deviation)
  - Normal distribution N(0, σ²)
  - Automatic clipping (0-255)

### 2. **Spatial Filtering**
- **Manual Convolution**
  - Custom kernel size (3x3, 5x5, 7x7, etc.)
  - Edge padding untuk border pixels
  - Support multi-channel images
  
- **4 Filter Types**
  - Min, Max, Mean, Median
  - Optimized untuk speed
  - Consistent behavior across grayscale/color

### 3. **Quantitative Analysis**
- **MSE (Mean Squared Error)**
  - Pixel-wise comparison
  - Range:  0 (identical) to ∞
  - Formula: `MSE = (1/n) Σ(original - filtered)²`

- **CSV Export**
  - Structured data untuk analisis lanjut
  - Compatible dengan Excel/Pandas
  - Headers: Mode, Noise, Filter, MSE

### 4. **Visualization**
- **Comparison Panels**
  - 2×3 grid layout (6 images per panel)
  - Original | Noisy | Filtered (Min/Max/Mean/Median)
  - Labeled dengan informasi lengkap
  
- **High Quality Output**
  - PNG format (lossless)
  - Original resolution preserved
  - Professional labeling

### 5. **Batch Processing**
- Process multiple images
- Configurable noise levels
- Parallel processing ready

---

## 📦 Instalasi

```bash
# Clone repository
git clone https://github.com/bagaspng/image-noise-reduction.git
cd image-noise-reduction

# Install dependencies
pip install -r requirements.txt
