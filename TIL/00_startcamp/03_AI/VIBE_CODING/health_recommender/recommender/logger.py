# 운동 기록 관리 모듈
import csv
import os
from datetime import datetime
from .user_input import UserInfo

class WorkoutLogger:
    def __init__(self, log_path: str = "data/workout_log.csv"):
        self.log_path = log_path
        # data 폴더가 없으면 생성
        log_dir = os.path.dirname(self.log_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # 파일이 없으면 헤더 생성
        if not os.path.exists(self.log_path):
            with open(self.log_path, mode="w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "날짜", "이름", "운동부위", "운동환경", "기구보유", "몸상태", "신장", "체중", "골격근량", "체지방량", "추천종목", "추천루틴", "주의사항"
                ])

    def add_record(self, user: UserInfo, recommend: dict):
        today = datetime.now().strftime("%Y-%m-%d")
        with open(self.log_path, mode="a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                today,
                user.name,
                ",".join(user.recent_parts),
                user.environment,
                user.equipment,
                user.condition,
                user.height if user.height else "",
                user.weight if user.weight else "",
                user.smm if user.smm else "",
                user.body_fat if user.body_fat else "",
                recommend.get("종목", ""),
                recommend.get("루틴", ""),
                recommend.get("주의", "")
            ])

    def load_records(self):
        records = []
        if not os.path.exists(self.log_path):
            return records
        with open(self.log_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(row)
        return records

    def get_user_history(self, name: str):
        records = self.load_records()
        return [r for r in records if r["이름"] == name]
