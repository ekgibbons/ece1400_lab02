print("One a scale of 1-10, how much are you loving ECE 1400?")
love_level = int(input())

if love_level < 1:
    print("I said scale of 1->10")
elif 1 <= love_level <= 3:
    print("Come on, this helps you get a job")
elif 3 < love_level <= 6:
    print("There is nothing lukewarm about Python programming")
elif 6 < love_level <= 10:
    print("Glad you are liking it so far")
elif 10 < love_level:
    print("<3") 
