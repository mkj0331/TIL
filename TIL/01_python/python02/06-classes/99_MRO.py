O = object
class D(O): pass
class E(O): pass
class F(O): pass
class B(D, E): pass
class C(F, D): pass
class A(B, C): pass

# A 클래스의 상속 탐색 순서를 출력
print(A.__mro__) 
# C3 선형화 규칙 -> 머리를 기준으로 다른 라인에 해당 머리가 머리가 아닌 곳에 있으면 건너 뜀!

