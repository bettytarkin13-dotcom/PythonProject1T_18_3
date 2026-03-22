#Q2-A

def safe_code():
    code_safe=[77,12,43,100,51]
    index=0

    while index<len(code_safe):
        user_input=int(input("Please enter a number: "))

        if user_input==code_safe[index]:
            index+=1
            print("correct!")
        else:
            index=0
            print("incorrect!start over..")

    print("safe unlocked!")

safe_code()