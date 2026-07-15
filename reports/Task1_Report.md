# Brent Oil Price Change Point Analysis
## Task 1 Report: Bayesian Change Point Analysis of Brent Oil Prices

## 1. Introduction

This project focuses on analyzing Brent crude oil price movements using exploratory data analysis and Bayesian Change Point Analysis.

The objective is to identify significant structural changes in oil price behavior and investigate whether these changes correspond with major economic and geopolitical events.

Understanding oil price transitions is important because crude oil prices influence energy markets, inflation, government policies, and investment decisions.

---

# 2. Dataset Description

The analysis uses daily Brent crude oil price data.

The dataset contains:

- Date: Daily observation date
- Price: Brent crude oil price in USD per barrel

The dataset contains:

- 9,927 daily observations
- Period: May 1987 to 2022

The raw dataset was stored separately from processed data following good data management practices.

---

# 3. Data Preparation

The following preprocessing steps were performed:

- Converted Date column into datetime format.
- Verified numerical format of price values.
- Checked for missing values.
- Removed invalid observations.
- Created processed dataset for modeling.

The cleaned dataset was saved as:


---

# 4. Exploratory Data Analysis

## 4.1 Brent Oil Price Trend

The historical price visualization shows significant fluctuations throughout the observed period.

Major market movements include:

- Early 1990s geopolitical uncertainty.
- 2008 global financial crisis.
- 2014 oil price decline.
- 2020 COVID-19 market shock.
- 2022 geopolitical disruptions.

---

## 4.2 Rolling Average Analysis

A 30-day rolling average was calculated to smooth daily fluctuations and identify long-term trends.

The rolling average demonstrates periods where the underlying price trend changed significantly.

---

## 4.3 Volatility Analysis

A 30-day rolling volatility measure was calculated using daily returns.

Periods of increased volatility correspond with major market uncertainty events.

---

## 4.4 Log Return Analysis

Log returns were calculated to analyze daily percentage changes in Brent prices.

The log return series highlights periods of extreme market movements.

---

# 5. Stationarity Testing

The Augmented Dickey-Fuller (ADF) test was applied to the log return series.

Results:

ADF Statistic:
p-value:

The p-value is significantly below the 0.05 threshold.

Therefore, the null hypothesis of non-stationarity was rejected.

The log return series was considered stationary and suitable for further time-series modeling.

---

# 6. Bayesian Change Point Analysis

A Bayesian Change Point model was implemented using PyMC.

The model assumes that the statistical behavior of oil prices changes at an unknown point.

The model estimates:

- Change point location
- Mean price before the change
- Mean price after the change
- Price variability

Bayesian sampling was performed using Markov Chain Monte Carlo (MCMC).

---

# 7. Model Results

The Bayesian model identified the most probable structural change point:

## Detected Change Point

Estimated market characteristics:

Before change point:

After change point:

The results indicate a significant shift in the underlying price level of Brent crude oil.

---

# 8. Historical Event Comparison

The detected change point was compared with a structured historical events dataset.

The closest recorded event was:

| Event | Date | Difference |
|---|---|---|
| Iraq War begins | 20 March 2003 | 706 days |

The detected change point does not directly correspond to one specific event.

Instead, the structural shift likely reflects multiple interacting factors, including:

- Increasing global oil demand.
- Supply constraints.
- Geopolitical uncertainty.
- Market expectation changes.

---

# 9. Software Engineering Practices

The project follows a structured workflow:

- Separation of raw and processed datasets.
- Reusable Python modules.
- Automated testing.

Implemented modules:

Testing was implemented using pytest.

---

# 10. Limitations

The analysis has several limitations:

- The Bayesian model identifies statistical changes but cannot prove direct causality.
- Historical events may influence markets with delays.
- Multiple economic factors can contribute to price transitions.

---

# 11. Conclusion

This project demonstrates how Bayesian Change Point Analysis can identify structural changes in Brent crude oil prices.

The detected February 2005 change point highlights a significant shift in oil price behavior.

Combining statistical modeling with historical event analysis provides a stronger understanding of commodity market dynamics and supports evidence-based decision making.