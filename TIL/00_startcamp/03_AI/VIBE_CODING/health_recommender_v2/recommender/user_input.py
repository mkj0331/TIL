# 사용자 정보 입력 처리 모듈
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class UserInfo:
    name: Optional[str] = None
    age: Optional[int] = None
    recent_parts: Optional[List[str]] = field(default_factory=list)
    environment: Optional[str] = None  # '헬스장' 또는 '홈트'
    equipment: Optional[str] = None    # '충분', '부족' 등
    condition: Optional[str] = None    # '양호', '피로', '통증' 등
    height: Optional[float] = None
    weight: Optional[float] = None
    smm: Optional[float] = None  # 골격근량(선택)
    body_fat: Optional[float] = None  # 체지방량(선택)
    goal: Optional[str] = None  # '감량', '유지', '증량' 등

def input_user_info() -> UserInfo:
    print("[헬린이 맞춤 운동 추천 서비스] 사용자 정보를 입력하세요.")
    name = input("이름 (예: 홍길동, 선택): ") or None
    try:
        age = int(input("나이 (예: 25, 선택): ") or 0) or None
    except ValueError:
        age = None
    recent_parts_raw = input("가장 최근에 한 운동 부위 (예: 가슴,등,어깨, 선택, 복수 입력 시 콤마로 구분): ") or ""
    recent_parts = [part.strip() for part in recent_parts_raw.split(',') if part.strip()]
    environment = input("운동 환경 (예: 헬스장, 홈트, X): ") or None
    equipment = input("헬스장 기구 보유 여부 (예: 충분, 부족, X): ") or None
    condition = input("몸 상태 (예: 양호, 피로, 통증, X): ") or None
    try:
        height = float(input("신장(cm, 선택, 예: 175): ") or 0) or None
    except ValueError:
        height = None
    try:
        weight = float(input("체중(kg, 선택, 예: 70): ") or 0) or None
    except ValueError:
        weight = None
    try:
        smm = float(input("골격근량(kg, 선택, 예: 32): ") or 0) or None
    except ValueError:
        smm = None
    try:
        body_fat = float(input("체지방량(kg, 선택, 예: 18): ") or 0) or None
    except ValueError:
        body_fat = None
    goal = input("운동 목적 (예: 감량, 유지, 증량, 선택): ") or None
    return UserInfo(
        name=name,
        age=age,
        recent_parts=recent_parts,
        environment=environment,
        equipment=equipment,
        condition=condition,
        height=height,
        weight=weight,
        smm=smm,
        body_fat=body_fat,
        goal=goal
    )
