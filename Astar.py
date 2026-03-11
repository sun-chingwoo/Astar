from queue import PriorityQueue
from pyamaze import maze,agent

def hueristic(p1,p2):
    x1,y1=p1
    x2,y2=p2

    return abs(x2-x1)+abs(y2-y1)

def Astar(m):
    start=(m.rows,m.cols)
    goal=(1,1)

    g_score={ cell: 999 for cell in m.grid} #distance from start to this point 
    g_score[start]=0  
    f_score={ cell: 999 for cell in m.grid} # f=g+h the value/distance for a point on the grid
    f_score[start]=g_score[start]+hueristic(start,goal)

    priqueue=PriorityQueue()
    priqueue.put((f_score[start],hueristic(start,goal),start)) #fscore of the current cell,hueristic cost of current cell,co ordinates of current cell
    path={}
    
    while not priqueue.empty() :
        curr=priqueue.get()[2]
        if curr==goal:
            print("Goal reached")
            break
        
        for d in "EWNS":
            if m.maze_map[curr][d]==1:
                if d=='E':
                    nxtcell=(curr[0],curr[1]+1)
                if d=='W':
                    nxtcell=(curr[0],curr[1]-1)
                if d=='N':
                    nxtcell=(curr[0]-1,curr[1])
                if d=='S':
                    nxtcell=(curr[0]+1,curr[1])

                if ( g_score[curr]+1+hueristic(nxtcell,goal))<f_score[nxtcell]:
                    g_score[nxtcell]=g_score[curr]+1
                    f_score[nxtcell]=g_score[curr]+1+hueristic(nxtcell,goal)
                    priqueue.put((f_score[nxtcell],hueristic(nxtcell,goal),nxtcell))
                    path[nxtcell]=curr

    realpath={}
    current=goal
    while current!=start:        #reversing the values of dict as a single point we cant have 2 values but 2 values have a single point
        realpath[path[current]]=current
        current=path[current]
    return realpath





            
        

m=maze(10,10)
m.CreateMaze()
finalpath=Astar(m)
a=agent(m)
m.tracePath({a:finalpath})
print(finalpath)
m.run()