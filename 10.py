#　10.インタラクティブなウィジェット

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトルの表示
st.title('Streamlit 超入門')

# チェックボックスにチェックが入った場合のみ画像を表示
if st.checkbox('Show Image'):
    img = Image.open('hinano.webp')
    st.image(img, caption='Hinano chan', use_column_width=True)

# 表示させる値を選べるようになる
option1 = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)
'あなたが好きな数字は', option1, 'です。'

option2 = st.text_input('あなたの趣味を教えてください')
'あなたの趣味は', option2, 'です。'

condition = st.slider('あなたの今の調子は？', 0,100,50)
'あなたの今の調子は' , condition

#詳細はhttps://docs.streamlit.io/library/api-reference/widgets