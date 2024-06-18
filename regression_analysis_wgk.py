# 여론조사 Raw Data 단순 선형회귀분석

# 라이브러리 설치
import pandas as pd
import os
import statsmodels.api as sm

# 경로와 파일명
data_path = 'data'
file_name = 'sample.xlsx'

# 파일 경로 생성
full_path = os.path.join(data_path, file_name)

# 데이터 불러오기
data = pd.read_excel(full_path)

# 독립 변수, 종속 변수 설정
X = data['Q1']
y = data['Q2']

# 상수항 추가
X = sm.add_constant(X)

# 회귀 모델 적합
model = sm.OLS(y, X).fit()

# 회귀 결과 출력
model_summary = model.summary()
print(model_summary)