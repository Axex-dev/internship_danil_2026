number = int(input())
letter = []
for i in range(number):
   letter.append(int(input()))
ans = 0
for i in range(1, number):
    ans += min(letter[i], letter[i-1])
print(ans)

#5
#3 4 2 5 5
#a b c d e
#a b c d e
#a b   d e
#  b`  d e
#      d e