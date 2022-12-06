#　12.プログレスバーの表示

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# タイトルの表示
st.title('Streamlit 超入門')
st.write('プログレスバーの表示')

'Start!!'
time.sleep(1)

#プログレスバー
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
time.sleep(1)
'Done!!!!!'

#エキスパンダー
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1に対する回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2に対する回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3に対する回答')