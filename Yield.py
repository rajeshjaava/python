def test(n):
    return n*n

def getSquare(n):
    for i in range(n):
        yield test(i)

sq = getSquare(10)
for i in sq:
    print(i)