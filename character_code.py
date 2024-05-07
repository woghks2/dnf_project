# %%
from concurrent.futures import ThreadPoolExecutor, as_completed
from API_request import DNFAPI
from config import API_KEY,BASE_PATH
import pandas as pd
import os
import glob
loader = DNFAPI(API_KEY)

# %%
def get_character_code(sv_eng, cha_name):
    # 캐릭터 코드 가져오기 / 오류 나는 경우는 None
    try:
        cha_code = loader.get_character(sv_eng, cha_name)
        return cha_code['characterId'][0]
    except Exception as e:
        print(f"Error getting character code for {cha_name}: {e}")
        return None

def run(file_path):
    
    df = pd.read_csv(file_path)
    total = len(df)
    cha_codes = [None]*total

    # 병렬 처리
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(get_character_code,row['sv_eng'],row['cha_name']):
                    i for i, row in df.iterrows()}
        # 맞는 인덱스에 전달받은 캐릭터 코드 입력
        for future in as_completed(futures):
            index = futures[future]
            try:
                cha_code = future.result()
                cha_codes[index] = cha_code
                print(index)
            except Exception as e:
                print(f"Error in future: {e}")

    df['cha_code'] = cha_codes
    # 결과 데이터프레임 저장
    df.to_csv(f'{file_path}', index=False, encoding = 'utf-8-sig')
    print(f'{file_path} saved')

# %%
path = os.path.join(BASE_PATH,'data\crawling_data\data_20240503\*.csv')
file_names = glob.glob(path)
# %%
for file_name in file_names:
    print(file_name)
    run(file_name)
