# diabetes

Red Wine Quality Prediction
by Jie Hu, Email: jie.hu.ds@gmail.com

This markdown will use explorsive data analysis to figure out which attributes affect quality of red wine significantly. To do this, I use the dataset including the quality rate by at least 3 experts and the chemical properties of the wine. This dataset might indicate how current experts, representing the test nowadays, think what a good red wine is.

Univariate Plots Section
Explore part
To begin with, let’s summarise the data:

## 'data.frame':    1599 obs. of  12 variables:
##  $ fixed.acidity       : num  7.4 7.8 7.8 11.2 7.4 7.4 7.9 7.3 7.8 7.5 ...
##  $ volatile.acidity    : num  0.7 0.88 0.76 0.28 0.7 0.66 0.6 0.65 0.58 0.5 ...
##  $ citric.acid         : num  0 0 0.04 0.56 0 0 0.06 0 0.02 0.36 ...
##  $ residual.sugar      : num  1.9 2.6 2.3 1.9 1.9 1.8 1.6 1.2 2 6.1 ...
##  $ chlorides           : num  0.076 0.098 0.092 0.075 0.076 0.075 0.069 0.065 0.073 0.071 ...
##  $ free.sulfur.dioxide : num  11 25 15 17 11 13 15 15 9 17 ...
##  $ total.sulfur.dioxide: num  34 67 54 60 34 40 59 21 18 102 ...
##  $ density             : num  0.998 0.997 0.997 0.998 0.998 ...
##  $ pH                  : num  3.51 3.2 3.26 3.16 3.51 3.51 3.3 3.39 3.36 3.35 ...
##  $ sulphates           : num  0.56 0.68 0.65 0.58 0.56 0.56 0.46 0.47 0.57 0.8 ...
##  $ alcohol             : num  9.4 9.8 9.8 9.8 9.4 9.4 9.4 10 9.5 10.5 ...
##  $ quality             : int  5 5 5 6 5 5 5 7 7 5 ...
The dataset includes 1599 observations with 12 variables.

Then let’s explot the variables one by one. Because all the variables are numeric, I will mainly use histogram to explore and figure out if there’re something interesting worth further steps.

- quality -

Quality is what this report concerns with, the rate here represent average rate from at least 3 experts. First let’s see how the quality of 1599 wine distributed.



##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   3.000   5.000   6.000   5.636   6.000   8.000
## 
##   3   4   5   6   7   8 
##  10  53 681 638 199  18
Quality, ranging from 3-8, is integer type data. About 82.5% observations get 5-6 ratings, while only 14.2% (227 counts) got 3,7 or 8 scores on quality rating. Because the score were average made by 3 or more experts.

Now let’s check quality by dividing them into 3 groups: Low”(3-4), “Moderate”(5-6), “High”(7-8)

## 
##      Low(3-4) Moderate(5-6)     High(7-8) 
##            63          1319           217


The moderate quality wines takes up most part and we have much less data on low/high quality wines, which might produce some bias in this analysis. But I will assume the data is reliable and trustworthy.

-fixed.acidity-



##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##    4.60    7.10    7.90    8.32    9.20   15.90
“fixed.acidity” is a measure of inside liquid concentration. The histogram a little right-skewed distributed with some outliers located at right side. The most frequent values are between 7-8. IQR is 2.1. The maximum is a little far from 3rd quantile compared with IQR.

To improve the plot, I removed the top 1% and bottom 1% data and use log transformation:

##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   5.300   7.100   7.900   8.294   9.200  13.200
Now the 3rd quantile is not far from max value, and data gathers more around center.



It looks much better, symmetric without too much attention on outliers. We can see majority fixed acidity gathering in middle part.

-volatile.acidity-



##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.1200  0.3900  0.5200  0.5278  0.6400  1.5800
“volatile.acidity” is measure of acidity above-surface of liquid. The histogram is right-skewed distributed with some outliers located at right side. The most frequent values are between 0.4-0.6. IQR is 0.25.

To improve the plot, I removed the top 1% outliers and use log transformation:

##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.1600  0.3900  0.5200  0.5213  0.6300  1.0100
Now the IQR is 0.11, data concentrates more on center.



It looks much better, symmetric and bell shaped without extreme outliers. We can see majority volatile acidity gathering in middle part. The most common log10(volatile.acidity + 1) values are between 0.19 and 0.21

-citric.acid-



##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.000   0.090   0.260   0.271   0.420   1.000
“citric.acid” is right-skewed distributed with some outliers located at very right side. The most frequent values 0. It’s also interesting a lot of wine have citric.acid = 0, IQR is 0.33.

To improve the plot, I just removed the top 1% outliers and use log transformation (the downside has a lot of value without citric acid so it’s better to keep them):

##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0100  0.1300  0.2800  0.2902  0.4400  0.7000
Now the IQR is 0.31, data gathers more in center.

This time, I use square root instead of log10, because log10 plot has binwidth varies significantly.



It looks much better. But notice the scale of citric acid is not evenly distributed, instead, the scale is exponentially decreased. This plot can let us more focus on majority citric acid gathering in middle part.
The most common citric.acid values are around 0.49. Before it was 0.1, by using higher accurate, we can see it has been changed.

-residual.sugar-



##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.900   1.900   2.200   2.539   2.600  15.500
“residual.sugar” is right-skewed distributed with a lot of outliers located at right side and a little bit at left side. The most frequent values are between 1.9-2.4. IQR is 1.7. However, the maximum is locate too far away from 3rd quantile.

To improve the plot, I just removed the top and bottom 10% outliers and use log transformation, because this time we have too many outliers with extreme value:

##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   1.700   1.950   2.200   2.245   2.500   3.500
Now the IQR is 0.55, data gathers more in center.



It looks much better, more symmetric without extreme outliers. From this plot, we can see more details, for example, the most common value is 2.0!
