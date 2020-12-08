# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1790117
# Date: 10/3/2020

credit_at_pass = int()
defer = int()
fail = int()

msg_for_progress = "Progress."  # Messages for outputs.
msg_for_module_trailer = "Progress-module trailer."
msg_for_module_retriever = "Do not progress-module retriever."
msg_for_exclude = "Exclude."

def get_input():
    global credit_at_pass
    global defer
    global fail
    while True:
        try:
            credit_at_pass = int(input("Enter your  pass credits : "))
            while credit_at_pass not in [0,20,40,60,80,100,120]:
                print("Range error.")
                credit_at_pass = int(input("Enter your  pass credits : "))
            break


        except ValueError:
            print("Enter an integer.")

    while True:
        try:
            defer = int(input("Enter your  defer credits : "))
            while defer not in [0,20,40,60,80,100,120]:
                 print("Range error.")
                 defer = int(input("Enter your  pass credits : "))
            break

        except ValueError:
            print("Enter an integer.")

    while True:
        try:
            fail = int(input("Enter your  fail credits : "))
            while fail not in [0,20,40,60,80,100,120]:
                 print("Range error.")
                 fail = int(input("Enter your  fail credits : "))
                 
            break

        except ValueError:
            print("Enter an integer.")


def Rules():


    if credit_at_pass == 120:
        print(msg_for_progress)

    elif credit_at_pass == 100 :
        print(msg_for_module_trailer)

    elif fail in [120,100,80]:
        print(msg_for_exclude)

    else:
        print(msg_for_module_retriever)


get_input()
while credit_at_pass+defer+fail != 120:
    print("Total incorrect.")
    get_input()
Rules()






