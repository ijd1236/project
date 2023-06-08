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
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'NanumGothic'


def get_country_info(country_name):
    url = f"https://restcountries.com/v2/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
    return None
def get_country_info2(max_country):
    url = f"https://restcountries.com/v2/name/{max_country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
    return None



df3 = pd.read_csv('data/df3.csv', index_col=0)
df3 = df3.dropna()
df3 = df3.reset_index(drop=True)

df3['면적당 인구밀도'] = df3['면적당 인구밀도'].str.replace(',', '').astype(float)
df3['출생'] = df3['출생'].str.replace(',', '').astype(float)
df3['사망'] = df3['사망'].str.replace(',', '').astype(float)
df3['폰 보급률'] = df3['폰 보급률'].str.replace(',', '').astype(float)


def run_app_ml():
    st.subheader('국가 정보 분석')
    if st.checkbox('데이터',  value=True):
        st.dataframe(df3)
        st.text('CEI = 사이버 보안 노출지수, GCI= 글로벌 사이버 보안지수 , DDL = 디지털 개발수준')
        st.text('해당 데이터는 정확도를 위해 결측치를 제거한 데이터 입니다')
    if st.checkbox('데이터 요약 통계',  value=True):
        a=df3.describe()
        st.dataframe(a)

    max_row = df3.loc[df3['GDP'].idxmax()]
    max_country = max_row['Country']
    max_min = df3.loc[df3['GDP'].idxmin()]
    min_country = max_min['Country']
    if st.button("GDP가 가장 높은 국가와 가장 낮은 국가"):
        st.subheader("GDP가 가장 높은 국가")
        st.write(f"국가명: {max_country}")
        st.write(f"GDP: {df3['GDP'].max()}$")
        country_info2 = get_country_info2(max_country)
        if country_info2 is not None and isinstance(country_info2, dict):
            st.write("국기 이미지:")
            flag_url = country_info2.get('flags', {}).get('png', '')
            if flag_url:
                response = requests.get(flag_url)
                if response.status_code == 200:
                    flag_image = Image.open(BytesIO(response.content))
                    st.image(flag_image, use_column_width=True)
                else:
                    st.write("국기 이미지를 가져올 수 없습니다.")
            else:
                st.write("국기 이미지를 찾을 수 없습니다.")
        st.subheader("GDP가 가장 낮은 국가")
        st.write(f"국가명: {min_country}")
        st.write(f"GDP: {df3['GDP'].min()}$")
        country_info3 = get_country_info2(min_country)
        if country_info2 is not None and isinstance(country_info3, dict):
            st.write("국기 이미지:")
            flag_url = country_info3.get('flags', {}).get('png', '')
            if flag_url:
                response = requests.get(flag_url)
                if response.status_code == 200:
                    flag_image = Image.open(BytesIO(response.content))
                    st.image(flag_image, use_column_width=True)
                else:
                    st.write("국기 이미지를 가져올 수 없습니다.")
            else:
                st.write("국기 이미지를 찾을 수 없습니다.")
    
    max = df3.loc[df3['인구'].idxmax()]
    max_p = max['Country']
    min = df3.loc[df3['인구'].idxmin()]
    min_p = min['Country']
    if st.button("인구가 가장 많은 국가와 가장 적은 국가"):
        country_info4 = get_country_info2(max_p)
        st.subheader("인구가 가장 많은 국가")
        st.write(f"국가명: {max_p}")
        st.write(f"인구: {country_info4.get('population', '')}")
        if country_info4 is not None and isinstance(country_info4, dict):
            st.write("국기 이미지:")
            flag_url = country_info4.get('flags', {}).get('png', '')
            if flag_url:
                response = requests.get(flag_url)
                if response.status_code == 200:
                    flag_image = Image.open(BytesIO(response.content))
                    st.image(flag_image, use_column_width=True)
                else:
                    st.write("국기 이미지를 가져올 수 없습니다.")
            else:
                st.write("국기 이미지를 찾을 수 없습니다.")
        country_info5 = get_country_info2(min_p)
        st.subheader("인구가 가장 적은 국가")
        st.write(f"국가명: {min_p}")
        st.write(f"인구: {country_info5.get('population', '')}")
        if country_info5 is not None and isinstance(country_info5, dict):
            st.write("국기 이미지:")
            flag_url = country_info5.get('flags', {}).get('png', '')
            if flag_url:
                response = requests.get(flag_url)
                if response.status_code == 200:
                    flag_image = Image.open(BytesIO(response.content))
                    st.image(flag_image, use_column_width=True)
                else:
                    st.write("국기 이미지를 가져올 수 없습니다.")
            else:
                st.write("국기 이미지를 찾을 수 없습니다.")
    max2 = df3.loc[df3['국가 면적(mi)'].idxmax()]
    max_map = max2['Country']
    min2 = df3.loc[df3['국가 면적(mi)'].idxmin()]
    min_map = min2['Country']
    country_info6 = get_country_info2(max_map)
    country_info7 = get_country_info2(min_map)
    if st.button("가장 영토가 큰 국가와 작은 국가"):
        st.subheader("영토가 가장 큰 국가")
        st.write(f"국가명: {max_map}")
        st.write(f"면적: {country_info6.get('area', '')} km²")
        if country_info6 is not None and isinstance(country_info6, dict):
            st.write("국기 이미지:")
            flag_url = country_info6.get('flags', {}).get('png', '')
            if flag_url:
                response = requests.get(flag_url)
                if response.status_code == 200:
                    flag_image = Image.open(BytesIO(response.content))
                    st.image(flag_image, use_column_width=True)
                else:
                    st.write("국기 이미지를 가져올 수 없습니다.")
            else:
                st.write("국기 이미지를 찾을 수 없습니다.")
        st.subheader("영토가 작은 국가")
        st.write(f"국가명: {min_map}")
        st.write(f"면적: {country_info7.get('area', '')} km²")
        if country_info7 is not None and isinstance(country_info7, dict):
            st.write("국기 이미지:")
            flag_url = country_info7.get('flags', {}).get('png', '')
            if flag_url:
                response = requests.get(flag_url)
                if response.status_code == 200:
                    flag_image = Image.open(BytesIO(response.content))
                    st.image(flag_image, use_column_width=True)
                else:
                    st.write("국기 이미지를 가져올 수 없습니다.")
            else:
                st.write("국기 이미지를 찾을 수 없습니다.")
    if st.checkbox('지역별 DDL,GDP 평균',  value=True):
        mean_GCI = df3.groupby('Region')['DDL'].mean()
        fig, ax = plt.subplots(1, 1)
        ax.set_title('지역별 DDL 평균', size=12)
        ax.bar(mean_GCI.index, mean_GCI.values, color='#FFFF00', alpha=0.8)
        ax.set(ylabel='Values')
        plt.xticks(rotation = 20)
        st.pyplot(fig)
        mean_GDP = df3.groupby('Region')['GDP'].mean()
        fig2, ax2 = plt.subplots(1, 1)
        ax2.set_title('지역별 GDP 평균', size=12)
        ax2.bar(mean_GDP.index, mean_GDP.values, color='#00FF00', alpha=0.8)
        ax2.set(ylabel='Values')
        plt.xticks(rotation = 20)
        st.pyplot(fig2)


    data = df3.columns[2:]
    st.subheader('조건별 상관관계 분석')
    column_list =st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.',data)
    if len(column_list) >= 2 :
        fig3=plt.figure(figsize=(14, 12))
        sns.heatmap(data=df3[column_list].corr(), annot=True, cmap='coolwarm')
        plt.title('상관관계 히트맵')
        st.pyplot(fig3)
    if st.button("전체 상관관계 보기") :
        fig3=plt.figure(figsize=(15, 12))
        sns.heatmap(data = df3.iloc[:, 2:].corr(), annot=True, cmap='coolwarm')
        plt.title('상관관계 히트맵')
        st.pyplot(fig3)
    st.subheader("상관관계 분석 결과 서로 밀접한 상관관계가 있는 요소는 'GDP', 'GCI', 'CEI', 'DDL', '폰 보급률' 입니다 ")
    st.image('data/20230607_160654.png', use_column_width=True)
    st.subheader("다른 요소들과 달리 CEI(사이버보안 노출 지수)는 다른   요소들과 음의 상관관계를 나타내고 있습니다.")
    fig_a = plt.figure()
    plt.scatter(df3['CEI'], df3['GDP'])
    plt.xlabel('CEI')
    plt.ylabel('GDP')
    st.pyplot(fig_a)

    fig_b = plt.figure()
    plt.scatter(df3['CEI'], df3['DDL'])
    plt.xlabel('CEI')
    plt.ylabel('DDL')
    st.pyplot(fig_b)
    st.text("요소들과 가장 높은 상관관계를 보이는 요소'DDL(디지털 개발지수), 'GDP' 와 CEI의 관계를 산점도로 나타낸 자료입니다.")
    good =  df3.sort_values(['GDP',  'GCI', 'CEI'], ascending=[False,True,True])
    good['Rank'] = range(1, len(good) + 1)
    good['Rank'] = good['Rank'].astype(str) + '위'
    st.dataframe(good)
    st.subheader("국가 순위 검색하기")
    st.text("해당 순위는 GDP, DDP가 높으면서  CEI가 낮은순으로 책정되었습니다.")
    number = st.selectbox("원하는 순위를 입력하세요", good['Rank'])
    selected_country = good.loc[good['Rank'] == number, 'Country'].values[0]
    if st.button("검색"):
        country_info = get_country_info(selected_country)
        if country_info is not None and isinstance(country_info, dict):
            st.write("국기 이미지:")
            flag_url = country_info.get('flags', {}).get('png', '')
            if flag_url:
                response = requests.get(flag_url)
                if response.status_code == 200:
                    flag_image = Image.open(BytesIO(response.content))
                    st.image(flag_image, use_column_width=True)
                else:
                    st.write("국기 이미지를 가져올 수 없습니다.")
            else:
                st.write("국기 이미지를 찾을 수 없습니다.")
            st.write(f"국가 이름: {country_info.get('name', '')}")
            st.write(f"수도: {country_info.get('capital', '')}")
            st.write(f"인구: {country_info.get('population', '')}")
            st.write(f"면적: {country_info.get('area', '')} km²")
            gdp_value = good.loc[good['Country'] == selected_country, 'GDP'].values[0]
            GCI_value = good.loc[good['Country'] == selected_country, 'GCI'].values[0]
            DDL_value = good.loc[good['Country'] == selected_country, 'DDL'].values[0]

            st.write(f"1인당 GDP: {int(gdp_value)}$")
            st.write(f"GCI(글로벌 사이버 보안지수): {int(GCI_value)}")
            st.write(f"DDL(디지털 개발수준): {int(DDL_value)}")
            languages = country_info.get('languages', [])
            if languages:
                languages_str = ', '.join(str(lang['name']) for lang in languages)
                st.write(f"언어: {languages_str}")
            else:
                st.write("언어: 정보 없음")
        else:
            st.write("국가 정보를 찾을 수 없습니다.")