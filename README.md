
# KPI レーダーチャート可視化ツール

このプロジェクトは、KPI（重要業績評価指標）をレーダーチャートで可視化するPythonスクリプトです。  
`matplotlib` を使用して視覚的にわかりやすいグラフを生成します。

---

## 機能

- **レーダーチャート作成**  
  任意のKPIラベルとスコアを入力することで、パフォーマンスを視覚化します。
- **日本語対応**  
  日本語フォントの設定を含み、文字化けを防止。
- **柔軟性**  
  KPIデータを簡単にカスタマイズ可能。

---

## 実行方法

### 1. 必要なライブラリをインストール

以下のコマンドを使用して、依存ライブラリをインストールします：

```bash
pip install matplotlib numpy
```

### 2. スクリプトの実行

次に、`main.py` を実行します：

```bash
python main.py
```

### 3. 出力

スクリプト実行後、以下のようなレーダーチャートが表示されます：

- KPIのスコアがレーダーチャート形式で可視化。
- 各軸に対応するKPIラベルが表示。

---

## ファイル構成

```
.
├── main.py          # レーダーチャート生成スクリプト
├── README.md        # このファイル
└── requirements.txt # 依存ライブラリ（オプション）
```

---

## カスタマイズ方法

### KPIデータの変更

`main.py` 内の以下の部分を編集して、KPIラベルとスコアを変更できます：

```python
kpi_labels = ['売上', '顧客満足度', '新規顧客獲得率', '従業員満足度', '利益率']
kpi_values = [80, 70, 85, 90, 75]
```

- **KPIラベル**: 評価項目の名前（例: "売上", "利益率"）。
- **KPIスコア**: 各項目のスコア（例: 80, 90）。

### 日本語フォントの変更

システム環境に応じてフォントを変更する場合は、以下を編集します：

```python
rcParams['font.family'] = 'Hiragino Sans'  # Mac
# rcParams['font.family'] = 'Meiryo'  # Windows
# rcParams['font.family'] = 'Noto Sans JP'  # Linux
```

---

## 要件

- Python 3.7以上
- 必須ライブラリ: `matplotlib`, `numpy`

`requirements.txt` を利用してインストールする場合：

```bash
pip install -r requirements.txt
```

---

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) の下で提供されています。

---

## 貢献

バグ報告や機能リクエストがある場合は、Issueを作成してください。Pull Requestも歓迎です！

---

## 開発者

- **名前**: Takuya Sato
- **GitHub**: [https://github.com/timeless-residents](https://github.com/timeless-residents)
