from main import *



tests = [
    "123",          # 123
    "1 + 2 + 3",    # 6
    "8 ** 2",       # 64
    "(2 + 3) * 5",  # 25
    "10 - (3 - 2)"  # 9
]

for test in tests:
    # print(validate(test))
    print(evaluate(parse(test)))