import streamlit as st


def run_app_home():
    st.subheader('환영합니다')
    st.markdown('<span style="font-size: 24px;">복용 약물 분석 앱입니다</span>', unsafe_allow_html=True)
    st.markdown('<span style="font-size: 21px;">데이터 분석도 가능하고, 고객 정보를 넣으면 복용할 약물도 예측해줍니다.</span>', unsafe_allow_html=True)
    st.image('https://cdn.crowdpic.net/detail-thumb/thumb_d_D4D3EB91A5D95F732027B622EE30E61D.jpg')
    st.write('해당 데이터는 kaggle의 (https://www.kaggle.com/datasets/prathamtripathi/drug-classification) 에서 가져왔습니다')