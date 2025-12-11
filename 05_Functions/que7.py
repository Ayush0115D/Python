def print_kwargs(**kwargs):#function to take multiple keyword arguments,we have now 2 types of arguments/parameters
    for key, value in kwargs.items(): #kwargs is a dictionary, so we can use items() to get key and value pairs
        print(f"{key}: {value}") #another syntax to print key and value in dictionary format


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")