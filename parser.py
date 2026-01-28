from utils import *
from rich import print



class Rule:
    def __init__(self, children):
        from AST import EPSILON
        self.children = [c for c in children if not c == EPSILON]

        
    def __hash__(self):
        return self.name.__hash__()

        
    def __repr__(self):
        return f"{self.name[1:-1]}"
            
                
    def __str__(self):
        return "".join(map(str, self.children))



def parse(expr: str) -> Rule:
    from AST import GRAMMAR, is_expected, retype, OPERATORS, K, EPSILON, TERMINALS, EXPECTED_TOKENS
    from main import dFlag

    tokens = tokenize(expr)

    # A list of states organized by step (i.e. number of processed tokens).
    # For each step, there is a list of states (which is a list of tokens or nodes).
    current_states = [[]]
    future_states = []

    if dFlag:
        from AST import EXPECTED_TOKENS
        print(EXPECTED_TOKENS)
    
    # For each token, advance a step and begin processing states
    for token in tokens:
      
        # For each state at the previous step, 
        # add to the current step with the newest token
        current_states = list(map(lambda x: x + [token], current_states))
        
        # If we could have an epsilon transition, then simulate it and add it to the future states
        # if (is_expected(EPSILON, token)):
        #     current_states.extend(list(map(lambda x: x + [EPSILON], current_states)))
        #     future_states.extend(current_states)
        
        if token in OPERATORS: continue

        reducible_states = list(current_states)

        if dFlag: print("Current states", current_states)

        # We need to reduce all the new states at the current step

        # Select a state from the current set for reducible states,
        # and add the reduction to both the set of states at this step, and
        # the set of further reducible states.
        while reducible_states:
            state = reducible_states.pop()

            for rule, alternatives in GRAMMAR.items():
                for pattern in alternatives:
                    idx = len(state)-len(pattern)
                    reducible = state[idx:]

                    # Reduce only states that can produce a valid parse
                    if (
                        retype(state[-1]) in pattern
                        and len(pattern) == len(reducible)
                        and compare(reducible, pattern)
                    ):
                        reduced = state[:idx] + [rule(reducible)]

                        reducible_states.append(reduced)

                        # Proceed with only states that can produce a valid parse using maximum K-token validation;
                        # idx == k means the validation has reached the first token, which is vacuously true.
                        if all(idx == k or is_expected(reduced[idx-k], reduced[idx-k-1]) for k in range(min(K, len(reduced)))):
                            future_states.append(reduced)
                            
        current_states, future_states = future_states or current_states, []

        if dFlag: 
            print("Future states", current_states)
            print()
            
    # Filter for accepting state; if not found return None explicitly
    acceptable_states = [ 
        state[0] for state in current_states if (
            len(state) == 1 
            and isinstance(state[0], list(GRAMMAR.keys())[0]) 
            and str(state[0]) == expr
        )
    ]

    print(list(map(str, acceptable_states)))

    return acceptable_states[0] if acceptable_states else None
    


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
                break
        else: raise SyntaxError(f"unrecognized token in input '{string}'")

    return tokens
