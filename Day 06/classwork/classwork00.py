# creating a program that will tell the user his/her age after 3 years

# დავადეკლარირე int ტიპის ცვლადი სახელად age და მნიშვნელობად მივანიჭე input("enter your age: ")
age = int(input("enter your age: "))

# დავადეკლარირე int ტიპის ცვლადი სახელად new_age და მნიშვნელობად მივანიჭე age + 3
new_age = (age + 3)

# print ფუნქციის მეშვეობით ტერმინალში გამოვიტანე after three years your age will be; 
# გამოვიძახე new_age ცვლადი და print ფუნქციით მისი მნიშვნელობაც გამოვიტანე ტერმინალში 
print("after three years your age will be", new_age)