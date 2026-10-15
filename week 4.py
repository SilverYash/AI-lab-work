class state:
    h = 0
    g =0
    f = 0
    parent = None
    s = []

def count_tiles(curr,goal):
    s = curr.s
    g =goal.s
    count = 0
    i = 0
    while i<len(s):
        if s[i] != g[i]:
            count+=1
        i+=1
    return count

def get_neighbours(curr):
    neighbours= []
    b = curr.s.index(0)
    r = b//3
    c = b%3
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    for d in directions:
        nr = d[0]
        nc = d[1]

        mr = nr+r 
        mc = nc+c

        if mr >=0 and mr<3:
            if mc >= 0 and mc<3:
                n = mr*3 +mc
                new = state()
                new.s = curr.s.copy()
                new.s[b] , new.s[n] = new.s[n],new.s[b]
                
                neighbours.append(new)
    return neighbours




def solve(start,goal):
    queue = [start]
    seen = set()
    
    while queue:
        queue.sort(key=lambda x: x.f)
         
        curr = queue.pop(0)
        seen.add(tuple(curr.s))
        if curr.s == goal.s:
            path = []
            while curr.parent != None:
                path.append(curr.parent.s)
                curr = curr.parent
            return path
        n = get_neighbours(curr)
        for i in n:
            if  tuple(i.s) in seen:
                continue
            g = curr.g +1
            h = count_tiles(i, goal)
            f = g+h
            i.g =g
            i.h = h
            i.f = f
            i.parent = curr
            queue.append(i)

start = state()
start.s = [1,2,3,4,5,6,7,8,0]
goal  = state()
goal.s = [1,2,3,4,5,6,7,0,8]
print("start state is ", list(start.s))
print("goal state is  ", list(goal.s))
print("the path to goal state is", solve(start,goal))


        


    
