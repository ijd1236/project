import streamlit as st


def run_app_home():
    
    st.subheader('환영합니다')
    st.markdown('<span style="font-size: 24px;">국가 정보확인, 사이버 지수 분석 앱입니다.</span>', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 24px;">국가의 정보를 확인하고, 사이버 지수를 분석할 수 있습니다.</span>', unsafe_allow_html=True)
    st.image('https://cdn.itbiznews.com/news/photo/202211/83255_78807_502.jpg')