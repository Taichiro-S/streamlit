#　11.レイアウトを整える

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトルの表示
st.title('Streamlit 超入門')

#サイドバー
condition = st.sidebar.slider('あなたの今の調子は？', 0,100,50)
'あなたの今の調子は' , condition

#２カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


#エキスパンダー
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1に対する回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2に対する回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3に対する回答')