"""
1)შექმენი ფუნქცია სახელად say_hello(), რომელიც ბეჭდავს ფრაზას:
hello world!
"""
def say_hello():
    print("hello world!")

say_hello()

"""
2)შექმენი ფუნქცია greet(name), რომელიც იღებს ერთ არგუმენტს — name— და ბეჭდავს:
გამარჯობა, <სახელი>!
"""
def greet(name):
    print("გამარჯობა " + name)

greet("andria")


"""
3)შექმენი ფუნქცია multiply_by_two(number), რომელიც იღებს ერთ რიცხვს და ბეჭდავს მის ორმაგს.
"""
def multiply_by_two(number):
    print(number * 2)

multiply_by_two(5)