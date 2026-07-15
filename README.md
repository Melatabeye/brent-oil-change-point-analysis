# Bayesian Change Point Analysis of Brent Oil Prices

## Project Overview

This project analyzes Brent crude oil price movements using exploratory data analysis and Bayesian Change Point Analysis.

The objective is to identify structural changes in oil price behavior and relate detected changes to major historical market events.

---

## Business Objective

Oil price fluctuations affect energy companies, governments, investors, and policy decisions.

This project provides a data-driven approach to:

- Identify significant changes in Brent oil price behavior.
- Understand historical market transitions.
- Associate structural changes with economic and geopolitical events.

---

## Dataset

Source:
Brent crude oil daily prices dataset.

The dataset contains:

- Date
- Brent crude oil price (USD per barrel)

The analysis covers daily observations from 1987 to 2022.

---

## Project Structure


---

## Methodology

### 1. Exploratory Data Analysis

The analysis includes:

- Price trend visualization
- Rolling averages
- Volatility analysis
- Log returns
- Augmented Dickey-Fuller stationarity testing

### 2. Bayesian Change Point Analysis

A Bayesian model was implemented using PyMC to detect structural breaks in Brent oil prices.

The model estimates:

- Change point location
- Average price before the change
- Average price after the change
- Price uncertainty

---

## Key Result

The Bayesian model identified a structural change around:

**23 February 2005**

Estimated average prices:

Before change:
- Approximately $21.43 per barrel

After change:
- Approximately $76.27 per barrel

---

## Historical Event Comparison

The detected change point was compared with major historical events.

The closest recorded event was:

**Iraq War begins (20 March 2003)**

However, the change point did not directly correspond to one single event, suggesting that oil market transitions are influenced by multiple economic and geopolitical factors.

---

## Testing

Basic unit testing was implemented using pytest.

Run:

---

## Installation

Install dependencies:

Run notebooks using Jupyter:

---

## Conclusion

The project demonstrates how Bayesian Change Point Analysis can identify structural changes in commodity markets and provide insights into periods of significant price behavior shifts.

