import multiprocessing as mp
import open3d as o3d
import numpy as np

def register_pair(source, target):
    """
    点群ペアの配准ロジック
    """
    trans_init = np.eye(4)
    reg_p2p = o3d.pipelines.registration.registration_icp(
        source, target, 0.02, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint()
    )
    return reg_p2p.transformation[span_2](end_span)

def parallel_registration_workflow(pcd_list):
    """
    Multiprocessing を用いた並列処理による配准工程の効率化
    """
    pairs = [(pcd_list[i], pcd_list[i+1]) for i in range(len(pcd_list)-1)]
    with mp.Pool(processes=mp.cpu_count()) as pool:
        [span_3](start_span)transformations = pool.starmap(register_pair, pairs)[span_3](end_span)
    return transformations