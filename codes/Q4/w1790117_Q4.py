# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1790117
# Date:


credit_at_pass = int()  # Declaring all variables used in the program.
defer = int()
fail = int()
hist = str()

progress_counter = 0  # Declaring all counters.
trailer_counter = 0
retriever_counter = 0
exclude_counter = 0

msg_for_progress = "Progress."  # messages for outcomes.
msg_for_module_trailer = "Progress-module trailer."
msg_for_module_retriever = "Do not progress-module retriever."
msg_for_exclude = "Exclude."



credit={120,100,100,80,60,40,20,20,20,0}
defer={0,20,0,20,40,40,40,20,0,0}
fail={0,0,20,20,20,40,60,80,100,120}

def output_previous_data(): #Output for previously entered data.
    print("These are the output for previously entered data.")
    print(msg_for_progress)
    print(msg_for_module_trailer)
    print(msg_for_module_trailer)
    print(msg_for_module_retriever)
    print(msg_for_module_retriever)
    print(msg_for_module_retriever)
    print(msg_for_module_retriever)
    print(msg_for_exclude)
    print(msg_for_exclude)
    print(msg_for_exclude)
    print(msg_for_exclude)



def histogram():  # Histogram
    print("Progress", progress_counter, " :", progress_counter * '*')
    print("Trailing", trailer_counter, " :", trailer_counter * '*')
    print("Retriever", retriever_counter, ":", retriever_counter * '*')
    print("Excluded", exclude_counter, " :", exclude_counter * '*')
    print(total_count, "outcomes in total.")


def get_input():
    global credit_at_pass
    global defer
    global fail
    while True:
        try:
            credit_at_pass = int(input("Enter your  pass credits : "))
            while credit_at_pass not in [0, 20, 40, 60, 80, 100, 120]:
                print("Range error.")
                credit_at_pass = int(input("Enter your  pass credits : "))
            break


        except ValueError:
            print("Enter an integer.")

    while True:
        try:
            defer = int(input("Enter your  defer credits : "))
            while defer not in [0, 20, 40, 60, 80, 100, 120]:
                print("Range error.")
                defer = int(input("Enter your  pass credits : "))
            break

        except ValueError:
            print("Enter an integer.")

    while True:
        try:
            fail = int(input("Enter your  fail credits : "))
            while fail not in [0, 20, 40, 60, 80, 100, 120]:
                print("Range error.")
                fail = int(input("Enter your  fail credits : "))

            break

        except ValueError:
            print("Enter an integer.")


def Rules():
    global progress_counter  # Using globally stored value in the counter.
    global exclude_counter
    global trailer_counter
    global retriever_counter
    global total_count

    if credit_at_pass == 120:
        print()
        print(msg_for_progress)
        progress_counter += 1

    elif credit_at_pass == 100:
        print()
        print(msg_for_module_trailer)
        trailer_counter += 1

    elif fail in [120, 100, 80]:
        print()
        print(msg_for_exclude)
        exclude_counter += 1

    else:
        print()
        print(msg_for_module_retriever)
        retriever_counter += 1

    total_count = progress_counter + trailer_counter + retriever_counter + exclude_counter


while hist != 'q':
    get_input()
    while credit_at_pass + defer + fail != 120:
        print("Total incorrect.")
        get_input()
    else:
        Rules()
        print(" ")
        hist = str(input("Press q for the histogram or press Enter to submit another record : "))
        print()
        if hist == 'q':
            print("Processing the histrogram. please wait..")
            histogram()
            print()
            output_previous_data()



