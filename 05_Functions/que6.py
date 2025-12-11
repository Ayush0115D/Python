def sum_all(*args): #function to multiple arguments,args is a tuple, so we can use it like a list
    # *args allows us to pass a variable number of arguments to the function
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))