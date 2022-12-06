import copy
print("Day 5")

with open("Day5.txt", "r") as file: 
   content = file.read()
   crates = content.split("\n\n")[0]
   procedure = content.split("\n\n")[1]
   crates = crates.split("\n")
   stacks = list(crates[-1].split("   "))
   stacks = list(map(lambda el:[el], stacks))
   crates = crates[ : -1]
   for line in range(len(crates)):
       crates[line] = crates[line].replace('   ', '[0]')
       crates[line] = crates[line].replace(' ','')
       crates[line] = crates[line].split('][')
       crates[line] = [item.replace('[','') for item in crates[line]]
       crates[line] = [item.replace(']','') for item in crates[line]]
   for stack in range(len(stacks)):
       tempstack = []
       for line in range(len(crates)):
           crt = crates[line][stack]
           if crt != '0':
               tempstack.append(crt)
       stacks[stack] = tempstack

   procedure = procedure.split("\n")
   for line in range(len(procedure)):
       procedure[line] = procedure[line].replace('move ', '')
       procedure[line] = procedure[line].replace('from ', '')
       procedure[line] = procedure[line].replace('to ', '')
       procedure[line] = procedure[line].split()
       for i in range(len(procedure[line])):
           procedure[line][i] = int(procedure[line][i])
   # Part 1
   #Movement:
   copystackspart1 = copy.deepcopy(stacks)
   for step in range(len(procedure)):
       for move in range(procedure[step][0]):
           tmp = copystackspart1[procedure[step][1]-1].pop(0)
           copystackspart1[procedure[step][2]-1].insert(0, tmp)
   topcrates =[]
   for top in range(len(copystackspart1)):
       topcrates.append(copystackspart1[top][0])
   topcrates = ''.join(topcrates)
   print("Part 1:", topcrates)

   # Part 2
   #Movement:
   copystackspart2 = copy.deepcopy(stacks)
   for step in range(len(procedure)):
       for move in range(procedure[step][0]):
           tmp = copystackspart2[procedure[step][1]-1].pop(0)
           copystackspart2[procedure[step][2]-1].insert(0 + move, tmp)
   topcrates2 =[]
   for top in range(len(copystackspart2)):
       topcrates2.append(copystackspart2[top][0])
   topcrates2 = ''.join(topcrates2)
   print("Part 2:", topcrates2)
