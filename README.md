# 3D点群データからCAD図面への自動生成パイプライン

## プロジェクト概要
非構造的な3D点群データから幾何学的特徴を抽出し、セマンティック情報（属性情報）を持つCAD図面を自動生成します。

## 主要な成果
- 工数削減: 従来の手動モデリングと比較し平面図作成時間を約50%削減。
- 高精度: 外壁面の自動抽出において精度±5mm以内を達成。
- 最適化: KD-Tree導入により､数億点規模のデータに対する高速な近傍探索を実現。

## 技術スタック
- 言語: Python 3.8+
- ライブラリ: Open3D,NumPy,Scipy,ezdxf,PyAutoCAD
- アルゴリズム: RANSAC,KD-Tree,ICP Registration
- 環境: Windows(AutoCAD)

## 導入機能
1. Denoising: KD-Treeを用いた統計的外れ値除去。
2. Extraction: RANSACによる外壁面のセグメンテーション。
3. CAD Mapping: ezdxfを活用した､階層別レイヤーを含むDXF/DWG形式の自動出力。