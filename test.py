import random_walk, pylab

def sim_test(trials, numOfDaysPeryear, numbOfDays, numStocks, price, bias=0.1):
	random_walk.runTest(trials, numOfDaysPeryear, numbOfDays, numStocks, price, bias)
	pylab.show()


"""
a test with 2 trials running for 100
days with 40 stocks with price equals
to 50. default bias
"""
# sim_test(2, 100.0, 100, 40, 50)

"""
a test with 4 trials running for 200
days with 200 stocks with price equals
to 100 with 0.5 bias
"""
# sim_test(4, 200.0, 200, 200, 100, 0.5)

"""
a test with 3 trials running for 50
days with 10 stocks with price equals
to 10 with maximum bias
"""
# sim_test(3, 50.0, 50, 10, 10, 1.0)

"""
a test with 5 trials running for 150
days with 150 stocks with price equals
# to 200. bias of 0.3
"""
# sim_test(5, 150.0, 150, 150, 200, 0.3)

"""constant values with increasing biases"""
# sim_test(3, 200.0, 200, 500, 100) #default bias of 0.1
# sim_test(3, 200.0, 200, 500, 100, 0.2) 
# sim_test(3, 200.0, 200, 500, 100, 0.3)
# sim_test(3, 200.0, 200, 500, 100, 0.4)
sim_test(3, 200.0, 200, 500, 100, 0.5)
# sim_test(3, 200.0, 200, 500, 100, 0.6)
# sim_test(3, 200.0, 200, 500, 100, 0.7)
# sim_test(3, 200.0, 200, 500, 100, 0.8)
# sim_test(3, 200.0, 200, 500, 100, 0.9)
# sim_test(3, 200.0, 200, 500, 100, 1.0)


"""
CONCLUSION

	A higher bias in the stock prices will lead to a more predictable change in prices.
	The momentum tells how affected the prices are based on the former prices.


	The changes in the graph are most visible when changing the bias compared to other
	factors such as the number of days, stocks, prices or momentum
"""

