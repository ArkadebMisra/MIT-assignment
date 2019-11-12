def find_saving(current_saving, R):
	return current_saving*R/12

class Savings(object):
	"""Abstact class to simulate savings"""
	
	def __init__(self, total_cost, ann_rate, ann_salary, salary_increase, portion_saved):
		"""Assumes total_cost,ann_rate
			and ann_sallary are float.
			Creates a new savings plan"""
		self.total_cost =  total_cost
		self.portion_down_payment = total_cost*0.25
		self.ann_rate = ann_rate
		self.ann_salary = [ann_salary]
		#self.monthly_salary = self.ann_salary[-1]/12
		self.salary_increase = salary_increase
		self.portion_saved = portion_saved
		self.current_savings = [0.0,]
		self.new_saving = 0
		
	def	make_saving(self):
		salary_month = len(self.current_savings)
		#print(salary_month)
		if salary_month%6 == 0:
			new_salary = self.ann_salary[-1]+self.salary_increase*self.ann_salary[-1]
			self.ann_salary.append(new_salary)
			#self.new_saving = self.current_savings[-1] + find_saving(self.current_savings[-1], self.ann_rate)\
			#					+ ((new_salary/12)*self.portion_saved)
		self.new_saving = self.current_savings[-1] + find_saving(self.current_savings[-1], self.ann_rate)\
							+ ((self.ann_salary[-1]/12)*self.portion_saved)
		if self.current_savings[-1] < self.portion_down_payment:
			self.current_savings.append(self.new_saving)
			self.make_saving()
		else:
			return
	
	def get_savings(self):
		return self.current_savings
		
	def get_months(self):
		return len(self.current_savings)	
	
	def get_salaries(self):
		return self.ann_salary
	

annual_salary  = 120000
save_port = .05
home_cost = 500000
salary_incr = .03
my_savings = Savings(home_cost, 0.04, annual_salary, salary_incr, save_port)
my_savings.make_saving()
print("Total months ", my_savings.get_months())		
#print(my_savings.get_savings())
print(my_savings.get_savings())
