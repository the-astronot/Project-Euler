'''
PROBLEM 18:

By starting at the top of the triangle below and moving to 
adjacent numbers on the row below, the maximum total from top to bottom is 23.

    3
   7 4
  2 4 6
 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem 
by trying every route. However, Problem 67, is the same challenge with a 
triangle containing one-hundred rows; it cannot be solved by brute force, 
and requires a clever method! ;o)

'''


def run():
    tree_vals = prepare_tree()
    stacked_vals = []
    for branch in tree_vals:
        stack_branch = [0 for _ in branch]
        stacked_vals.append(stack_branch)
    
    for y in range(len(tree_vals)-1, -1, -1):
        for x in range(len(tree_vals[y])):
            if y == len(tree_vals)-1:
                stacked_vals[y][x] = tree_vals[y][x]
            else:
                stacked_vals[y][x] = max(stacked_vals[y+1][x], \
                                        stacked_vals[y+1][x+1]) + \
                                        tree_vals[y][x]
    print("The Best Path Yields: {}".format(stacked_vals[0][0]))


def prepare_tree():
    value_tree = []
    branches = tree.split("\n")
    for branch in branches:
        value_tree.append(branch.split(" "))
    for branch in value_tree:
        for x in range(len(branch)):
            branch[x] = int(branch[x])
    return value_tree


tree = "\
75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\
"


if __name__== '__main__':
    run()
