from LA.Vector import Vector

if __name__ == '__main__':
    vec1 = Vector([5, 2])
    vec2 = Vector([5, 2])
    print(vec1)
    print(len(vec1))

    print("{}+{}={}".format(vec1, vec2, vec1 + vec2))
    print("{}+{}={}".format(vec1, vec2, vec1 - vec2))

    print("{}*{}={}".format(vec1, 3, vec1 * 3))
    print("{}*{}={}".format(3, vec2, 3 * vec2))
    print("-{}={}".format(vec2, +vec2))
    print("+{}={}".format(vec2, -vec2))

    zero2 = Vector.zero(2)
    print(zero2)
    print("{}+{}={}".format(vec2, zero2, vec2 + zero2))

    print("normalize {} is {}".format(vec2, vec2.normalize().norm()))

    try:
        zero2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}".format(zero2))
