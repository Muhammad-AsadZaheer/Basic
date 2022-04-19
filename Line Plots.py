# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 07:58:38 2022

@author: Asad
"""

#importing Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#dataset loading

dataset=pd.read_csv(r"C:\Users\Asad\Desktop\juypter_notebook\datasets\Chilla_data2_for_plots.csv")

#print loaded dataset

dataset

#allocating values to x and y coordinates

sns.lineplot(x="Where do you live?", y="Age", data=dataset)

#Theme setting

sns.set_theme(style="ticks", color_codes=True)

#Adding ttile to plot

plt.title("this is my first line graph on own dataset")
plt.show()



#Here we will add x and y coordinate labels

##importing Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#dataset loading

dataset=pd.read_csv(r"C:\Users\Asad\Desktop\juypter_notebook\datasets\Chilla_data2_for_plots.csv")

#print loaded dataset

dataset

#allocating values to x and y coordinates

sns.lineplot(x="Qualification_completed", y="Age", data=dataset)

#Theme setting

sns.set_theme(style="ticks", color_codes=True)

#Adding Lables to plot

plt.xlabel("this is my X label")
plt.ylabel("this is my Y label")

#Adding ttile to plot

plt.title("this is my first line graph on own dataset")
plt.show()



#section 3

##importing Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset

dataset=pd.read_csv(r"C:\Users\Asad\Desktop\juypter_notebook\datasets\Chilla_data2_for_plots.csv")

#Describing dataset

dataset.describe()


#allocating values to x and y coordinates

plot = sns.lineplot(x="Qualification_completed", y="Age", data=dataset)

#Adding title

plt.title("this is my first title dataset")

#Adding limit to x and y axis

plt.xlim(1)
plt.ylim(5)

#show plot

plt.show()


#importing libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset

data_set= pd.read_csv(r"C:\Users\Asad\Desktop\juypter_notebook\datasets\Chilla_data2_for_plots.csv")

#data_set.describe()
#first_plot=sns.lineplot(x="What are you?", y = "Blood group", data=data_set,  color='#a862a7', linewidth=5)

#allocating values to x and y coordinates

first_plot=sns.lineplot(x = "Age", y = "Marital Status?", hue = "Purpose_for_chilla", data=data_set,  color='#a862a7', linewidth=5)


#setting plot style

first_plot = sns.set_style("dark")

#reoving despine

sns.despine(left=False, bottom=False)

#Setting digure size, you can modify that according to your requirements

first_plot= plt.figure(figsize=(12,4))

#Show plot

plt.show()

