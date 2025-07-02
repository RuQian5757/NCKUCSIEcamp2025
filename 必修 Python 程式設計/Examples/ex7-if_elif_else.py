deadline = int(input("Deadline: "))

if deadline >= 24*7:
    print("Play LOL")
elif deadline < 24*7 and deadline > 24:
    print("Chill ...")
else:
    print("copy paste")
