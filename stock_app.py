#Jupyter-notebookの必要なコードをコピペ

import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

st.title('株価可視化アプリ')

st.sidebar.write("""
# GAFA株価
こちらは株価可視化ツールです。\n
以下のオプションから表示日数を指定できます。
"""
)

st.sidebar.write("""
## 表示日数選択
"""
)

#日数を範囲指定で選べるようにして、daysに代入

days = st.sidebar.slider('日数',1,50,20)

st.write(f"""
### 過去 ***{days}日間*** のGAFAの株価
"""
)

#毎回データを読み込まなくてもよいようにcacheしておく
@st.cache
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

#以下のコードの実行でエラーが起きたさいに実行するコードをexceptに書く

try:
    st.sidebar.write("""
    ### 株価の範囲指定
    """)

    #株価の範囲を範囲指定で選べるようにして、yminとymaxに代入

    ymin,ymax = st.sidebar.slider(
        "範囲を指定してください",
        0.0, 3500.0, (0.0, 3500.0)
    )

    tickers = {
        'apple': 'AAPL',
        'meta': 'META',
        'google': 'GOOGL',
        'microsoft': 'MSFT',
        'netflix': 'NFLX',
        'amazon': 'AMZN'
    }

    df = get_data(days, tickers)

    #表示する会社名を選択できるようにする
    #第一引数に表示させたいもののリスト
    #第二引数にデフォルトで表示させたいもののリスト
    companies = st.multiselect(
        '会社名を選択してください',
        list(df.index),
        ('google','amazon','meta','apple')
    )

    #ひとつも選択されなかった場合にエラーメッセージをだす

    if not companies:
        st.error('少なくとも一社は選んでください')
    else:
        data = df.loc[companies]
        st.write("### 株価(USD)",data.sort_index())
        #データの整形
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date'])
        data = data.rename(
            columns={'value' : 'Stock Prices(USD)'}
        )

        chart= (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x='Date:T',
                y=alt.Y('Stock Prices(USD):Q', stack=None, scale=alt.Scale(domain=[ymin,ymax])),
                color='Name:N'
            )
        )

        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
        "おっと！なにかエラーが起きているようです"
    )
