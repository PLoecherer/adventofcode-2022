print("Day 1")
with open("Day1.txt", "r") as file: 
   content = file.read()
   groups = content.split("\n\n")
   calories = []
   for elf in range(len(groups)):
       groups[elf] = groups[elf].split("\n") 
       cal = 0
       for cali in range(len(groups[elf])):
           cal += int(groups[elf][cali])
       calories.append(cal)
   print("Part1", max(calories))
   calories.sort(reverse=True)
   max3cal = 0;
   for i in range(3):
       max3cal += calories[i]
   print("Part2", max3cal)








