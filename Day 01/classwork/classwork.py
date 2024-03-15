name = "Ioane"
surname = "Dolidze"
# name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო (მინიჭების ოპერატორი)
# ioane არის ცვლადისთვის მნიშვნელობა
print(name)
print(surname)
# print ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი


name = "Ioane" # str (tring), სტრინგია ყველაფერი რაც მოქცეულია ბრჭყალებში
age = 16 # int (integer), მთელი რიცხვი
height = 74.5 # float, ათწილადი
knows_programming = False # booLean (booL),  True ან False როცა გვქავს (True და False იწერება სულ დიდი ასოთი)
loves_homeland = True  # booLean     თუ ცვლადი შედგება ერთზე მეტი სიტყვისგან მათ ვანცალკევებთ ქვედა ტირით (snakecase-სტანდარტული)
print(name + " " + surname)


print(type(age))
print(type(name))
print(type(surname))                    
print(type(knows_programming))
print(type(height))


#print(name + " " + age) არ იმუშავებს, რადგან ცვლადების განსსხვავებულ ტიპებს (str და int) ვერ შევკრებთ, შეგვიძლია ჩავწეროთ შემდეგნაირად:
print(name + " " + str(age))