# %% job group histogram

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def job_hist():
    df = pd.read_csv('character_info.csv')
    plt.rc("font", family = "Malgun Gothic")
    sns.set(font="Malgun Gothic", rc={"axes.unicode_minus":False}, style='white')

    info = {
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

    for job_group, jobs in info.items():
        plt.figure(figsize=(5 * len(jobs), 5))
        for i, job_name in enumerate(jobs, start=1):
            plt.subplot(1, len(jobs), i)
            sns.histplot(df[df['job_name'] == job_name]['fame'], bins=55, kde=True)
            plt.title(job_name)
            plt.xlabel('명성')
            plt.ylabel('인원수')
        plt.tight_layout()
        plt.show()