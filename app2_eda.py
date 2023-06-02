import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim


df = pd.read_csv('data/Cyber_security.csv')
df2 = pd.read_csv('data/countries-of-the-world.csv')
df2 = df2.drop('Region', axis=1)

df['Country'] = df['Country'].str.strip()
df2['Country'] = df2['Country'].str.strip()

df['Country'] = df['Country'].str.upper()
df2['Country'] = df2['Country'].str.upper()

df['Country'] = df['Country'].replace('United States', 'USA')
df2['Country'] = df2['Country'].replace('United States', 'USA')
df3 = pd.merge(df, df2, on = 'Country', how='left')
df3 = df3.drop('Agriculture', axis=1)
df3.rename(columns={'Population':'인구', 'Pop. Density (per sq. mi.)': '면적당 인구밀도', 'Area (sq. mi.)' : '국가 면적(mi)','GDP ($ per capita)': 'GDP',  'Phones (per 1000)':'폰 보급률', 'Birthrate':'출생', 'Deathrate' : '사망'})




df.loc[df['Country'] == 'United States', 'Country'] = 'Usa'


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

def County():
    st.title("국가 정보 검색")
    country_name = st.selectbox("국가 이름을 입력하세요", df3['Country'])
    if st.button("검색"):
        country_info = get_country_info(country_name)
        if country_info is not None and isinstance(country_info, dict):
            st.write(f"국가 이름: {country_info.get('name', '')}")
            st.write(f"수도: {country_info.get('capital', '')}")
            st.write(f"인구: {country_info.get('population', '')}")
            st.write(f"면적: {country_info.get('area', '')} km²")
            st.write(f"1인당 gdp[]")
            languages = country_info.get('languages', [])
            if languages:
                languages_str = ', '.join(str(lang['name']) for lang in languages)
                st.write(f"언어: {languages_str}")
            else:
                st.write("언어: 정보 없음")
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
        else:
            st.write("국가 정보를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
