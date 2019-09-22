# Author：George Ling

age_of_me = 56

count = 0
while count <3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_me :
        print("yes,you got it.")
        break
    elif guess_age > age_of_me :
        print("try smaller！")
    else:
        print("try bigger!")
    count +=1
    if count == 3:
        continue_confirm = input("try more?")
        if continue_confirm !='n':
            count =0
else:
    print("you have tried too much times.")