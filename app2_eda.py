import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim


# df = pd.read_csv('data/Cyber_security.csv')
# df2 = pd.read_csv('data/countries-of-the-world.csv')
# df2 = df2.drop('Region', axis=1)

# df['Country'] = df['Country'].str.strip()
# df2['Country'] = df2['Country'].str.strip()

# df['Country'] = df['Country'].str.upper()
# df2['Country'] = df2['Country'].str.upper()

# df['Country'] = df['Country'].replace('United States', 'USA')
# df2['Country'] = df2['Country'].replace('United States', 'USA')
# df3 = pd.merge(df, df2, on = 'Country', how='left')
# df3 = df3.drop('Agriculture', axis=1)
# df3.rename(columns={'Population':'인구', 'Pop. Density (per sq. mi.)': '면적당 인구밀도', 'Area (sq. mi.)' : '국가 면적(mi)','GDP ($ per capita)': 'GDP',  'Phones (per 1000)':'폰 보급률', 'Birthrate':'출생', 'Deathrate' : '사망'})

df3 = pd.read_csv('data/df3.csv', index_col=0)




df3.loc[df3['Country'] == 'United States', 'Country'] = 'Usa'


import streamlit as st
import requests


def get_country_info(country_name):
    url = f"https://restcountries.com/v2/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
    return None
# def get_country_info2(max_country):
#     url = f"https://restcountries.com/v2/name/{max_country}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         if isinstance(data, list) and len(data) > 0:
#             return data[0]
#     return None

