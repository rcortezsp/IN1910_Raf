def fibonacci(n):
    F0 = 0
    F1 = 1
    if n == 2:
        return (F0+F1)
    elif n == 1:
        return F1
    elif n == 0:
        return F0
    else:
        return fibonacci(n-1)+fibonacci(n-2)


class Fibonacci:
    def __init__(self):
        self.memory = {0: 1, 1: 1}

    def __call__(self, n):

        if n in self.memory.keys():
            return self.memory[n]
        else:
            for n_n in range(2,n+1):
                self.memory[n_n] = self.memory[n_n-1] + self.memory[n_n-2]
            return self.memory[n]
        pass

class Factorial:
    def __init__(self):
        self.memory = {0: 1}

    def __call__(self, n):

        if n in self.memory.keys():
            return self.memory[n]
        else:
            for n_n in range(1,n+1):
                self.memory[n_n] = n_n* self.memory[n_n-1]
            return self.memory[n]
        pass


if __name__ == "__main__":
    for n in range(1,11):
        print(f'F{n}:{fibonacci(n)}')

    fib = Fibonacci()
    print(fib(100))

    def test_fibonacci():
        computed = []
        for i in range(1,11):
            computed.append(fibonacci(i))
        assert computed == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_Factorial():
        f = Factorial()
        computed = []
        for i in range(6):
            computed.append(f(i))

        assert computed == [1, 1, 2, 6, 24, 120]

    test_fibonacci()
    test_Factorial()
