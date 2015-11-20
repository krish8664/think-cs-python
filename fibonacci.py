
fib = {0:1, 1:1}

def fibonacci(n):
    ''' Prints the fibonacci of n, using stored values of previous cases inorder to reduce the recursion overhead'''
    if fib.has_key(n):
	return fib[n]
    else:
	fib[n] =  fibonacci(n-1) + fibonacci(n-2)
	return fib[n]

def main():
    limit = int(raw_input())
    print fibonacci(limit)

if __name__ == '__main__':
    main()
