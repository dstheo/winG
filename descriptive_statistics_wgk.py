# 여론조사 Raw Data 기술 통계 분석

# 라이브러리 설치
import pandas as pd
import os

# 경로와 파일명
data_path = 'data'
file_name = 'sample.xlsx'

# 파일 경로 생성
full_path = os.path.join(data_path, file_name)

# 데이터 불러오기
data = pd.read_excel(full_path)

# 결측치 확인
missing_values = data.isnull().sum()
missing_values = missing_values[missing_values > 0]

# 기술 통계량 계산
descriptive_stats = data.describe()
descriptive_stats.loc['median'] = data.median()
descriptive_stats.loc['mode'] = data.mode().iloc[0]

# 출력
## 결측값 출력
if missing_values.empty:
    print("결측값이 없습니다.")
else:
    print(f"결측값이 있는 열과 결측값의 개수: {missing_values}")

## 기술 통계량 출력
print(descriptive_stats.round(3))