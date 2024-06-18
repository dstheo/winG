# winGkorea Consulting Workspace

윈지코리아에서 진행한 데이터 전처리, 통계분석 작업 공간입니다. <br/>
회사로 들어오는 Raw Data 기반으로 코딩하였습니다. <br/>
기술 통계량 분석, 상관분석 가능합니다.
<br/>
<br/>

## 1. 설치 방법

### Windows

- 버전 확인
    - Windows 10
    - Python 3.10.11
<br/>

- 원격 저장소 로컬로 다운로드

```
git clone https://github.com/dstheo/winG.git
```
<br/>

- 가상환경 설치 후 접속

```
virtualenv venv
source venv/Scripts/activate
```
<br/>

- 필수 라이브러리 설치

```
pip install -r requirements.txt
```
<br/>

- 주의사항
    - Windows 11, MacOS에서 작업해보지 않음
    - Python 버전이 3.7 이상이고 3.10 이하 (matplotlib 충돌)
    - 모든 라이브러리는 최신 버전 사용함 (24.06.12 기준)
<br/>

## 2. 주요 기능
### descriptive_statistics_wgk.py
- 데이터 불러오기
- 결측치 확인
- 기술 통계량 계산

### correlation_analysis_wgk.py
- 데이터 불러오기
- 결측치 확인
- 정규성 검정
- Pearson, Spearman, Kendall 상관계수 계산
- 분석 내용 엑셀로 저장

### correlation_analysis_heatmap_wgk.py
- 데이터 불러오기
- 상관분석 후 Heatmap 시각화(Pearson, Spearman, Kendall)

### correlation_analysis_2columns_wgk.py
- 데이터 불러오기
- 2개의 열 공분산, Pearson, Spearman, Kendall 상관계수 계산 후 출력

### regression_analysis_wgk.py
- 데이터 불러오기
- X, y 열 지정
- 독립 변수 1개로 회귀분석 후 출력
