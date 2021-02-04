#define stack and all its methods
class Stack:
	def __init__(self):
		self.items = [];

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		return self.items.append(item)
	
	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


s = Stack()

#input to be tested
#inputList = ["(",")"]
print("Enter an input to check if the braces are balanced")
inputList = input()
#iterator, coming from C and Java


#check for popping from empty stack, would give unbalanced and balanced as a result
emptyCheck = 0

for x in inputList:
	if x=="(" or x=="[" or x=="{":
		s.push(x)

	if x==")" or x=="]" or x=="}":
		try:
			s.pop()
			
			
		except IndexError as e:
			print("unbalanced")
			emptyCheck = 1
	
	


if s.isEmpty() and emptyCheck == 0:
	print("balanced")
else:
	print("unbalanced")






