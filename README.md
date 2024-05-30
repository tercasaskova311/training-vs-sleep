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

**a) Scatter Plot**:
- **Objective**: To analyze the relationship between Training Stress Score (TSS) and sleep performance.
- **Findings**: The scatter plot illustrates the correlation between TSS and sleep performance, providing insights into their relationship.

**b) Bar Plot**:
- **Objective**: To show average TSS by workout type.
- **Findings**:
  - **Bike and XC-Ski**: These workouts have the highest average TSS.
  - **Insight**: Although the athlete does not ski frequently, XC-Ski sessions have a high TSS, indicating intense training.

**c) Correlation Matrix Heatmap**:
- **Objective**: To visualize correlation coefficients between various metrics.
- **Interpretation**:
  - **Color Scheme**:
    - Dark Red: Perfect positive correlation (1.0).
    - Dark Blue: Perfect negative correlation (-1.0).
    - White: No correlation (0).
      
  - **Findings**:
    - **Sleep Duration and Sleep Performance % (0.918)**: There is a strong positive correlation between sleep duration and sleep performance percentage, suggesting that longer sleep duration is associated with higher sleep performance.
    - **Sleep Duration and Deep Sleep (SWS) Duration (0.741)**: There is a moderate positive correlation between sleep duration and the duration of deep sleep, indicating that longer sleep tends to include more deep sleep.

#### Summary of Average Values

- **Average Sleep Duration**: 8 hours and 20 minutes.
- **Average Sleep Performance**: 79.096%.
- **Average Deep Sleep (SWS) Duration**: 84.9 minutes.
  - *Note*: Most adults need around 1.5–2 hours of deep sleep per night.
- **Average TSS**: 102.43.
  - **TSS® Guide**:
    - Below 150 (low): Recovery likely completed by the next day.
    - 150 to 300 (medium): Possible leftover tiredness the next day, likely gone by the second day.
    - 300 to 450 (high): Some tiredness even after two days.
    - More than 450 (very high): Likely tired for several days after the ride.

This project demonstrates a comprehensive analysis of the relationship between training and sleep in a professional athlete. By employing rigorous data cleaning, standardization, and analysis techniques, significant correlations were uncovered, highlighting the importance of sleep in athletic performance. These insights can be instrumental for athletes and coaches in optimizing training and recovery strategies.
