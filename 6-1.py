#직각삼각형

""" for i in range(1,6):
    print("*" * i) """
    
    
""" for ii in range(5,0,-1):
    print("*" * ii) """
    
    
#이등변삼각형

""" for i in range(1,6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) """


#다이아몬드

""" for i in range(1,6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
    

for i in range(6,0,-1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) """
    
    
# 5x5

""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """


""" line = []
for i in range(1,6):
    for j in range(1,6):
        num = ((j - 1)*5) + i
        line.append(num)
    print(line)
    line = [] """
    
    
""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num += -1
        line.append(num)
    print(line)
    line = [] """
    
    
#가위바위보

""" import random

def get_computer_choice():
    choices = ['1','2','3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")
        return
    
print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요")
chnum = input()
# pcnum = get_computer_choice()


determine_winner(chnum) """





# 파일처리

""" file = open("temp.txt", "w")
file.close()

file = open("temp.txt", "r")
file.close()

file = open("temp.txt", "a")
file.close()

file = open("temp.txt", "r+")
file.close() """



# file = open("temp.txt", "w")

""" file.write("hello\n")
file.write("world")

file.close() """


""" file = open("c:/Users/Catholic/temp.txt", "w")
for i in range(100):
    file.write(f"{i}\n") """
    
""" file = open("c:/Users/Catholic/temp.txt", "a")
file.write("hello\n")
file.write("world")

file.close() """


""" file = open("c:/Users/Catholic/temp.txt", "r")
# res = file.read()
# print(res)
# res = file.readline()
for i in range(110):
    res = file.readline(i)
    print(res)


file.close() """


""" file = open("c:/Users/Catholic/temp.txt", "r")
line = file.readlines()
for l in line:
    print(l)
    
file.close() """


file = open("c:/Users/Catholic/temp.txt", "r")
for line in file:
    print(line)
    
file.close()