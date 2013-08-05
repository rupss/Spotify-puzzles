import sys

def get_binary_reversed_number(num): 
    original_binary = bin(num)
    reversed_binary = original_binary[::-1]
    reversed_binary = reversed_binary[0:len(reversed_binary)-2]
    reversed_num = int(reversed_binary, 2)
    return reversed_num

def main(): 
    try: 
        print(get_binary_reversed_number(int(sys.stdin.readline())))
    except: 
        print "Error: type in a single integer"

if __name__ == "__main__":
    main()