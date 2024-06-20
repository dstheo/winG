# 여론조사 응답 정성 데이터 전처리

# 라이브러리 설치
import pandas as pd
import konlpy
import json
import os

# 경로와 파일명
data_path = 'data'
file_name = 'nlp_sample.xlsx'

# 파일 경로 생성
full_path = os.path.join(data_path, file_name)

# 데이터 불러오기
data = pd.read_excel(full_path)

# 정성 데이터 열 이름 지정
column = 'Q1'

# 정규표현식으로 데이터 편집
data[column] = data[column].str.replace('[^가-힣]', ' ', regex = True)

# NaN 값을 빈 문자열로 대체
data[column] = data[column].fillna('')

# 데이터 문자열로 변환
data[column] = data[column].astype(str)

# 명사 추출
kkma = konlpy.tag.Kkma() # 형태소 분석기 꼬꼬마(Kkma)
nouns = data[column].apply(kkma.nouns)

# 단어 데이터프레임 만들기
nouns = nouns.explode()

# 글자수 2개 이상
data_word = pd.DataFrame({'word': nouns})
data_word['count'] = data_word['word'].str.len()
data_word = data_word.query('count >= 2')

# 단어별 그룹핑 및 내림차순 정렬
data_word = data_word.groupby('word', as_index = False).count().sort_values('count', ascending = False)

# 딕셔너리 생성
dic_word = data_word.set_index('word').to_dict()['count']

# 엑셀 저장
data_word.to_excel('단어빈도.xlsx', index = False)

# 텍스트 파일로 저장
with open('워드클라우드.txt', 'w', encoding = 'utf-8') as file:
    for key, value in dic_word.items():
        file.write(f'{key}: {value}\n')