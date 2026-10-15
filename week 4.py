import random

class state:
  c = []
  cost = 0



def cost(board,n):
  count = 0
  i =0 
  while i<=n-2:
    j = 0
    while j<=n-1:
      if (board.c[i] == board.c[j]) or (abs(board.c[i] - board.c[j]) == j-i):
        count +=1
      j+=1
    i+=1
  return count


def hillclimb(current,n):
  #for initial state
  
  
  current.cost = cost(current,n)
  print("the cost of initial state is", current.cost)

  while current.cost!= 0:
    best = state()
    best.cost = 1000000000

    c = 0
    while c <=n-1:
      r = 0
      while r<=n-1 and r != current.c[c]:
        neighbour = state()
        neighbour.c = current.c[:]
        neighbour.c[c] =r
        
        neighbour.cost= cost(neighbour,n)
        if neighbour.cost<best.cost:
          best = neighbour
        r+=1
      c+=1
    if best.cost >= current.cost:
      print("local minimum reached")
      print("cost of the final state =" ,current.cost)
      print("the final state is" ,current.c)
      return
    current  = best
  return current.c 

n = int(input("enter the board size (number of queens):"))
i = 0
current = state()
while i<n:
  print("enter the row positon of queen of col ",i)
  r = int(input())
  if r<0 or r>n-1:
    input("invalid type again press enter to reenter")
  else:
    current.c.append(r)
    i+=1



print("the initial state is", current.c)
hillclimb(current,n)





