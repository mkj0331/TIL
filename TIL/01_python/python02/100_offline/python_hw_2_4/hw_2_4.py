# 문제
# 동물의 특성을 가진 클래스를 상속과 다형성을 활용하여 구현하시오.

# 요구사항
# 코드를 실행하고, 출력 결과를 확인한다.

# 아래에 코드를 작성하시오.

# Animal 클래스를 정의한다.
class Animal:
    # Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
    def __init__(self, name): # name : 각 동물 인스턴스의 이름을 기록할 변수
        self.name = name
    
    # Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
    def speak(self): # why?
        pass
    # Animal class를 상속받을 자식 클래스들이 모두 speak 메서드를 각자의 역할로써 정의하고 있다.
    # 즉, 하위 클래스들이 모두 공통적으로 speak 메서드를 가지고 있을 것이다라는 사실을 명시
        
# Dog와 Cat 클래스를 정의하고, Animal 클래스를 상속받는다.
class Dog(Animal):
    # Dog 클래스는 speak 메서드를 오버라이딩하여 "Woof!"를 반환한다.
    def speak(self):
        return 'Woof!'
        
class Cat(Animal):
    # Cat 클래스는 speak 메서드를 오버라이딩하여 "Meow!"를 반환한다.
    def speak(self):
        return 'Meow!'

# Flyer와 Swimmer 클래스를 정의한다.
class Flyer:
    # Flyer 클래스는 fly 메서드를 가진다. 이 메서드는 "Flying"을 반환한다.
    def fly(self):
        return 'Flying'
    
class Swimmer:    
    # Swimmer 클래스는 swim 메서드를 가진다. 이 메서드는 "Swimming"을 반환한다.
    def swim(self):
        return 'Swimming'

# Duck 클래스를 정의하고, Flyer와 Swimmer 클래스를 다중 상속받는다.
    # Duck 클래스는 Animal 클래스를 상속받고, 이름을 인자로 받는 생성자 메서드를 가진다.
    # Duck 클래스는 speak 메서드를 오버라이딩하여 "Quack!"을 반환한다.  
class Duck(Flyer, Swimmer, Animal):
    def speak(self):
        return 'Quack!'

# make_animal_speak 함수를 정의한다.
    # 이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
def make_animal_speak(instance):
    print(instance.speak())

dog1 = Dog("말티즈")
cat1 = Cat("페르시안 블루")
duck1 = Duck("거위")

make_animal_speak(dog1)
make_animal_speak(cat1)
make_animal_speak(duck1)
print(duck1.fly())
print(duck1.swim())