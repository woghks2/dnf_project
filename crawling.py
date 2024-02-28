# %% [0] import
from config import BASE_PATH
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time
import glob
import os

# %% [1] job code

jobs_code = [('0_1', '웨펀마스터'), ('0_2', '소울브링어'), ('0_3', '버서커'), ('0_4', '아수라'), ('0_5', '검귀'),
 ('11_1', '소드마스터'), ('11_2', '다크템플러'), ('11_3', '데몬슬레이어'), ('11_4', '베가본드'), ('11_5', '블레이드'),
 ('7_1', '남넨마스터'), ('7_2', '남스트라이커'), ('7_3', '남스트리트파이터'), ('7_4', '남그래플러'),
 ('1_1', '여넨마스터'), ('1_2', '여스트라이커'), ('1_3', '여스트리트파이터'), ('1_4', '여그래플러'),
 ('2_1', '남레인저'), ('2_2', '남런처'), ('2_3', '남메카닉'), ('2_4', '남스핏파이어'), ('2_5', '어썰트'),
 ('5_1', '여레인저'), ('5_2', '여런처'), ('5_3', '여메카닉'), ('5_4', '여스핏파이어'),
 ('8_1', '엘레멘탈 바머'), ('8_2', '빙결사'), ('8_3', '블러드 메이지'), ('8_4', '스위프트 마스터'), ('8_5', '디멘션워커'),
 ('3_1', '엘레멘탈 마스터'), ('3_2', '소환사'), ('3_3', '배틀메이지'), ('3_4', '마도학자'), ('3_5', '인챈트리스'),
 ('4_1', '남크루세이더'), ('4_2', '인파이터'), ('4_3', '퇴마사'), ('4_4', '어벤저'),
 ('14_1', '여크루세이더'), ('14_2', '이단심판관'), ('14_3', '무녀'), ('14_4', '미스트리스'),
 ('6_1', '로그'), ('6_2', '사령술사'), ('6_3', '쿠노이치'), ('6_4', '섀도우댄서'),
 ('12_1', '엘븐나이트'), ('12_2', '카오스'), ('12_3', '팔라딘'), ('12_4', '드래곤나이트'),
 ('13_1', '뱅가드'), ('13_2', '듀얼리스트'), ('13_3', '드래고니안 랜서'), ('13_4', '다크 랜서'),
 ('15_1', '히트맨'), ('15_2', '요원'), ('15_3', '트러블 슈터'), ('15_4', '스페셜리스트'),
 ('16_1', '뮤즈'), ('16_2', '트래블러'),
 ('9_0', '다크나이트'), ('10_0', '크리에이터')]
# %% [2] Crwaling Function

# %%% [2-1] initialize_driver

def initialize_driver(url: str):
    
    # 1. 버전에 맞는 크롬 드라이버를 다운로드 후, 경로 지정
    chrome_driver_path = 'C:/chromedriver/chromedriver.exe'
    
    # 2. 크롬 드라이버 실행 시, 경로에 접근해서 버전에 맞는 드라이버 선택
    service = webdriver.ChromeService(executable_path = chrome_driver_path)
    
    # 3. 크롬 드라이버 실행
    driver = webdriver.Chrome(service=service)
    
    # 4. 크롬 드라이버 실행
    driver.get(url)
    
    return driver

# %%% [2-2] select_job

def select_job(driver, job_id: str):
    
    # 1. 직업 드롭박스 선택 후 클릭 (active 상태)
    driver.find_element(By.ID,'fameSelectedJob').click()
    
    # 2. 직업 코드에 해당하는 드랍박스를 찾기
    job_element = driver.find_element(By.XPATH, f"//a[@data-id='{job_id}']")
    
    # 3. 직업 선택
    job_element.click()

# %%% [2-3] set_fame
def set_fame(driver, max_fame: int):

    # 1. 이스핀즈 명성인 33043 이상만 표본으로 처리
    if max_fame < 33043:
        return False
    
    # 2. 검색 창 명성 범위 입력
    input_field = driver.find_element(By.ID, 'fame2')
    input_field.clear()
    input_field.send_keys(max_fame)
    input_field = driver.find_element(By.ID, 'fame1')
    input_field.click() 
    
    # 3. 검색 버튼 클릭
    search = driver.find_element(By.ID, 'fameSearchBtn')
    search.click()
    
    return True

# %%% [2-4] scrape_characters

