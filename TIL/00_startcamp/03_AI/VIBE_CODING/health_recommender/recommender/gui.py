# PyQt5 기반 GUI 모듈
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit
)
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
        self.recent_parts_input = QLineEdit()
        self.environment_input = QLineEdit()
        self.equipment_input = QLineEdit()
        self.condition_input = QLineEdit()
        self.height_input = QLineEdit()
        self.weight_input = QLineEdit()
        self.smm_input = QLineEdit()
        self.body_fat_input = QLineEdit()

        layout.addWidget(QLabel("이름"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("최근 운동 부위(콤마로 구분, 예: 가슴,등,어깨)"))
        layout.addWidget(self.recent_parts_input)
        layout.addWidget(QLabel("운동 환경(헬스장/홈트)"))
        layout.addWidget(self.environment_input)
        layout.addWidget(QLabel("헬스장 기구 보유 여부(충분/부족)"))
        layout.addWidget(self.equipment_input)
        layout.addWidget(QLabel("몸 상태(양호/피로/통증 등)"))
        layout.addWidget(self.condition_input)
        layout.addWidget(QLabel("신장(cm, 선택)"))
        layout.addWidget(self.height_input)
        layout.addWidget(QLabel("체중(kg, 선택)"))
        layout.addWidget(self.weight_input)
        layout.addWidget(QLabel("골격근량(kg, 선택)"))
        layout.addWidget(self.smm_input)
        layout.addWidget(QLabel("체지방량(kg, 선택)"))
        layout.addWidget(self.body_fat_input)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        btn = QPushButton("운동 추천 받기")
        btn.clicked.connect(self.on_recommend)
        layout.addWidget(btn)

        self.setLayout(layout)

    def on_recommend(self):
        try:
            user = UserInfo(
                name=self.name_input.text(),
                recent_parts=[p.strip() for p in self.recent_parts_input.text().split(",") if p.strip()],
                environment=self.environment_input.text(),
                equipment=self.equipment_input.text(),
                condition=self.condition_input.text(),
                height=float(self.height_input.text()) if self.height_input.text() else None,
                weight=float(self.weight_input.text()) if self.weight_input.text() else None,
                smm=float(self.smm_input.text()) if self.smm_input.text() else None,
                body_fat=float(self.body_fat_input.text()) if self.body_fat_input.text() else None
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
