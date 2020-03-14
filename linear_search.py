from datetime import datetime

def now():
    return datetime.now()
    
def get_input(path):
    inp = []
    with open(path) as file:
        a = file.read()
    inp = a.split()
    return inp

def linear_search(inp, search, flag):
    for i in range(len(inp)):
        if search == int(inp[i]):
            print('element found at {}'.format(i))
            if flag == True:
                return i
def main():
    inp = get_input(r"C:\Users\Gangam.Ram\Desktop\Harsha Assignment\File 6.txt")
    search = int(input('Please enter a number: '))
    
    flag = bool(input())
    
    execution_start = now()
    index = linear_search(inp, search, flag)
    execution_end = now()
    
    total_time = execution_end  - execution_start 
    
    print(total_time)
    
    
if __name__ == "__main__":
    main()
    
# file 1 => 0.001004 sec || 0.001037 sec
# file 2 => 0.000998 sec || 0.002001 sec
# file 3 => 0.007998 sec || 0.007999 sec
# file 4 => 0.016992 sec || 0.026000 sec
# file 5 => 0.016999 sec || 0.017001 sec
# file 6 => 0.003003 sec || 0.022001 sec