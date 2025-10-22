import numpy as np

# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1
PARABOLA=0; SIGMOID=1



class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner(PARABOLA)


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self, trajectoryType):
        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]

        pointList = []

        if trajectoryType == PARABOLA:
            # Parabola
            for i in np.arange(0, 1.51, 0.01):
                pointList.append([i, i**2]) 
        elif trajectoryType == SIGMOID:
            # Sigmoid
            for i in np.arange(0, 2.51, 0.01):
                sigmoidCalc = 2/(1 + np.e**(-2*i))-1
                pointList.append([i, sigmoidCalc]) 

        return pointList

