print("Day 6")

with open("Day6.txt", "r") as file: 
   content = file.read()
   data = list(content)

   # Part1
   marker = 4
   found = False
   while found == False:
       if len(set(data[marker-4:marker])) == 4:
            print("Part 1: ", marker, " characters had to be processed before the first start-of-packet marker was detected")
            found = True
       elif marker == len(data):
            print("Part 1: After all characters have been processed there was no start-of-packet marker detected")
            break
       marker += 1

   # Part2
   messagemarker = 14
   messagefound = False
   while messagefound == False:
       if len(set(data[messagemarker-14:messagemarker])) == 14:
            print("Part 2: ", messagemarker, " characters had to be processed before the first start-of-message marker was detected")
            messagefound = True
       elif messagemarker == len(data):
            print("Part 2: After all characters have been processed there was no start-of-message marker detected")
            break
       messagemarker += 1
                  
