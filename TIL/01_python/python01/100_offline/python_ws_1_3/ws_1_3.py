import module_ws13

users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

# 아래에 코드를 작성하시오.

# 나이가 18세 이상인 사용자를 필터링하는 함수를 작성하시오.
def filter_age(users):
    for user in users:
        if user['age'] < 18:
            users.remove(user)
    return users            

# 활성화된(is_active가 True인) 사용자를 필터링하는 함수를 작성하시오.
def filter_active(users):
    for user in users:
        if not user['is_active']:
            users.remove(user)
    return users

# 나이가 18세 이상이고 활성화된 사용자를 필터링하는 함수를 작성하시오.
def filter_all(users):
    res = []
    for user in users:
        if (user['age'] >= 18) and (user['is_active']):
            res.append(user)
    return res

# 위의 함수를 별도의 모듈로 작성하고, 이를 메인 파일에서 불러와 사용하시오.
a = module_ws13.filter_age(users)
print(f"Adults: {a}")

b = module_ws13.filter_active(users)
print(f"Active Users: {b}")

c = module_ws13.filter_all(users)
print(f"Adult Active Users: {c}")