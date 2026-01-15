# from utils import *
# from parser import Rule, TERMINALS

# TERMINALS: set
# rule: Rule
# debug: bool


# def partition(expected: set, expr: str, sep: list) -> list|None:
#     # print(expected, expr, sep)
#     # {'print(f"split: {expr} with {sep}")' if debug else ''}

#     if not sep: return [expr] if expr else []

#     x = sep.pop()
#     if x in expr:
#         segments = (list(c for c in expr) if x == "" else expr.split(x, expr.count(x)))
#         print(x, segments)
#         for i in range(len(segments)):
#             print("Iter:", i, "|", segments[i:], "|", set(t for t in TERMINALS if t in "".join(segments[i:])), set(t for t in TERMINALS if t in "".join(segments[i:])).difference(expected))
#             if set(t for t in TERMINALS if t in "".join(segments[i:])).issubset(expected):
#                 left = partition(expected, f"{x}".join(segments[:i]), sep)
#                 right = f"{x}".join(segments[i:])
#                 print("L", left, "R", right)
#                 return None if (left == None) else left + [x] + ([right] if right else [])

#     return None


# def l_partition(t, e, s): 
#     split = partition(t, e[::-1], s[::-1])
#     return [s[::-1] for s in split][::-1] if split else None


# # print(l_partition(
# #     {'', ' ** ', '9', '3', ')', '1', ' / ', '(', '4', '5', '6', '.', '7', ' // ', '8', '2', '0'}, "(2 + 3) * 5", [' * ']
# # ))

# print(partition(
#     {'', ' ** ', '9', '3', ')', '1', ' / ', '(', '4', '5', '6', '.', '7', ' // ', '8', '2', '0'}, "(2 + 3) * 5", [' * ']
# ))

x = "1"
for x in "123214124":
    print(x)