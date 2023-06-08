import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.geocoders import Nominatim

from matplotlib import font_manager, rc




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
            region_value = df3.loc[df3['Country'] == country_name, 'Region'].values[0] 
            st.write(f"국가 이름: {country_info.get('name', '')}")
            st.write(f"지역 : {int(region_value)}$")
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
