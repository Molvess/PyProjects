class MyEvenNumbers:
    def __init__(self, start=2, end=20):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end if end % 2 == 0 else end - 1
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            x = self.current
            self.current += 2
            return x
        else:
            raise StopIteration

myclass = MyEvenNumbers(start=4, end=20)

for x in myclass:
    print(x)