import ezdxf

class CadExporter:
    def __init__(self, filename="automated_output.dxf"):
        self.doc = ezdxf.new('R2010')
        self.msp = self.doc.modelspace()
        # セマンティックマッピング: 属性（レイヤー）の設定
        [span_4](start_span)self.doc.layers.new(name='EXTERIOR_WALL', dxfattribs={'color': 1})[span_4](end_span)

    def add_wall_layer(self, points):
        """
        抽出した外壁データをレイヤー情報を持つCADデータとして書き出し
        """
        [span_5](start_span)self.msp.add_lwpolyline(points, dxfattribs={'layer': 'EXTERIOR_WALL'})[span_5](end_span)

    def save(self, path):
        self.doc.saveas(path)