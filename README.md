# Japan vs Philippines GDP per Capita Analysis
This project compares GDP per capita trends between Japan and the Philippines using historical World Bank data and Python.
GDP per capita is used to compare the approximate economic output per person between the two countries and to examine how the gap has changed over time.
The analysis includes long-term trends, moving averages, growth rates, ratios, the GDP per capita gap, and correlation analysis.

## Research Questions
* How has GDP per capita changed in Japan and the Philippines over time?
* How large has the GDP per capita gap been?
* How have growth rates changed between the two countries?
* Has the Philippines experienced long-term growth relative to Japan?
* How strongly are GDP per capita levels in the two countries statistically related?

## Data
**Source**: World Bank Open Data
**Countries**: Japan, Philippines
**Indicator**: GDP per capita

## Tools Used
* Python
* pandas
* matplotlib
* NumPy

## Analysis
### 1. GDP per Capita Trend Comparison
Compares GDP per capita levels in Japan and the Philippines over time.
### 2. Moving Average Analysis
Uses a 5-year moving average to reduce short-term fluctuations and highlight long-term trends.
### 3. GDP per Capita Gap
Calculates:
**Japan GDP per Capita - Philippines GDP per Capita**
This measures the difference in GDP per capita between the two countries.
### 4. Growth Rate Analysis
Examines year-to-year changes in GDP per capita.
### 5. GDP per Capita Ratio
Calculates the relative size of the Philippines' GDP per capita compared with Japan.
### 6. Correlation Analysis
Uses a scatter plot, correlation coefficient, and regression line to examine the relationship between GDP per capita in Japan and the Philippines.

## Key Findings
* Japan maintained a substantially higher GDP per capita than the Philippines throughout the observed period.
* The Philippines showed consistent long-term growth as an emerging economy.
* The gap between Japanese and Philippine GDP per capita changed considerably over time.
* The GDP per capita ratio indicates that Philippine GDP per capita remained substantially below Japan's throughout the observed period.
* The correlation between Japanese and Philippine GDP per capita was approximately **0.74**, indicating a relatively strong positive relationship.
* The positive relationship suggests that the two countries' GDP per capita levels tended to increase over the long term, although correlation alone does not establish a causal relationship.

## Visualization
### GDP per Capita Comparison
![GDP per Capita Analysis](gdp_per_capita_analysis.png)
The visualization includes GDP per capita trends, the GDP per capita gap, growth rates, the ratio between the two countries, and a scatter plot showing their statistical relationship.

## Interpretation
The long-term increase in Philippine GDP per capita reflects substantial economic growth over the observed period.

However, GDP per capita alone does not fully measure living standards or individual income.

GDP per capita can also be affected by:
* Population changes
* Inflation
* Exchange rates
* Economic structure
* Differences in purchasing power

For this reason, GDP per capita should be interpreted alongside other indicators such as inflation, unemployment, and GDP growth.

## Limitations
This project focuses on GDP per capita and does not directly measure:
* Income inequality
* Household income
* Purchasing power
* Cost of living
* Quality of life
* Distribution of economic growth

Correlation analysis also measures association rather than causation.

## Future Improvements
* Compare GDP per capita using purchasing power parity (PPP)
* Adjust GDP per capita for inflation
* Add GDP growth rates
* Compare additional ASEAN economies
* Analyze income inequality
* Examine convergence between the two economies
* Build an interactive Power BI dashboard

## What I learned
Through this project, I practiced:
* Working with World Bank economic data
* Data cleaning and processing using pandas
* Creating time-series visualizations
* Calculating moving averages and growth rates
* Comparing economic indicators between countries
* Performing correlation and regression analysis
* Interpreting economic data while considering its limitations

## Future Project
This analysis will be combined with my GDO, inflation, and unemployment projects to create a broader:
**Japan vs Philippines Economic Comparison**
using Python, SQL, and Power BI.
