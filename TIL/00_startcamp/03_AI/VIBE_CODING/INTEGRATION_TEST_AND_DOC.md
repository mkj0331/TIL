# 통합 테스트 및 실행 방법 안내

## 1. 파이썬 환경 준비
- Python 3.8 이상이 설치되어 있어야 합니다.
- 설치 확인: 
  ```bash
  python --version
  ```

## 2. 필수 패키지 설치
- PyQt5 등 필요한 패키지를 설치합니다.
- 설치 명령:
  ```bash
  pip install pyqt5
  ```

## 3. 프로젝트 폴더 구조 확인
- 아래와 같은 구조로 파일이 준비되어 있어야 합니다.
  ```
  health_recommender/
  ├── main.py
  ├── recommender/
  │   ├── __init__.py
  │   ├── user_input.py
  │   ├── recommender.py
  │   ├── logger.py
  │   └── gui.py
  ├── data/
  │   └── sample_users.csv
  ├── tests/
  │   └── test_recommender.py
  └── README.md
  ```

## 4. 단위 테스트 실행
- 추천 알고리즘 및 기록 관리 모듈의 테스트를 실행합니다.
- 명령어:
  ```bash
  set PYTHONPATH=.
  python -m unittest health_recommender/tests/test_recommender.py
  ```
- (Windows 환경 기준, 경로 구분자와 PYTHONPATH 설정에 주의)
- 테스트가 정상적으로 통과하면, 주요 기능이 정상 동작함을 의미합니다.

## 5. 예시 데이터 확인 및 활용
- `data/sample_users.csv` 파일을 열어 예시 사용자 데이터를 확인합니다.
- 필요시 데이터를 수정하거나 추가할 수 있습니다.

## 6. GUI 실행 및 통합 테스트
- GUI를 통해 실제 추천 및 기록 기능을 테스트합니다.
- 실행 명령:
  ```bash
  python health_recommender/main.py
  ```
- 실행 후, 각 입력란에 정보를 입력하고 '운동 추천 받기' 버튼을 클릭합니다.
- 추천 결과가 화면에 표시되고, 기록이 자동 저장됩니다.

## 7. 운동 기록 확인
- 기록은 `data/workout_log.csv` 파일에 저장됩니다.
- 파일을 열어 추천 이력 및 입력 정보를 확인할 수 있습니다.

## 8. 오류 및 문제 해결
- PyQt5 미설치 시, 설치 안내 메시지가 출력됩니다. 위 설치 명령을 참고하세요.
- 기타 오류 발생 시, 에러 메시지를 확인하고 입력값을 점검하세요.

## 9. 확장 및 커스터마이즈
- 알고리즘, 입력 항목, 기록 방식 등은 각 모듈별로 자유롭게 수정 및 확장 가능합니다.
- 추가 기능 요청 시 README.md 및 INTEGRATION_TEST_AND_DOC.md에 문서화하세요.

---
10년차 파이썬 개발자의 관점에서, 모든 단계별 실행 방법을 상세히 안내하였습니다. 실제 운영 환경에 맞게 경로 및 명령어를 조정해 사용하세요.
