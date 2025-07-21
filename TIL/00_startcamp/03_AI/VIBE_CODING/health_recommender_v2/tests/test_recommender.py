# 추천 알고리즘 테스트 코드
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from health_recommender.recommender.user_input import UserInfo
from health_recommender.recommender.recommender import recommend_exercise
from health_recommender.recommender.logger import WorkoutLogger

class TestRecommender(unittest.TestCase):
    def test_recommend_exercise_logic(self):
        user = UserInfo(
            name="테스트유저",
            recent_parts=["가슴", "삼두"],
            environment="헬스장",
            equipment="충분",
            condition="양호",
            height=175,
            weight=75,
            smm=32,
            body_fat=18
        )
        result = recommend_exercise(user)
        self.assertIn("종목", result)
        self.assertIn("루틴", result)
        self.assertIn("주의", result)
        self.assertTrue(result["종목"])

    def test_logger_add_and_load(self):
        log_path = "test_workout_log.csv"
        logger = WorkoutLogger(log_path)
        user = UserInfo(
            name="홍길동",
            recent_parts=["등", "어깨"],
            environment="홈트",
            equipment="부족",
            condition="피로",
            height=168,
            weight=68,
            smm=28,
            body_fat=22
        )
        recommend = recommend_exercise(user)
        logger.add_record(user, recommend)
        records = logger.load_records()
        self.assertTrue(any(r["이름"] == "홍길동" for r in records))
        # 테스트 후 파일 삭제
        if os.path.exists(log_path):
            os.remove(log_path)

if __name__ == "__main__":
    unittest.main()
