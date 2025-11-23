import cv2
import numpy as np
import os

def mse(img1, img2):
    return np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def add_salt_pepper(img, prob):
    """
    Tambah noise salt & pepper ke citra grayscale atau color.
    prob = proporsi total pixel yang terkena noise (contoh: 0.02 = 2%)
    """
    noisy = img.copy()
    h, w = img.shape[:2]

    rnd = np.random.rand(h, w)
    salt_mask = rnd < (prob / 2.0)
    pepper_mask = rnd > (1.0 - prob / 2.0)

    if img.ndim == 2:
        noisy[salt_mask] = 255
        noisy[pepper_mask] = 0
    else:
        noisy[salt_mask, :] = 255
        noisy[pep_mask := pepper_mask, :] = 0 if False else None
        noisy[pepper_mask, :] = 0

    return noisy

def add_gaussian(img, sigma):
    """
    Tambah noise Gaussian ke citra grayscale atau color.
    """
    noise = np.random.normal(0, sigma, img.shape)
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def apply_filter(img, size, mode):
    """
    Filter manual (min, max, mean, median) untuk grayscale & color.
    Menggunakan padding 'edge' supaya semua pixel terproses (border tidak hitam).
    """
    r = size // 2
    if img.ndim == 2:
        h, w = img.shape
        padded = np.pad(img, ((r, r), (r, r)), mode='edge')
        out = np.zeros_like(img)

        for i in range(h):
            for j in range(w):
                win = padded[i:i+size, j:j+size]

                if mode == "min":
                    val = win.min()
                elif mode == "max":
                    val = win.max()
                elif mode == "mean":
                    val = win.mean()
                elif mode == "median":
                    val = np.median(win)
                else:
                    raise ValueError("Mode filter tidak dikenal")

                out[i, j] = int(round(val))

    else:
        h, w, c = img.shape
        padded = np.pad(img, ((r, r), (r, r), (0, 0)), mode='edge')
        out = np.zeros_like(img)

        for i in range(h):
            for j in range(w):
                for ch in range(c):
                    win = padded[i:i+size, j:j+size, ch]

                    if mode == "min":
                        val = win.min()
                    elif mode == "max":
                        val = win.max()
                    elif mode == "mean":
                        val = win.mean()
                    elif mode == "median":
                        val = np.median(win)
                    else:
                        raise ValueError("Mode filter tidak dikenal")

                    out[i, j, ch] = int(round(val))

    return out.astype(np.uint8)

def add_label_bar(img, text):
    """
    Menambahkan bar tulisan di bawah gambar.
    Output selalu 3-channel (BGR) supaya aman digabung.
    """
    if img.ndim == 2:
        img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        img_color = img.copy()

    h, w = img_color.shape[:2]

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.9
    thickness = 2
    padding_x = 10

    (text_w, text_h), baseline = cv2.getTextSize(text, font, font_scale, thickness)
    bar_h = max(60, text_h + baseline + 20)

    bar = np.full((bar_h, w, 3), 255, dtype=np.uint8)

    y = (bar_h + text_h) // 2 - baseline

    cv2.putText(
        bar,
        text,
        (padding_x, y),
        font,
        font_scale,
        (0, 0, 0),
        thickness,
        cv2.LINE_AA,
    )

    return np.vstack([img_color, bar])

def save_panel(original, noisy, filtered_dict, mode_desc, noise_desc,
               filter_size, out_path):
    tiles = []

    tiles.append(add_label_bar(original, f"Original ({mode_desc})"))
    tiles.append(add_label_bar(noisy, f"Noisy {noise_desc}"))
    tiles.append(add_label_bar(filtered_dict["min"], f"Min {filter_size}x{filter_size}"))
    tiles.append(add_label_bar(filtered_dict["max"], f"Max {filter_size}x{filter_size}"))
    tiles.append(add_label_bar(filtered_dict["mean"], f"Mean {filter_size}x{filter_size}"))
    tiles.append(add_label_bar(filtered_dict["median"], f"Median {filter_size}x{filter_size}"))

    row1 = cv2.hconcat(tiles[0:3])
    row2 = cv2.hconcat(tiles[3:6])
    panel = cv2.vconcat([row1, row2])

    cv2.imwrite(out_path, panel)

