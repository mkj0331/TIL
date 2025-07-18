# 사용자 정보 입력 처리 모듈
from dataclasses import dataclass
from typing import Optional

@dataclass
class UserInfo:
    name: str
    recent_parts: list[str]  # 최근 운동 부위(복수 선택 가능)
    environment: str  # '헬스장' 또는 '홈트'
    equipment: str    # '충분', '부족' 등
    condition: str    # '양호', '피로', '통증' 등
    height: Optional[float] = None
    weight: Optional[float] = None
    smm: Optional[float] = None  # 골격근량(선택)
    body_fat: Optional[float] = None  # 체지방량(선택)

def input_user_info() -> UserInfo:
    print("[헬린이 맞춤 운동 추천 서비스] 사용자 정보를 입력하세요.")
    name = input("이름: ")
    recent_parts_raw = input("가장 최근에 한 운동 부위(복수 선택 가능, 예: 가슴,등,어깨,이두,삼두,하체,유산소): ")
    recent_parts = [part.strip() for part in recent_parts_raw.split(',') if part.strip()]
    environment = input("운동 환경(헬스장/홈트): ")
    equipment = input("헬스장 기구 보유 여부(충분/부족): ")
    condition = input("몸 상태(양호/피로/통증 등): ")
    try:
        height = float(input("신장(cm, 선택): ") or 0) or None
    except ValueError:
        height = None
    try:
        weight = float(input("체중(kg, 선택): ") or 0) or None
    except ValueError:
        weight = None
    try:
        smm = float(input("골격근량(kg, 선택): ") or 0) or None
    except ValueError:
        smm = None
    try:
        body_fat = float(input("체지방량(kg, 선택): ") or 0) or None
    except ValueError:
        body_fat = None
    return UserInfo(
        name=name,
        recent_parts=recent_parts,
        environment=environment,
        equipment=equipment,
        condition=condition,
        height=height,
        weight=weight,
        smm=smm,
        body_fat=body_fat
    )
