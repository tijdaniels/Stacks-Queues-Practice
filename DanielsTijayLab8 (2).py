import queue



infile = open("candy.txt", "r")

candy = infile.readline()
originals = [] #stack
left = [] #Queue
table = [] #Queue
while candy != "":
    candy = candy.rstrip("\n")
    originals.append(candy)
    candy = infile.readline()
infile.close()

print("Your Original List of Candy is:\n")
print(originals)
color = []

for x in range(len(originals)):
    if originals[x] != "yellow" and originals[x] !="blue":
        left.append(originals[x])
    else:
        table.append(originals[x])

print("\nYour left over candy put back in the container in right order is:\n")
print(left)

print("\nThe order of candy on the table is\n")
print(table)

    
    
