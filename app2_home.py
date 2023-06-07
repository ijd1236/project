import streamlit as st


def run_app_home():
    st.subheader('환영합니다')
    st.markdown('<span style="font-size: 24px;">국가 정보확인, 국가 정보 분석 앱입니다.</span>', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 24px;">국가의 정보를 확인하고, 국가 정보를 분석할 수 있습니다.</span>', unsafe_allow_html=True)
    st.image('https://m.happypuzzle.co.kr/web/product/big/PL/PL1000-1134.jpg', use_column_width=True)
    st.write("데이터 출처는 Kaggle( https://www.kaggle.com/) 에서 공유한 (https://www.kaggle.com/datasets/katerynameleshenko/cyber-security-indexes) 와  (https://www.kaggle.com/datasets/darshanprabhu09/countries-economy-gdp-and-everything) 이 두개의  데이터 합친 데이터 입니다 ")