def process_mode(img, name, label_mode, out_dir, mse_table,
                 sp_levels=[0.02, 0.08], gauss_levels=[10, 25],
                 filter_size=3):
    base_fname = f"{out_dir}/{name}_{label_mode}.png"
    cv2.imwrite(base_fname, img)

    mode_desc = "Gray" if label_mode == "gray" else "Color"
    filter_modes = ["min", "max", "mean", "median"]

    for p in sp_levels:
        noisy = add_salt_pepper(img, p)
        noise_tag = f"sp_{int(p*100)}"
        cv2.imwrite(f"{out_dir}/{name}_{label_mode}_{noise_tag}.png", noisy)

        filtered_dict = {}

        for mode in filter_modes:
            filtered = apply_filter(noisy, filter_size, mode)
            filtered_dict[mode] = filtered

            error = mse(img, filtered)
            mse_table.append([label_mode, f"SP {p}", mode, error])
            print(f"MSE {name} | {label_mode} | SP {p} | {mode}: {error:.3f}")

        noise_desc = f"Salt & Pepper {int(p*100)}%"
        panel_path = f"{out_dir}/{name}_{label_mode}_{noise_tag}_panel.png"
        save_panel(img, noisy, filtered_dict, mode_desc, noise_desc,
                   filter_size, panel_path)

    for s in gauss_levels:
        noisy = add_gaussian(img, s)
        noise_tag = f"gauss_{s}"
        cv2.imwrite(f"{out_dir}/{name}_{label_mode}_{noise_tag}.png", noisy)

        filtered_dict = {}

        for mode in filter_modes:
            filtered = apply_filter(noisy, filter_size, mode)
            filtered_dict[mode] = filtered

            error = mse(img, filtered)
            mse_table.append([label_mode, f"GAUSS {s}", mode, error])
            print(f"MSE {name} | {label_mode} | GAUSS {s} | {mode}: {error:.3f}")

        noise_desc = f"Gaussian σ={s}"
        panel_path = f"{out_dir}/{name}_{label_mode}_{noise_tag}_panel.png"
        save_panel(img, noisy, filtered_dict, mode_desc, noise_desc,
                   filter_size, panel_path)

def process_image(path, name):
    print(f"\n=== Memproses {name} ===")

    if not os.path.isfile(path):
        print(f"[ERROR] File tidak ditemukan: {path}")
        return

    img = cv2.imread(path)
    if img is None:
        print(f"[ERROR] Gagal membaca file: {path}")
        return

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    out_dir = f"results/{name}"
    ensure_dir(out_dir)

    cv2.imwrite(f"{out_dir}/{name}_original_color.png", img)

    mse_table = []

    sp_levels = [0.02, 0.08]
    gauss_levels = [10, 25]
    filter_size = 3

    process_mode(img_gray, name, "gray", out_dir, mse_table,
                 sp_levels=sp_levels, gauss_levels=gauss_levels,
                 filter_size=filter_size)

    process_mode(img, name, "color", out_dir, mse_table,
                 sp_levels=sp_levels, gauss_levels=gauss_levels,
                 filter_size=filter_size)

    mse_path = f"{out_dir}/{name}_mse.csv"
    with open(mse_path, "w") as f:
        f.write("Mode,Noise,Filter,MSE\n")
        for mode_label, noise_label, filt, val in mse_table:
            f.write(f"{mode_label},{noise_label},{filt},{val}\n")

    print(f"\n✔ Semua hasil untuk {name} disimpan di folder: {out_dir}")
    print(f"✔ Tabel MSE: {mse_path}\n")

process_image("Lake Bled, Slovenia.jpeg", "lake")
process_image("potrait.jpeg", "potrait")

print("\n=== SELESAI ===")
