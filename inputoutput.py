def readfile(filename, W_and_numclasslist, wlist, vlist, clist):
    openfile = open(filename)
    W = int(openfile.readline())
    num_class = int(openfile.readline())
    weightlist = openfile.readline().split(', ')
    valuelist = openfile.readline().split(', ')
    classlist = openfile.readline().split(', ')
    openfile.close()
    W_and_numclasslist.append(W)
    W_and_numclasslist.append(num_class)
    weightlist[len(weightlist)-1] = weightlist[len(weightlist)-1].strip('\n')
    valuelist[len(valuelist)-1] = valuelist[len(valuelist)-1].strip('\n')
    classlist[len(classlist)-1] = classlist[len(classlist)-1].strip('\n')
    for i in weightlist:
         wlist.append(int(i))
    for i in valuelist:
        vlist.append(int(i))
    for i in classlist:
        clist.append(int(i))

def writefile(filename, totalvalue, bitstring):
    openfile = open(filename, mode = 'w')
    openfile.write(str(totalvalue)+ '\n')
    c = 0
    while c <= len(bitstring) - 1:
        if c == len(bitstring) - 1 :
            openfile.write(str(bitstring[c]))
        else:
            openfile.write(str(bitstring[c])+', ')
        c = c + 1
    openfile.close()