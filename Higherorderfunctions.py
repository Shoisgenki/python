# accepts function as an argument

# or

# returns a function    (Functions are also treated as objects)


# def loud(m):
   # return m.upper()


# def quiet(m):
   # return m.lower()


# def hello(n):
   # text = n("Hello")
   # print(text)


# hello(loud)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)

print(divide(10))


