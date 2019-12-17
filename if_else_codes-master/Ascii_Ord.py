print"enter your number"
character=input()
if character>=ord("A") and character<=ord("Z"):
    print"capital"
elif character>=ord("a") and character<=ord("z"):
    print"small"
elif (character<65 or character>90) or (character<96 or character>=123):
    print"Not alphabet"


