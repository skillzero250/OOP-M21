class Selector:
    def __init__(self, values):
        self.values = values

    def get_odds(self):
        return [value for value in self.values if value % 2 != 0]

    def get_evens(self):
        return [value for value in self.values if value % 2 == 0]


values = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))