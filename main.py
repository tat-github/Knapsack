from inputoutput import*
from bruteforce import*
from branch_bounds import*
# readfile 
W_and_numclasslist = []
wlist = []
vlist = []
clist = []

print(" Please input 'small dataset' or 'large dataset': ")
dataset = input()

print(" Please input x of name file INPUT_x.txt: ")
input = input()
# change input file name to run each file input
readfile(dataset + '/' + 'INPUT_'+ input +'.txt',W_and_numclasslist, wlist, vlist, clist)

print("Readfile into list")
print(W_and_numclasslist)
print(wlist)
print(vlist)
print(clist)

#change input into list of tuples like: [(weight, cost), (weight, cost), ...]
parts = []
i = 0
while i < len(wlist):
    parts.append(wlist[i])
    parts.append(vlist[i])
    i = i + 1

weight_cost = [(parts[i], parts[i + 1]) for i in range(0, len(parts), 2)]


#brute force
maxvalue, bitlist = brute_force(len(wlist), W_and_numclasslist[0], weight_cost)
print("Output of bruteforce")
print(maxvalue)
print(bitlist)

writefile('output_bruteforce_'+ input +'.txt', maxvalue, bitlist)

#branch_bounds
maxvalue, bitlist = branch_and_bounds(len(wlist), W_and_numclasslist[0], weight_cost)
print("Output of branch_and_bounds")
print(maxvalue)
print(bitlist)

writefile('output_branch_and_bounds_' + input + '.txt', maxvalue, bitlist)




