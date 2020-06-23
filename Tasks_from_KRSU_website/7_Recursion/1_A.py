def TowerOfHanoi(n , source, destination, auxilliary):
    

    if n==1: 
        print (source,"->",destination)
        return
    TowerOfHanoi(n-1, source, auxilliary, destination) 
    print (source,"->",destination)
    TowerOfHanoi(n-1, auxilliary, destination, source)
    
n = int(input())
TowerOfHanoi(n,'1','3','2') 
print(2 ** n - 1)
