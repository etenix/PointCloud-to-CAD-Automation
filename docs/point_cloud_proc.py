import open3d as o3d
import numpy as np

class WallExtractor:
    def __init__(self, pcd_path):
        """
        初期化: 数億点規模の点群データをロード
        """
        [span_0](start_span)self.pcd = o3d.io.read_point_cloud(pcd_path)[span_0](end_span)

    def denoise_with_kdtree(self):
        """
        KD-Tree 空間データ構造を用いた高速な近傍探索とノイズ除去
        """
        # 統計的な外れ値除去
        [span_1](start_span)cl, ind = self.pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)[span_1](end_span)
        self.pcd = self.pcd.select_by_index(ind)
        return self.pcd

    def ransac_wall_extraction(self, distance_threshold=0.005):
        """
        RANSACアルゴリズムによる平面フィッティング
        ±5mm以内の精度で建物の外壁面を自動認識・抽出
        """
        plane_model, inliers = self.pcd.segment_plane(
            distance_threshold=distance_threshold,
            ransac_n=3,
            num_iterations=1000
        [span_2](start_span))
        wall_cloud = self.pcd.select_by_index(inliers)
        remaining_cloud = self.pcd.select_by_index(inliers, invert=True)
        
        return wall_cloud, plane_model, remaining_cloud
