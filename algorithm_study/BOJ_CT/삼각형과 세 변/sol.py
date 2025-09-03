import sys
sys.stdin = open('input.txt')

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break

    sides = sorted([a, b, c])

    if sides[2] >= sides[0] + sides[1]:
        print('Invalid')
        continue

    sides = set(sides)
    if len(sides) == 1:
        print('Equilateral')
    elif len(sides) == 2:
        print('Isosceles')
    else:
        print('Scalene')
