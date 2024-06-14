# 여론조사 Raw Data 상관분석
# 정규성 검정을 수행하지만, 리커트 척도여서 pearson 말고 spearman 사용

# 라이브러리 설치
import pandas as pd
import os
from scipy.stats import shapiro

# 경로와 파일명
data_path = 'data'
file_name = 'sample.xlsx'
output_file_name = 'correlation_results.xlsx'

# 파일 경로 생성
full_path = os.path.join(data_path, file_name)
output_full_path = os.path.join(data_path, output_file_name)

# 데이터 불러오기
data = pd.read_excel(full_path)

# 결측치 확인
missing_values = data.isnull().sum()
missing_values = missing_values[missing_values > 0]

# 정규성 검정 함수
def normality_test(data):
    normality_results = {}
    for column in data.columns:
        stat, p = shapiro(data[column])
        normality_results[column] = {'Statistic': stat, 'p-value': p.round(3)}
    return normality_results

# 정규성 검정 수행 후 요약
normality_results = normality_test(data)
normality_df = pd.DataFrame.from_dict(normality_results, orient = 'index').reset_index()
normality_df.columns = ['Variable', 'Statistic', 'p-value']
normality_df['Normal Distribution'] = normality_df['p-value'] > 0.05 # p-value > 0.05이면 정규분포를 따름

# 상관계수 행렬 계산('pearson', 'spearman', 'kendall')
pearson_corr_matrix = data.corr(method = 'pearson')
spearman_corr_matrix = data.corr(method = 'spearman')
kendall_corr_matrix = data.corr(method = 'kendall')

# 출력
## 결측치 출력
if missing_values.empty:
    print("결측값이 없습니다.")
else:
    print(f"결측값이 있는 열과 결측값의 개수: {missing_values}")

print(normality_df) # 정규성 검정 결과
print(pearson_corr_matrix) # pearson 상관계수
print(spearman_corr_matrix) # spearman 상관계수
print(kendall_corr_matrix) # kendall 상관계수

# 엑셀 파일로 저장
with pd.ExcelWriter(output_full_path) as writer:
    normality_df.to_excel(writer, sheet_name = 'Normality Test', index = False)
    pearson_corr_matrix.to_excel(writer, sheet_name = 'Pearson Correlation')
    spearman_corr_matrix.to_excel(writer, sheet_name = 'Spearman Correlation')
    kendall_corr_matrix.to_excel(writer, sheet_name = 'Kendall Correlation')

print(f'Results have been saved to {output_full_path}')