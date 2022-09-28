import pandas as pd
import argparse

config = dict()


def parse_args(args:list):
    """
    CLおよび他のモジュールからの呼び出しの両者に対応するため
    parseargを関数内で処理する
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='specify the path of kraken2 reoport file', required=False)
    return parser.parse_args(args)


def set_config():
    """
    parsearg関数をよびconfigに設定値を追加する
    :return:
    """
    args = parse_args(sys.argv[1:])
    global config
    config["d"] = args.d


def fromat_df(file_path:str):
    """
    Kraken2レポートファイルを
    plotly表示用に整形したDataFrameに変換する
    :param file_path: Kraken2report file path
    :return: dataframe
    """
    df_tmp = pd.reaad_csv(file_path, sep='\t')
    df = df_tmp.set_index(["root", "1", "R"])
    df.columns = ["Percentage", "Fragments_clade", "Fragments_direct"]
    return df


