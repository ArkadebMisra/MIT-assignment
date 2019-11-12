import pylab
def find_saving(current_saving, R):
	return current_saving*R/12

class Savings(object):
	"""Abstact class to simulate savings"""
	
	def __init__(self, total_cost, ann_rate, ann_salary, salary_increase):
		"""Assumes total_cost,ann_rate
			and ann_sallary are float.
			Creates a new savings plan"""
		self.total_cost =  total_cost
		self.portion_down_payment = total_cost*0.25
		self.ann_rate = ann_rate
		self.first_salary = ann_salary
		self.ann_salary = [ann_salary]
		#self.monthly_salary = self.ann_salary[-1]/12
		self.salary_increase = salary_increase
		self.portion_saved = 0.0
		self.current_savings = [0.0]
		self.new_saving = 0
		
				
			
	def	make_saving(self,portion_saved):	
		salary_month = len(self.current_savings)
		#print(salary_month)
		if salary_month%6 == 0:
			new_salary = self.ann_salary[-1]+self.salary_increase*self.ann_salary[-1]
			self.ann_salary.append(new_salary)
			#self.new_saving = self.current_savings[-1] + find_saving(self.current_savings[-1], self.ann_rate)\
			#					+ ((new_salary/12)*self.portion_saved)
		self.new_saving = self.current_savings[-1] + find_saving(self.current_savings[-1], self.ann_rate)\
							+ ((self.ann_salary[-1]/12)*portion_saved)
		if len(self.current_savings)<=36:
			#print("new saving", self.new_saving)
			self.current_savings.append(self.new_saving)
			self.make_saving(portion_saved)
		# ~ else:
			# ~ print("last savings",self.current_savings[-1])
		return self.current_savings[-1]
				
	def find_port_saved(self, low=0, high=10000):
		low = low
		high = high
		mid = (low+high)//2
		port_saved = mid/10000
		print("Portion saved = ",port_saved)
		saved = self.make_saving(port_saved)
		print("saved = ",saved)
		if (saved > self.portion_down_payment - 100) and (saved < self.portion_down_payment + 100):
			return port_saved
		else:
			self.current_savings = [0.0]
			self.ann_salary = [self.first_salary]
			self.new_saving = 0
			if saved < self.portion_down_payment - 100:
				self.find_port_saved(low = mid, high = high)
			else:
				self.find_port_saved(low = low, high = mid)
		
	
	def get_savings(self):
		return self.current_savings
		
	def get_months(self):
		return len(self.current_savings)	
	
	def get_salaries(self):
		return self.ann_salary
	

annual_salary  = 150000
#save_port = .05
home_cost = 1000000
salary_incr = .07
my_savings = Savings(home_cost, 0.04, annual_salary, salary_incr)
print("Portion of salary should be saved ", my_savings.find_port_saved())		
# ~ print(my_savings.get_savings())
# ~ print(my_savings.get_savings())
# ~ pylab.figure(1)
# ~ pylab.plot(my_savings.get_savings())
# ~ pylab.show()
