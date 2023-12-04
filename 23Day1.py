print("Day 1")
with open("23Day1.txt", "r") as file: 
   content = file.read()
   lines = content.split("\n")
   cal_value = 0
   for line in range(len(lines)):
       act = lines[line]
       num = []
       dig = 0
       for car in range(len(act)):
            if act[car].isdigit(): 
                num += act[car]
                dig = dig + 1
       value = int(num[-1]) + int(num[0])*10
    
       cal_value += value
   print("part1:", cal_value)

   cal_value2 = 0
   for line in range(len(lines)):
       act = lines[line]
       num = []
       dig = 0
       act = act.replace("one", "one1one")
       act = act.replace("two", "two2two")
       act = act.replace("three", "three3three")
       act = act.replace("four", "four4four")
       act = act.replace("five", "five5five")
       act = act.replace("six", "six6six")
       act = act.replace("seven", "seven7seven")
       act = act.replace("eight", "eight8eight")
       act = act.replace("nine", "nine9nine")
       for car in range(len(act)):
            if act[car].isdigit(): 
                num += act[car]
                dig = dig + 1
       value = int(num[-1]) + int(num[0])*10
    
       cal_value2 += value
   print("Part2:", cal_value2)
 








