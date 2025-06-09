# Gold Trade Analysis

## Overview
This project provides a comprehensive analysis of the gold market, examining recent trends, price movements, and key market drivers. The analysis includes technical indicators, support/resistance levels, and macroeconomic factors such as inflation data, central bank policies, and geopolitical tensions.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Analysis Methodology](#analysis-methodology)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Historical gold price analysis
- Technical indicator calculations
- Support and resistance level identification
- Macroeconomic factor analysis
- Data visualization
- Trading strategy recommendations

## Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Gold-Trade-Analysis.git
cd Gold-Trade-Analysis
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Data Sources
- Gold price data: [Yahoo Finance](https://finance.yahoo.com/quote/GC=F/)
- Economic indicators: [FRED](https://fred.stlouisfed.org/)
- Central bank data: [World Gold Council](https://www.gold.org/)
- Geopolitical events: Various financial news sources

## Project Structure
```
Gold-Trade-Analysis/
├── data/               # Raw and processed data files
├── notebooks/          # Jupyter notebooks for analysis
├── src/               # Source code
│   ├── data/         # Data processing scripts
│   ├── analysis/     # Analysis modules
│   └── visualization/# Visualization tools
├── tests/            # Unit tests
├── requirements.txt  # Project dependencies
└── README.md        # Project documentation
```

## Analysis Methodology
1. **Data Collection**
   - Historical price data
   - Economic indicators
   - Market sentiment
   - Geopolitical events

2. **Technical Analysis**
   - Moving averages
   - RSI (Relative Strength Index)
   - MACD (Moving Average Convergence Divergence)
   - Support and resistance levels

3. **Fundamental Analysis**
   - Inflation metrics
   - Interest rates
   - Currency strength
   - Market sentiment

4. **Risk Assessment**
   - Volatility analysis
   - Correlation studies
   - Market regime identification

## Usage
1. Data Collection:
```python
python src/data/collect_data.py
```

2. Run Analysis:
```python
python src/analysis/main.py
```

3. Generate Visualizations:
```python
python src/visualization/create_charts.py
```


## Contact 
Project Link: [https://github.com/yourusername/Gold-Trade-Analysis](https://github.com/yourusername/Gold-Trade-Analysis)
