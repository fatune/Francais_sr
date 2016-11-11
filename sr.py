import random

def return_next_index():
	trial = random.uniform(0,1)
	i = 0.0
	while True:
		if trial > 1/(3**i): break
		i=i+1
	return int(i) -1

class sr2:
	def __init__(self, deck, fresh_stack_capacity = 5, number_of_stacks = 1):
                self.__stacks = []
                self.__current_item = None
		self.name = deck["name"]
		self.title = deck["title"]
		self.template =  deck["template"]
		self.qparser = deck["qparser"]
		self.aparser = deck["aparser"]
		self.to_learn_stack = deck["questions"]
		for i in range(number_of_stacks):
			self.__stacks.append([])
		self.fresh_stack_capacity = fresh_stack_capacity
	
	def get_next_item(self):
                if self.__current_item:
                    self.rate_current_item(0)

		# add new element in fresh stack if there any to add
		if not len(self.__stacks[0])>self.fresh_stack_capacity and len(self.to_learn_stack) > 0:
			self.__stacks[0].append(self.to_learn_stack.pop(0))
				
		# chose next item
		while True:
			idx = return_next_index()
			for current_stack in range(len(self.__stacks)):
				if idx < len(self.__stacks[current_stack]): break
				idx -= len(self.__stacks[current_stack])
			if len(self.__stacks[current_stack])>idx: 
				break # random index is good big
		self.__current_item = self.__stacks[current_stack].pop(idx)
		self.current_stack = current_stack
		return self.get_last_item_again()

	def get_last_item_again(self):
		return [self.qparser(self.__current_item[0],self.__current_item[1]),
                        self.aparser(self.__current_item[0],self.__current_item[1])]

	def rate_current_item(self, rate):
		current_stack = self.current_stack
		if rate == +1 and current_stack < (len(self.__stacks)-1): current_stack += 1
		if rate == -1 and current_stack > 0 : current_stack -= 1
		self.__stacks[current_stack].append(self.__current_item)
		self.__current_item = None

