import streamlit as st
import os 
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image #이미지 처리하는 라이브러리
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

import streamlit as st



df = pd.read_csv('data/drug200.csv')

def run_app_eda():
    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df)
        st.text('Age = 나이, Sex = 성별, BP = 혈압, Cholesterol = 콜레스테롤, Na_to_K = 혈중 나트륨 대 칼륨 비율, Drug = 복용 약물')
    else:
       pass
    st.subheader('혈중 나트륨 칼륨 비율이 가장 높은사람')
    st.dataframe(df.loc[df['Na_to_K'].max() == df['Na_to_K'],])
    st.subheader('혈중 나트륨 칼륨 비율이 가장 낮은 사람')
    st.dataframe(df.loc[df['Na_to_K'].min() == df['Na_to_K'],])
    st.subheader('종류별 약 복용 비율')
    fig = plt.figure(figsize = (6,3),dpi = 200)
    sns.countplot(data = df , x = 'Drug')

    st.pyplot(fig)

    data = df.columns[0:5]
    st.subheader('산점도로 선택한 조건에 따른 약물 분포 보기')
    choice_list = st.multiselect('두가지 조건을 선택하세요',data )        
    if len(choice_list) == 2 :  
        fig2=plt.figure(figsize = (9,4))
        sns.scatterplot(data = df , x = choice_list[0] , y = choice_list[1],hue = 'Drug')
        st.pyplot(fig2)

    st.subheader('조건별 상관 관계 분석')
    column_list =st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.',data)
    if len(column_list) >= 2 :
        label_encoder = LabelEncoder()
        df['Sex'] = label_encoder.fit_transform( df['Sex'] )
        df['BP'] = label_encoder.fit_transform( df['BP'] )
        df['Cholesterol'] = label_encoder.fit_transform( df['Cholesterol'] )
        fig3 = plt.figure()
        sns.heatmap(data=df[column_list].corr(), annot =True, vmin=-1, vmax = 1, cmap='coolwarm', fmt='.2f', linewidths= 0.5)
        st.pyplot(fig3)
        st.text('성별 = 여자0 ,남자1, 혈압 = 높음0, 낮음1, 중간2, 콜레스테롤 = 높음0 중간1 ')

