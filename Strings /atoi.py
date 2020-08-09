"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""
class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()
        numb_set = {"0","1","2","3","4","5","6","7","8","9"}
        sign_set = {"-", "+"}
        numb = 0 
        low = -2147483648
        high = 2147483647
        negative_flag = False
        
        for i in range(len(string)):
            s = string[i]
            if(s in sign_set  and  i == 0):
                if(s is "-"):
                    negative_flag = True
            elif(s in numb_set):
                numb = numb * 10 + int(s)
            else:
                break
                
        if(numb >= 1 and negative_flag):
            numb *= -1 
        
        if(numb > high ):
            return high 
        
        if(numb < low):
            return low 
        
        return numb 