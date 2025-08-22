import csv
import requests

# 파일 경로 설정
input_file_path = 'users.csv'
api_url = 'http://127.0.0.1:8000/accounts/signup/'  # Django 서버의 회원 가입 엔드포인트

# 입력 파일 읽고 데이터 변환
def read_and_prepare_user_data(file_path):
    users = {}
   
    return list(users.values())

# 사용자 데이터로 회원 가입 API 호출
def register_users(users, api_url):
    pass

users = read_and_prepare_user_data(input_file_path)
register_users(users, api_url)
