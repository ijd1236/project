import streamlit as st
import pandas as pd
from app_home import run_app_home
from app2_eda import County
from app_ml import run_app_ml



def main():
    st.title('국가 정보와 사이버 보안 지수 분석 앱')
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0]:
        run_app_home()
    elif choice == menu[1]:
        County()
    else :
        run_app_ml()
if __name__ == '__main__':
    main()