def scrape_characters(driver, job_name: str):
    
    # 1. 현재 드라이버의 HTML 불러오기
    html = driver.page_source
    time.sleep(1)
    # 2. 현재 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')
    
    # 3. 캐릭터 결과 불러오기
    article = soup.find('article', class_='charsrch_result')
    
    # 4. 최대 20개의 결과 데이터 캐릭터 별로 파싱하기
    characters = article.find_all('dl')

    # 5. 각 캐릭터 별 정보 파싱
    data = []
    for character in characters:
        
        # 서버영문, 서버한글, 서버숫자
        sv_eng = character.dt['data-sv'] # cain
        sv_kor = character.dt['data-svk'] # 카인
        
        # 캐릭터 이미지 코드, 캐릭터 이름, 직업명
        cha_img_code = character.dt['data-ch']
        cha_name = character.dt['data-nm']
        job_name = character.find('p', class_='job').get_text(strip=True)       
        
        # 명성, 레벨
        lv = character.find('p', class_='lv').get_text(strip=True)
        fame = character.find('p', class_='fame').get_text(strip=True)
        fame = int(fame.replace(",", ""))
        # 딕셔너리로 변경
        row = {'sv_kor': sv_kor, 'sv_eng': sv_eng,
               'cha_img_code': cha_img_code,
               'cha_name': cha_name,'job_name': job_name[:-len(sv_kor)].lstrip('眞 '),
               'lv': int(lv[3:]), 'fame': fame}
        data.append(row)

    # return data, row['fame'] # data와 최소 명성치 반환
    return data, fame # data와 최소 명성치 반환

# %%% [2-5] save_to_csv

def save_to_csv(data: list, save_path: str, file_name: str):
    
    # 1. 데이터 프레임 생성 이후 이스핀즈 미만 명성 절사
    df = pd.DataFrame(data)
    df = df[df['fame'] >= 33043]
    
    # 2. 중복 데이터 제거
    df = df.drop_duplicates(subset=['sv_eng','cha_name'])
    
    # 3. 최종 파일 경로 설정
    final_path = os.path.join(save_path, f"{file_name}.csv")
    
    # 4. 데이터 저장
    df.to_csv(final_path, index=False, encoding='utf-8-sig')
    print(f'{file_name}.csv is saved')
    
# %% [3] Integrate job data
def integrate_data(save_path: str, file_name: str):
    
    # 1. CSV 파일들 읽기
    csv_files = glob.glob(os.path.join(save_path, "*.csv"))
    final_path = os.path.join(save_path, f"{file_name}.csv")
    
    # 2. 통합 데이터 프레임
    df = pd.DataFrame()
    
    # 3. 데이터 프레임 concat
    for jobs,file in zip(jobs_code,csv_files):
        job_name = jobs[1]
        data = pd.read_csv(file, encoding='utf-8-sig')
        df = pd.concat([df, data], ignore_index=True)
        print(f'{job_name} data is integrated')
    
    # 4. 데이터 프레임 저장
    df.to_csv(final_path, index=False, encoding='utf-8-sig')
    print(f'{file_name}.csv is saved')
# %% [4] run
def run(start_fame):
    
    # 1. base path에 데이터를 저장할 폴더 생성
    today = datetime.now().strftime("%Y%m%d")
    base_path = BASE_PATH
    folder_name = f"data_{today}"
    save_path = os.path.join(base_path,'crawling_data',folder_name)
    os.makedirs(save_path, exist_ok=True)
    
    # 2. 공홈 크롤링 링크
    url = 'https://df.nexon.com/world/fame'
    for job_id, job_name in jobs_code[-1:]:
        
        # 3. 직업 별 검색 조건 설정
        driver = initialize_driver(url)
        select_job(driver, job_id)
        max_fame = start_fame
        time.sleep(1) # HTML 업데이트 대기
        
        # 4. 크롤링
        datas = []
        while True:
            
            # 이스핀즈 미만 명성 절사
            if not set_fame(driver, max_fame):  
                break
            time.sleep(0.4) # HTML 업데이트 대기. 짧게 해도 duplicate로 중복 제거
            
            # 5. 데이터 업데이트
            data, max_fame = scrape_characters(driver, job_name)
            datas.extend(data)

        driver.quit()
        
        # 6. 현재 데이터를 파일명 job_namd으로 save path에 저장
        save_to_csv(datas, save_path, job_name)
        
    # 7. 데이터 통합
    integrate_data(save_path,'character')

# %% run code : 약 2시간 30분 소요
run(62000)