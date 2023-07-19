
import re
import argparse
from googletrans import Translator

def translate_katakana_blocks_to_english(text):
    translator = Translator()

    # カタカナの正規表現パターン
    katakana_pattern = r'[ァ-ン\ー]+'
    
    # カタカナの塊を検索
    katakana_blocks = re.findall(katakana_pattern, text)

    # カタカナを英語に翻訳
    translated_text = text
    for block in katakana_blocks:
        translation = translator.translate(block, src='ja', dest='en')
        translated_text = translated_text.replace(block, translation.text)

    return translated_text
    
def remove_katakana_and_hiragana(text, without_english_translation, without_katakana):
    # カタカナとひらがなの正規表現パターン
    pattern = r'[ぁ-ん]'
    if without_katakana:
      pattern = r'[ぁ-んァ-ン\ー]'
    # 正規表現パターンに一致する部分を空文字列に置換
    hiragana_removed = re.sub(pattern, '', text)

    if without_english_translation:
        katakana_removed = hiragana_removed
    else:
        katakana_removed = translate_katakana_blocks_to_english(hiragana_removed)
        pattern = r'[ぁ-んァ-ン\ー]'
        # 正規表現パターンに一致する部分を空文字列に置換
        katakana_removed = re.sub(pattern, '', katakana_removed)
    # 句読点を使って文章を分割する正規表現パターン
    pattern = r'[。、]'
    # 正規表現パターンに一致する部分で文章を分割
    sentences = re.split(pattern, katakana_removed)
    # 空の文字列を削除
    sentences = [s for s in sentences if s.strip()]
    return sentences

def main():
    parser = argparse.ArgumentParser(description='Process Japanese text with optional English translation.')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    parser.add_argument('-k','--withoutkatakana', action='store_true', help='Remove all katakana')
    parser.add_argument('-e','--withouten', action='store_true', help='Do not perform English translation')

    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f:
        japanese_text = f.read()

    split_text = remove_katakana_and_hiragana(japanese_text, args.withouten, args.withoutkatakana)

    with open(args.output_file, 'w', encoding='utf-8') as f:
        for sentence in split_text:
            f.write(sentence + '\n')

if __name__ == "__main__":
    main()

