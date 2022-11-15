class Number:
    def __init__(self) -> None:
        self.age = 10

    def incage(self):
        print(self.age + 1)


x = Number()

l = ["X", "X", "X"]
s = set(l)
print(len(set(l)) == 1)
print(s.pop())
