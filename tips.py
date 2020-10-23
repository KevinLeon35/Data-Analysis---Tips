import pandas as pd
import datetime as dt
from pandas_datareader import data
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
%matplotlib inline

#import all modules

tips = sns.load_dataset('tips')   #use the sns module to load default tips dataframe within sns, store it as tips. data_source generating

tips.head() #show the top 5 rows of tips

tips.describe()

tips.groupby()

tips.info()

sns.distplot(tips['total_bill'],kde=False,bins=35)  #shows the total bill as x axis and counts of different bills as y axis

sns.jointplot(x= "total_bill", y="tip", data = tips, kind="hex") #shows a jointplot with total bill as x axis, tip as y axis, and hex as the kind.

sns.pairplot(tips, hue="sex") #do jointplots for every single combination of numeric columns in the tips dataframe, different sex column will have different color

sns.barplot(x = "sex", y ="total_bill", data=tips)

sns.countplot(x="sex", data=tips)

sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker") #categolize by smokers or not, doesnt include outliners

sns.violinplot(x="day", y= "total_bill", data=tips, hue = "sex", split=True) #include outliners, has more info than boxplot.

sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue="sex", split=True) #jitter = True to seperate stack points

sns.swarmplot(x='day', y='total_bill', data=tips) #swarmplot is a combo of violinplot and stripplot together

sns.factorplot(x='day', y='total_bill', data=tips, kind='bar') #equals to a barplot, all plots can be called in this way.

tips1 = tips.groupby("time")

tips1.head()

tips1.size()

tips1.last()

tips1.first()

tips1.groups

tips1.get_group("Lunch")

tips1.get_group("Dinner")

tips1.max()

tips1.min()

tips1.sum()

tips1.mean()

tips1["tip"].sum()

tips1["total_bill"].sum()

tips2 = tips.groupby("day")

tips2.head()

