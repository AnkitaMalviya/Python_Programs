counter = 0
string = "navgurukul"
while (counter < len(string)):
    if string[counter] == "g":
        break
    print(string[counter])
    counter += 1
print("The end", string[counter])
