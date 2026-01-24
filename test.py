from main import *
from rich import print



tests = [
    # ("123", 123),          # 123
    # ("1 + 2 + 3", 6),    # 6
    # ("8 ** 2", 64),       # 64
    # ("(2 + 3) * 5", 25),  # 25
    ("10 - (3 - 2)", 9),  # 9
    # ("10 - 3 - 2", 5)  # 5
]

# tests = [
#     ("(x)", "(x)")
# ]

for test, solution in tests:
    # print(validate(test))
    AST = parse(test)
    print("\nPARSED\n")
    print(AST)
    print(type(AST))
    result = evaluate(AST)
    print(result if result == solution else f"ERROR: value of {test} should be {solution}, but received {result or "False|None"}")
    print()
