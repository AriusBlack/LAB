if __name__ == '__main__':

    #List Comprehensions :
    #---------------------

    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)
    #=> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    squares_2 = list(map(lambda x: x**2, range(10)))
    print(squares_2)
    #=> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    squares_3 = [x**2 for x in range(10)]
    print(squares_3)
    #=> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    squares_4 = list(map(lambda x: x**2, squares))
    print(squares_4)
    #=> [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]

    for x in squares:
        print(x)
    #=> 0
    # 1
    # 4
    # 9
    # 16
    # 25
    # 36
    # 49
    # 64
    # 81
