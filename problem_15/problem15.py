'''
PROBLEM 15:

Starting in the top left corner of a 2×2 grid, and only being able 
to move to the right and down, there are exactly 6 routes to the 
bottom right corner.

How many such routes are there through a 20×20 grid?

'''
    

def run_recursive():
    #global paths
    global memory
    size = 20
    paths = [0 for _ in range(size)]
    memory = [[0 for _ in range(size+1)] for _ in range(size+1)]
  
    sum = step_memory(0,0,size)
    print("The Number of Paths for a {0}x{0} grid is: {1}".format(size, sum))
    

def step(x,y,size): # Deprecated
    global paths
    sum = 0
    if x == y:
        if x == size and y == size:
            sum = 1
        else:
            if paths[size-x] != 0:
                return paths[size-x]
            else:
                if x < size:
                    sum += step(x+1,y,size)
                if y < size:
                    sum += step(x,y+1,size)
                paths[size-x] = sum
    else:
        if x < size:
            sum += step(x+1,y,size)
        if y < size:
            sum += step(x,y+1,size)
    
    return sum


def step_memory(x,y,size):
    global memory
    if memory[x][y] == 0:
        sum = 0
        if x < size:
            sum += step_memory(x+1,y,size)
        if y < size:
            sum += step_memory(x,y+1,size)
        if x == size and y == size:
            sum = 1
        memory[x][y] = sum
    return memory[x][y]
    


paths = [] # Deprecated
memory = []


if __name__ == '__main__':
    run_recursive()
