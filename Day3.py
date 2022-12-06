from ast import Lambda
import string

print("Day 3")
def split_in_half(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
def common(lista, listb):
    res = []
    for x in lista:
        if x in listb:
            if x not in res:
                res.append(x)
    return res
def common3(lista, listb, listc):
    res = []
    for x in lista:
        if x in listb:
            if x in listc:
                if x not in res:
                    res.append(x)
    return res

with open("Day3.txt", "r") as file: 
   content = file.read()
   rucksacks = list(map(list, content.split("\n")))
   valuemap = list(string.ascii_lowercase)
   valuemap.extend(list(string.ascii_uppercase))
   mapvalue = list(range(1, 53))
   value = dict(zip(valuemap, mapvalue))

   # Part1
   rucksacksplit = list(map(split_in_half, rucksacks))
   faileditem = []
   for i in range(len(rucksacksplit)):
       faileditem.append(common(rucksacksplit[i][0],rucksacksplit[i][1]))
   result = 0
   for i in range(len(faileditem)):
       result += value.get(faileditem[i][0])
   print("Part1", result)

   # Part2
   badges = []
   for i in range(len(rucksacks)//3):
       badges.append(common3(rucksacks[i*3],rucksacks[i*3+1],rucksacks[i*3+2]))
   result2 = 0
   for i in range(len(badges)):
       result2 += value.get(badges[i][0])
   print("Part2", result2)
