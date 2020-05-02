x = int(input())
R = 0
while x>0:
    d = x%10
    R = 10*R +d
    x = x// 10
print(R)
