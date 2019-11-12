def find_saving(current_saving, R):
	return current_saving*R/12

class Savings(object):
	"""Abstact class to simulate savings"""
	
	def __init__(self, total_cost, ann_rate, ann_salary, portion_saved):
		"""Assumes total_cost,ann_rate
			and ann_sallary are float.
			Creates a new savings plan"""
		self.total_cost =  total_cost
		self.portion_down_payment = total_cost*0.25
		self.ann_rate = ann_rate
		self.monthly_salary = ann_salary/12
		self.portion_saved = portion_saved
		self.current_savings = [0.0,]
		self.months = 0
		self.new_saving = 0
		
	def	make_saving(self):
			self.new_saving = self.current_savings[-1] + find_saving(self.current_savings[-1], self.ann_rate)\
							+ (self.monthly_salary*self.portion_saved)
			if self.current_savings[-1] < self.portion_down_payment:
				self.current_savings.append(self.new_saving)
				self.make_saving()
			else:
				return
	
	def get_savings(self):
		return self.current_savings
		
	def get_months(self):
		return len(self.current_savings)-1	
	

annual_salary  = 80000
save_port = .1
home_cost = 800000
my_savings = Savings(home_cost, 0.04, annual_salary, save_port)
my_savings.make_saving()
print("Total months ", my_savings.get_months())		
#print(my_savings.get_savings())
