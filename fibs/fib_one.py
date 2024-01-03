class FibonacciRecursive:
    def main(self, number: int) -> int:
        return number if number <= 1 else (self.main(number - 1)) + (self.main(number - 2))

class FibonnaciIterative:
    def main(self, number: int) -> int:
        if number <= 1:
            return number
        
        sequence: list = [0, 1] 
        # sequence: list = [sequence[fib_num - 1] + sequence[fib_num - 2] for fib_num in range(2, number + 1)]
        # print(sequence_two)

        for fib_num in range(2, number + 1):
            sequence.append(sequence[fib_num - 1] + sequence[fib_num - 2])

        return sequence[number]

my_fib: object = FibonacciRecursive()
print(my_fib.main(6))

my_fib: object = FibonnaciIterative()
print(my_fib.main(6))
