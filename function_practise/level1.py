# level 1 problems in function practice problems

# old mcdonalds problem

def old_macdonald(st):
    temp="initial: "
    for i in range(len(st)):
        if i==0 or i==1:
            temp+=st[i].upper()
        else:
            temp+=st[i]
    return temp
    
# master yoda problem

def master_yoda(text):
    text+=' '
    lis=[]
    i=1
    while i<=len(text):
        temp=''
        if text[i]==' ':
            continue
        while text[i] != ' ' and i < len(text):
            temp=temp+text[i]
            i++;
        lis.append(temp)
        i++;
    lis.reverse()
    ans=" ".join(lis)
    print(lis)
    return ans
    
 # Almost There problem
 
def almost_there(n):
    return (abs(100-n)<=10 or abs(200-n)<=10)
