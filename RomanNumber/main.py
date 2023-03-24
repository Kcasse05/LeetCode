
def romanToInt(s: str) -> int:
        translate = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000     
        }
        
        #pointer to move backward 
        i =  len(s) -1
        solution = 0
        while i >= 0 :
            if i != 0: 
                if translate[s[i-1]] == 1 and (translate[s[i]] == 5 or translate[s[i]] == 10):
                        solution += translate[s[i]] - translate[s[i-1]]
                        i = i - 2

                    
                elif translate[s[i-1]] == 10 and (translate[s[i]] == 50 or translate[s[i]] == 100):
                        solution += translate[s[i]] - translate[s[i-1]]
                        i = i - 2

                    
                elif translate[s[i-1]] == 100 and (translate[s[i]] == 500 or translate[s[i]] == 1000):
                        solution += translate[s[i]] - translate[s[i-1]]
                        i = i - 2 
                else: 
                    solution  += translate[s[i]]
                    i = i - 1
                    

            else:
                solution  += translate[s[i]]
                i = i - 1
                
        return solution
    
def main():
    romanNumber = "DCXXI"
    Integer = romanToInt(romanNumber)
    assert romanToInt(romanNumber) == 58
if __name__ == '__main__':
    main()