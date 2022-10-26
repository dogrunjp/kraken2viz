# kraken2viz

Kraken2vizはKraken2のレポートファイルをDataFrameに変換し、
解析・可視化までの処理を自動化するツールです。

Jupyter notebook内での利用、あるいはコマンドラインでの画像出力に利用することを想定しています。

## Kraken2のレポートファイルについて

Kraken2の二種類のレポートのうち "tab-delimited with one line per taxon"な標準形式のファイルを利用する

## 利用例

### ライブラリのインストール

```
$ cd kraken2viz  # kraken2vizローカルレポジトリのsetup.pyと同じレベルのに移動する
$ pyenv local hoge # Jupyter notebook（あるいはPythonの対話モード）で利用する仮想環境を起動する
$ pip install -e . # setup.pyに記述された設定で仮想環境にkraken2vizがインストールされる

```

### 出力

```
$ python  # pythonから対話環境に入る・もしくはJupyter notebookを開く
```

#### レポートファイルをそのまま可視化する
``` Python
from kraken2viz import plot, convert
df = convert.plotly_df("Kraken2のレポートファイル")
plot.plotly_summary(df)
```

#### 複数サンプルをStacked Barplotとして可視化する

```Python
from kraken2viz import plot, convert
df = convert.plotly_dfs(["レポートファイル#1", "レポートファイル#２"])
plot.plotly_bars(df)

```


## 実装予定・実装したい機能
- コマンドラインでの出力
- png書き出し（CLで処理する用）
- 描画するランク指定
- colorスケール指定
- 可視化用にフォーマットしたDataFrameのCSVファイルへの書き出し機能
- Percentage以外の値の利用
