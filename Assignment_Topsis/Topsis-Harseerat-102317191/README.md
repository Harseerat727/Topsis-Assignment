# TOPSIS Package

This package implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method.

## Installation
pip install Topsis-Harseerat-102317191

## Usage
topsis input.csv "1,1,1,2" "+,+,-,+" output.csv

## Input Rules
- CSV file must have at least 3 columns
- First column is identifier
- Other columns must be numeric
- Weights and impacts must be comma-separated

## Output
Generates a CSV file with TOPSIS score and rank.
