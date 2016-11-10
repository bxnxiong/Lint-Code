# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        if len(points) <= 1: return len(points)
        
        res = 2
        for i in range(len(points)):
            dict = {}
            duplicate = 0
            
            for j in range(i+1,len(points)):
                
                # check if are same points
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                # if not put in dictionary
                else:
                    k = self.getSlope(points[i],points[j])
                    if k not in dict:
                        dict[k] = 2 # including the anchor point i itself
                    else:
                        dict[k] += 1
            freq = 1 # base frequency
            if dict != {}: # either not all are same points, or when i != n-1
                freq = max(dict.values())
            if freq + duplicate > res:
                res = freq + duplicate
        return res
        
    def getSlope(self,pointA,pointB):
        dy = (pointA.y-pointB.y)
        dx = float(pointA.x-pointB.x)
        if dx == 0:
            return float('Inf')
        else:
            return dy/dx