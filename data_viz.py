# %% job group histogram

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False

class DataViz:
    
    def __init__(self, base_path: str):
        self.base_path = base_path
        
        self.job_infos = {
            "(남) 귀검사": ["웨펀마스터", "소울브링어", "버서커", "아수라", "검귀"],
            "(여) 귀검사": ["소드마스터", "다크템플러", "데몬슬레이어", "베가본드", "블레이드"],
            "(남) 격투가": ["남넨마스터", "남스트라이커", "남스트리트파이터", "남그래플러"],
            "(여) 격투가": ["여넨마스터", "여스트라이커", "여스트리트파이터", "여그래플러"],
            "(남) 거너": ["남레인저", "남런처", "남메카닉", "남스핏파이어", "어썰트"],
            "(여) 거너": ["여레인저", "여런처", "여메카닉", "여스핏파이어"],
            "(남) 마법사": ["엘레멘탈 바머", "빙결사", "블러드 메이지", "스위프트 마스터", "디멘션워커"],
            "(여) 마법사": ["엘레멘탈 마스터", "소환사", "배틀메이지", "마도학자", "인챈트리스"],
            "(남) 프리스트": ["남크루세이더", "인파이터", "퇴마사", "어벤저"],
            "(여) 프리스트": ["여크루세이더", "이단심판관", "무녀", "미스트리스"],
            "도적": ["로그", "사령술사", "쿠노이치", "섀도우댄서"],
            "나이트": ["엘븐나이트", "카오스", "팔라딘", "드래곤나이트"],
            "마창사": ["뱅가드", "듀얼리스트", "드래고니안 랜서", "다크 랜서"],
            "총검사": ["히트맨", "요원", "트러블 슈터", "스페셜리스트"],
            "아처": ["뮤즈", "트래블러"],
            "외전": ["다크나이트", "크리에이터"]
            }
        
        self.job_groups = list(self.job_infos.keys())
        self.jobs = []
        for jobs_group in self.job_infos.values():
            self.jobs.extend(jobs_group)
    
    def get_date_list(self):
        '''
        폴더 내 파일명 추출
        '''
        file_names = glob.glob(os.path.join(self.base_path, 'data_*'))
        file_names = [os.path.basename(f).lstrip('data_') for f in file_names]        
        return file_names
    
    def group_hist(self, date: str, group: str):
        '''
        str format : YYYYMMDD
        직업군 선택 시 해당 직업군에 속하는 직업들의 명성 분포 출력
        '''
        
        file_name = f'data_{date}'
        jobs = self.job_infos[group]
        jobs_count = len(jobs)

        fig, axes = plt.subplots(1, jobs_count, figsize=(jobs_count*5,5))
        
        for idx,job in enumerate(jobs):
            ax = axes[idx]
            ax.set_title(job)
            df_job = pd.read_csv(os.path.join(self.base_path,file_name,f'{job}.csv'))
            df_fame = df_job['fame']
            bins = (df_fame.iloc[0]-df_fame.iloc[-1])//500 + 1
            sns.histplot(df_fame, ax=ax,
                         bins=bins, kde=True)
            
        plt.tight_layout()
        plt.show()
        return fig
    
    def job_hist(self, date: str, job: str):
        '''
        str format : YYYYMMDD
        '''
        
        file_name = f'data_{date}'
        df_job = pd.read_csv(os.path.join(self.base_path,file_name,f'{job}.csv'))
        
        fig, ax = plt.subplots(figsize=(10,6))
        sns.histplot(df_job['fame'], kde=True, ax=ax)
        ax.set_title(f'{job}')
        plt.tight_layout()
        plt.show()
        return fig