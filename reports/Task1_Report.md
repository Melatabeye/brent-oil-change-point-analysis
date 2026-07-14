# Brent Oil Price Change Point Analysis
## Task 1: Analysis Planning and Data Understanding

## 1. Introduction

This project focuses on analyzing how major geopolitical, economic, and policy events influence Brent crude oil prices. The objective is to identify structural changes (change points) in the historical Brent oil price series and understand the relationship between significant events and oil market fluctuations.

The analysis is conducted for Birhan Energies to provide data-driven insights that support investors, policymakers, and energy sector stakeholders in understanding oil price risks and market behavior.

---

# 2. Data Analysis Workflow

The analysis will follow a structured data science workflow:

## Step 1: Data Collection and Preparation

- Obtain historical Brent oil price data covering daily observations from May 1987 to September 2022.
- Load the dataset into Python using pandas.
- Convert date variables into datetime format.
- Check for missing values, duplicate records, and data consistency.
- Prepare additional variables such as daily returns and volatility measures.

## Step 2: Exploratory Data Analysis (EDA)

The exploratory analysis will include:

- Visualization of Brent oil price trends over time.
- Identification of major price increases and declines.
- Analysis of periods with high market volatility.
- Calculation of log returns:

  log return = log(price_t) - log(price_t-1)

- Stationarity testing using statistical methods such as the Augmented Dickey-Fuller test.

## Step 3: Event Research and Integration

Major oil market events will be compiled into a structured event dataset including:

- Date of event
- Event description
- Event category
- Expected market impact

Events include:
- Geopolitical conflicts
- OPEC production decisions
- Economic crises
- International sanctions
- Global disruptions

## Step 4: Bayesian Change Point Analysis

A Bayesian change point model will be developed using PyMC.

The model will:

- Identify dates where the statistical behavior of oil prices changes.
- Estimate average price levels before and after detected changes.
- Quantify the magnitude of market shifts.
- Evaluate uncertainty using Bayesian posterior distributions.

## Step 5: Interpretation and Reporting

Detected change points will be compared with historical events to develop hypotheses about possible drivers of oil price changes.

Results will be communicated through:

- Visualizations
- Statistical summaries
- Dashboard outputs
- Stakeholder-focused reports

---

# 3. Assumptions

The analysis assumes:

- Historical Brent oil prices accurately represent global crude oil market conditions.
- Major geopolitical and economic events are potential drivers of structural market changes.
- The selected events represent important external factors affecting oil prices.
- Statistical change points indicate periods of unusual market behavior.

---

# 4. Limitations

## Correlation vs Causation

A detected relationship between an event and an oil price change does not prove that the event directly caused the price movement.

For example, if a price increase occurs after an OPEC announcement, the change may also be influenced by other factors such as:

- Global demand changes
- Currency movements
- Inventory levels
- Other geopolitical developments

Therefore, this analysis identifies associations and possible explanations rather than establishing definite causal relationships.

## Other Limitations

- The model mainly focuses on price history and selected events.
- External economic variables such as GDP, inflation, and exchange rates are not included.
- Market reactions may occur before or after the actual event date.
- Multiple events may happen simultaneously, making attribution difficult.

---

# 5. Communication Strategy

The findings will be communicated through:

## Reports

A detailed analytical report will summarize:

- Major detected change points
- Associated events
- Quantified price impacts
- Recommendations

## Dashboard

An interactive dashboard will allow stakeholders to:

- Explore historical prices
- View detected structural changes
- Filter important events
- Understand market reactions

## Presentations

Results will be presented using:

- Time-series charts
- Change point visualizations
- Event impact summaries

The target audience includes:

- Energy investors
- Policymakers
- Energy companies
- Market analysts
