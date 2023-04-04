"""Illustrative example: Enumerating the powerset of a set represented as a list"""

S = ['a', 'b', 'c']

def powerset(s: list[str]) -> list[list[str]]:
    """The set of subsets of s"""
    if len(s) == 0:
        # Base case: The only subset of s is s
        return [[]]
    else:
        e = s[0]  #  There must be at least one element
        rest = s[1:]
        rest_subsets = powerset(rest)
        with_e = [[e] + other for other in rest_subsets]
        without_e = rest_subsets
        return with_e + without_e

print(powerset(S))

