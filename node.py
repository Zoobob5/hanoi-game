# Node class
class Node:

	# Function to initialize the
	# node object
	def __init__(self, data):

		# Assign data
		self.data = data

		# Initialize next as null
		self.next = None

# Linked List class
class LinkedList:

	# Function to initialize the
	# Linked List object
	def __init__(self):
		self.head = None

# This function is in LinkedList class
# Function to insert a new node at
# the beginning
    def push(self, new_data):

	# 1 & 2: Allocate the Node &
	#	 Put in the data
	    new_node = Node(new_data)

	# 3. Make next of new Node as head
	    new_node.next = self.head

	# 4. Move the head to point to new Node
	    self.head = new_node

    # This function is in LinkedList class.
# Inserts a new node after the given
# prev_node. This method is defined
# inside LinkedList class shown above
    def insertAfter(self, prev_node, new_data):

	# 1. Check if the given prev_node exists
	    if prev_node is None:
		print ("The given previous node must in LinkedList.")
		return

	# 2. Create new node &
	# 3. Put in the data
	    new_node = Node(new_data)

	# 4. Make next of new Node as next of prev_node
	    new_node.next = prev_node.next

	# 5. make next of prev_node as new_node
	    prev_node.next = new_node
