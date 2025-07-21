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