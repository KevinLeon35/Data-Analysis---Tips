import pandas as pd
import datetime as dt
from pandas_datareader import data
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
%matplotlib inline

#import all modules

tips = sns.load_dataset('tips')   #use the sns module to load default tips dataframe within sns, store it as tips. data_source generating

