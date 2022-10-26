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
    # レコード数が多すぎると処理しきれないため、Percentageを指定しデータを丸めるオプションを実装する
    # defautl Trueで 0.00%であればレコードを省く
    # 閾値は設定できるようにする

    df_tmp = pd.read_csv(file, sep='\t', header=None)
    # rankがRに当たる行をヘッダとする
    header = df_tmp[df_tmp.iloc[:,3]=="R"]
    df_tmp.rename(columns=header.iloc[0],inplace=True)
    # Scientific name, Tax ID, Rankに当たる行をマルチインデックスとする
    df = df_tmp.set_index(["root", 1, "R"])
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
