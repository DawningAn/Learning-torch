# i = 1
# j = 1
# while i <= 5:
#     while j <= i:
#         print("*",end = " ")
#         j +=1
#     print()
#     j =1
#     i +=1

row = 1
col =1

while row <= 9:
    while col <= row:
        print("%d * %d = %d" %(col,row,col*row),end = " ")
        col +=1
    print()
    row +=1
    col = 1
