# 여론조사 Raw Data 2개 열 상관분석

# 라이브러리 설치
import pandas as pd
import numpy as np
import scipy.stats as stats
import os

# 경로와 파일명
data_path = 'data'
file_name = 'sample.xlsx'

# 파일 경로 생성
full_path = os.path.join(data_path, file_name)

# 데이터 불러오기
data = pd.read_excel(full_path)

# 두 개 열 선택
column1 = 'Q1'
column2 = 'Q2'

# 공분산 계산
covariance = np.cov(data[column1], data[column2])[0, 1]

# 피어슨 상관계수, p-value 계산
pearson_corr, pearson_p = stats.pearsonr(data[column1], data[column2])

# 스피어만 상관계수, p-value 계산
spearman_corr, spearman_p = stats.spearmanr(data[column1], data[column2])

# 켄달 순위 상관계수, p-value 계산
kendall_corr, kendall_p = stats.kendalltau(data[column1], data[column2])

# 출력
print(f"공분산 (Covariance): {covariance}")
print(f"피어슨 상관계수 (Pearson correlation): {pearson_corr:.3f}, p-value: {pearson_p:.3f}")
print(f"스피어만 상관계수 (Spearman correlation): {spearman_corr:.3f}, p-value: {spearman_p:.3f}")
print(f"켄달 상관계수 (Kendall correlation): {kendall_corr:.3f}, p-value: {kendall_p:.3f}")