# %% [0] import
from API_request import DNFAPI
from config import API_KEY,BASE_PATH
from datetime import datetime, timedelta
import json
import os,glob
import pandas as pd

loader = DNFAPI(API_KEY)
folder_path = os.path.join(BASE_PATH,'data','timeline_data')
# %% [1] day timeline

def get_day_timeline(sv_eng, cha_code, start, day):
    
    date_format = '%Y.%m.%d %H:%M'
    start_datetime = datetime.strptime(start, date_format) + timedelta(days=day)
    end_datetime = datetime.strptime(start, date_format) + timedelta(days=day+1) + timedelta(minutes=-1) 
    
    # 당일 06:00 ~ 다음날 05:59
    start = start_datetime.strftime(date_format)
    end = end_datetime.strftime(date_format)
    
    day_timeline = {'레기온': {'이스핀즈':0, '차원회랑': 0,'어둑섬': 0},
                '특수던전' : {'코드네임 게이볼그': 0, '이면 경계': 0}, # 게이볼그 에픽로그가 없어서 안잡힘
                '레이드': {'기계 혁명': {'easy': 0, 'normal': 0,'hard': 0},
                          '아스라한': 0}, # 개전/노말/하드
                '에픽획득': 0, '플레이 로그': [0]*24}  
        
    # timeline 데이터 요청
    log_datas = loader.get_timeline(sv_eng, cha_code, start, end, limit=100)
    
    if log_datas == None:
        return day_timeline
    
    이면경계 = False
    for raw_timeline in log_datas['timeline']['rows']: # log 확인
        
        # log의 time 추출하기
        log_time = datetime.strptime(raw_timeline['date'], '%Y-%m-%d %H:%M')
        hour = log_time.strftime('%H')

        # log 발생시점 수집 -> 모든 로그 수집
        day_timeline['플레이 로그'][int(hour)] += 1

        # 획득 에픽아이템 체크
        if raw_timeline['code'] in (504,505,507,513): # 상자, 드랍, 레이드카드, 클리어 카드
            day_timeline['에픽획득'] += 1

            # 이면경계 클리어 로그 -> 클리어 로그 존재 x -> 보상의 에픽으로 확인
            if (raw_timeline['code'] == 505 and 
                raw_timeline['data']['dungeonName'] == '이면 경계' and not 이면경계):
                day_timeline['특수던전']['이면 경계'] += 1
                이면경계 = True

        # 레이드 클리어 로그       
        if raw_timeline['code'] == 201:
            
            if raw_timeline['data']['raidName'] == '기계 혁명':
                mode_name = raw_timeline['data']['modeName']
                
                # 하드 바칼 이전 / 이후의 로그 shape이 다름
                if mode_name == '바칼 레이드':
                    if 'hard' in raw_timeline['data'] and raw_timeline['data']['hard']:
                        day_timeline['레이드']['기계 혁명']['hard'] += 1
                    else:
                        day_timeline['레이드']['기계 혁명']['normal'] += 1
                else:
                    day_timeline['레이드']['기계 혁명']['easy'] += 1
                    
            elif raw_timeline['data']['raidName'] == '아스라한':
                day_timeline['레이드']['아스라한'] += 1
                
        # 레기온 클리어 로그
        if raw_timeline['code'] == 209:
            region_name = raw_timeline['data']['regionName']
            day_timeline['레기온'][region_name] += 1
            
    return day_timeline

# %% [2] integrate_timeline
def integrate_timeline(row: dict, data: dict):
    
    for key in row:
        if key == '레기온':
            for dungeon in row['레기온']:
                data['레기온'][dungeon] += row['레기온'][dungeon]
                
        elif key == '레이드':
            for raid_name in row['레이드']:
                if raid_name == '기계 혁명':
                    for difficulty in row['레이드']['기계 혁명']:
                        data['레이드']['기계 혁명'][difficulty] += row['레이드']['기계 혁명'][difficulty]
                elif raid_name == '아스라한':
                    data['레이드']['아스라한'] += row['레이드']['아스라한']
                    
        elif key == '특수 던전':
            for dungeon in row['특수 던전']:
                data['특수 던전'][dungeon] += row['특수 던전'][dungeon]
                
        else:
            for hour,playtime in enumerate(row['플레이 로그']):
                data['플레이 로그'][hour] += playtime
    return data

# %% [3] update_timeline
def update_timeline(timeline: dict, date: str, cha_code: str, adv_name: str, summary: bool):
    # 파일 열기
    try:
        with open(os.path.join(folder_path,f'{adv_name}.json'), 'r', encoding='utf-8') as file:
            timeline_json = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        timeline_json = {}
        
    # 처음 확인하는 캐릭터 처리
    if cha_code not in timeline_json:
        timeline_json[cha_code] = {"day":{}, "week":{}}
        
    # 타임라인 저장
    if not summary:
        timeline_json[cha_code]["day"][date] = timeline
    else:
        timeline_json[cha_code]["week"][date] = timeline
        
    # 파일 저장
    with open(os.path.join(folder_path,f'{adv_name}.json'), 'w', encoding='utf-8') as file:
        json.dump(timeline_json, file, ensure_ascii=False, indent=4)
        
