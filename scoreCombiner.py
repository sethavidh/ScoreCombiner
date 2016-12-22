# -*- coding: utf-8 -*-
"""
Combine scores
    get list of students from csv file
    get scores from several csv files
    output single csv file of each student's score in the same order in score files
    student's position in each file does not have to be the same
Created on Thu Dec 22 14:03:39 2016

@author: akepooh
"""

import sys

def readAllStds(file):
    std_file = open(file, "r", encoding='utf-8')
    rec_list = std_file.readlines()
    all_std = []
    for rec in rec_list:
        item_list = rec.split(',')
        all_std.append((item_list[1], item_list[2]))
    return all_std
    
std_file = sys.argv[1]
file_ls = sys.argv[2:]
print(file_ls)
std_t = readAllStds(std_file)
header = ['ID','Name']
score_d = {}
for sid,name in std_t:
    score_d[sid] = {}
    score_d[sid]['name'] = name
    score_d[sid]['score'] = []
    
for x in file_ls:
    fs = open(x, 'r', encoding='utf-8')
    h = fs.readline().strip().split(',')
    h_len = len(h)
    header += h[2:]
    for rec in fs.readlines():
        ls = rec.strip().split(',')
        print(ls)
        if not ls[0]: continue
        sc = ls[2:]
        sid = ls[0]
        #print(sid, sc)
        score_d[sid]['score'].extend(sc)

fs.close()
combined_file = open('combined.csv', 'w', encoding='utf-8')
print(','.join(header), file=combined_file)
for sid, name in std_t:
    print(sid +','+name, end='', file=combined_file)
    for sc in score_d[sid]['score']:
        print(','+sc,end='', file=combined_file)
    print('', file=combined_file)

        