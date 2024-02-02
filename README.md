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

## 작업 환경 세팅

* conda install -c conda-forge jupyterlab
* pip install jupyterlab-night

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