# %% [4] update_adventure
def update_adventure(adv_name: str, cha_code: str, sv_eng: str, cha_name: str):
    
    # 파일 열기
    try:
        with open(os.path.join(folder_path,'adventures.json'), 'r', encoding='utf-8') as file:
            adv_json = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        adv_json = {}
    
    # 처음 확인하는 데이터 처리
    if adv_name not in adv_json:
        adv_json[adv_name] = {}
    
    # 모험단 저장
    adv_json[adv_name][cha_code] = (sv_eng,cha_name)
    
    # 파일 저장
    with open(os.path.join(folder_path,'adventures.json'), 'w', encoding='utf-8') as file:
        json.dump(adv_json, file, ensure_ascii=False, indent=4)
# %% [5] get_character_timeline
def get_character_timeline(sv_eng: str, cha_code: str):
    
    # 날짜 포맷 맞추기
    date_format = '%Y.%m.%d %H:%M'
    start = '2024.03.14 06:00'
    end = '2024.04.10 06:00'
    start_date = datetime.strptime(start, date_format)
    end_date = datetime.strptime(end, date_format)
    
    week_timeline = {'레기온': {'이스핀즈':0, '차원회랑': 0,'어둑섬': 0},
                     '특수던전' : {'코드네임 게이볼그': 0, '이면 경계': 0}, # 게이볼그 에픽로그가 없어서 안잡힘
                     '레이드': {'기계 혁명': {'easy': 0, 'normal': 0,'hard': 0}, # 개전/노말/하드
                               '아스라한': 0},
                     '에픽획득': 0, '플레이 로그': [0]*24}
    
    # 모험단 정보 / 캐릭터 이름 확인
    temp = loader.get_timeline(sv_eng, cha_code,
                               '2024.02.21 06:00', '2024.02.22 05:59', limit=100)
    adv_name = temp['adventureName']
    cha_name = temp['characterName']
    
    # 모험단 캐릭터 업데이트
    update_adventure(adv_name, cha_code, sv_eng, cha_name)

    # 타임라인 업데이트
    day = 0
    while start_date <= end_date:
        # 날짜 변경
        start_date = datetime.strptime(start, date_format) + timedelta(days=day)
        
        # 일별 로그 불러오기
        day_timeline = get_day_timeline(sv_eng, cha_code, start_date.strftime(date_format),day)

        # 일별 로그 저장
        update_timeline(day_timeline , start_date.strftime('%Y.%m.%d'), cha_code, adv_name, False)
        
        # 주간 데이터 업데이트
        week_timeline = integrate_timeline(day_timeline, week_timeline)
        
        # 일주일 단위로 저장
        if day%7 == 6:
            print(start_date)
            update_timeline(week_timeline ,start_date.strftime('%Y.%m.%d') ,cha_code, adv_name, True)
            week_timeline = {'레기온': {'이스핀즈':0, '차원회랑': 0,'어둑섬': 0},
                             '특수던전' : {'코드네임 게이볼그': 0, '이면 경계': 0}, # 게이볼그 에픽로그가 없어서 안잡힘
                             '레이드': {'기계 혁명': {'easy': 0, 'normal': 0,'hard': 0}, # 개전/노말/하드
                                      '아스라한': 0},
                             '에픽획득': 0, '플레이 로그': [0]*24}
        day += 1
# %%
df = pd.read_csv(r'C:\Users\tbxkd\coding\project\dnf project\data\crawling_data\data_20240411\event_character.csv')
df



# %% log sample
''' raid
# 기계 혁명
   {'code': 201,
    'name': '레이드',
    'date': '2024-02-03 09:23',
    'data': {'raidName': '기계 혁명',
     'raidPartyName': '신용하드#]2200/140 랏버퍼분!!',
     'modeName': '바칼 레이드',
     'hard': True}}]}}
    
    {'code': 201,
     'name': '레이드',
     'date': '2023-05-13 10:37',
     'data': {'raidName': '기계 혁명',
      'raidPartyName': '442클) 일반 4.5+ 딜러',
      'modeName': '바칼 레이드'}}
    
    {'code': 201,
     'name': '레이드',
     'date': '2024-02-03 09:45',
     'data': {'raidName': '기계 혁명',
      'raidPartyName': '베짱이29호',
      'modeName': '개전'}},

    {'code': 201,
     'data': {'hard': True,
              'modeName': '바칼 레이드',
              'raidName': '기계 혁명',
              'raidPartyName': '앵이#5 하드 딜러버퍼'},
     'date': '2024-02-22 20:38',
     'name': '레이드'}
    
# 아스라한
    {'code': 201,
     'data': {'raidName': '아스라한', 'raidPartyName': '베짱이28호'},
     'date': '2024-02-22 12:45',
     'name': '레이드'}
    
# 혼돈의 오즈마
    {'code': 201,
     'data': {'raidName': '혼돈의 오즈마', 'raidPartyName': '호뚜라미'},
     'date': '2023-02-13 15:52',
     'name': '레이드'}
'''