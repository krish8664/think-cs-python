
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

def pascal_triangle(limit):
    for i in range(limit):
        for k in range(0,(limit-i-1)/2):
            print '\t',
        if i == 0:
            print "    ",
        for j in range(0,i+1):
            print factorial(i)/(factorial(j)*factorial(i-j)),
            print '\t',
        print 

def main():
    n = int(input())
    pascal_triangle(n+1)


if __name__ == "__main__":
    main()
