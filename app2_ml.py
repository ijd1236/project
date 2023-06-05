import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm



df3 = pd.read_csv('data/df3.csv', index_col=0)

df3['면적당 인구밀도'] = df3['면적당 인구밀도'].str.replace(',', '').astype(float)
df3['출생'] = df3['출생'].str.replace(',', '').astype(float)
df3['사망'] = df3['사망'].str.replace(',', '').astype(float)
df3['폰 보급률'] = df3['폰 보급률'].str.replace(',', '').astype(float)


def run_app_ml():
    st.subheader('사이버 보안지수 분석')
    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df3)
        st.text('CEI = 사이버 보안 노출지수, GCI= 글로벌 사이버 보안지수 , DDL = 디지털 개발수준')
    plt.rcParams['font.family'] = 'Malgun Gothic' #그래프에 한글 출력
    data = df3.columns[2:]
    st.subheader('조건별 상관 관계 분석')
    column_list =st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.',data)
    if len(column_list) >= 2 :
        fig3=plt.figure(figsize=(14, 12))
        sns.heatmap(data=df3[column_list].corr(), annot=True, cmap='coolwarm')
        plt.title('상관관계 히트맵')
        st.pyplot(fig3)
      


