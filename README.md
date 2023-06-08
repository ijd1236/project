# 앱 대시보드 개발 프로젝트

1. 데이터를 탐색한후, 데이터를 선택
2. 무엇을 분석할지 기획
3. 코랩에서 데이터 분석
4. 인공지능 개발이 가능한 데이터면, 데이터가공/학습
5. 앱 대시보드의 화면 기획
6. 개발해서 ec2에 적용
7. 깃허브 리드미 작성

http://3.38.179.112:8601/

![image](https://github.com/ijd1236/project/assets/130967884/ffb86be5-5aa4-46cb-8731-dc896805e3f4)

## 앱 정보

- 국가 정보를 확인하고
- 국가 정보를 분석하는 웹 대시보드입니다.
- 데이터 출처는 Kaggle( https://www.kaggle.com/) 에서 공유한 (https://www.kaggle.com/datasets/katerynameleshenko/cyber-security-indexes) 와 (https://www.kaggle.com/datasets/darshanprabhu09/countries-economy-gdp-and-everything) 이 두개의 데이터 합친 데이터 입니다.

## 국가 정보 검색

- 데이터의 County 열의 행 정보로 국가 이름을 입력받고
- requests 라이브러리를 사용해서
- https://restcountries.com/v2/name/(국가이름) 사이트에서 해당 국가의 정보를 웹 대시보드에 출력하도록 합니다.
![image](https://github.com/ijd1236/project/assets/130967884/c3c4086d-c1ba-481e-8ab7-6063a9487a8a)


## 자료 처리과정

- 두개의 자료를 하나로 합치고
- 데이터의 결측치를 처리합니다.
![image](https://github.com/ijd1236/project/assets/130967884/e9fb82eb-9da0-4d5b-ad32-30297f2cea79)
![image](https://github.com/ijd1236/project/assets/130967884/17ae8d21-2c7b-4f12-b6c8-e6b277cf5843)



## 국가정보 분석

- 자료 처리과정에서 정리한 데이터를 토대로 분석을 실행합니다.
- GDP, 인구, 영토가 가장 높고, 낮은 국가를 볼 수 있게 합니다.
![image](https://github.com/ijd1236/project/assets/130967884/a17792b5-ec02-47bf-9bf3-e3954b2b0fe9)
![image](https://github.com/ijd1236/project/assets/130967884/03019ec4-67e9-458e-9aad-65b7e1b2a0e1)

- 국가의 발전 수준을 나타내는 지표는 GDP와 DDL(디지털 개발 지수) 가 중요할것으로 보여 
- 각 지역의 GDP, DDL 평균을 막대 그래프로 시각화 하여 나타냅니다.
![image](https://github.com/ijd1236/project/assets/130967884/eddd4b72-4bf6-448e-80ac-aca150c5edb7)

- 열을 선택하여 히트맵으로 각 열간의 상관관계를 볼 수 있게 하고
- 전체 히트맵도 볼 수 있게합니다.
![image](https://github.com/ijd1236/project/assets/130967884/ef341206-6d04-426d-afae-5a892d3b6088)

- 히트맵으로 분석결과 상관관계 분석 결과 서로 밀접한 상관관계가 있는 요소는 'GDP', 'GCI', 'CEI', 'DDL', '폰 보급률'으로 나왔습니다
- 이중 CEI(사이버 노출지수)는 다른 요소들과 달리 양의 상관관계를 보여 CEI를 제외한 요소들과 가장 높은 양의 상관관계를 보이는 GDP, GCI와의 관계를 산점도로 나타냅니다.
![image](https://github.com/ijd1236/project/assets/130967884/a6178400-0ebc-4155-b41a-917424ec6bc4)

- 국가의 발전 수준을 나타내는 지표는 GDP와 DDL(디지털 개발 지수) 가 중요할것으로 보이고 이들이 높을 수록 CEI는 낮은 경향을 보이므로
- 마지막으로 GDP, DDP가 높으면서  CEI가 낮은순으로 데이터를 정렬하고 Rank열에 그 순서대로 순위를 매겨
- 국가의 순위를 검색하면 그 DDL, GCI가 추가된 국가 정보를 표기하도록 합니다.

![image](https://github.com/ijd1236/project/assets/130967884/65cb25c7-c543-4d9e-bd53-144fd64ec14c)







