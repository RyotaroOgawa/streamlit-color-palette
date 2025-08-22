import numpy as np
import streamlit as st
from sklearn.cluster import KMeans
from PIL import Image


def safe_open_rgba(uploaded_file):
    img = Image.open(uploaded_file)
    w, h = img.size
    if (w * h) > 5_000_000:
        scale = (w * h / 5_000_000) ** 0.5
        new_size = (int(w / scale), int(h / scale))
        img = img.resize(new_size, Image.LANCZOS)
    return img
    

def make_palette(img, k):
    arr = np.asarray(img).reshape(-1, 3)

    # K-meansで色を抽出
    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
    labels = kmeans.fit_predict(arr)
    colors = kmeans.cluster_centers_.astype(int)

    # 各色の割合を計算
    counts = np.bincount(labels)
    ratios = counts / counts.sum()

    # 割合順にソート
    sorted_indices = np.argsort(-ratios)
    colors = colors[sorted_indices]
    ratios = ratios[sorted_indices]

    # 結果を辞書のリストで返す
    result = []
    for color, ratio in zip(colors, ratios):
        result.append(
            {
                "k": int(k),
                "rgb": [int(color[0]), int(color[1]), int(color[2])],
                "hex": f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}",
                "ratio": float(ratio),
            }
        )

    return result
    

def make_palette_img(rgbs, swatch_size=64):
    k = len(rgbs)
    width = swatch_size * k
    height = swatch_size

    img = Image.new("RGB", (width, height))

    for i, rgb in enumerate(rgbs):
        color = tuple(rgb)
        x0 = i * swatch_size
        swatch = Image.new("RGB", (swatch_size, swatch_size), color)
        img.paste(swatch, (x0, 0))

    return img
    

@st.cache_data(show_spinner=False)
def cached_palette(file_bytes, k):
    return make_palette(file_bytes, k)

