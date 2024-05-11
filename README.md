# 던전앤파이터 신규 캐릭터 패키지 매출 분석



### 요약
* 프로젝트 기간
    * 8주 (3/14 ~ 5/9)

* 기술 스택
    * Python : pandas, selenium, matplolib, seaborn
    * MySQL : DB 구축
    * Tableau : 대시보드 제작 및 시각화

* 분석 목적
    * 신규 캐릭터와 성장 지원 이벤트, 관련 패키지를 분석하여 신규 패키지 매출을 분석한다.
    * 유저 풀 별 구매력 분석하여 추후 성장 지원 이벤트와 패키지를 개선한다.

* 분석 내용
  * report.py 참고
---

### 개요
* 아처의 신규 직업 헌터와 비질란테가 출시되었다. 출시된 여러 이벤트와 함께 신규 직업 패키지를 판매중이다.

* 던전앤파이터 유저 수와 신규 캐릭터 수를 알아보고, 이에 따른 육성 구간을 분석한다.
* 또한, 시계열 명성을 통해 유저를 분류하고 이에 따른 플래티넘 타입 패키지 매출과 구매율을 분석한다.
* 이 내용을 토대로 구매력이 높은 구간을 찾아 이벤트 보상과 패키지를 개선하여 매출을 향상시킨다. 

---

### 작업 순서
1. 신규 캐릭터와 관련된 이벤트 분석
2. 던전앤파이터 공식 홈페이지에서 웹크롤링으로 캐릭터들의 데이터 수집한다.
3. 각 유저들이 어떤 캐릭터를 키우는지 파악하기 위해 OPEN API를 통해 모험단을 조사한다.
4. 명성을 통해 퀘스트 클리어률을 파악하고 각 유저 별 신규 캐릭터 행동 유무 파악한다.
5. 액티브 유저의 패키지 구매 유무를 OPEN API를 통해 수집 후, 판매율 분석한다.

---

### 작업 환경 세팅

* pip install selenium
* pip install beautifulsoup4
* pip install webdriver_manager
* pip install requests
* pip install pymysql
* pip install sqlalchemy
* pip install seaborn 
* pip install scikit-learn