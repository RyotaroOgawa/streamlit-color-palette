# Streamlit Color Palette

画像から主要な色を抽出し、カラーパレットを生成してダウンロードできる Streamlit アプリです。  


## Demo

https://color-palette-maker.streamlit.app

## Table of Contents
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Usage](#-usage)
- [Run Locally](#-run-locally)
- [Deployment](#-deployment)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)
## Badges
![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg)
![Python](https://img.shields.io/badge/python-%203.12-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Tech Stack

- **App**: Python, Streamlit
- **Image**: Pillow (PIL)
- **Numeric**: NumPy
- **Clustering**: scikit-learn
- **Chart**: matplotlib
- **Dev**: Poetry


## Features

- 画像をアップロードすると主要色を自動抽出（クラスタ数 *k* をスライダーで指定）
- HEX / RGB 値の表示
- 各色の出現比率（割合）の可視化
- パレット画像のダウンロード
- ブラウザだけで動作（Python + Streamlit）

## Usage

##### 1) 画像（PNG/JPG/JPEG）をアップロード
##### 2) スライダーでクラスタ数 k（3〜7）を指定
##### 3) 抽出された色と HEX/RGB、出現比率を確認
##### 4) 画像/CSV のダウンロード

## Run Locally

Clone the project

```bash
  git clone https://github.com/RyotaroOgawa/streamlit-color-palette.git
```

Go to the project directory

```bash
  cd streamlit-color-palette
```

Create venv

```bash
  python -m venv .venv
  source .venv/bin/activate
```

Install deps

```bash
  poetry install -r requirements.txt
```

Start the server

```bash
  streamlit run myproject/app.py
```


## Deployment
**Streamlit Community Cloud**
##### 1) リポジトリを公開
##### 2) https://share.streamlit.io から Create app
##### 3) Repo / Branch / Main file（例：myproject/app.py）を指定
##### 4) デプロイ


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [Streamlit](https://streamlit.io)
 - [Pillow](https://pillow.readthedocs.io/en/stable/#)
 - [Numpy](https://numpy.org/ja/)
 - [scikit-learn](https://scikit-learn.org/stable/)
 - [matplotlib](https://matplotlib.org)

