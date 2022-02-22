def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    
    for i in range(2, n//2):
        if (n % i == 0):
            return False
            break
    else:
         return True

s=input()

x=s.find('9')

while True:
    
    c=int(s[x+6])
    

    if s[x+3]=='9' and s[x+9]=='0' and isPrime(c)==True:
        n=s[x:x+10]
        print(n)
        
        break
    else:
        if x+1>=len(s):
            break
        x=s.find('9',x+1)
        
      

        