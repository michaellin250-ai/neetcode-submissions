class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Pair each car's position with its speed 
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest_time = 0 #Time of the fleet closest to the target so far 

        #Process cars from closest to target to farthest 
        for p , s in cars:
            # Time for this car to reach the target 
            time = (target - p) / s

            #If this car takes longer than the fleet ahead, 
            #It cannot atch up, so it forms a new fleet 
            if time > slowest_time:
                fleets += 1
                slowest_time = time 
        
        return fleets 