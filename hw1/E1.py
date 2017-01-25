# NTU CSIE ADA hw 1 Topic Exercise 1 - Dynamic Programming
# Net

INP_FILE = './test_data/e1test.txt'


def load_data(filename):
    size = 0
    data = []
    
#   open datafile
    f = open(filename, 'r')

#   read the first line
    k = f.readline()
    haha = k.split()
    size = int(haha[0])
#   read the second line    
    k = f.readline()
    haha = k.split()
#   append the data to the array
    for x in haha:
        data.append(int(x))  
    f.close()
    return size , data

    
def main():
    size, data = load_data(INP_FILE)

    tmp_max = data[0]
    tmp_sum = 0
    
#    print(data)
    
    for x in data:
        tmp_sum += x
        if tmp_sum > tmp_max:
            tmp_max = tmp_sum
        if tmp_sum < 0:
            tmp_sum = 0
            
    print(tmp_max)
        
    
   
if __name__ == '__main__':
    main()