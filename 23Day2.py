print("Day 2")
with open("23Day2.txt", "r") as file: 
   content = file.read()
   Games = content.split("\n")
   sum_ids = 0
   max_red = 12
   max_green = 13
   max_blue = 14
   
   sum_power = 0

   for game in range(len(Games)):
      act = Games[game]
      act = act.replace("Game", "")
      act = act.replace(": ", "; ")
      turns = act.split("; ")
      act_id = int(turns.pop(0))
      valid = 0
      red = 1
      blue = 1
      green = 1
      
      for turn in range(len(turns)):
         game = turns[turn].split(", ")
         for col in range(len(game)):
            color = game[col].split(" ")
            if "red" in color[1]:
               if int(color[0]) > max_red:
                  valid = 1
               if int(color[0]) > red:
                  red = int(color[0])
            if "blue" in color[1]:
               if int(color[0]) > max_blue:
                  valid = 1
               if int(color[0]) > blue:
                  blue = int(color[0])
            if "green" in color[1]:
               if int(color[0]) > max_green:
                  valid = 1
               if int(color[0]) > green:
                  green = int(color[0])
      if valid == 0:
         sum_ids += act_id
      power = red * green * blue
      sum_power += power

   print("part1:", sum_ids )
   
   print("part2:", sum_power )