def County():
    st.text("해당 정보는 https://restcountries.com/v2, kaggle의 countries-of-the-world의 GDP 데이터를 사용했습니다.")
    st.title("국가 정보 검색")
    st.subheader("국가 전체 정보")
    country_name = st.selectbox("국가 이름을 입력하세요", df3['Country'])
    if st.button("검색"):
        country_info = get_country_info(country_name)
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
            gdp_value = df3.loc[df3['Country'] == country_name, 'GDP'].values[0]
            st.write(f"1인당 GDP: {int(gdp_value)}$")
            languages = country_info.get('languages', [])
            if languages:
                languages_str = ', '.join(str(lang['name']) for lang in languages)
                st.write(f"언어: {languages_str}")
            else:
                st.write("언어: 정보 없음")
        else:
            st.write("국가 정보를 찾을 수 없습니다.")
    # max_row = df3.loc[df3['GDP'].idxmax()]
    # max_country = max_row['Country']
    # max_min = df3.loc[df3['GDP'].idxmin()]
    # min_country = max_min['Country']
    # if st.button("GDP가 가장 높은 국가와 가장 낮은 국가"):
    #     st.subheader("GDP가 가장 높은 국가")
    #     st.write(f"국가명: {max_country}")
    #     st.write(f"GDP: {df3['GDP'].max()}$")
    #     country_info2 = get_country_info2(max_country)
    #     if country_info2 is not None and isinstance(country_info2, dict):
    #         st.write("국기 이미지:")
    #         flag_url = country_info2.get('flags', {}).get('png', '')
    #         if flag_url:
    #             response = requests.get(flag_url)
    #             if response.status_code == 200:
    #                 flag_image = Image.open(BytesIO(response.content))
    #                 st.image(flag_image, use_column_width=True)
    #             else:
    #                 st.write("국기 이미지를 가져올 수 없습니다.")
    #         else:
    #             st.write("국기 이미지를 찾을 수 없습니다.")
    #     st.subheader("GDP가 가장 낮은 국가")
    #     st.write(f"국가명: {min_country}")
    #     st.write(f"GDP: {df3['GDP'].min()}$")
    #     country_info3 = get_country_info2(min_country)
    #     if country_info2 is not None and isinstance(country_info3, dict):
    #         st.write("국기 이미지:")
    #         flag_url = country_info3.get('flags', {}).get('png', '')
    #         if flag_url:
    #             response = requests.get(flag_url)
    #             if response.status_code == 200:
    #                 flag_image = Image.open(BytesIO(response.content))
    #                 st.image(flag_image, use_column_width=True)
    #             else:
    #                 st.write("국기 이미지를 가져올 수 없습니다.")
    #         else:
    #             st.write("국기 이미지를 찾을 수 없습니다.")
    
    # max = df3.loc[df3['인구'].idxmax()]
    # max_p = max['Country']
    # min = df3.loc[df3['인구'].idxmin()]
    # min_p = min['Country']
    # if st.button("인구가 가장 많은 국가와 가장 적은 국가"):
    #     country_info4 = get_country_info2(max_p)
    #     st.subheader("인구가 가장 많은 국가")
    #     st.write(f"국가명: {max_p}")
    #     st.write(f"인구: {country_info4.get('population', '')}")
    #     if country_info4 is not None and isinstance(country_info4, dict):
    #         st.write("국기 이미지:")
    #         flag_url = country_info4.get('flags', {}).get('png', '')
    #         if flag_url:
    #             response = requests.get(flag_url)
    #             if response.status_code == 200:
    #                 flag_image = Image.open(BytesIO(response.content))
    #                 st.image(flag_image, use_column_width=True)
    #             else:
    #                 st.write("국기 이미지를 가져올 수 없습니다.")
    #         else:
    #             st.write("국기 이미지를 찾을 수 없습니다.")
    #     country_info5 = get_country_info2(min_p)
    #     st.subheader("인구가 적은 많은 국가")
    #     st.write(f"국가명: {min_p}")
    #     st.write(f"인구: {country_info5.get('population', '')}")
    #     if country_info5 is not None and isinstance(country_info5, dict):
    #         st.write("국기 이미지:")
    #         flag_url = country_info5.get('flags', {}).get('png', '')
    #         if flag_url:
    #             response = requests.get(flag_url)
    #             if response.status_code == 200:
    #                 flag_image = Image.open(BytesIO(response.content))
    #                 st.image(flag_image, use_column_width=True)
    #             else:
    #                 st.write("국기 이미지를 가져올 수 없습니다.")
    #         else:
    #             st.write("국기 이미지를 찾을 수 없습니다.")
    # max2 = df3.loc[df3['국가 면적(mi)'].idxmax()]
    # max_map = max2['Country']
    # min2 = df3.loc[df3['국가 면적(mi)'].idxmin()]
    # min_map = min2['Country']
    # country_info6 = get_country_info2(max_map)
    # country_info7 = get_country_info2(min_map)
    # if st.button("가장 영토가 큰 국가와 작은 국가"):
    #     st.subheader("영토가 가장 큰 국가")
    #     st.write(f"국가명: {max_map}")
    #     st.write(f"면적: {country_info6.get('area', '')} km²")
    #     if country_info6 is not None and isinstance(country_info6, dict):
    #         st.write("국기 이미지:")
    #         flag_url = country_info6.get('flags', {}).get('png', '')
    #         if flag_url:
    #             response = requests.get(flag_url)
    #             if response.status_code == 200:
    #                 flag_image = Image.open(BytesIO(response.content))
    #                 st.image(flag_image, use_column_width=True)
    #             else:
    #                 st.write("국기 이미지를 가져올 수 없습니다.")
    #         else:
    #             st.write("국기 이미지를 찾을 수 없습니다.")
    #     st.subheader("영토가 작은 국가")
    #     st.write(f"국가명: {min_map}")
    #     st.write(f"면적: {country_info7.get('area', '')} km²")
    #     if country_info7 is not None and isinstance(country_info7, dict):
    #         st.write("국기 이미지:")
    #         flag_url = country_info7.get('flags', {}).get('png', '')
    #         if flag_url:
    #             response = requests.get(flag_url)
    #             if response.status_code == 200:
    #                 flag_image = Image.open(BytesIO(response.content))
    #                 st.image(flag_image, use_column_width=True)
    #             else:
    #                 st.write("국기 이미지를 가져올 수 없습니다.")
    #         else:
    #             st.write("국기 이미지를 찾을 수 없습니다.")