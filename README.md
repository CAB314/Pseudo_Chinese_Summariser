# Pseudo_Chinese_Summariser

## Overview
This Python script is a tool for processing Japanese text by removing katakana and hiragana, and optionally translating katakana blocks to English.

$$ Dependencies
Install the following dependency:

googletrans==4.0.0-rc1
You can install it using the following command:

```
pip install googletrans==4.0.0-rc1
```

## Usage

```
python pseudo_chinese_summariser.py input_file.txt output_file.txt [-k] [-e]
```

your_script.py: The name of the script
input_file.txt: The path to the input file containing the Japanese text to be processed
output_file.txt: The path to the output file to save the processed text
Options:

- `-k`, `--withoutkatakana`: If specified, remove katakana, and skip English translation of katakana blocks. When this option is used, any text containing katakana will also be removed.
- `-e`, `--withouten`: If specified, skip English translation of katakana blocks in Japanese text.
  - `When used with '-k', katakana removal will take priority.
Note: This script uses the Google Cloud Translation API, so an internet connection is required. Be aware of the API usage limitations when processing large amounts of text. Additionally, the availability of Google Translate is subject to their own usage restrictions.

## Example
For example, if input_file.txt contains the following Japanese text:


```input_file.txt
自動繊維配置（AFP）の欠陥検出システムは、豊富なラベル付きの不良サンプルが必要なエンドツーエンドの教師あり学習法に基づいていますが、これらは十分な数を簡単に生成することができません。そこで、データ不足の問題に対処するため、小規模データセットに適したオートエンコーダベースの手法を提案します。基盤的な観点から見れば、問題は正常サンプルと異常サンプルの2値分類として簡略化できます。提案手法では、繊維レイアップ表面のデプスマップを各コンポジットストリップ（タウ）に合わせて分割した小さなウィンドウを使用します。異常がない一部のウィンドウは、オートエンコーダに渡されて入力を再構築し、通常サンプルでトレーニングされているため、これらのサンプルに対してより正確な再構築が行われます。したがって、再構築エラーの値は潜在的な異常があるかどうかの定量的な評価指標として使用されます。これらの値は組み合わせて異常マップを生成し、デプスマップでの製造欠陥の位置を特定できます。結果は、オートエンコーダが非常に限られたスキャン数でトレーニングされているにもかかわらず、提案手法は十分な2値分類精度を生み出し、欠陥の位置を特定できることを示しています。
```

Running the following command will remove hiragana and translate katakana blocks to English, and the result will be saved in output_file.txt:


```
python pseudo_chinese_summariser.py input_file.txt output_file.txt 
```

The contents of output_file.txt will be as follows:

```output_file.txt
自動繊維配置（AFP）欠陥検出システム
豊富ラベル付不良サンプル必要エンドツーエンド教師学習法基
十分数簡単生成
データ不足問題対処
小規模データセット適オートエンコーダベース手法提案
基盤的観点見
問題正常サンプル異常サンプル2値分類簡略化
提案手法
繊維レイアップ表面デプスマップ各コンポジットストリップ（タウ）合分割小ウィンドウ使用
異常一部ウィンドウ
オートエンコーダ渡入力再構築
通常サンプルトレーニング
サンプル対正確再構築行
再構築エラー値潜在的異常定量的評価指標使用
値組合異常マップ生成
デプスマップ製造欠陥位置特定
結果
オートエンコーダ非常限スキャン数トレーニング
提案手法十分2値分類精度生出
欠陥位置特定示
```
In this way, you can use this script to process Japanese text. For more details, please refer to the comments in the source code.


# 日本語テキストのカタカナとひらがなの除去と英語翻訳

## 概要

このPythonスクリプトは、与えられた日本語テキストからカタカナとひらがなを除去し、必要に応じてカタカナの塊を英語に翻訳するツールです。

## 依存関係

以下の依存関係をインストールしてください：

- googletrans==4.0.0-rc1

インストール方法：

```
pip install googletrans==4.0.0-rc1
```


## 使用方法

```
python pseudo_chinese_summariser.py input_file.txt output_file.txt [-k] [-e]
```

- `your_script.py`: プログラムのファイル名
- `input_file.txt`: 入力ファイルのパス（翻訳対象の日本語テキストが含まれているファイル）
- `output_file.txt`: 出力ファイルのパス（処理後のテキストを保存するファイル）

オプション：

- `-k`, `--withoutkatakana`: カタカナを削除する場合に指定します。このオプションを指定すると、カタカナを含むテキストも除去され、英語への翻訳も行われません。
- `-e`, `--withouten`: 英語への翻訳を行わない場合に指定します。このオプションを指定すると、日本語テキストのカタカナを英語に翻訳しません。
  - `-k` を使用した場合は、カタカナの削除が優先されます。

注意：このスクリプトは、Google Cloud Translation APIを使用しているため、インターネット接続が必要です。APIの使用制限により、大量のテキストを処理する場合は注意してください。
また、Google翻訳の制限に依存し、いつでも利用可能とは限りません。

## 使用例

例えば、`input_file.txt` に以下のような日本語テキストが含まれているとします：

```input_file.txt
自動繊維配置（AFP）の欠陥検出システムは、豊富なラベル付きの不良サンプルが必要なエンドツーエンドの教師あり学習法に基づいていますが、これらは十分な数を簡単に生成することができません。そこで、データ不足の問題に対処するため、小規模データセットに適したオートエンコーダベースの手法を提案します。基盤的な観点から見れば、問題は正常サンプルと異常サンプルの2値分類として簡略化できます。提案手法では、繊維レイアップ表面のデプスマップを各コンポジットストリップ（タウ）に合わせて分割した小さなウィンドウを使用します。異常がない一部のウィンドウは、オートエンコーダに渡されて入力を再構築し、通常サンプルでトレーニングされているため、これらのサンプルに対してより正確な再構築が行われます。したがって、再構築エラーの値は潜在的な異常があるかどうかの定量的な評価指標として使用されます。これらの値は組み合わせて異常マップを生成し、デプスマップでの製造欠陥の位置を特定できます。結果は、オートエンコーダが非常に限られたスキャン数でトレーニングされているにもかかわらず、提案手法は十分な2値分類精度を生み出し、欠陥の位置を特定できることを示しています。
```


以下のコマンドを実行すると、ひらがなが除去され、カタカナの英語への翻訳が行われた結果が `output_file.txt` に保存されます：

```
python pseudo_chinese_summariser.py input_file.txt output_file.txt 
```


`output_file.txt` の内容は次のようになります：

```output_file.txt
自動繊維配置（AFP）欠陥検出system
豊富label付不良sample必要End -to -end教師学習法基
十分数簡単生成
data不足問題対処
小規模data適Auto encoder base手法提案
基盤的観点見
問題正常sample異常sample2値分類簡略化
提案手法
繊維Layup表面Depth map各Composite strip（Tau）合分割小window使用
異常一部window
Auto encoder渡入力再構築
通常sampletraining
sample対正確再構築行
再構築error値潜在的異常定量的評価指標使用
値組合異常map生成
Depth map製造欠陥位置特定
結果
Auto encoder非常限scan数training
提案手法十分2値分類精度生出
欠陥位置特定示
```

以上のように、このスクリプトを使って日本語テキストを処理することができます。詳細については、ソースコードのコメントを参照してください。

