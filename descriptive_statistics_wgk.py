# 여론조사 로우 데이터의 기술 통계량 분석, 분포 확인

# 라이브러리 설치
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# 경로와 파일명
data_path = 'data'
file_name = 'testdata.xlsx'

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

# 히스토그램 서브플롯 크기 설정
numeric_columns = data.select_dtypes(include = 'number').columns
num_columns = len(numeric_columns)
num_rows = (num_columns + 3) // 4

fig, axes = plt.subplots(num_rows, 4, figsize = (20, num_rows * 5))

# 출력
## 결측값 출력
if missing_values.empty:
    print("결측값이 없습니다.")
else:
    print(f"결측값이 있는 열과 결측값의 개수: {missing_values}")

## 기술 통계량 출력
print(descriptive_stats.round(3))

## 히스토그램 출력
for i, column in enumerate(numeric_columns):
    ax = axes[i // 4, i % 4]
    data[column].hist(
        bins = 30,
        ax = ax,
        color = 'darkblue'
        )
    
    ax.set_title(f'Histogram of {column}')
    ax.yaxis.set_major_locator(MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(plt.MultipleLocator(200))

### 빈 서브플롯 제거
for j in range(i + 1, num_rows * 4):
    fig.delaxes(axes[j // 4, j % 4])

### 제목 설정
fig.suptitle('Histograms of All Numeric Columns', fontsize = 16)

plt.subplots_adjust(
    hspace = 0.6,
    wspace = 0.4,
    top = 0.9,
    bottom = 0.1
    )
plt.show()