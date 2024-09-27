import re


def unescape_markdown(text: str) -> str:
    markdown_symbols = r'([*_`\[\]()#+\-.!])'
    unescaped_text = re.sub(rf'\\{markdown_symbols}', r'\1', text)

    return unescaped_text
