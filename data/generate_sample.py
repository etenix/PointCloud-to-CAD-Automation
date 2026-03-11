import numpy as np
import open3d as o3d

def create_dummy_wall():
    """
    RANSACアルゴリズムをテストするための、ノイズを含む壁面（平面）データを生成
    """
    # 平面上の点を生成 (1000点)
    points = np.random.rand(1000, 3)
    points[:, 2] = points[:, 0] * 0.01 + points[:, 1] * 0.02  # ほぼ平らな面
    
    # ノイズを追加
    noise = np.random.normal(0, 0.002, points.shape)
    points += noise
    
    # 外れ値（ノイズ）を追加
    outliers = np.random.rand(100, 3) * 2.0
    all_points = np.vstack((points, outliers))
    
    # Open3Dオブジェクトに変換して保存
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(all_points)
    o3d.io.write_point_cloud("sample_scan.pcd", pcd)
    print("sample_scan.pcd を生成しました。")

if __name__ == "__main__":
    create_dummy_wall()