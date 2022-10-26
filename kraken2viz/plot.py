import plotly.express as px
from kraken2viz import convert
import argparse
import sys, os

# Todo: plotのx,y軸を設定にする


def plotly_summary(df):
    """
    Kraken2の標準レポートをそのままTaxonomyランクごとBarchartにプロットする
    :param df:
    :return:
    """
    # Todo: 行が長すぎるケースがあるため、オプションでタイムアウトなどの処理を入れる
    df4 = df.reset_index()
    fig = px.bar(df4, x="R", y="Percentage", color="root")
    fig.show()
    #fig.write_image("testtest_kraken2viz.png")


def plotly_bars(df):
    """
    複数のサンプルから得たKraken2の標準レポートをPlotlyのStacked barchartとして描画する
    :param df: サンプルごとに生成したDataFrameをconcat%整形したDataFrame
    :return:
    """
    fig = px.bar(df, x="Sample", y="Percentage", color="root")
    fig.show()


def parse_args(args:list):
    """
    CLおよび他のモジュールからの呼び出しの両者に対応するため
    parseargを関数内で処理する
    CLから呼ばれた場合のみconfigにオプションを保存する
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='specify the path of kraken2 reoport file', required=False)
    return parser.parse_args(args)


def set_config() -> dict:
    """
    parsearg関数をよびconfigに設定値を追加する
    :return:
    """
    args = parse_args(sys.argv[1:])
    configs = dict()
    configs["file_path"] = args.f
    return configs


if __name__=="__main__":
    configs = set_config()
    plotly_summary(convert.plotly_df(configs["file_path"]))
