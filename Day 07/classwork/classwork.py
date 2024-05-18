# state - მდგომარეობა

"""                                                  BOOLEAN TYPE DATA

boolean ტიპის მონაცემებს აქვთ ორი შესაძლო მნიშვნელობა: True და False  
"""
print(2 > 10)   # result: False
print(10 > 2)   # result: True

# ლოგიკური ოპერატორი იღებს რამოდენიმე input-ს და გვაძლევს ერთ output-ს
input1 = True
input2 = False
input3 = False
print(input1 or input2 or input3)   # result: True


#                                                   LOGICAL OPERATION TYPES

"""                                                 "or" logical operation 

or შედარების ოპერატორი არამკაცრია, 
რაც ნიშნავს, რომ თუ მოცემულ პირობათაგან ერთი მაინც არის ჭეშმარიტი, საბოლოოდ გამოსახულება ჭეშმარიტია
 მაგ: 
"""
number1 = 12
number2 = 11

print(number1 > number2 or number2 > number1)   # result: True

#                                                   "and" logical operation
"""   
and შედარების ოპერატორი მკაცრია,
რაც ნიშნავს, რომ თუ მოცემულ პირობათაგან ერთი მაინც არის მცდარი, საბოლოოდ გამოსახულება მცდარია
მაგ:                
"""
print(number1 > number2 and number2 > number1)   # result: False

# ლოგიკური ოპერაციის შედეგი ყოველთვის არის boolean ტიპის