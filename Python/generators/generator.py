def generator():
    yield 1
    yield 2
    yield 3
    yield 4

iterator = generator()

print(iterator)

print(iterator.__next__())
print()

for value in iterator:
    print(value)

print()
def square_genertor():
    n=1
    while n<=10:
        sq = n**2
        yield sq
        n+=1

iterator_sq = square_genertor()

for value in square_genertor():
    print(value)

print(type(iterator_sq))