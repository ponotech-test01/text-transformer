# my_custom_nodes/__init__.py

# nodesサブパッケージから必要なクラスをインポート
from .nodes import TextTransformerNode

# ComfyUIがノードを認識するために必要なマッピング
NODE_CLASS_MAPPINGS = {
    "TextTransformer": TextTransformerNode
}

# ComfyUIのUIでの表示名を定義
NODE_DISPLAY_NAME_MAPPINGS = {
    "TextTransformer": "Text Transformer"
}

# 他のスクリプトからインポート可能な要素を定義
__all__ = ['TextTransformerNode', 'NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']