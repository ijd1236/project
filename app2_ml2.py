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
import streamlit as st
import requests



df3 = pd.read_csv('data/df3.csv', index_col=0)
# df3 = df3.dropna()
# df3 = df3.reset_index(drop=True)

df3['면적당 인구밀도'] = df3['면적당 인구밀도'].str.replace(',', '').astype(float)
df3['출생'] = df3['출생'].str.replace(',', '').astype(float)
df3['사망'] = df3['사망'].str.replace(',', '').astype(float)
df3['폰 보급률'] = df3['폰 보급률'].str.replace(',', '').astype(float)
df = pd.read_csv('data/Cyber_security.csv')
df
df2 = pd.read_csv('data/countries-of-the-world.csv')
df2 = df2.drop('Region', axis=1)
df2 = df2.drop('Agriculture', axis=1)
df = df.drop('NCSI', axis=1)

def run_app_ml2():
    st.subheader('두개의 데이터')
    st.dataframe(df)
    st.text('CEI = 사이버 보안 노출지수, GCI= 글로벌 사이버 보안지수 , DDL = 디지털 개발수준')
    st.text('192 rows × 6 columns')
    st.dataframe(df2)
    st.text('Population =인구 Area (sq. mi.) =면적	Pop. Density (per sq. mi.) = 면적당 인구밀도 Phones (per 1000) = 폰 보급률')
    st.text('227 rows × 8 columns')
    st.subheader('국가(County)를 기준으로 데이터를 합칩니다. 합치는 과정에서 이름 통일을 위해 국가 이름을 대문자로 바꿉니다')
    st.dataframe(df3)
    st.text('192 rows × 12 columns')
    st.text('Population, Area (sq. mi.) ,Pop. Density (per sq. mi.) , Phones (per 1000) Birthrate, Deathrate 열은 순서대로 인구, 국가면적(mi), 면적당 인구밀도, 폰보급률, 출생, 사망으로 바꾸었습니다.')
    st.subheader('분석의 정확도를 위해 결측치를 삭제합니다')
    a3 = df3.dropna()
    a3 = a3.reset_index(drop=True)
    st.dataframe(a3)
    st.text('97 rows × 12 columns')
    

