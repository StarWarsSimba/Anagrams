"""Find anagrams (potentially multi-word) for a word or phrase."""

import config
import io
from letter_bag import LetterBag

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def read_word_list(f: io.TextIOBase) -> list[str]:
    """Reads list of words, exactly as-is except
    for stripping off leading and trailing whitespace
    including newlines.
    """
    word_list = []
    while True:
        word = f.readline()
        if word == "":
            break
        new_word = word.strip()
        word_list.append(new_word)
    return word_list


def search(letters: LetterBag,
           candidates: list[LetterBag],
           limit: int = 500,
           seed: str = "") -> list[str]:
    """Returns a list of anagrams for letters, where
     each anagram is constructed from entries in the
     candidates list.
     """

    result = []

    # List of candidates, limit, and result list are visible to the
    # nexted function, and need not be passed to it.

    def _search(letters: LetterBag,  # The letters we can draw from
                pos: int,  # Position in list of word list letterbags
                phrase: list[str]  # The phrase we are building
                ):
        """Recursive function has the effect of adding phrases to result"""
        ### Your code for body of _search goes here
        """for candidates in position `pos`..length of candidates list:
            if this candidate can be constructed from `letters`:
                extended phrase = phrase with word added
                if using it would leave `letters` empty (length 0):
                    add the extended phrase to `result`
                else:
                    make a recursive call to try using this word,
                    with the extended phrase, the remaining letters,
                    and searching from `pos + 1`
                    """
        if len(result) >= limit:
            return
        for i in range(pos, len(candidates), 1):
            c = candidates[i]
            if letters.contains(c):
                phrase.append(str(c))
                new_letters = letters.take(c)
                if new_letters.length == 0:
                    result.append(phrase)
                    phrase.clear()
                else:
                    _search(new_letters, i + 1, phrase)

    # Initiate a single search at position 0 with an empty phrase,
    # after seeding if appropriate
    phrase = []
    _search(letters, 0, phrase)
    return result
