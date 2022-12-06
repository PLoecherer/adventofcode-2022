print("Day 4")

with open("Day4.txt", "r") as file: 
   content = file.read()
   pairs = content.split("\n")
   for elves in range(len(pairs)):
       pairs[elves] = pairs[elves].split(",") 
       for elf in range(len(pairs[elves])):
           pairs[elves][elf] = pairs[elves][elf].split("-")
           for i in range(len(pairs[elves][elf])):
               pairs[elves][elf][i] = int(pairs[elves][elf][i])

   # Part 1
   count = []
   for elves in range(len(pairs)):
       if pairs[elves][0][0] <= pairs[elves][1][0] and pairs[elves][0][1] >= pairs[elves][1][1]:
           count.append(1)
       elif pairs[elves][0][0] >= pairs[elves][1][0] and pairs[elves][0][1] <= pairs[elves][1][1]:
           count.append(1)
       else:
           count.append(0)
   print("Part 1:", sum(count), "of", len(pairs))

   # Part 2
   count2 = []
   for elves in range(len(pairs)):
       if pairs[elves][0][1] < pairs[elves][1][0] or pairs[elves][0][0] > pairs[elves][1][1]:
           count2.append(0)
       else:
           count2.append(1)
   print("Part 2:", sum(count2), "of", len(pairs))