# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:24:08 2019

@author: админ
"""

import pandas as pd
import numpy as np

data = pd.read_table("lenses_fromLecture.tab", header = 0, skiprows = (1,2))

freq_tables = []

cnt = data.shape[1]
cnt_for = 0
features_list = []
for f in data.columns:
    cnt_for += 1
    if cnt_for != cnt:
        #print(f)
        features_list.append(f)
print(features_list)

for label, content in data.iteritems():
    if label == "lenses": continue
    freq_tables.append(data.groupby([label, data.columns[-1] ]).size().reset_index())
err_rate = []
most_freq = []

err = []
ft = []

cnt_for = 0
for el in freq_tables:
    #print("c0 - {0}, c1 - {1}, c2 - {2}\n".format(el.columns[0], el.columns[1], el.columns[2]))
    print(el.columns[0])
    print(el.columns[1])
    print(el.columns[2])
    col0 = el.columns[0]
    col1 = el.columns[1]
    col2 = el.columns[2]
    print(el[col0])
    print(el[col1])
    print(el[col2])
    ft.append({el.columns[0]:{col0:{col1:}}})
    if cnt_for != 4: 
        #print("el = {0}\n".format(el[0]))
        b = 5
    cnt_for += 1
    for l in el:
        #print(l)
        b = 5
a = [{'age':{'young':{'hard':1,'soft':2,'none':2}, 'p':{'hard':1,'soft':1,'none':4}}}]
