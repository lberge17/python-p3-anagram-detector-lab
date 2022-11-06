class Anagram:
    
    def __init__(self, word):
        self._word = word

    def match(self, list):
        return [word for word in list if set(word) == set(self._word)]