# HOWTO find anagrams for phrases

Suppose we want have the phrase "let's find anagrams", and wish to 
discover that the same letters can produce the phrases 
"flat mass in danger",  "grand mess at final", and "grin 
less at mad fan",  among many others.  

Finding anagrams for a single word is straightforward, through 
_canonicalization_,  producing a unique representative for all words 
constructed from the same collection of letters.  The
[Jumbler project](https://github.com/UO-CS210/jumbler) is an example 
of this strategy.  We could try to apply this strategy to find 
anagrams for phrases, but the collection of canonical 
representatives for all phrases up to some limited length would be 
too enormous.  We must find a better way. 

## Enumerating subsets

We will again find anagrams while searching a list of words.  
However, instead of checking each individual word to determine 
whether its letters can form the whole anagram, we will try to 
assemble _collections_ of words.  We will need to systematically 
enumerate combinations of words.  Each combination will be a subset 
of the word list.  

We can enumerate subsets of a set (called the _powerset_) recursively.  
Given a set _S_, there are two possibilities: 

- Set _S_ is empty.  The only subset of _S_ is itself. (This is the 
  base case.)
- Set _S_ is not empty, so there is some element _e_ in _S_.  Let 
  _S'_ be _S \ {e}_, i.e., the set of all elements _except_ e in _S_.
  The subsets of _S_ consist of all the subsets of _S'_, and in 
  addition all the subsets of _S'_ with the addition of _e_.  In 
  other words, we just need to consider the subsets that _do_ 
  include _e_ and the subsets that _do not_ include _e_. 

We'll make this concrete by making a simple (and not very efficient) 
version of the recursive definition in Python: 

```python
"""Illustrative example: Enumerating the powerset of a set represented as a list"""

S = ['a', 'b', 'c']

def powerset(s: list[str]) -> list[list[str]]:
    """The set of subsets of s"""
    if len(s) == 0:
        # Base case: The only subset of s is s
        return [[]]
    else:
        # Recursive case.  s contains at least one element. 
        e = s[0]        #  There must be at least one element
        rest = s[1:]    #  The rest of the list
        rest_subsets = powerset(rest)  # Recursive call on shorter list
        with_e = [[e] + other for other in rest_subsets]
        without_e = rest_subsets
        return with_e + without_e

print(powerset(S))
```

This prints 
```pycon
[['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]
```

## Enumerating sets of words 

We can apply essentially the same tactic to produce combinations of 
words in a word list.  However, instead of producing _all_ 
combinations, we can produce only combinations that can be formed
from the letters in our phrase.   In pseudocode: 



