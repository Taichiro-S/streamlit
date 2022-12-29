import streamlit as st
import numpy as np
import pandas as pd

# タイトルの表示
st.title('Streamlit 超入門')

# 文字の追加
st.write('DataFrame')

# 適当な表
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

# 表の表示
# ソートができるインタラクティブな表
st.write(df)

# 表の大きさを変えられる
# ほかにもいろいろな加工が可能
st.dataframe(df.style.highlight_max(axis=0), width = 1000, height = 1000)

# ソートなどができないstaticな表
st.table(df.style.highlight_max(axis=0))

# 詳しくはhttps://docs.streamlit.io/library/api-reference


# マークダウン記法

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


#乱数を20行３列の表にしたもの(列名a,b,c)
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)

#この表を折れ線グラフに
st.line_chart(df)

#この表を折れ線グラフに(中身を塗りつぶす)
st.area_chart(df)

# 棒グラフ
st.bar_chart(df)

# 詳しくはhttps://docs.streamlit.io/library/api-reference/charts


#東京新宿付近の緯度と経度の組100個を表にしたもの
df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

#地図上に場所をマッピング
st.map(df)


#画像の表示
from PIL import Image

st.write('Display Image')
img = Image.open('hinano.webp')
st.image(img, caption='Hinano chan', use_column_width=True)

