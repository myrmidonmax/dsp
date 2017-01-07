[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

 from __future__ import print_function, division
 
 import nsfg, thinkstats2, thinkplot
 import numpy as np
 
 def BiasPmf(pmf, label):
	new_pmf = pmf.Copy(label = label)
 
	for x, p in pmf.Items():
 new_pmf.Mult(x, x)
 
	new_pmf.Normalize()
	return new_pmf
 
 preg = nsfg.ReadFemResp()
 
 numkdhh = preg["numkdhh"]
 
 pmf = thinkstats2.Pmf(numkdhh)
 biased_pmf = BiasPmf(pmf, "Biased survey result kids in household")
 
 thinkplot.PrePlot(2)
 thinkplot.Pmfs([pmf, biased_pmf])
 thinkplot.Show(xlabel='class size', ylabel='PMF')
