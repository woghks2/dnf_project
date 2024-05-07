# %%
from concurrent.futures import ThreadPoolExecutor, as_completed
from API_request import DNFAPI
from config import API_KEY,BASE_PATH
import pandas as pd
import numpy as np

loader = DNFAPI(API_KEY)
# %%
def get_title(row):
    sv_eng, cha_code = row['sv_eng'], row['cha_code']
    try:
        temp = loader.get_equipment(sv_eng, cha_code)
        return temp['equipment'][1]['itemName']
    except Exception as e:
        print(f"Error getting title for {cha_code}: {e}")
        return None

def run(csv_file):
    df = pd.read_csv(csv_file)
    total = len(df)
    titles = [None] * total
    
    # 병렬 처리
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(get_title, row): index for index, row in df.iterrows()}
        
        # 맞는 인덱스에 전달받은 캐릭터 코드 입력
        for future in as_completed(futures):
            try:
                result = future.result()
                index = futures[future]
                titles[index] = result
                print(index)
            except Exception as e:
                print(f"Error in future: {e}")

    df['title'] = titles
    # 결과 데이터프레임 저장
    df.to_csv(f"{csv_file.split('.')[0]}_titles.csv", index=False, encoding='utf-8-sig')
    print(f'{csv_file} 완료')

path = os.path.join(BASE_PATH,'data\crawling_data\data_20240425\신직업_title.csv')
run(path)