
class Node:
	''' A basic linked list implementation '''
	def __init__(self, cargo, next = None):
		''' Initialise the node'''
		self.cargo = cargo
		self.next = next

class Queue:
	''' A queue data structure '''
	def __init__(self):
		''' Initialise the queue '''
		self.length = 0
		self.head = None
		self.last = None

	def isEmpty(self):
		return self.length == 0

	def insert(self, cargo):
		''' Insert an element to the queue'''
		node = Node(cargo)
		node.next = None
		if self.head == None:
			# If empty queue then first element is the head
			self.head = node
			self.last = node
		else:
			last = self.last
			last.next = node
			self.last = node
			self.length += 1

	def remove(self):
		''' Remove element from queue, FIFO basis '''
		cargo = self.head.cargo
		self.head = self.head.next
		self.length -= 1
		if self.length == 0:
			self.last = None
		return cargo

	def __str__(self):
		''' Print the queue '''
		last = self.head
		string = ''
		while last:
			string += str(last.cargo) + ' '
			last = last.next
		return string

def main():
	aQueue = Queue()
	aQueue.insert(10)
	aQueue.insert(20)
	aQueue.insert(30)
	print aQueue
	aQueue.remove()
	print aQueue

if __name__ == '__main__':
	main()
