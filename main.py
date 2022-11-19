from inputoutput import*

# contain class
W_and_numclasslist = []
wlist = []
vlist = []
clist = []

readfile('INPUT_01.txt',W_and_numclasslist, wlist, vlist, clist)

print(W_and_numclasslist)
print(wlist)
print(vlist)
print(clist)

bitlist = [0,1,1,0,1,0,1]

writefile('output_01.txt', str(W_and_numclasslist[0]), bitlist)

enumclass= []
for i in clist:
    if len(enumclass) == 0:
        enumclass.append(i)
    else:
        check = 0
        for c in enumclass:
            if i == c:
                check = 1
        if check == 0:
            enumclass.append(i)
            
print(enumclass)



