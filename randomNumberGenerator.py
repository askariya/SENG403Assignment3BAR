from random import randint

flag = 1
maximum = 0
while flag:
    maximum = int(input("Enter the maximum amount: "))
    if (maximum < 20):
        print("Not large enough   ;)   ---> please try again")
        flag = 1
    else:
        flag = 0

bug_list = []

for index in range(0, 20):
    flag = 0
    while flag == 0:
        bugNum = randint(0, maximum)
        if bugNum in bug_list:
            flag = 0
        else:
            bug_list.append(bugNum)
            flag = 1
            print("Index " + str(index) + ": " + str(bugNum))
