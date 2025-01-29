# バウンディングボックスアノテーションツール

このリポジトリには、画像にバウンディングボックスを描画し、結果をJSON形式で保存するPythonスクリプトが含まれています。

## 📌 特徴
- 指定したフォルダ内の全ての画像を自動的に処理
- マウス操作でバウンディングボックスを描画
- `output/` フォルダ内にJSONとして保存
- 複数のフォルダの画像に対応

---

## 🚀 インストールとセットアップ

### **1. リポジトリをクローン**
```sh
git clone https://github.com/yourusername/makeJsonBox.git
cd makeJsonBox
```

### **2. 仮想環境をセットアップ**
```sh
python -m venv myenv
source myenv/bin/activate  # macOS/Linux用
# Windowsの場合: myenv\Scripts\activate
```

### **3. 依存関係をインストール**
```sh
pip install -r requirements.txt
```

---

## 🖼️ スクリプトの使い方

### **1. 画像フォルダを準備**
プロジェクトディレクトリ内に `photos1/` や `photos2/` のような画像フォルダを作成し、画像を配置します。

### **2. スクリプトを実行**
画像フォルダに移動してスクリプトを実行します。
```sh
cd photos1  # 画像フォルダに移動
python ../makeBountyBoxToJson.py
```

### **3. 画像をアノテーション**
- 画像が順番に表示されます。
- マウスでクリック＆ドラッグしてバウンディングボックスを描画。
- `Esc` キーを押すと次の画像に進む。
- 全ての画像を処理した後、結果が `output/` にJSON形式で保存されます。

### **4. JSON出力フォーマット**
例 (`output/photos1.json`):
```json
[
    {
        "image": "image1.jpg",
        "bounding_boxes": [
            {"x_min": 100, "y_min": 200, "x_max": 300, "y_max": 400}
        ]
    },
    {
        "image": "image2.jpg",
        "bounding_boxes": [
            {"x_min": 150, "y_min": 250, "x_max": 350, "y_max": 450}
        ]
    }
]
```

---

## 📁 プロジェクト構成
```
makeJsonBox/
├── makeBountyBoxToJson.py  # メインスクリプト
├── myenv/                   # 仮想環境（Git管理外）
├── output/                  # JSON出力フォルダ
├── photos1/                 # 画像フォルダの例
├── photos2/                 # 別の画像フォルダ
├── requirements.txt         # 必要なライブラリ一覧
└── README.md                # このファイル
```

---

## 🔥 補足事項
- 画像フォーマットは **JPEGまたはPNG** に対応。
- `output/` フォルダが存在しない場合、自動で作成されます。
- `photos1/`, `photos2/` など、複数のフォルダを作成して繰り返し処理が可能。

---

## 🌍 コントリビューション
リポジトリのフォークやプルリクエストを歓迎します！バグや提案があれば GitHub の issue に投稿してください。

---

## 📜 ライセンス
このプロジェクトは MIT ライセンスのもとで公開されています。

