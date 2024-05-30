### Data Analytics Project: Training vs. Sleep in Professional Cycling

Overview:

In this project I analyzes the relationship between training and sleep performance in a professional mountain biker. Data was gathered using two sport devices: the Whoop band, which monitors sleep, strain, and recovery, and the Garmin bike computer, which tracks cycling performance metrics such as heart rate, distance, and power. The goal is to understand how sleep correlates with training performance.

-------------
#### Data Preparation and Cleaning

**Excel Data Cleaning**:
- **Data Sources**: Two spreadsheets, "sleeps" and "workouts_trainingpeaks," provided by a World Cup MTB rider.
- **Cleaning Process**: 
  - Removed null rows and cells.
  - Addressed missing values.
  - Standardized unstructured time columns.
- **Outcome**: Two cleaned and standardized spreadsheets ready for further analysis.

**SQL Data Standardization**:
- **Tasks Performed**:
  - Joined tables to consolidate data.
  - Removed duplicates and handled cells with missing values.
  - SQL code used for this process is attached.
- **Outcome**: A standardized dataset ready for analysis.

#### Data Analysis and Visualization

**Python Analysis**:
Using Python libraries/Pandas and Matplotlib, I conducted the final data analysis and visualization.

**Data Description**:
- **TSS (Training Stress Score)**: Provided by the Garmin bike computer, TSS measures the stress put on the body from a ride. It is calculated using Normalized Power (NP), Intensity Factor (IF), and ride duration. TSS helps determine the best combination of workouts and rest periods.
- **Sleep Performance**: WHOOP calculates sleep performance by measuring the sleep you got compared to the sleep your body needs, giving a score from 0 to 100%.
- **Deep Sleep (SWS)**: Known as slow wave sleep, it is one of the four stages of sleep and is crucial for physical restoration.

**a) Scatter Plot**:Workout Types and Sleep Duration

- **Objective**: To analyze the relationship between Training Stress Score (TSS) and sleep performance.
- **Findings**: The scatter plot illustrates the correlation between TSS and sleep performance, providing insights into their relationship.

The analysis of average sleep duration by workout type showed:
- **Run**: Highest average sleep duration (approximately 544 minutes).
- **Custom**: High average sleep duration (approximately 523 minutes).
- **Bike**: Moderate average sleep duration (approximately 510 minutes).
- **MTB (Mountain Biking)**: Slightly lower average sleep duration (approximately 501 minutes).
- **Other**: Lowest average sleep duration (approximately 492 minutes).


**b) Bar Plot**: Sleep Performance by Workout Type
- **Objective**: To show average TSS by workout type.
  
The analysis of average sleep performance by workout type showed:
- **Run**: Highest average sleep performance (approximately 86.67%).
- **Custom**: High average sleep performance (approximately 85.33%).
- **Bike**: Moderate average sleep performance (approximately 80.72%).
- **MTB (Mountain Biking)**: Slightly lower average sleep performance (approximately 77.69%).
- **Other**: Lowest average sleep performance (approximately 73.65%).
  
**c) Correlation Matrix Heatmap**:
- **Objective**: To visualize correlation coefficients between various metrics.
- **Interpretation**:
  - **Color Scheme**:
    - Dark Red: Perfect positive correlation (1.0).
    - Dark Blue: Perfect negative correlation (-1.0).
    - White: No correlation (0).
     
The correlation matrix and heatmap revealed key relationships among the sleep and training metrics:
- **Strong Positive Correlations**:
  - **Sleep and Sleep Performance % (0.918)**: Longer sleep duration is associated with better sleep performance.
  - **Sleep and Deep (SWS) duration (0.741)**: Longer sleep duration tends to include more deep sleep.
- **Moderate Positive Correlations**:
  - **Sleep Performance % and Deep (SWS) duration (0.721)**: Higher sleep performance is linked with more deep sleep.
- **Weak or No Correlations**:
  - **TSS and other metrics**: Training Stress Score (TSS) has very weak correlations with sleep duration, sleep performance, and deep sleep duration, indicating that TSS does not significantly impact these sleep metrics.
-------

### Conclusion
The data analysis shows that:
- Longer sleep duration positively impacts sleep performance and deep sleep duration.
- Training Stress Score (TSS) does not significantly correlate with sleep metrics.



