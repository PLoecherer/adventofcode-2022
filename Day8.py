import numpy as np
print("Day 8")

with open("Day8.txt", "r") as file: 
    data = file.read()
    trees = data.splitlines()
    for line in range(len(trees)):
        trees[line] = list(trees[line])
        trees[line] = [int(tree) for tree in trees[line]]

    gridsize = len(trees)

    #Part 1
    vis_trees = np.full_like(trees, 0)
    #by lines:
    for line in range(gridsize):
        biggestleft = -1
        biggestright = -1
        for column in range(gridsize):
            if trees[line][column] > biggestleft:
                vis_trees[line][column] = 1
                biggestleft = trees[line][column]
            if trees[line][gridsize-1-column] > biggestright:
                vis_trees[line][gridsize-1-column] = 1
                biggestright = trees[line][gridsize-1-column]
    #by columns:
    for column in range(gridsize):
        biggestdown = -1
        biggestup = -1
        for line in range(gridsize): 
            if trees[line][column] > biggestdown:
                vis_trees[line][column] = 1
                biggestdown = trees[line][column]
            if trees[gridsize-1-line][column] > biggestup:
                vis_trees[gridsize-1-line][column] = 1
                biggestup = trees[gridsize-1-line][column]
    print("Part 1:", sum(sum(vis_trees)))

    #Part 2
    scenic_scores = np.full_like(trees, 1)
    #by lines:
    for line in range(gridsize):
        for column in range(gridsize):
            scoreright = 0
            height = trees[line][column]
            for rcolumn in range(column +1, gridsize): 
                if height > trees[line][rcolumn]:
                    scoreright += 1
                elif height == trees[line][rcolumn]:
                    scoreright += 1
                    break
                elif height < trees[line][rcolumn]:
                    scoreright += 1
                    break
            scenic_scores[line][column] *= scoreright
        for column in reversed(range(gridsize)):
            scoreleft = 0
            height = trees[line][column]
            for lcolumn in reversed(range(column)): 
                if height > trees[line][lcolumn]:
                    scoreleft += 1
                elif height == trees[line][lcolumn]:
                    scoreleft += 1
                    break
                elif height < trees[line][lcolumn]:
                    scoreleft += 1
                    break
            scenic_scores[line][column] *= scoreleft

    #by columns:
    for column in range(gridsize):
        for line in range(gridsize):
            scoredown = 0
            height = trees[line][column]
            for dline in range(line +1, gridsize): 
                if height > trees[dline][column]:
                    scoredown += 1
                elif height == trees[dline][column]:
                    scoredown += 1
                    break
                elif height < trees[dline][column]:
                    scoredown += 1
                    break
            scenic_scores[line][column] *= scoredown
        for line in reversed(range(gridsize)):
            scoreup = 0
            height = trees[line][column]
            for uline in reversed(range(line)): 
                if height > trees[uline][column]:
                    scoreup += 1
                elif height == trees[uline][column]:
                    scoreup += 1
                    break
                elif height < trees[uline][column]:
                    scoreup += 1
                    break
            scenic_scores[line][column] *= scoreup
    maximum_scenic_score = max([max(score) for score in scenic_scores])
    print("Part 2:", maximum_scenic_score)
