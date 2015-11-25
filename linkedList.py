

class Node:
    def __init__(self, cargo=None, next=None):
	self.cargo = cargo
	self.next = next

    def __str__(self):
	return str(self.cargo)

def printList(node):
    nodeList =[]
    while node:
	nodeList.append(node.cargo)
	node = node.next
    return nodeList

def main():
    print 'Foo'
    n1 = Node(10)
    n2 = Node(20, n1)
    n3 = Node(30, n2)
    print printList(n2)    

if __name__ == '__main__':
    main()
