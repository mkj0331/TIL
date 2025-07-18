# PyQt5 기반 GUI 모듈
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit
)
from PyQt5.QtCore import Qt
from .user_input import UserInfo
from .recommender import recommend_exercise
from .logger import WorkoutLogger

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("헬린이 맞춤 운동 추천 서비스")
        self.logger = WorkoutLogger()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        layout.addWidget(QLabel("이름 (예: 홍길동, 선택)"))
        layout.addWidget(self.name_input)

        self.age_input = QLineEdit()
        layout.addWidget(QLabel("나이 (예: 25, 선택)"))
        layout.addWidget(self.age_input)

        self.recent_parts_input = QLineEdit()
        layout.addWidget(QLabel("최근 운동 부위 (예: 가슴,등,어깨, 선택, 복수 입력 시 콤마로 구분)"))
        layout.addWidget(self.recent_parts_input)

        self.environment_input = QLineEdit()
        layout.addWidget(QLabel("운동 환경 (예: 헬스장, 홈트, 선택)"))
        layout.addWidget(self.environment_input)

        self.equipment_input = QLineEdit()
        layout.addWidget(QLabel("헬스장 기구 보유 여부 (예: 충분, 부족, 선택)"))
        layout.addWidget(self.equipment_input)

        self.condition_input = QLineEdit()
        layout.addWidget(QLabel("몸 상태 (예: 양호, 피로, 통증, 선택)"))
        layout.addWidget(self.condition_input)

        self.height_input = QLineEdit()
        layout.addWidget(QLabel("신장(cm, 선택, 예: 175)"))
        layout.addWidget(self.height_input)

        self.weight_input = QLineEdit()
        layout.addWidget(QLabel("체중(kg, 선택, 예: 70)"))
        layout.addWidget(self.weight_input)

        self.smm_input = QLineEdit()
        layout.addWidget(QLabel("골격근량(kg, 선택, 예: 32)"))
        layout.addWidget(self.smm_input)

        self.body_fat_input = QLineEdit()
        layout.addWidget(QLabel("체지방량(kg, 선택, 예: 18)"))
        layout.addWidget(self.body_fat_input)

        self.goal_input = QLineEdit()
        layout.addWidget(QLabel("운동 목적 (예: 감량, 유지, 증량, 선택)"))
        layout.addWidget(self.goal_input)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        btn = QPushButton("운동 추천 받기")
        btn.clicked.connect(self.on_recommend)
        layout.addWidget(btn)

        self.setLayout(layout)

    def on_recommend(self):
        try:
            age = None
            if self.age_input.text():
                try:
                    age = int(self.age_input.text())
                except ValueError:
                    age = None
            user = UserInfo(
                name=self.name_input.text() or None,
                age=age,
                recent_parts=[p.strip() for p in self.recent_parts_input.text().split(",") if p.strip()],
                environment=self.environment_input.text() or None,
                equipment=self.equipment_input.text() or None,
                condition=self.condition_input.text() or None,
                height=float(self.height_input.text()) if self.height_input.text() else None,
                weight=float(self.weight_input.text()) if self.weight_input.text() else None,
                smm=float(self.smm_input.text()) if self.smm_input.text() else None,
                body_fat=float(self.body_fat_input.text()) if self.body_fat_input.text() else None,
                goal=self.goal_input.text() or None
            )
            result = recommend_exercise(user)
            self.logger.add_record(user, result)
            msg = f"[추천 결과]\n종목: {result['종목']}\n루틴: {result['루틴']}\n주의: {result['주의']}"
            self.result_box.setText(msg)
        except Exception as e:
            QMessageBox.critical(self, "오류", str(e))

def run_gui():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
