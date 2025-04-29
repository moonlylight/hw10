from math import gcd

class Rational:
    def __init__(self, numerator, denominator=None):
        if denominator is None:
            parts = numerator.split('/')
            numerator, denominator = int(parts[0]), int(parts[1])
        self.n = numerator
        self.d = denominator
        self.reduce()

    def reduce(self):
        common_divisor = gcd(self.n, self.d)
        self.n //= common_divisor
        self.d //= common_divisor

    def __add__(self, other):
        if isinstance(other, Rational):
            numerator = self.n * other.d + other.n * self.d
            denominator = self.d * other.d
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.n + other * self.d
            return Rational(numerator, self.d)

    def __radd__(self, other):
        return self + other

    def __call__(self):
        return self.n / self.d

    def __str__(self):
        return f"{self.n}/{self.d}"

class RationalList:
    def __init__(self):
        self.elements = []

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self.elements[index] = value
        else:
            raise ValueError("Only Rational objects can be added to RationalList")

    def __len__(self):
        return len(self.elements)

    def __add__(self, other):
        new_list = RationalList()
        new_list.elements = self.elements.copy()
        if isinstance(other, RationalList):
            new_list.elements += other.elements
        elif isinstance(other, (Rational, int)):
            new_list.elements.append(Rational(other, 1) if isinstance(other, int) else other)
        else:
            raise ValueError("Unsupported type for addition with RationalList")
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.elements += other.elements
        elif isinstance(other, (Rational, int)):
            self.elements.append(Rational(other, 1) if isinstance(other, int) else other)
        else:
            raise ValueError("Unsupported type for addition with RationalList")
        return self

    def append(self, value):
        if isinstance(value, Rational):
            self.elements.append(value)
        else:
            raise ValueError("Only Rational objects can be appended to RationalList")

    def sum(self):
        total = Rational(0, 1)
        for element in self.elements:
            total += element
        return total

    def __iter__(self):
        self.sorted_elements = sorted(self.elements, key=lambda x: (-x.d, -x.n))
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.sorted_elements):
            result = self.sorted_elements[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

def process_input_files(input_files, output_file):
    rational_list = RationalList()
    for input_file in input_files:
        with open(input_file, 'r') as infile:
            for line in infile:
                numbers = line.strip().split()
                for number in numbers:
                    if '/' in number:
                        try:
                            rational_list.append(Rational(number))
                        except ValueError:
                            continue
                    else:
                        try:
                            rational_list.append(Rational(int(number), 1))
                        except ValueError:
                            continue
    with open(output_file, 'w') as outfile:
        outfile.write(f"{rational_list.sum()()}\n")
        for rational in rational_list:
            outfile.write(f"{rational}\n")

input_files = ["input01.txt", "input02.txt", "input03.txt"]
output_file = "output.txt"

process_input_files(input_files, output_file)

rational_list = RationalList()
rational_list.append(Rational("1/3"))
rational_list.append(Rational("2/5"))
rational_list.append(Rational("4/5"))
rational_list.append(Rational("5/7"))

with open(output_file, 'a') as outfile:
    for rational in rational_list:
        outfile.write(f"{rational}\n")