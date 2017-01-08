[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

  
 from __future__ import print_function, division
 
 import nsfg, thinkstats2, thinkplot
 import numpy as np
 
 
 sample = np.random.random(1000)
 

#CDF
 
 cdf = thinkstats2.Cdf(sample, label = "random numbers")
 ranks = [cdf.PercentileRank(x) for x in sample]
 
 rank_cdf = thinkstats2.Cdf(ranks)
 thinkplot.Cdf(rank_cdf)
 thinkplot.Show(xlabel="percentile rank", ylabel="CDF")

#PMF
 
 pmf = thinkstats2.Pmf(sample, label='actual')
 thinkplot.Pmf(pmf)
 thinkplot.Show(xlabel="random no between 0 and 1", ylabel="PMF")
