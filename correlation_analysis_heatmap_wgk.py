# 여론조사 Raw Data 상관분석 Heatmap

# 라이브러리 설치
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# 경로와 파일명
data_path = 'data'
file_name = 'sample.xlsx'

# 파일 경로 생성
full_path = os.path.join(data_path, file_name)

# 데이터 불러오기
data = pd.read_excel(full_path)

# Heatmap 함수 정의
def plot_correlation_heatmap(correlation_matrix, title, cmap = 'Blues'):
    """
    Description
    ----------------------------------
    상관관계 행렬 시각화 함수

    Parameters
    ----------------------------------
    correlation_matrix: 상관 관계 행렬 (DataFrame)
    title: Heatmap Title (String)
    cmap: colormap name (String, default = 'Blues')
    """
    plt.figure(figsize = (12, 10))
    sns.heatmap(correlation_matrix, annot = True, fmt = '.2f', cmap = cmap, linewidths = 0.5)
    plt.title(title)
    plt.show()

# 상관계수 행렬 계산('pearson', 'spearman', 'kendall')
pearson_corr_matrix = data.corr(method = 'pearson')
spearman_corr_matrix = data.corr(method = 'spearman')
kendall_corr_matrix = data.corr(method = 'kendall')

# 출력
plot_correlation_heatmap(spearman_corr_matrix, 'Spearman Correlation Matrix')