#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
#
testingrooms = ['A','B','C']
for room in testingrooms:
    testingroom_path = 'testingroom' + room + '\experiment_data.csv'
    rawdata_path = 'rawdata\experiment_data_' + room + '.csv'
    shutil.copy = (testingroom_path, rawdata_path)


#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT

data = np.empty((0,5))
for room in testingrooms:
    new_path = 'rawdata\experiment_data_' + room + '.csv'
    temp_array = sp.loadtxt(new_path, delimiter=',')
    data = np.vstack([data,temp_array])

#%%
# calculate overall average accuracy and average median RT
#
acc_avg = np.mean(data[:,3])*100  # 91.48% #3 = accuracy column
mrt_avg = np.mean(data[:,4])   # 477.3ms #4 = RT column


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#
word_accuracy = []
word_RT = []
face_accuracy = []
face_RT = []

for i in range(92): #92 is for 92 participants/rows
    stim = int(data[i][1])
    if stim == 1:
        word_accuracy.append(data[i][3])
        word_RT.append(data[i][4])
    else:
        face_accuracy.append(data[i][3])
        face_RT.append(data[i][4])

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms
word_accuracy_avg = np.mean(word_accuracy)*100
word_mrt_avg = np.mean(word_RT)

face_accuracy_avg = np.mean(face_accuracy)*100
face_mrt_avg = np.mean(face_RT)

#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
accuracy_wp_list = []
accuracy_bp_list = []
mrt_wp_list = []
mrt_bp_list = []

for i in range(92):
    stim = int(data[i][2])
    if stim == 1:
        accuracy_wp_list.append(data[i][3])
        mrt_wp_list.append(data[i][4])
    else:
        accuracy_bp_list.append(data[i][3])
        mrt_bp_list.append(data[i][4])

accuracy_wp = np.mean(accuracy_wp_list)*100  # 94.0%
accuracy_bp = np.mean(accuracy_bp_list)*100  # 88.9%
mrt_wp = np.mean(mrt_wp_list) # 469.6ms
mrt_bp = np.mean(mrt_bp_list)  # 485.1ms


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
words_wp = []
words_bp = []
faces_wp = []
faces_bp = []

for i in range(92):
    stim = int(data[i][1])
    pair = int(data[i][2])
    if stim == 1 and pair == 1:
        words_wp.append(data[i][4])
    elif stim == 1 and pair == 2:
        words_bp.append(data[i][4])
    elif stim == 2 and pair == 1:
        faces_wp.append(data[i][4])
    elif stim == 2 and pair == 2:
        faces_bp.append(data[i][4])

words-white/pleasant = np.mean(words_wp) #478.4ms
words-black/pleasant = np.mean(words_bp) #500.3ms
faces-white/pleasant = np.mean(faces_wp) #460.8ms
faces-black/pleasant = np.mean(faces_bp) #469.9ms


#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats

t-test_words = scipy.stats.ttest_rel(words-white/pleasant, words-black/pleasant)
t-test_faces = scipy.stats.ttest_rel(faces-white/pleasant, faces-black/pleasant)

# words: t=-5.36, p=2.19e-5
# faces: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))

#stim avg 
print("\nWORD AVERAGES: {:.2f}%, {:.1f} ms".format(word_accuracy_avg, word_mrt_average))
print("\nFACE AVERAGES: {:.2f}%, {:.1f} ms".format(face_accuracy_avg, face_mrt_average))
##condition avg
print("\nACCURACY AVERAGES FOR WHITE/BLACK PLEASANT: {:.2f}%, {:.1f}".format(accuracy_wp,accuracy_bp))
print("\nREACTION TIME AVERAGES FOR WHITE/BLACK PLEASANT: {:.2f}%, {:.1f} ms".format(mrt_wp,mrt_bp))
print("\nREACTION TIME AVERAGES FOR WORDS FOR WHITE PLEASANT: {:.2f} ms".format(words-white/pleasant))
print("\nREACTION TIME AVERAGES FOR WORDS FOR BLACK PLEASANT: {:.2f} ms".format(words-black/pleasant))
print("\nREACTION TIME AVERAGES FOR FACES FOR WHITE PLEASANT: {:.2f} ms".format(faces-white/pleasant))
print("\nREACTION TIME AVERAGES FOR FACES FOR BLACK PLEASANT: {:.2f} ms".format(faces-black/pleasant))
#ttest 
print("\nT-TEST STATS FOR WORDS: {:.2f}".format(t-test_words))
print("\nT-TEST STATS FOR FACES: {:.2f}".format(t-test_faces))
