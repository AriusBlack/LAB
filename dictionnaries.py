if __name__ == '__main__':

    # Accesing a dictionnary in a list:

    fruits.extend({"banana" : 2})
    print(fruits)

    # for f in fruits.index("banana").keys():
    #     print(f)
    # => for f in fruits.index("banana").keys():
    # AttributeError: 'int' object has no attribute 'keys'

    print(fruits[-1].values())
