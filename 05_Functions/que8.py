def even_generator(limit):
    for i in range(2, limit + 1, 2):# start from 2, go to limit, step by 2  
     yield i #yield in place of return, it will return one value at a time, so we can use it like a generator
    # this function generates even numbers up to the limit
for num in even_generator(10):
    print(num)