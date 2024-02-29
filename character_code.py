# %%
from concurrent.futures import ThreadPoolExecutor, as_completed
from API_request import DNFAPI
from config import API_KEY,BASE_PATH
import pandas as pd
import os
import glob

loader = DNFAPI(API_KEY)

base_path = BASE_PATH
folder_path = os.path.join(base_path,'crawling_data','data_20240220')
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
# %%
def get_character_code(sv_eng, cha_name):
    try:
        cha_code = loader.get_character(sv_eng, cha_name)
        return cha_code['characterId'][0]
    except Exception as e:
        print(f"Error getting character code for {cha_name}: {e}")
        return None

def run(csv_files):

    for csv_file in csv_files:
        print(csv_file)

        df = pd.read_csv(csv_file)
        total = len(df)
        cha_codes = [None]*total

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(get_character_code,row['sv_eng'],row['cha_name']):
                       i for i, row in df.iterrows()}
            for future in as_completed(futures):
                index = futures[future]
                try:
                    cha_code = future.result()
                    cha_codes[index] = cha_code
                except Exception as e:
                    print(f"Error in future: {e}")

        df['cha_code'] = cha_codes
        # 결과 데이터프레임 저장
        df.to_csv(f"{csv_file.split('.')[0]}_with_codes.csv", index=False, encoding = 'utf-8')
        print(f'{csv_file} 완료')

run(csv_files)
