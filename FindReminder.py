a = int(input())
tests = []
for i in range(a):
    tests.append([int(i) for i in input().split()])
for i in tests:
    print(i[0]%i[1]
