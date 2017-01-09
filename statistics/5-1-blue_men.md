[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

 from __future__ import print_function, division
 
 import thinkstats2, thinkplot, scipy.stats
 import numpy as np
 
 def EvalNormalCdf(x, mu, sigma):
	return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)
 
 mu=178
 sigma=7.7
 
 min_height_cm = 177.8
 max_height_cm = 185.4
 
 blue_man_percentage = EvalNormalCdf(max_height_cm, mu, sigma) - EvalNormalCdf(min_height_cm, mu, sigma)
 
 print(blue_man_percentage)
