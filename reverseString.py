
def reverse(someString):
    ''' Print the reverse of a string'''
    return reverse(someString[1:]) + someString[0] if someString else ''

def main():
    inputString = raw_input()
    print reverse(inputString)

if __name__ == '__main__':
    main()
