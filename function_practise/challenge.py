# challenge problems

#Spy Game

def spy_game(lis):
    temp=[]
    for item in lis:
        if item==0 or item==7:
            temp.append(item)
            
    for i in range(0,len(temp)-2):
        if (temp[i]*100 +temp[i+1]*10+temp[i+2])==7:
            return True
    return False

# Count primes( USING SIEVE OF ERATOSTHENES

def count_primes(num):
    visited=[None]*1000
    for i in range(1000):
        visited[i]=True
    visited[0]=False
    visited[1]=False
    for i in range(1000):
        if visited[i]==True:
            for j in range(i*i,1000,i):
                visited[j]=False
    count=0
    for i in range(0,num+1):
        if visited[i]==True:
            count+=1
    return count
# End your file in a good manner !
