# NTU CSIE ADA hw 1 Problem 3 - Red Persimmons
# Net

#import numpy as np

INP_FILE = './test_data/p3test.txt'



def load_data(filename):
    prop = []

    
#   open datafile
    f = open(filename, 'r')

#   read the first line
    k = f.readline()
    haha = k.split()
    prop.append(int(haha[0]))
    prop.append(int(haha[1]))
    data = []
#   read the following line 
    for i in range(prop[0]):
        k = f.readline()
        data.append(k)

#   append the data to the array
    f.close()
    return prop , data

def prefix_comp(row1,row2,numCol):
    num = 0
    for i in range(numCol):
        if row1[i] != row2[i]:
            num += 1
        else:
            break
    return num
    
    
def main():
    
    prop, data = load_data(INP_FILE)
#    print(prop)
#    print(data)

    sum = 0
    for i in range(prop[0]-1):
        k = np.array(range(prop[0]-i-1))
        k += i+1
        for j in k:
            sum += prefix_comp(data[i],data[j],prop[1])
            
    print(sum/prop[0])
            
        

    
    
 
 
 
 

if __name__ == '__main__':
    main()