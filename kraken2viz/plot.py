import plotly.express as px


def plotly_summary(df):
    # Percent Stackedの利用例が列指向が多いため天地しないまま扱う
    df4 = df.reset_index()
    fig = px.bar(df4, x="R", y="Percentage", color="root")
    fig.show()
