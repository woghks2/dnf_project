던전앤파이터 데이터 분석 프로젝트
===

## 프로젝트 개요
- 이 프로젝트는 던전앤파이터 데이터를 수집하고 분석하여 인사이트를 도출합니다.
- 크롤링 및 Open API를 활용하여 다양한 데이터 포인트를 수집하고, 이를 통해 게임의 매출, 리텐션 등의 분석을 수행합니다.

## 데이터 수집
1. **[던전앤파이터 공식 홈페이지](https://df.nexon.com/)**:
   - 웹 크롤링을 통해 데이터를 수집합니다.
2. **[네오플 Open API](https://developers.neople.co.kr/)**:
   - [[Open API 목록]](https://developers.neople.co.kr/contents/apiDocs/df)를 사용하여 실시간 데이터를 수집합니다.

![pipeline](https://github.com/woghks2/dnf_project/blob/master/docs/pipeline.png?raw=true)

## 분석 내용
- **신규 패키지 매출 분석**: 신규 패키지의 매출 추세를 분석합니다.
- **신규 직업 리텐션 분석**: 신규 직업의 플레이어 리텐션율을 분석합니다.

## 설치 및 실행
*  **필수 라이브러리 설치**
   - pip install -r requirements.txt

## 파일 구조
```
projdct
├─ configs : 프로젝트 설정 파일이 포함된 디렉토리입니다.
│     │ 
│     └─ config_ex.py
│ 
├─ data : 데이터 파일이 저장되는 디렉토리입니다.
│    │
│    └─ character_info 
│            └─ character.csv
│            └─ job_name.csv
│    │
│    └─ crawling_data : 공식 홈페이지에서 크롤링한 데이터를 저장합니다.
│            └─ yyyymmdd
│                   └─ job_name.csv
│
├─ docs : 프로젝트 문서 및 참고 자료를 포함하는 디렉토리입니다.
│
├─ out : 분석 결과 및 레포트가 포함된 Jupyter Notebook 파일이 저장됩니다.
│   └─ project1
│
│   └─ project2
│
├─ scripts : 데이터 크롤링, 수집 및 분석을 수행하는 스크립트가 포함된 디렉토리입니다.
│
├─ src : 프로젝트의 주요 소스 코드가 포함된 디렉토리입니다.
│
└─ test : 테스트 코드 및 유닛 테스트가 포함된 디렉토리입니다.
```

## 분석 레포트
- out/ 디렉토리에는 각 분석 프로젝트의 레포트가 포함된 Jupyter Notebook 파일들이 있습니다.
- 이 파일들은 분석 과정 및 결과를 상세히 설명하며, 프로젝트의 인사이트를 제공합니다.