from problog.extern import problog_export
import math

@problog_export('+int','+int','+int','+int','-int') 
def eucldist(x1,y1,x2,y2):
    p1 = [x1.number,y1.number]
    p2 = [x2.number,y2.number]
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return int(distance)  

