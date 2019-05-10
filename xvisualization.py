# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:30:15 2019

@author: Devadasan Kizhapat

This is a visualization script file.

Using pandas, matplotlib and seaborn modules
"""

# pip install pandas
# pip install matplotlib
# pip install seaborn

my_data_dir = 'E:\\Mydata'

# get functions
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset

tips =sns.load_dataset('tips')
# print (tips)
#tips=pd.read_csv(my_data_dir+"tips.csv")
#print(show)
# using lmplot
"""
print ('using lm plot')
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()
"""
# grouping using hue
"""
print ('grouping with hue')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='Set1')
plt.show()
"""
# groupng using col
"""
print ('grouping with col')
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
plt.show()

# using residplot 1
"""
"""
print ('using residual plot 1')
sns.residplot(x='size', y='total_bill', data=tips, color='blue')
plt.show()
"""
# using residplot 2
"""
print ('using residual plot 2')
sns.residplot(x='total_bill', y='tip', data=tips, color= 'blue')
plt.show()

# using stripplot

print ('using strip plot')
sns.stripplot(y= 'tip', data=tips)
plt.ylabel('tip ($)')
plt.show()

# grouping with stripplot
"""
"""
print ('grouping with strip plot')
sns.stripplot(x='day', y='tip',hue='sex', data=tips)
plt.ylabel('tip ($)')
plt.show()
"""
# spreading out stripplots
"""
print ('spreading out strip plots')
sns.stripplot(x='day', y='tip', data=tips, size=4, jitter=False)
plt.ylabel('tip ($)')
plt.show()
"""
# using swarmplot
"""
print ('using swarm plot')
sns.swarmplot(x='day', y='tip',data=tips)
plt.ylabel('tip ($)')
plt.show()
"""
# more grouping with swarmplot
"""
print ('more grouping with swarm plot')
sns.swarmplot(x='day', y='tip', data=tips, hue='sex')
plt.ylabel('tip ($)')
plt.show()
"""
# changing orientation
"""
print ('changing orientation of swarm plot')
sns.swarmplot(x='tip', y='day', data=tips, hue='sex', orient='h')
plt.ylabel('tip ($)')
plt.show()
"""
# using boxplot and violinplot
"""
print ('using box & violin plots')
plt.subplot(1,2,1)
sns.boxplot(x='day', y='tip', data=tips)
plt.ylabel('tip ($)')
plt.subplot(1,2,2)
sns.violinplot(x='day', y='tip', data=tips)
plt.ylabel('tip ($)')
plt.tight_layout()
plt.show()
"""
# combining plots
"""
print ('combining violin & strip plots')
sns.violinplot(x='day', y='tip', data=tips, inner=None, color='lightgray')
sns.stripplot(x='day', y='tip', data=tips, size=4, jitter=True)
plt.ylabel('tip ($)')
plt.show()

# using jointplot

print ('using joint plot')
sns.jointplot(x= 'total_bill', y= 'tip', data=tips)
plt.show()
"""
# jointplot using KDE
"""
print ('joint plot using KDE')
sns.jointplot(x='total_bill', y= 'tip', data=tips, kind='kde')
plt.show()
"""
# using pairplot
"""
print ('using pair plot')
sns.pairplot(tips)
plt.show()
"""
# using pairplot with hue

print ('using pair plot with hue')
sns.pairplot(tips, hue='sex')
plt.show()


