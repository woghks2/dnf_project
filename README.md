# 던전앤파이터 신규 캐릭터 패키지 매출 분석



### 요약
* 프로젝트 기간
    * 7주 (3/14 ~ 5/2)

* 기술 스택
    * Python : pandas, selenium, matplolib, seaborn
    * MySQL : DB 구축
    * Tableau : 대시보드 제작 및 시각화

* 분석 목적
    * 신규 캐릭터와 성장 지원 이벤트, 관련 패키지를 분석하여 신규 패키지 매출을 분석한다.
    * 유저 풀 별 구매력 분석하여 추후 성장 지원 이벤트와 패키지를 개선한다.

---

### 개요
* 신규 레이드 `아스라한 : 무의장막` 출시를 앞두고 아처의 신규 직업 `비질란테, 헌터`가 출시됐다.

* 신규 레이드 출시를 앞둔 지금, 던전앤파이터 유저 수를 조사한다.

* 또한, 신규 캐릭터 육성 유저 풀을 구분하여 유저 구분에 따른 `패키지 구매율을 조사한다.`

---

### 작업 순서
1. 신규 캐릭터와 관련된 이벤트 분석
2. 던전앤파이터 공식 홈페이지에서 웹크롤링으로 캐릭터들의 데이터 수집
3. 각 유저들이 어떤 캐릭터를 키우는지 파악하기 위해 OPEN API를 통해 모험단 조사
4. 명성을 통해 각 유저 별 신규 캐릭터 행동 유무 파악
5. 액티브 유저의 패키지 구매 유무를 OPEN API를 통해 수집 후, 판매율 분석

---

### 작업 환경 세팅

* pip install selenium
* pip install beautifulsoup4
* pip install webdriver_manager
* pip install requests
* pip install pymysql
* pip install sqlalchemy
* pip install seaborn 
* *pip install scikit-learn