# my_custom_nodes/nodes/__init__.py

# 個別のモジュールからクラスをインポート
from .text_transformer import TextTransformerNode

# このサブパッケージから他のスクリプトがインポート可能な要素を定義
__all__ = ['TextTransformerNode']