#!/usr/bin/env python
# -*- coding: utf-8 -*-

import GPy
import csv, json, ast
import numpy as np
import matplotlib.pyplot as plt

GPy.plotting.change_plotting_library('plotly')

X = np.random.uniform(-3.,3.,(20,1))
Y = np.sin(X) + np.random.randn(20,1)*0.05

#with open('UEXCC_INF_P00_CUA002_SEN002_AGU.csv','r') as csvfile:
with open('UEXCC_INF_PS1_CUA001_SEN002_ELE.csv', 'r') as csvfile:

	spamreader = csv.DictReader(csvfile)
	l = list()
	for row in spamreader:
		l.append((dict(json.loads(row["created_at"]))["epoch_time"], dict(json.loads(row["data"]))['Potencia_activa_L3']))
	l = sorted(l)
	l = l[0:5000]
	X = np.array([x for x,_ in l])
	Y = np.array([float(y) for _,y in l])
	plt.plot(X,Y)
	plt.show()

	X = X.reshape(len(X),1)
	Y = Y.reshape(len(Y), 1)
	my = Y.mean()
	print my
	Y = Y - my

	print len(l)



kernel = GPy.kern.RBF(input_dim=1, variance=0.95, lengthscale=1.)

m = GPy.models.GPRegression(X,Y,kernel)
#m.optimize(messages=True)

print m

fig = m.plot()
GPy.plotting.show(fig, filename='basic_gp_regression_notebook')