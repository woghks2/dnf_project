# config.py

# ! PROJECT PATH
PROJECT_PATH = "your_path\\dnf_project"
DATA_PATH = "your_path\\dnf_project\\data"

# ! API_KEY
API_KEYS_DICT = {
    # -> googld
    'API_KEY1': 'API',
    'API_KEY2': 'API',
    'API_KEY3': 'API',
    'API_KEY4': 'API',
    'API_KEY5': 'API',
    'API_KEY6': 'API',
    'API_KEY7': 'API',
    'API_KEY8': 'API',
    'API_KEY9': 'API',
    'API_KEY10': 'API',
    # -> naver
    'API_KEY11': 'API',
    'API_KEY12': 'API',
    'API_KEY13': 'API',
    'API_KEY14': 'API',
    'API_KEY15': 'API',
    'API_KEY16': 'API',
    'API_KEY17': 'API',
    'API_KEY18': 'API',
    'API_KEY19': 'API',
    'API_KEY20': 'API'
}
API_KEYS = list(API_KEYS_DICT.values())

# ! MySQL config info
MYSQL_CONFIGS = {
    'MYSQL_USER' : 'MySQL 사용자 이름',
    'MYSQL_PASSWORD' : 'MySQL 비밀번호',
    'MYSQL_HOST' : 'MySQL 호스트',
    'MYSQL_PORT' : '포트번호',
    'DATABASE' : '데이터베이스 이름 '
}
MYSQL_CONNECTION_STRING = f"mysql+mysqlconnector://{MYSQL_CONFIGS['MYSQL_USER']}:{MYSQL_CONFIGS['MYSQL_PASSWORD']}@{MYSQL_CONFIGS['MYSQL_HOST']}:{MYSQL_CONFIGS['MYSQL_PORT']}/{MYSQL_CONFIGS['DATABASE']}"

# ! PostgreSQL config info
PostgreSQL_CONFIGS = {
    'PostgreSQL_USER': 'PostgreSQL 사용자 이름',
    'PostgreSQL_PASSWORD': 'PostgreSQL 비밀번호',
    'PostgreSQL_HOST': 'PostgreSQL 호스트',
    'PostgreSQL_PORT': 'PostgreSQL 포트',
    'DATABASE': '데이터베이스 이름'
}

PostgreSQL_CONNECTION_STRING = f"postgresql://{PostgreSQL_CONFIGS['PostgreSQL_USER']}:{PostgreSQL_CONFIGS['PostgreSQL_PASSWORD']}@{PostgreSQL_CONFIGS['PostgreSQL_HOST']}:{PostgreSQL_CONFIGS['PostgreSQL_PORT']}/{PostgreSQL_CONFIGS['DATABASE']}"


# ! SUPERSET config info
SUPERSET_CONFIGS = {
    'SUPERSET_USER' : 'Superset 사용자 이름',
    'SUPERSET_PASSWORD' : 'Superset 비밀번호',
    'SUPERSET_PORT' : 'Superset 포트 번호'
}
SECRET_KEY = 'Superset 시크릿 키'

# * superset download

# step 1: 설치
    # conda create -n superset python=3.9
    # conda activate superset
    # pip install apache-superset
    
# step 2: 설정
    # openssl rand -base64 42 -> SUPERSET CONFIG에 키 저장
    # envs//superset 폴더 superset_config.py에 SECRET_KEY = '시크릿 키' 저장
    # pip install pillow -> 에러 발생한 경우
    
# step 3: 재설정
    # conda activate superset
    # set FLASK_APP=superset
    # superset upgrade db
    
# step 4: 유저등록    
    # Username [admin]:
    # User first name [admin]:
    # User last name [user]:
    # Email [admin@fab.org]:
    # Password:
    # Password repeat:

# step 5: 실행
    # conda activate dashboard
    # set FLASK_APP=superset
    # superset run -p 8088 --with-threads --reload --debugger