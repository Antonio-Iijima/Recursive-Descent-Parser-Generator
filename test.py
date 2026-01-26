from main import *
from rich import print

from time import time


tests = [
    ("123", 123),
    ("1 + 2 + 3", 6),
    ("8 ** 2", 64),
    ("(2 + 3) * 5", 25),
    ("10 - (3 - 2)", 9),
    ("10 - 3 - 2", 5), 
    ("1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1", 10),
    ("1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1", 1)
]

# tests = [
#     ("(x)", "(x)")
# ]

for test, solution in tests:

    start = time()

    # print(validate(test))
    AST = parse(test)
    print("\nPARSED\n")
    print(AST)
    print(type(AST))
    result = evaluate(AST)
    print(result if result == solution else f"ERROR: value of {test} should be {solution}, but received {result or "False|None"}")
    print()

    print(f"Runtime: {time()-start}")