import random

def return_next_index():
	trial = random.uniform(0,1)
	i = 0.0
	while True:
		if trial > 1/(3**i): break
		i=i+1
	return int(i) -1

class sr:
	stacks = []
	current_item = []
	current_stack = 0

	def __init__(self, to_learn_stack, fresh_stack_capacity = 5, number_of_stacks = 4):
		for i in range(number_of_stacks):
			self.stacks.append([])
			self.to_learn_stack = to_learn_stack
			self.fresh_stack_capacity = fresh_stack_capacity
	
	def get_next_item(self):
		# add new element in fresh stack if there any to add
		if not len(self.stacks[0])>self.fresh_stack_capacity and len(self.to_learn_stack) > 0:
			self.stacks[0].append(self.to_learn_stack.pop(0))
				
		# chose next item
		while True:
			idx = return_next_index()
			for current_stack in range(len(self.stacks)):
				if idx < len(self.stacks[current_stack]): break
				idx -= len(self.stacks[current_stack])
			if len(self.stacks[current_stack])>idx: 
				break # random index is good big
		self.current_item = self.stacks[current_stack].pop(idx)
		self.current_stack = current_stack
		return self.current_item

	def get_last_item_again(self):
		return self.current_item

	def rate_current_item(self, rate):
		current_stack = self.current_stack
		if rate == +1 and current_stack < (len(self.stacks)-1): current_stack += 1
		if rate == -1 and current_stack > 0 : current_stack -= 1
		self.stacks[current_stack].append(self.current_item)
