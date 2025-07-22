# 아래에 코드를 작성하시오.

# Product 클래스를 정의한다.
class Product:
    # Product의 인스턴스 수를 기록할 수 있는 클래스 변수 product_count를 정의하고, 0을 할당한다.
    product_count = 0
    # 생성자 메서드를 정의한다.
        # 생성자 메서드는 상품의 이름(name)과 가격(price)을 인자로 받는다.
        # 각 인스턴스는 고유한 이름과 가격을 담을 수 있는 name과 price 변수를 가지고, 인자로 넘겨받은 값을 할당받는다.
    def __init__(self, name, price):
        self.name = name
        self.price = price 
        # 인스턴스가 생성될 때마다 product_count가 1 증가해야 한다.
            # product_count는 클래스 변수이므로 인스턴스가 직접적으로 클래스 변수를 변화시키지 않는다.
        Product.product_count += 1

    # 상품의 정보를 출력하는 display_info 인스턴스 메서드를 정의한다.
    def display_info(self):
        # 이 함수의 본 역할은? 상품의 정보를 출력하는 것!
        # print(self.name, self.price)
        # return self.name, self.price # 반환 값을 여러 객체로 만들면, 파이썬이 알아서 튜플로 묶어준다.
        return f"상품명: {self.name}, 가격: {self.price}원"

# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 정보를 출력한다.
p1 = Product('사과', 1000)
p2 = Product('바나나', 1500)
print(p1.display_info())
print(p2.display_info())

# Product 클래스의 product_count를 출력한다.
pc = Product.product_count
print(f"총 상품 수: {pc}")