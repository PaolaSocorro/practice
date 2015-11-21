def palindrome(word):
    #no spaces
    #no uppercase 
    #no weird punctuation 
    palindrome = False
    for i in xrange(len(word)/2):
    
        if word[i] == word[-(i+1)]:
            print word[i],i,"\n"
            palindrome = True
            print palindrome
        else:
            palindrome = False
            print palindrome
            
    return palindrome
    
        
palindrome("racecar")

n = "eye"
if n == n[::-1]:
    print "palindrome"
else:
    print "not palindrome"