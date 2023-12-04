print("Day 3")
with open("test.txt", "r") as file: 
   content = file.read()
   Lines = content.split("\n")
   New_Lines = []
   for line in Lines:
      char_line = []
      for char in line:
         char_line.append(char)
      New_Lines.append(char_line)
   print(New_Lines)
   num_Lines = len(New_Lines)
   num_Columns = len(New_Lines[0])
   print(num_Lines, num_Columns)
   for row in range(num_Lines):
      