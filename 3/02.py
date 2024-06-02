class ReversedList:
    def __init__(self, list):
        self.list = list[::-1]

    def __len__(self):
        return len(self.list)

    def __getitem__(self, index):
        return self.list[index]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])