import mysql.connector
from mysql.connector import Error

# todo : 데이터 저장 chunk 단위로 넣기 (하나씩 넣으면 시간 오래걸림, 한 번에 넣으면 오류 발생)
class MySQL_DB:
    
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        # * MySQL DB에 연결
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Database connection successful.")
        except Error as e:
            print(f"Error: {e}")

    def disconnect(self):
        # * MySQL DB 연결 끊기
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query: str, params: tuple = None):
        # * MySQL DB CRUD 작업
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"Error: {e}")
        finally:
            print("Query executed successfully.")
            cursor.close()

    def fetch_all(self, query: str, params: tuple = None):
        # * MySQL 데이터 가져오기
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()

    def fetch_one(self, query: str, params: tuple = None):
        # * MySQL 데이터 가져오기 (단일 행)
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
