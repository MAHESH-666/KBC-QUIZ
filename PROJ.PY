print("WELCOME TO KOUN BANEGA CROREPATI")
money=0
for i in range(1):
    print(" ")
print("Before We Start Game, The Most Important Questions..??")
Q = input("Who is Prime Minister of India: ")
if Q =="narendra modi":
    print("Congrats....!")
else:
    print("wrong Answer")
    print("OKAY..Let's Begin The Show...!")

Question_list=["1.Who Won IPL 2021 Title ??? ",
               "2.Who is The Brand Ambassador of AUDI ??",
               "3.Will You Slap Your Girlfriend For 100M$ ??",
               "4.Who Invented The BULB ?",
               "5.Which of These Terms can only be used for Women ??"]

Answer_List=["CSK",
             "Virat Kohli",
             "100% YES",
             "Thomas Edison",
             "Suhagan"]

option1 = ["A. MI",
           "B. CSK",
           "C. SRH",
           "D. KKR"]


option2 = ["A. Ratan Tata",
           "B. Virat Kohli",
           "C. M.S DHONI",
           "D. ELON MUSK"]


option3 = ["A. yes",
           "B. no",
           "C. Never",
           "D. 100% YES"]


option4 = ["A. Elon MUsk",
           "B. Thomas Edison",
           "C. Modi ji",
           "D. Amit Shah"]


option5 = ["A. Suhagan",
           "B. Women HAHAHA Women HAHAHA",
           "C. Female",
           "D. Sugandi"]

# Question1
for i in range(1):
  print(" ")
print("1st Question :", Question_list[0])
for i in range(1):
  print(" ")
for opt1 in option1:
  print(opt1)
for i in range(1):
  print(" ")
answer1 = input("Note: Give Capital Answer, Your Answer A, B, C, D: ")
for i in range(1):
  print(" ")
if answer1 == "B":
  print("Correct! YOU WON 250000 RS")
  print("WOW ","\U0001F600")

  money += 250000 
else:
  print("Incorrect!" ,("SORRY","\U0001F612"))

# Question2
for i in range(1):
  print(" ")
print("2nd Question :", Question_list[1])
for i in range(1):
  print(" ")
for opt2 in option2:
  print(opt2)
for i in range(1):
  print(" ")
answer2 = input("Note: Give Capital Answer, Your Answer A, B, C, D: ")
for i in range(1):
  print(" ")
if answer2 == "B":
  print("Correct! YOU WON 500000 RS")
  print("WOW ","\U0001F600")
  money += 250000 
else:
  print("Incorrect!" ,("SORRY","\U0001F612"))

# Question3
for i in range(1):
  print(" ")
print("3rd Question :", Question_list[2])
for i in range(1):
  print(" ")
for opt3 in option3:
  print(opt3)
for i in range(1):
  print(" ")
answer3 = input("Note: Give Capital Answer, Your Answer A, B, C, D: ")
for i in range(1):
  print(" ")
if answer3 == "D":
  print("Correct! YOU WON 750000 RS")
  print("WOW ","\U0001F600")
  money += 250000 
else:
  print("Incorrect!" ,("SORRY","\U0001F612"))

# Question4
for i in range(1):
  print(" ")
print("4th Question :", Question_list[3])
for i in range(1):
  print(" ")
for opt4 in option4:
  print(opt4)
for i in range(1):
  print(" ")
answer4 = input("Note: Give Capital Answer, Your Answer A, B, C, D: ")
for i in range(1):
  print(" ")
if answer4 == "B":
  print("Correct! YOU WON 900000 RS")
  print("WOW ","\U0001F600")
  money += 150000
else:
  print("Incorrect!" ,("SORRY","\U0001F612"))

# Question5
for i in range(1):
  print(" ")
print("5th Question :", Question_list[4])
for i in range(1):
  print(" ")
for opt5 in option5:
  print(opt5)
for i in range(1):
  print(" ")
answer5 = input("Note: Give Capital Answer, Your Answer A, B, C, D: ")
for i in range(1):
  print(" ")
if answer5== "A":
  print("Correct! YOU WON 10000000 RS")
  print("WOW ","\U0001F600")
  print("WOW ","\U0001F600")
  money += 250000 
else:
  print("Incorrect!" ,("SORRY","\U0001F612"))


  print("You Won",money, "Rupees.")
  print("\U0001F92A")
  print("\U0001F92A")
  print("\U0001F92A")
  print("\U0001F92A")