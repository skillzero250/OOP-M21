class A:
    def __str__(self):
        return "A"

    def hello(self):
        print("Hello")


class B:
    def __str__(self):
        return "B"

    def good_evening(self):
        print("Good evening")


class C(A, B):
    def __getattribute__(self, name):
        if name == "__str__":
            return super().__getattribute__("__str__")
        return super().__getattribute__(name)


class D(A, B):
    def __getattribute__(self, name):
        if name == "__str__":
            return super().__getattribute__("B__str__")
        return super().__getattribute__(name)


c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)