import streamlit as st
import pandas as pd
from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io



df = pd.read_csv('data/drug200.csv')

def main():
    with st.sidebar:
        choose = option_menu("메뉴", ["Home", "EDA", "ML"],
                            icons=['house', 'bi bi-bar-chart-steps', 'bi bi-person-fill'],
                            menu_icon="bi bi-capsule", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )
    menu = ['Home', 'EDA', 'ML']

    if choose == menu[0]:
        run_app_home()
    elif choose == menu[1]:
        run_app_eda()
    else :
        run_app_ml()
if __name__ == '__main__':
    main()
