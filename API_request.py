# %% [0] Import
import pandas as pd
import requests
import pprint
from PIL import Image
from io import BytesIO
from config import API_KEY,BASE_PATH

# %% [1] HTTP,API error check

def error_check(fn):
    def wrapper(*args,**kwargs):
        try:
            result = fn(*args,**kwargs)
            return result
        except Exception as e:
            error_reason = type(e).__name__
            error_message = str(e)
            print(f"에러 원인: {error_reason}")
            print(f"에러 메시지: {error_message}")
    return wrapper

# %% [2] Dataloader

class DNFAPI:

    # API 키 입력
    def __init__(self,api_key):
        self.api_key = api_key

    # error에 맞는 메세지 출력
    def find_error(response):
        error_codes = {
            200: ("정상적인 응답", "정상적인 응답입니다."),
            400: ("요청에 대한 유효성 검증 실패 또는 필수 파라미터 에러", "요청에 대한 유효성 검증 실패 또는 필수 파라미터 에러입니다."),
            401: ("인증 오류", "인증 오류가 발생했습니다."),
            404: ("존재하지 않은 리소스 또는 페이지", "존재하지 않은 리소스 또는 페이지입니다."),
            500: ("시스템 오류", "시스템 오류가 발생했습니다."),
            503: ("시스템 점검", "시스템 점검 중입니다.")
        }

        common_errors = {
            "API000": ("API Key 미입력", "API Key가 입력되지 않았습니다."),
            "API001": ("유효하지 않은 게임아이디", "유효하지 않은 게임아이디입니다."),
            "API002": ("API Key 사용량 초과", "API Key의 사용량이 초과되었습니다."),
            "API003": ("유효하지 않은 API Key", "유효하지 않은 API Key입니다."),
            "API004": ("차단된 API Key", "차단된 API Key입니다."),
            "API005": ("해당 게임으로 발급되지 않은 API Key", "해당 게임으로 발급되지 않은 API Key입니다."),
            "API006": ("유효하지 않은 HTTP 헤더 요청", "유효하지 않은 HTTP 헤더 요청입니다."),
            "API007": ("클라이언트 소켓 통신 오류", "클라이언트 소켓 통신 오류가 발생했습니다."),
            "API900": ("유효하지 않은 URL", "유효하지 않은 URL입니다."),
            "API901": ("유효하지 않은 요청 파라미터", "유효하지 않은 요청 파라미터입니다."),
            "API999": ("시스템 오류", "시스템 오류가 발생했습니다.")
        }

        dnf_errors = {
            "DNF000": ("유효하지 않은 서버아이디", "유효하지 않은 서버아이디입니다."),
            "DNF001": ("유효하지 않은 캐릭터 정보", "유효하지 않은 캐릭터 정보입니다."),
            "DNF003": ("유효하지 않은 아이템 정보", "유효하지 않은 아이템 정보입니다."),
            "DNF004": ("유효하지 않은 경매장 및 아바타마켓 상품 정보", "유효하지 않은 경매장 및 아바타마켓 상품 정보입니다."),
            "DNF005": ("유효하지 않은 스킬 정보", "유효하지 않은 스킬 정보입니다."),
            "DNF006": ("타임라인 검색 시간 파라미터 오류", "타임라인 검색 시간 파라미터 오류가 발생했습니다."),
            "DNF007": ("경매장 아이템 검색 갯수 제한", "경매장 아이템 검색 갯수 제한이 초과되었습니다."),
            "DNF008": ("다중 아이템 검색 갯수 제한", "다중 아이템 검색 갯수 제한이 초과되었습니다."),
            "DNF009": ("아바타 마켓 타이틀 검색 갯수 제한", "아바타 마켓 타이틀 검색 갯수 제한이 초과되었습니다."),
            "DNF900": ("유효하지 않은 URL", "유효하지 않은 URL입니다."),
            "DNF901": ("유효하지 않은 요청 파라미터", "유효하지 않은 요청 파라미터입니다."),
            "DNF980": ("시스템 점검", "시스템 점검 중입니다."),
            "DNF999": ("시스템 오류", "시스템 오류가 발생했습니다.")
        }

        status_code = response.status_code
        error_code = response.json().get("code")

        if status_code in error_codes:
            return error_codes[status_code]
        elif error_code in common_errors:
            return common_errors[error_code]
        elif error_code in dnf_errors:
            return dnf_errors[error_code]
        else:
            return ("알 수 없는 오류", "알 수 없는 오류가 발생했습니다.")

    @error_check
    def get_server(self, print_flag=False):
        url = f'https://api.neople.co.kr/df/servers?apikey={self.api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            server_info = response.json()

            if print_flag:
                pprint.pprint(server_info)
            return pd.DataFrame(server_info['rows'])

    @error_check
    def job_dfs(self, temp_data, new_jobs_data):
        new_jobs_data[temp_data['jobGrowName']] = temp_data['jobGrowId']
        if 'next' in temp_data:
            self.job_dfs(temp_data['next'], new_jobs_data) 

    @error_check
    def get_jobs(self, print_flag=False):

        url = f'https://api.neople.co.kr/df/jobs?apikey={self.api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            jobs_info = response.json()

            if print_flag:
                pprint.pprint(jobs_info)

            new_jobs_info = {}
            for job in jobs_info['rows']:
                new_jobs_info[job['jobName']] = job['jobId']
                for job_grow in job['rows']:
                    self.job_dfs(job_grow,new_jobs_info)
            return new_jobs_info

    @error_check
    def get_character(self, serverId, characterName, jobId='', jobGrowId='', isAllJobGrow=False, wordType='match', limit=10, print_flag=False):
        url = f'https://api.neople.co.kr/df/servers/{serverId}/characters?characterName={characterName}&jobId={jobId}&jobGrowId={jobGrowId}&isAllJobGrow={isAllJobGrow}&limit={limit}&wordType={wordType}&apikey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            character_info = response.json()
            df_character_info = pd.DataFrame(character_info['rows'])
            if print_flag:
                pprint.pprint(df_character_info)
            return df_character_info

    @error_check
    def get_character_img(self, serverId, characterId, imgSize=2):
        url = f'https://img-api.neople.co.kr/df/servers/{serverId}/characters/{characterId}?zoom={imgSize}'
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            return img

    @error_check
    def get_timeline(self, serverId, characterId, startDate, endDate, limit=10, code='', next='',print_flag=False):
        url = f'https://api.neople.co.kr/df/servers/{serverId}/characters/{characterId}/timeline?limit={limit}&code={code}&startDate={startDate}&endDate={endDate}&next={next}&apikey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            timeline_info = response.json()
            if print_flag:
                pprint.pprint(timeline_info)
            return timeline_info

    @error_check
    def get_equipment(self, serverId, characterId, print_flag=False):
        url = f'https://api.neople.co.kr/df/servers/{serverId}/characters/{characterId}/equip/equipment?apikey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            equip_info = response.json()
            if print_flag:
                pprint.pprint(equip_info)
            return equip_info
        
    @error_check
    def get_creature(self, serverId, characterId, print_flag=False):
        url = f'https://api.neople.co.kr/df/servers/{serverId}/characters/{characterId}/skill/buff/equip/creature?apikey={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            creature_info = response.json()
            if print_flag:
                pprint.pprint(creature_info)
            return creature_info