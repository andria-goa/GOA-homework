"""
1)შექმენით ფუნქცია რომელიც იღებს 2 არგუმნეტს, რიცხვს და სტრინგს, შემდეგ უნდა უნდა დააბრუნოთ სტრინგი გამრვლებული ამ რიცხვზე
მაგ:გამოძახებისას მივუთითეთ "guramchiko", 5
უნდა გამოიტანოს "guramchikoguramchikoguramchikoguramchikoguramchiko"
ამ რიცხვ არგუმენტს გაუწერეთ defaul value რომელიც იქნება 0
"""
def gamravleba(n, t=0):
    return n * t

sedegi = gamravleba("guramchiko", 5)
print(sedegi)  



"""
2)შექმენით ფუნქცია რომელიც იღებს 2 რიცხვს, სიგრძეს და სიგანეს მართკუთხედის, შემდეგ დააბრუნეთ 2 რიცხვი, ამ მართკუთხედის პერიმეტრი და ფართობი
როგორ გამოითლება მართკუთხედის ფართობი:მისი სიგრძე უნდა გავამრავლოთ მის სიგანეზე
როგორ გამოითვლება მართკუთხედის პერიმეტრი:2*(სიგრძე+სიგანე)
შემდეგ, ერთ ხაზზე შექმენით 2 ცვლადი, და გაუტოლეთ ამ ფუნქციის გამოძახებას
perimeter, area = my_func(100, 50)
შემდეგ დაწერეთ კომენტარებით რას უდრის თითოეული
"""
def rectangle_info(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area

perimeter, area = rectangle_info(100, 50)

#პერიმეტრი 300
#ფართობი 5000




"""
4)შექმენით ფუნქცია, რომელიც ხატავს ოთხუკთედს Turtle ბიბლიოკეთის გამოყენებით
"""
import turtle

def otxkudxedi():
    for hi in range(4):
        turtle.forward(100) 
        turtle.right(90)     

otxkudxedi()
turtle.done()