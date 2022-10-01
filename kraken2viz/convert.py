import pandas as pd
from typing import List
import re

key_column = "Percentage"


def plotly_df(file: str) -> pd.DataFrame:
    """
    Kraken2レポートファイルを
    plotly表示用に整形したDataFrameに変換する
    :param file: Kraken2report file path
    :return: pd.DataFrame
    """
    df_tmp = pd.read_csv(file, sep='\t')
    # レポートファイルの先頭行の値が固定値と思われるためインデックス名としているが
    # インデックス名は付け替えた方が良いかもしれない
    df = df_tmp.set_index(["root", "1", "R"])
    df.columns = ["Percentage", "Fragments_clade", "Fragments_direct"]
    return df


def plotly_dfs(files:List[str]) -> pd.DataFrame:
    """
    複数サンプルのレポートを読み込みをDataFrameに変換の後concatと整形を行い
    :param files:
    :return: pd.DataFrame
    """
    dfs = list()
    for i, f in enumerate(files):
        sample_name = re.split(r'\/|\.', f)[-2]
        dfs.append(plotly_df(f))
        # サンプル名のカラムを追加
        dfs[i]["Sample"] = sample_name
        if i == 0:
            dfs[i].sort_values(by=key_column, ascending=False, inplace=True)

    dfs_concat = pd.concat(dfs)
    dfs_concat.reset_index(inplace=True)
    dfs_concat_s = dfs_concat[dfs_concat["R"] == "S"]
    dfs_concat_s["root"] = dfs_concat_s["root"].map(lambda x: x.strip())

    return dfs_concat_s


def concat_dfs(dfs: List[pd.DataFrame])-> pd.DataFrame:
    """
    複数のサンプルのDataFrameをplotlyのBarchartに合わせてconcatし整形する
    :return: pd.DataRrame
    """
    pass
