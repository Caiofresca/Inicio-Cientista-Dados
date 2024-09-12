import streamlit as st
import numpy as np
import pandas as pd

st.write('Tarefa Módulo 15')

if st.button('Diga Olá'):
    st.write('Olá! Você clicou no botão!')

options = st.multiselect(
    'Quais são suas cores favoritas?',
    ['Verde', 'Amarelo', 'Azul', 'Vermelho'])
st.write('Você selecionou:', options)



dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

x = st.slider('x') # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.title('My first app')

st.write('Here\'s our first attempt at using data to create a table:')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

bar_chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)
st.bar_chart(bar_chart_data)

import time

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'

st.subheader('Raw data')
st.write(df)

