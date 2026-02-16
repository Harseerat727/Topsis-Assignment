# TOPSIS Assignment – Multi-Criteria Decision Making

## Overview
This project implements **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** for multi-criteria decision-making.  
The assignment is divided into three parts:

1. **Part I – Command Line Python Program**  
2. **Part II – Python Package** (uploadable to PyPI)  
3. **Part III – Web Service (Flask)** with email functionality  

---

## Folder Structure

Topsis-Assignment/
├── CLI/ # Part I - Command Line program
│ └── topsis.py
├── Package/ # Part II - Python Package
│ └── topsis_pkg/
│ ├── init.py
│ └── topsis_module.py
│ └── setup.py
├── FlaskWeb/ # Part III - Flask Web Service
│ ├── app.py
│ └── index.html
├── sample_data.csv # Example CSV file
├── requirements.txt # Dependencies
├── README.md # Project instructions
└── LICENSE


---

## Part I – Command Line Python Program

### Usage
```bash
python CLI/topsis.py <InputFile> <Weights> <Impacts> <OutputFile>
Example
python CLI/topsis.py sample_data.csv 1,1,1,2 +,+,-,+ result.csv
Input CSV must have 3 or more columns (first = alternative, rest = numeric criteria)

Weights and impacts must match the number of numeric columns

Impacts: + (benefit), - (cost)

Output CSV contains Topsis Score and Rank

Sample Input (sample_data.csv)
Model,Price,Mileage,Comfort,Safety
Car A,20000,13,3,5
Car B,25000,12,4,4
Car C,30000,18,5,1
Car 4,35000,11,2,3
Sample Output (result.csv)
Model	Price	Mileage	Comfort	Safety	Topsis Score	Rank
Car C	30000	18	5	1	0.679	1
Car A	20000	13	3	5	0.623	2
Car B	25000	12	4	4	0.396	3
Car 4	35000	11	2	3	0.301	4
Part II – Python Package
Installation
Install the package from PyPI:

pip install Topsis-Harseerat-102317191==1.0.0
Usage (Command Line via Package)
topsis-cli sample_data.csv 1,1,1,2 +,+,-,+ result.csv
Produces the same Topsis Score and Rank as the CLI script

Package version used: 1.0.0

Folder Details
Package/
└── topsis_pkg/
    ├── __init__.py
    └── topsis_module.py
Part III – Web Service (Flask)
Run the Web App
python FlaskWeb/app.py
Opens at: http://127.0.0.1:5000

Use index.html form to:

Upload CSV file

Enter weights and impacts

Enter email address

The result CSV will be sent automatically to the email provided

Example Email Result
Model	Price	Mileage	Comfort	Safety	Topsis Score	Rank
Car C	30000	18	5	1	0.679	1
Car A	20000	13	3	5	0.623	2
Car B	25000	12	4	4	0.396	3
Car 4	35000	11	2	3	0.301	4
Input Validation and Cleaning
Automatically handles:

Extra spaces in CSV

Non-numeric values (filled with column mean)

Missing values

Encoding issues (utf-8, latin1)

Checks:

Number of weights = number of impacts = number of numeric columns

Impacts are + or -

Email format is valid for web service

Dependencies
All dependencies are listed in requirements.txt:

pandas
numpy
flask
Install them using:

pip install -r requirements.txt
Author
Harseerat – Assignment Submission
GitHub: https://github.com/Harseerat727/Topsis-Assignment


---

This README includes:

- **Folder structure**  
- **CLI usage and results**  
- **Python package usage** (with `pip install`)  
- **Flask web service instructions**  
- **Sample input/output tables**  
- **Dependencies and validation**  

---
