def clean_name(name):
    name = name.strip()
    name = name.capitalize()
    return name

def make_greeting(name):
    return f"안녕하세요, {name}님!"
    
def process_namelist(name_list):
    for i in range(len(name_list)):
        if name_list[i] != " ":
            name_list[i] = make_greeting(clean_name(name_list[i]))
        else:
            name_list.remove(name_list[i])
    return name_list

# ----------------------------------------------------
# 아래 코드는 절대 수정하지 마시오.
# ----------------------------------------------------
raw_names = [
    "  홍길동",
    "김싸피 ",
    "   ",
    "lee sunsin"
]
result = process_namelist(raw_names)
print(result)