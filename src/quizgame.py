print('welcome to my quiz game')
willingness=input('Do you wanna play? :) ')
if willingness != 'yes':
    print("Seems you don't want to play, see you next time :( ")
    quit()

print('Okay, Lets start :) ')
score=0

answer=input('if you were born 10 years ago, How old would you be today? ')
if answer.lower() == "ten years":
    print("correct :) ")
else:
    print("Incorrect :( ")
    score=score


answer=input('How many dots does a single dice have ?')
if answer.lower() == "21":
    print("correct :) ")
    score+=1
else:
    print("Incorrect :( ")
    score=score


answer=input('how many elements are there in the periodic table ? ')
if answer.lower() == "118":
    print("correct :) ")
    score = score + 1
else:
    print("Incorrect :( ")
    score=score


answer=input('What do caterpillars become when they die ? ')
if answer.lower() == "butterflies":
    print("correct :) ")
    score+=1
else:
    print("Incorrect :( ")
    score=score

answer=input('why do things get down when you throw them up? ')
if answer.lower() == "gravity":
    print("correct :) ")
    score+=1
else:
    print("Incorrect :( ")
    score=score

print('Lets see how you performed :)' )
print("you got "+ str(score) + " questions right out of 5 ")
percentage= (score/5) * 100
print("You got " + str(percentage) + " % ")