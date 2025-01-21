"""
KPIをレーダーチャートで可視化するスクリプト
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントの設定
rcParams['font.family'] = 'Hiragino Sans'  # Mac用の設定
# rcParams['font.family'] = 'Meiryo'  # Windowsの場合はこちらを使用
# rcParams['font.family'] = 'Noto Sans JP'  # Linuxの場合はこちらを使用

def create_radar_chart(kpi_labels, kpi_values):
    """
    レーダーチャートを作成して表示する関数

    Args:
        kpi_labels (list): KPIのラベル一覧
        kpi_values (list): KPIの値一覧（スコア）
    """
    # データの前処理
    num_vars = len(kpi_labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    kpi_values += kpi_values[:1]  # 閉じるために最初の値を末尾に追加
    angles += angles[:1]

    # 描画の設定
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, kpi_values, color='blue', alpha=0.25)
    ax.plot(angles, kpi_values, color='blue', linewidth=2)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20', '40', '60', '80', '100'], color="grey", size=10)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(kpi_labels, size=12)

    # グラフのタイトル
    plt.title('KPI可視化', size=16, color='blue', y=1.1)
    plt.show()

def main():
    """
    メイン関数: レーダーチャートの作成を実行
    """
    # KPIデータの定義
    kpi_labels = ['売上', '顧客満足度', '新規顧客獲得率', '従業員満足度', '利益率']
    kpi_values = [80, 70, 85, 90, 75]  # 各KPIのスコア

    # レーダーチャートを作成
    create_radar_chart(kpi_labels, kpi_values)

if __name__ == "__main__":
    main()
