# ერთი ტოლობით იქმნება ცვლადი
name = "Ioane"

# ორი ტოლობით ხდება მარცხენა და მარჯვენა მნიშვნელობების შედარება
print(5 == 5)

# ძახილის ნიშანი და ტოლობა - არ არის ტოლი
print(5 != 6)



for i in range(41):
    print(i)
"""
for არის ციკლის keyword

i არის საიტერაციო ცვლადი, მთვლელი  (იტერაცია ნიშნავს განმეორებას)

in range არის დიაპაზონში

range(20) ნიშნავს, რომ შეიქმნება მათემატიკური მიმდევრობა რომლის სიგრძეა 20

range არის მეთოდი რომელსაც არგუმენტად გადაეცა მნიშვნელობა 20    
"""


i = 0
while  i < 41:
    print(i)
    i += 1  # იგივეა რაც i = i +1 
"""
i = 0 არის საიტერაციო ცვლადის დეკლარაცია

while(სანამ) არის ციკლის შესაქმნელად საჭირო keyword-ი

ციკლი იმუშავებს მანამ, სანამ i ნაკლები იქნება 41-ზე

თითოეულ დატრიალებაზე დაიპრინტება საიტერაციო ცვლადი i, რომლის მნიშვნელობაც გაიზრდება 1 - ით

i += 1 ეს არის საიტერაციო ცვლადის ინკრემენტაცია (გაზრდა)       """                                    