import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


def run_app_ml():
    st.subheader('복용할 약물 예측')

    # 성별, 나이, 연봉, 카드빚, 자산을
    # 유저한테 입력받는다.


    # 버튼을 누르면 예측한 금액을 표시한다.
    age = st.number_input('나이 입력', 18, 100)

    gender = st.selectbox('성별선택', ['남자', ' 여자'])
    if gender == '남자'  : 
        gender = 1
    else : 
        gender = 0

    bp =st.selectbox('혈압 입력', ['높음', '낮음', '보통'])
    if bp == '높음':
        bp = 0
    elif bp == '낮음':
        bp = 1
    else:
        bp = 2
    


    cs = st.selectbox('콜레스테롤 입력', ['높음', '보통'])
    if cs == '높음':
        cs = 0
    else : 
        cs = 1

    nk = st.number_input('혈중 나트륨, 칼륨 비율 입력', step=0.1)

    if st.button('복용할 약물 예측'):

        new_data =np.array([gender, age, bp, cs, nk])
        new_data =new_data.reshape(1, 5)

        regressor=joblib.load('data/regressor.pkl')

        y_pred =regressor.predict(new_data)
        cap = 0
        if int(y_pred) == 0:
            cap = 'drugA'
        elif int(y_pred) == 1:
            cap = 'drugC'
        elif int(y_pred) == 2:
            cap = 'drugB'
        elif int(y_pred) == 3:
            cap = 'drugX'
        else :
           cap = 'DrugY'                
        print(y_pred)
        st.text(f'{str(cap)} 약을 복용합니다. ')
