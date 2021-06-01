import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.beta_columns(2)

button = left_column.button('ボタン')

if button:
    right_column.write('右からむだよ')

expander = st.beta_expander('質問１')
expander.write('回答１')
expander = st.beta_expander('質問２')
expander.write('回答２')
expander = st.beta_expander('質問３')
expander.write('回答３')