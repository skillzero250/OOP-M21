class MinMaxWordFinder():

    def __init__(self):
        self.minword = 0
        self.maxword = 0
        self.list_word = []

    def add_sentence(self, text):
        self.list_word += text.split()
        self.minword = len(min(self.list_word, key=len))
        self.maxword = len(max(self.list_word, key=len))

    def shortest_words(self):
        return sorted(list(filter(lambda x: len(x) == self.minword, self.list_word)))

    def longest_words(self):
        return sorted(set(filter(lambda x: len(x) == self.maxword, self.list_word)))


# Ваш код

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('abc')
finder.add_sentence('world')
finder.add_sentence('def')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))