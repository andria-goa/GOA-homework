
password = "secret word" #ვქმნით პაროლს ანუ ცვლადს
guess = input() # ვაწერინებთ მომხმარებელს შეყვანილ პაროლს
while guess != password: # სანამ მომხმარებელი არ შეიყვანს სწორ პაროლს გამეორდება
    guess = input() # მომხმარებელი ისევ უნდა შეიყვანოს პაროლი
print("Access granted") # თუ მომხმარებელი სწორ პაროლს შეიყვანს მაშინ გამოაქვს ეს ტექსტი


number = int(input())
if number > 3:
    print("GOA")
else:
    print("AOG")