from myLA.Vector import Vector

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
