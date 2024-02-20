# 던전앤파이터 고객 현황 분석

---

1. 신규 컨텐츠의 부재로 인한 이탈고객 현황 분석
    * 선계 상급던전, 이면 경계 등 성장형 던전으로 설계된 보상의 역할 분석
        - 이면 경계 업데이트 전 명성 분포와 후 명성 분포를 비교
    * 어둑섬 등 최종 컨텐츠의 등장 시 참여율 분석
        - 클리어 로그 확인
    * 기존의 오래된 컨텐츠(이스핀즈, 바칼, 회랑)의 참여율 분석
        - 바칼 레이드 같은 경우 레이드 보상이 충분하지 않다. (장비, 골드, 융합픽 관점에서)
        - 부캐릭터 육성에 필수적이긴 하나, 이 보상을 받게되면 보상이 매력적이지 않음
        
2. 신규 이벤트에 따른 신규 또는 복귀 유저 현황 분석
    * 베히의 성장지원 등 신규 캐릭터 육성을 위한 이벤트 진행 시 참여율
        - 신규 캐릭터 생성량 비교
    * 13강 무기, 클레압 등 신규 캐릭터 육성에 도움이 되는 이벤트 진행 시 참여율
        - 신규 캐릭터 생성량 비교

---

## 작업 순서
1. 공식 홈페이지에서 닉네임/서버/이미지코드/직업/명성 정보 크롤링.
   * 110lv 이상 모든 데이터 존재.
   * 타 사이트들과 달리 가장 최신 정보. 캐릭터명 변경 / 모험단명 변경 파악 쉬움
  
2. 캐릭터 별 API 요청 -> 캐릭터 코드와 모험단 정보 필요
   * 서버/캐릭터 이름을 넣어서 캐릭터 코유 코드 획득
   * 캐릭터 고유 코드를 넣어서 캐릭터 코드와 모험단 정보 획득
  
3. 캐릭터 별 timeline 구축
   * 일일 컨텐츠 보다 주간 컨텐츠가 중요하니 주간 단위로 정보 수집
   * 획득한 에픽 로그를 통해서 플레이 시간대 확인
   * 모험단 별로 캐릭터 로그를 통합해서 모험단 별 타임라인 생성
  
4. timeline 분석
   * 업데이트 시기 별 active 캐릭터 수 / 유저 수 분석
   * 컨텐츠 소모 속도에 따른 유저 수 분석
   * 성장 이벤트에 따른 active 캐릭터 수 변화 분석
  
5. dashboard 만들기
   1. 전체 현황
       * 현재 active 유저 수 / 전월대비  active 유저 수 변화
       * 현재 active 캐릭터 수 / 전월 대비 active 유저 수 변화
       * 플레이 시간대 선호도
   2. 모험단 별 현황
       * 획득 에픽량 캘린더 히트맵
       * 레기온 / 레이드 / 상급던전 / 특수던전 등 던전 클리어 그래프
       * 전체 플레이 시간대와 유저 플레이 시간대 비교
  

---

## 작업 환경 세팅

* conda install -c conda-forge jupyterlab
* pip install jupyterlab-night
* conda install -c conda-forge nodejs

* conda install spyder-notebook -c conda-forge
* conda install spyder-terminal -c conda-forge

* pip install selenium
* pip install beautifulsoup4
* pip install webdriver_manager
* pip install requests

* pip install pymysql
* pip install sqlalchemy

* pip install seaborn
* pip install dash