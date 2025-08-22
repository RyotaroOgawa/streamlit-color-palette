import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from module import cached_palette, make_palette_img, safe_open_rgba
from PIL import Image
import io
import const

st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)

st.title("🎨 Color Palette Maker")

uploaded_file = st.file_uploader(
    "画像をアップロードしてください", type=["jpg", "png", "jpeg"]
)


if uploaded_file is not None:
    img = safe_open_rgba(uploaded_file).convert("RGB")
    with st.expander("画像プレビュー"):
        st.image(img, use_container_width=True)
    k = st.slider("抽出する色の数", min_value=3, max_value=7, value=5)
    with st.spinner("抽出中..."):
        result = cached_palette(img, k)
    hexes = [item["hex"] for item in result]
    rgbs = [item["rgb"] for item in result]
    ratios = np.array([item["ratio"] for item in result])
    cols = st.columns(len(hexes))

    # 左から割合順に色を表示
    for col, hex_c in zip(cols, hexes):
        col.markdown(
            f"<div style='height:56px;border:1px solid #ddd;background:{hex_c};'></div>",
            unsafe_allow_html=True,
        )
        col.code(f"{hex_c}", language="text")

    # データ表
    df = pd.DataFrame(
        [
            {"HEX": h, "R": r, "G": g, "B": b, "割合": f"{rt:.1%}"}
            for h, (r, g, b), rt in zip(hexes, rgbs, ratios)
        ]
    )
    st.dataframe(df, use_container_width=True)

    # 円グラフ
    fig, ax = plt.subplots()
    ax.pie(
        ratios,
        colors=hexes,
        autopct="%1.1f%%",
        startangle=0,
        counterclock=True,
    )
    ax.axis("equal")
    st.pyplot(fig)

    palette_img = make_palette_img(rgbs)
    st.image(palette_img, use_container_width=True)

    buf = io.BytesIO()
    palette_img.save(buf, format="PNG")
    buf.seek(0)
    st.download_button(
        "カラーパレットをダウンロード (PNG)",
        data=buf,
        file_name="palette.png",
        mime="image/png",
    )

else:
    st.info("画像をアップロードすると、ここに結果が表示されます。")
