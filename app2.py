import streamlit as st
import pandas as pd
from app2_home import run_app_home
from app2_eda import County
from app2_ml import run_app_ml
from app2_ml2 import run_app_ml2
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io
from matplotlib import font_manager, rc




def main():
    with st.sidebar:
        choose = option_menu("메뉴", ["Home", "국가 정보 검색", "자료 처리과정" ,"국가정보 분석"],
                            icons=['house', 'bi bi-globe-asia-australia','bi bi-card-text', 'bi bi-globe'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "red", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )
    menu = ['Home', '국가 정보 검색', '자료 처리과정', '국가정보 분석']
    if choose == menu[0]:
        run_app_home()
    elif choose == menu[1]:
        County()
    elif choose == menu[2]:
        run_app_ml2()
    else :
        run_app_ml()
if __name__ == '__main__':
    main()
