#Quiz game

question_answer = {"What is the largest animal on earth? " : "Blue whale", 
                    "In what year did World War II end? " : "1945", 
                    "In what year was Brazil discovered? " : "1500",
                    "What's the first letter of the alphabet? " : "A", 
                    "What's the last letter of the alphabet? " : "Z"}

while True:
    for key, value in question_answer.items():
        answer = input(key)
        answer = answer.capitalize()
        if answer == value:
            print("CORRECT!")
        else:
            print("INCORRECT! Try again!")
            break
            
    print("CONGRATULATIONS! YOU WON!")
    break