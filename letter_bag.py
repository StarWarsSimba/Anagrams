"""A bag of letters for finding anagrams.
Associates a cardinality (count) with each character
in the bag.
"""


def normalize(phrase: str) -> list[str]:
    """Normalize word or phrase to the
    sequence of letters we will try to match, discarding
    anything else, such as blanks and apostrophes.
    Return as a list of individual letters.
    """
    letters = []
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            letters.append(phrase[i].lower())
    return letters


class LetterBag:
    """A bag (also known as a multiset) is
    a map from keys to non-negative integers.
    A LetterBag is a bag of single character
    strings.
    """
    def __init__(self, word=""):
        """Create a LetterBag"""
        self.word = word.strip()
        normal = normalize(self.word)
        self.length = len(normal)  # Counts letters only!
        self.letters = {}
        for i in normal:
            if i not in self.letters:
                self.letters[i] = 1
            else:
                self.letters[i] += 1

    def __len__(self):
        return self.length

    def __str__(self):
        return self.word

    def __repr__(self):
        counts = [f"{ch}:{n}" for ch, n in self.letters.items() if n > 0]
        return f'LetterBag({self.word}/[{", ".join(counts)}])'

    def contains(self, other: "LetterBag") -> bool:
        """Determine whether enough of each letter in
        other LetterBag are contained in this LetterBag.
        """
        for i in other.letters:
            if i not in self.letters or self.letters[i] == 0:
                return False
            if self.letters[i] < other.letters[i]:
                return False
        return True

    def copy(self) -> "LetterBag":
        """Make a copy before mutating."""
        copy_ = LetterBag()
        copy_.word = self.word
        copy_.letters = self.letters.copy()  # Copied to avoid aliasing
        copy_.length = self.length
        return copy_

    def take(self, other: "LetterBag") -> "LetterBag":
        """Return a LetterBag after removing
        the letters in other.  Raises exception
        if any letters are not present.
        """
        bag = self.copy()
        assert bag.contains(other)
        for letter, count in other.letters.items():
            assert bag.letters[letter] >= count
            bag.letters[letter] -= count
            bag.length -= count
        return bag
