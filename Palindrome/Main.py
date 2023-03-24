def isPalindrome( x: int) -> bool:
    palindrome = False 
    if x < 0:
        return palindrome
    else:
        mystr = str(x)
        
        if len(mystr) == 1:
            palindrome = True
        for i in range(int((len(mystr)/2.0))):
            if mystr[i] == mystr[len(mystr) - i -1]:
                palindrome  = True
            else:
                palindrome = False
                break
    return palindrome

print(isPalindrome(1000021))