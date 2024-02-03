# Reference

---

## Dungeon and Fighter API
1. 던전앤파이터 API 발급
    * https://dfmania.tistory.com/15

---

## Selenium
1. 크롬 드라이버 버전 호환성 오류 해결
    
    - github 링크에서 현재 사용하는 크롬 버전에 맞는 크롬 드라이버를 다운로드한다. (링크 복사 후 이동)
    - 크롬 드라이버가 깔려있는 파일 경로에 chromedriver.exe을 대체한다.
    
    * https://velog.io/@syiee/Chrome-Web-Driver-%EC%B5%9C%EC%8B%A0-%EB%B2%84%EC%A0%84-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-119
    * https://github.com/GoogleChromeLabs/chrome-for-testing/blob/main/data/latest-versions-per-milestone-with-downloads.json

2. 공식 홈페이지 크롤링 문제

    - 명성 구간 입력 시, 한쪽 입력하면 자동으로 +- 2000의 범위가 채워짐
    - time.sleep() 같은 메서드를 사용하지 않으면 업데이트가 되지 않은 HTML을 불러오는 문제 발생
    - 첫 루프에서 오류가 날 경우, 코드가 실행되지 않는데 충분한 시간을 주고 이를 해결
    
    * https://dfmania.tistory.com/19 : HTML 사용
    * https://wikidocs.net/149358 : 셀레니움 사용법
    * https://www.codeit.kr/community/questions/UXVlc3Rpb246NjRkYTJhNmI4ZTViYmUzNDJhMjA5YjE4 : 웹 드라이버 버전 오류 해결

---

## SUPERSET

*
*
*
