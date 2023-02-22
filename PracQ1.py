# Program : Given an array of size n and elements upto n+1,find the missing element using atmost 1 loop

n = int(input("Enter size of array n:"))
a = eval(input("Enter list with el upto n+1:"))
s = [0]*(n+2)
for i in range(n):
    s[a[i]] = 1
flag = 0
for i in range(1, n+2):
    if s[i] == 0:
        print("Found!\nMissing element :", i)
        flag = 1
        break
if flag == 0:
    print("Not found\n")
