
def printMultiples(num):
    ''' Print all the multples of num till num*num '''
    for i in range(1, num + 1):
   	print str(num*i) + '\t',

def printMulTables(limit):
    ''' Print multiples of 1 to limit'''
    for i in range(1, limit+1):
        printMultiples(i)
	print

def main():
    limit = int(raw_input())
    printMulTables(limit)

if __name__ == '__main__':
    main()
