from random import choice


questions = ["why is earth round?" , "why are fruits healthy? " , "why is  the sky blue?"]

question = choice(questions)

answer = input(question).lower().strip()
while answer != "just because" :
    answer = input("why?: ").strip().lower()
print("Oh...okay")    
    
