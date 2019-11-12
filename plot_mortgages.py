import pylab

def findPayment(loan, r, m):
	"""Assumes lone and r are float and m is an int
	return the monthly payment for a motgage of size 
	loan at a monthly rate of r for m months"""
	return loan*((r*(1+r)**m)/((1+r)**m -1))
	
	
class Mortgage(object):
	"""Abstract class to build different kind of mortgages"""
	def __init__(self, loan, annRate, months):
		"""Assumes loan and annRate are float and months an int
		Creates  a new mortgage of sizeloan, duration months
		and annual rate annRate"""
		self.loan = loan
		self.rate = annRate/12
		self.months = months
		self.paid = [0.0]
		self.outstanding = [loan]
		self.payment = findPayment(loan, self.rate, months)
		self.legend = None #description of mortgage
		
	def makePayment(self):
		"""make a payment"""
		self.paid.append(self.payment)
		reduction = self.payment - self.outstanding[-1]*self.rate
		self.outstanding.append(self.outstanding[-1] - reduction)
		
	def getTotalPaid(self):
		"""return the total ammount paid so far"""
		return sum(self.paid)
		
	def __str__(self):
		return self.legend
	
	def plot_payments(self, style):
		pylab.plot(self.paid[1:], style, label = self.legend)
		
	def plot_balance(self, style):
		pylab.plot(self.outstanding, style, label = self.legend)
		
	def plot_tot_pd(self,  style):
		tot_pd = [self.paid[0]]
		for i in range(1, len(self.paid)):
			tot_pd.append(tot_pd[-1] + self.paid[i])
		pylab.plot(tot_pd, style, label = self.legend)
		
	def plot_net(self, style):
		tot_pd = [self.paid[0]]
		for i in range(1, len(self.paid)):
			tot_pd.append(tot_pd[-1] + self.paid[i])
		equity_acquired =  pylab.array(self.loan)*len(self.outstanding)
		equity_acquired =  equity_acquired - pylab.array(self.outstanding)
		net = pylab.array(tot_pd) - equity_acquired
		pylab.plot(net, style, label = self.legend)
		

class Fixed(Mortgage):
	def __init__(self, loan, r, months):
		Mortgage.__init__(self, loan, r, months)
		self.legend = 'Fixed, ' + str(round(r*100, )) + '%'
		
class FixedWithPts(Mortgage):
	def __init__(self, loan, r, months, pts):
		Mortgage.__init__(self, loan, r, months)
		self.pts = pts
		self.paid = [loan*(pts/100)]
		self.legend = 'Fixed, ' + str(round(r*100, )) + '% '\
						+ str(pts) + ' points'
						
class TwoRate(Mortgage):
	def __init__(self, loan, r, months, teaserRate, teaserMonths):
		Mortgage.__init__(self,loan, r, months)
		self.teaserMonths = teaserMonths
		self.teaserRate = teaserRate
		self.nextRate = r/12
		self.legend = str(teaserRate*100)\
						+'% for ' + str(self.teaserMonths)\
						+' months, then ' + str(round(r*100,2)) + '%'
	
	def makePayments(self):
		if len(self.paid)== self.teaserMonths + 1:
			self.rate = self.nextRate
			self.payment = self.findPayment(self.outstanding[-1],
											self.rate,
											self.months - teaserMonths)
		
		Mortgage.makePayment(self)
		

def plot_mortgages(morts, amt):
	def label_plot(figure, title, x_label, y_label):
		pylab.figure(figure)
		pylab.title(title)
		pylab.xlabel(x_label)
		pylab.ylabel(y_label)
		pylab.legend(loc = 'best')
		
	styles = ['k-', 'k-.', 'k:']
	#Give name to figure numbers
	payments, cost, balance, net_cost = 0, 1, 2, 3
	for i in range(len(morts)):
		pylab.figure(payments)
		morts[i].plot_payments(styles[i])
		pylab.figure(cost)
		morts[i].plot_tot_pd(styles[i])
		pylab.figure(balance)
		morts[i].plot_balance(styles[i])
		pylab.figure(net_cost)
		morts[i].plot_net(styles[i])
	label_plot(payments, 'Monthly Payments of $' + str(amt) +' Mortgages',\
				'Months', 'Monthly payments')
	label_plot(cost, 'Cash Outlay of $' + str(amt) +' Mortgages',\
				'Months', 'Total payments')
	label_plot(balance, 'Balance Remaining of $' + str(amt) +' Mortgages',\
				'Months', 'Remaining Loan balance of $')
	label_plot(net_cost, 'Net Cost of $' + str(amt) +' Mortgages',\
				'Months', 'payment - Equality $')
	pylab.show()
		
		
def compareMortgages(amt, years, fixedRate, pts, ptsRate,
					 varRate1, varRate2, varMonths):
	
	totMonths = years*12
	fixed1 = Fixed(amt, fixedRate, totMonths)
	fixed2 = FixedWithPts(amt,ptsRate,totMonths, pts)
	twoRate = TwoRate(amt, varRate2,totMonths, varRate1, varMonths)
	morts = [fixed1, fixed2, twoRate]
	for m in range(totMonths):
		for mort in morts:
			mort.makePayment()
			
	for m in morts:
		print(m)
		print(' Total payments = $' + str(int(m.getTotalPaid())))
	plot_mortgages(morts, amt)
	
		
compareMortgages(amt=200000, years=30, fixedRate=0.07,
				 pts=3.25, ptsRate=0.05,varRate1=0.045,
				 varRate2=0.095, varMonths=48)

