import pandas as pd


def plotly_df(file_path:str):
    """
    Kraken2レポートファイルを
    plotly表示用に整形したDataFrameに変換する
    :param file_path: Kraken2report file path
    :return: dataframe
    """
    df_tmp = pd.read_csv(file_path, sep='\t')
    df = df_tmp.set_index(["root", "1", "R"])
    df.columns = ["Percentage", "Fragments_clade", "Fragments_direct"]
    return df

