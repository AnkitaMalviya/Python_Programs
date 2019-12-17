def check_numbers(num1,num2):
    index=0
    while index<len(num1):
        if num1[index] and num2[index] %2==0:
            print"dono numbers even hai"
        else:
            print"dono numbers even nahi hai"
        index=index+1
check_numbers([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])