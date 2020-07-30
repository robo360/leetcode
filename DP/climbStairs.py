"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def climbStairs(self, n: int) -> int:
        storage = {}
        if(n == 1):
            return 1
        elif(n == 2):
            return 2
        else:
            i = 3;
            storage[1] = 1
            storage[2] = 2
            while(i <= n):
                storage[i] = storage[i-1] + storage[i-2]
                i += 1

            return storage[n]
