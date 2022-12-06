from ast import Lambda
import string

print("Day 2")
with open("Day2.txt", "r") as file: 
   content = file.read()
   groups = content.split("\n")
   rounds = []
   points = []
   for elf in range(len(groups)):
       groups[elf] = groups[elf].split(" ") 
   for elf in range(len(groups)):
       pnt = 0
       if groups[elf][1] == "X":
           pnt += 1
           if groups[elf][0] == "A":
               pnt += 3
           elif groups[elf][0] == "B":
               pnt += 0
           elif groups[elf][0] == "C":
               pnt += 6
       if groups[elf][1] == "Y":
           pnt += 2
           if groups[elf][0] == "A":
               pnt += 6
           elif groups[elf][0] == "B":
               pnt += 3
           elif groups[elf][0] == "C":
               pnt += 0
       if groups[elf][1] == "Z":
           pnt += 3
           if groups[elf][0] == "A":
               pnt += 0
           elif groups[elf][0] == "B":
               pnt += 6
           elif groups[elf][0] == "C":
               pnt += 3
       points.append(pnt)
   gespoints = sum(points)
   print("Part1", gespoints)
   points2 = []
   for elf in range(len(groups)):
       pnt = 0
       if groups[elf][1] == "X":
           pnt += 0
           if groups[elf][0] == "A":
               pnt += 3
           elif groups[elf][0] == "B":
               pnt += 1
           elif groups[elf][0] == "C":
               pnt += 2
       if groups[elf][1] == "Y":
           pnt += 3
           if groups[elf][0] == "A":
               pnt += 1
           elif groups[elf][0] == "B":
               pnt += 2
           elif groups[elf][0] == "C":
               pnt += 3
       if groups[elf][1] == "Z":
           pnt += 6
           if groups[elf][0] == "A":
               pnt += 2
           elif groups[elf][0] == "B":
               pnt += 3
           elif groups[elf][0] == "C":
               pnt += 1
       points2.append(pnt)
   gespoints = sum(points2)
   print("Part2", gespoints)
