# 프로젝트 진입점
if __name__ == "__main__":
    try:
        from recommender.gui import run_gui
        run_gui()
    except ImportError:
        print("PyQt5가 설치되어 있지 않습니다. 'pip install pyqt5'로 설치 후 실행하세요.")
