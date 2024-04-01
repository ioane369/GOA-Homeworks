"""                                             Creating a street quiz
Black guy in Bensimons asks a passerby "what kind of man are you?"
according to probable answers, his fate will be decided:
1) beating
2) brotherhood
3) robbery      """

print("Black guy in Bensimons: Hey boy, what kind of man are you?")
print("""a) Get lost until I beat your ass
b) I'm from da hood  
c) I'm just a man""")

user_choice1 = input("Enter your choice: ")

if user_choice1 == "a":
    print("""You: Get lost until I beat your ass         
Black guy in Bensimons: I'll show you whos ass is going to be beaten!
(pulls out a gun and makes you look like Megamind)""")
elif user_choice1 == "b":
    print("""You: I'm from da hood
Black guy in Bensimons: Sorry my G. (Gives you a fist bump)""")
elif user_choice1 == "c":
    print("""Black guy in Bensimons: Pulls out a gun and says: ok "just a man", give me everything you have! (Leaves you with only the panties)""")
else:
    print("Invalid choice")