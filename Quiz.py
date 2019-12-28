print("Mathematics Quiz")
question1 = "What is a testcase?"
options1 = "a. A specific scenario with an expected result\nb. An unexpected situation in Testlink"
print(question1)
print(options1)

while True:
    response = input("Hit 'a', or 'b' for your answer\n")

    if response == "a":
        break
    else:
        print("Incorrect!!! Try again.")

        while True:
            response = input("Hit 'a', or 'b' for your answer\n")

            if response == "d":
                stop = True
                break
            else:
                print("Incorrect!!! You ran out of your attempts")
                stop = True
                break
        if stop:
            break

# DO the same for the next questions of your round (copy-paste-copy-paste).
# At the end of the round, paste the following code for the bonus question.

# Now the program will ask the user to go for the bonus question or not

while True:
    bonus = input("Would you like to give a try to the bonus question?\nHit 'y' for yes and 'n' for no.\n")

    if bonus == "y":
        print("Who invented Python")
        print("a. Dennis Ritchie\nb. Guido van Rossum\nc. Mark Zuckerberg\nd. Larry Wall")

        while True:
            response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")

            if response == "b":
                break
            else:
                print("Incorrect!!! Try again.")

            while True:
                response = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")


                if response == "c":
                    stop = True
                    break
                else:
                    print("Incorrect!!! You ran out of your attempts")
                    stop = True
                    break
            if stop:
                break
        break
    elif bonus == "n":
        break
    else:
        print("INVALID INPUT!!! Only hit 'y' or 'n' for your response")

# Now do the same as done above for the next round and another bonus question.
