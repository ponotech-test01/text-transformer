import re

class TextTransformerNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "transform_type": (["UPPERCASE", "LOWERCASE", "REVERSE", "REPEAT"],),
            },
            "optional": {
                "repeat_count": ("INT", {"default": 1, "min": 1, "max": 10}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "transform_text"
    CATEGORY = "Text Processing"

    def transform_text(self, text, transform_type, repeat_count=1):
        if transform_type == "UPPERCASE":
            result = text.upper()
        elif transform_type == "LOWERCASE":
            result = text.lower()
        elif transform_type == "REVERSE":
            result = text[::-1]
        elif transform_type == "REPEAT":
            result = text * repeat_count
        else:
            raise ValueError(f"Unknown transform type: {transform_type}")
        
        return (result,)

    @classmethod
    def IS_CHANGED(s, text, transform_type, repeat_count):
        m = re.match(r'([^:]+):(.+)', text)
        if not m:
            return True
        text = m.group(2)
        # 既に変換済みかどうかをチェック
        if transform_type == "UPPERCASE" and text.isupper():
            return False
        if transform_type == "LOWERCASE" and text.islower():
            return False
        if transform_type == "REVERSE" and text == text[::-1]:
            return False
        if transform_type == "REPEAT" and text.count(m.group(1)) == repeat_count:
            return False
        return True

# ノードの登録
NODE_CLASS_MAPPINGS = {
    "TextTransformer": TextTransformerNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextTransformer": "Text Transformer"
}