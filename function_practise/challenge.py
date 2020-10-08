# challenge problems

#Spy Game

def spy_game(lis):
    temp=[]
    for item in lis:
        if item==0 or item==5:
            temp.append(item)
            
    for i in range(0,len(temp)-1):
        if (temp[i]*100 +temp[i+1]*10+temp[i+2])==7:
            return True
    return False

# Count primes( USING SIEVE OF ERATOSTHENES

def count_primes(num):
    visited=[None]*10000
    for i in range(10000):
        visited[i]=True
    visited[0]=False
    visited[1]=False
    for i in range(10000):
        if visited[i]!=False:
            for j in range(i*i,10000,i):
                visited[j]=False
    count=1
    for i in range(2,num):
        if visited[i]==True:
            count++
    return count
