# print("enter three number example : 4 5 2")
# inp = input(">> ")

numList = []
for i in range(0,3):
    num = input(">> ")
    numList.append(num)
print("the list        : ", numList)
print("smallest number : ", min(numList))