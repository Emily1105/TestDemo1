# a,b = map(int,input().split(" "))
# c = a+b
# print(c)

# n,sum = int(input()),0
# for i in range(n):
#     a,b = map(int,input().split(" "))
#     sum = a + b
#     print(sum)

# a,b = map(int, input().split(" "))
# while a!=0 and b!=0:
#     print(a+b)


# while True:
#     l1=input().split(" ")
#     sum = 0
#     if int(l1[0])==0:
#         break
#     else:
#         for i in l1[1:]:
#             sum+=int(i)
#         print(sum)


# while True:
#     l1 = input().strip().split(" ")
#     print("".join(sorted(l1)))


# a = int(input())
# b = int(input())
# c = []
# d = []
# if 0<=a<=10 and 0<=b<=1000:
#     for i in range(b):
#         c.append(input())
#     e = len(max(c).split(","))//a
#     for i in range(e+1):
#         for j in range(b):
#             d+=c[j].split(",")[i*a:(i+1)*a]
#     print(",".join(d))
# else:
#     print("输入有误")

# a,d,b = input().split(","),0,0
# print(a.index('1'))
# if a.count('0') > 0 and a.count('1') >0:
#     l1 = enumerate(a)
#     for i,j in l1:
#         if j == '1':
#             b = i
#         else:
#             c=min(i-b,a[i:].index('1'))
#             d=max(d,c)
#     print(d)



a,b,d = int(input()),[],[]
for i in range(a):
    b.append(input().split())
print(b)
c=input()
for i in b:
    print(i)
    if i[0]!=c or i[1]!=c or i[1]!=0:
        d.append(i)
print(d)