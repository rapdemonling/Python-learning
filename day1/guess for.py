# Author：George Ling

age_of_me = 26

count = 0
for i in range(3):
    guess_age = int(input("guess age:"))
    if guess_age == age_of_me :
        print("yes,you got it.")
        break
    elif guess_age > age_of_me :
        print("try smaller！")
    else:
        print("try bigger!")
else:
    print("you have tried too much times.")