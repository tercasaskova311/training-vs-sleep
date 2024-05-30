# Training vs. sleep in professional sport

This is a data analytics project analysing training of professional mountain biker, correlation in sleep and performance.

****Training vs Sleep.
This dataset compare data from a professional athlete who use Whoop devices for measuring HR, sleep performance and Garmin device to measure sport (mostly cycling performance).

1. Excel data cleaning. Excel had been used in the beginning of the process for cleaning two spreadsheet, sleeps and workouts_trainingpeaks. I had cleaned the data, as they contains null rows and cells, missing values, unstructured time column and others. Two cleaned and standardised spreadsheet had been made.

2. SQL - data standardisation, joining tables and comparing data. I had used Sql of joining tables, cleaning duplicates and cells with missing values. SQL code is uploaded.

3. Python - data analysis and visualisation - I had used python libraries pandas and matplotlib for last step of data analysis. 
 a)Scatter plot - analysing relationship between TSS and sleep performance. The scatter plot illustrates how these metrics correlate. 
b)bar plot - shows average TSS by workout type with Bike and XC-Ski being the highest. This is interesting data. XC-ski being at the top, even tho the athlete does not ski that often, these few xc-ski trains still does have the highest TSS after Bike. 
c)Correlation Matrix Heatmap 
 Correlation Coefficients:
-1.0 (Dark Red): Perfect positive correlation.
-1.0 (Dark Blue): Perfect negative correlation.
-0 (White): No correlation.

-Sleep and Sleep Performance % (0.918): There is a strong positive correlation between sleep duration and sleep performance percentage. This suggests that longer sleep duration is associated with higher sleep performance.
-Sleep and Deep (SWS) duration (0.741): There is a moderate positive correlation between sleep duration and the duration of deep sleep. This means that longer sleep tends to include more deep sleep.

Average values:
--------------
Average Sleep Duration: 8: 20 hod.
 Average Sleep Performance (%): 79.096
 Average Deep (SWS) Duration (minutes): 84.9
 Average TSS: 102.43
