b = input("Enter any number")
i = 1
while i< b:
    print(i)
    i += 1
# Adding one decorator
def real_fun(f):
    def inner_fun(s):
        return f(s) + " how are you?"
    return inner_fun

@real_fun
def fun(s):
    return s

# Use the decorated function
s = "hii bro!"
res = fun(s)
print(res)