name=input("enter your Name : ")
score=0
print("Select the right Animal Category")
print("Q1. Which of these Animals are a mammal?")
print("1. Dog, 2.Frog, 3.Parrot, 4. shark")
ans=int(input("Enter your choice : "))
if(ans == 1):
    score+=25
    print("Correct answer")
else:
    print("incorrect answer")

print("Q2. Which of these Animals are a Reptile?")
print("1. Fox, 2.Tiger, 3.Lizard, 4. shark")
ans=int(input("Enter your choice : "))
if(ans == 3):
    score+=25
    print("Correct answer")
else:
    print("incorrect answer")
print("Q3. Which of these Animals are an Amphibian?")
print("1. Fox, 2.Frog, 3.Lizard, 4. shark")
ans=int(input("Enter your choice : "))
if(ans == 2):
    score+=25
    print("Correct answer")
else:
    print("incorrect answer")
print("Q4. Which of these Animals are a bird?")
print("1. Fox, 2.Tiger, 3.Lizard, 4. Flamingo")
ans=int(input("Enter your choice : "))
if(ans == 4):
    score+=25
    print("Correct answer")
else:
    print("incorrect answer")
    
print("your score is: ",score)
