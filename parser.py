from utils import *
from rich import print


class Rule:
    def __init__(self, children):
        self.children = children

        
    def __hash__(self):
        return self.name.__hash__()

        
    def __repr__(self):
        return f"{self.name[1:-1]}" # [{str(self)}]
            
                
    def __str__(self):
        return "".join(map(str, self.children))


    # def __repr__(self):
    #     return str(self)



def parse(expr: str) -> Rule:
    from AST import GRAMMAR
    from main import dFlag

    # A list of states organized by step (i.e. number of processed tokens).
    # For each step, there is a list of states (which is a list of tokens or nodes).
    states: list[list] = []

    to_be_reduced = []

    # For each token, advance a step and add a new state.
    for token in tokenize(expr):
        states.append([])

        # if dFlag:
        #     print("Token:", token)
        #     print("States:", states)


        # For each state at the previous step, 
        # add to the current step with the newest token
        for state in states[-2] if len(states) > 1 else [[]]: 
            states[-1].append(state + [token])
        
        # We need to reduce all the new states at the current step
        to_be_reduced = list(states[-1])

        # Select a state from the current set for reducible states,
        # and add the reduction to both the set of states at this step, and
        # the set of further reducible states.
        while to_be_reduced:
            state = to_be_reduced.pop()

            for rule, alternatives in GRAMMAR.items():
                for pattern in alternatives:
                    i = -len(pattern)

                    if i == -len(state[i:]) and compare(state[i:], pattern):
                        # if dFlag: print("REDUCE", state[i:], "-->", rule)
                        reduced = state[:i] + [rule(state[i:])]
                        
                        states[-1].append(reduced)
                        # if state in states[-1]: states[-1].remove(state)
                        to_be_reduced.append(reduced)

    if dFlag: print([list(sorted(state, key=len, reverse=True)) for state in states])

    
    # Filter for accepting state; if not found return None explicitly
    for state in states[-1]:
        if len(state) == 1 and isinstance(state[0], list(GRAMMAR.keys())[0]):
            return state[0]
    return None

    
def validate(expr: str) -> str:
    parsed = parse(expr)
    return f"{{expr}} is not a valid expression." if (parsed == None) else f"{{parsed}} is a valid {{parsed.name}} expression."


def tokenize(string: str) -> list:
    from AST import TERMINALS

    tokens = []
    while string:
        for terminal in TERMINALS:
            if string.startswith(terminal) and not terminal == "":
                tokens.append(terminal)
                string = string.removeprefix(terminal)
    return tokens
