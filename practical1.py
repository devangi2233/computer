import array as a

a1 = a.array('i',[35, 24, 20, 5, 3, 29])

#a1.insert(3, 50)

#a1.pop(3)

#a1[2] = 25

a1.reverse()
for x in a1:
    print(x, end=" ")