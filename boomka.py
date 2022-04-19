str = input()
o = False
for i in range(len(str)):
    if (i == 3) or (i == len(str)-1):
        continue
    if str[i] == 'c':
        o = True
    print(str[i], end='')
if o == True:
    print("\nest bukva c\n")
