
#python 3.5

if __name__ == '__main__':

    fruits = ["orange", "cherry", "apple", "mango"]
    # List.index()
    #----------------------

    #List.index(target value, start index, end index)
    print("index for cherry is {}".format((fruits.index("cherry"))))
    # => index for cherry is 1

    print("index for cherry is {}".format((fruits.index("cherry", 0,3))))
    # => index for cherry is 1

    try:
        print("index for cherry is {}".format((fruits.index("cherry", 0,1))))
    except ValueError:
        print("cherry is not between index 0 and 1(non inclusive)")
    #=> cherry is not between index 0 and 1(non inclusive)

    #List.append()
    #-----------------------
    fruits.append("lemon")
    print(fruits)
    #=> ['orange', 'cherry', 'apple', 'mango', 'lemon']

    #List.extend()
    #----------------------
    fruits.extend(["kiwi","banana"])
    print(fruits)
    #=> ['orange', 'cherry', 'apple', 'mango', 'lemon', 'kiwi', 'banana']

    #List.insert()
    #----------------------
    fruits.insert(0, "ham")
    print(fruits)
    #=> ['ham', 'orange', 'cherry', 'apple', 'mango', 'lemon', 'kiwi', 'banana']

    fruits.insert(fruits.index("ham"), "honey")
    print(fruits)
    #=> ['honey', 'ham', 'orange', 'cherry', 'apple', 'mango', 'lemon', 'kiwi', 'banana']

    fruits.insert((len(fruits)-1), "lime")
    print(fruits)
    #=> ['honey', 'ham', 'orange', 'cherry', 'apple', 'mango', 'lemon', 'kiwi', 'lime', 'banana']

    #List.remove()
    #----------------------
    try:
        fruits.remove(-2)
    except ValueError:
        print("remove doesn't take index as argument but a value")
    #=> remove doesn't take index as argument but a value

    fruits.remove("ham")
    print(fruits)
    #=> ['honey', 'orange', 'cherry', 'apple', 'mango', 'lemon', 'kiwi', 'lime', 'banana']

    #List.pop()
    #---------------------
    fruits.pop(0)
    print(fruits)
    # => ['orange', 'cherry', 'apple', 'mango', 'lemon', 'kiwi', 'lime', 'banana']

    fruits.pop((len(fruits)-1))
    print(fruits)
    #=> ['orange', 'cherry', 'apple', 'mango', 'lemon', 'kiwi', 'lime']
    #len(fruits) throws an IndexError, out of range

    fruits.pop(2)
    print(fruits)
    #=> ['orange', 'cherry', 'mango', 'lemon', 'kiwi', 'lime']








