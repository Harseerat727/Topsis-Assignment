# TOPSIS Assignment – Multi-Criteria Decision Making

## Overview
This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method for multi-criteria decision-making. The assignment is divided into three parts. Part I focuses on implementing a command-line Python program that can take input data, weights, and impacts, perform the TOPSIS calculations, and produce the results with scores and ranks. Part II involves packaging the TOPSIS functionality into a Python package that can be installed via PyPI. Part III implements a Flask-based web service that allows users to upload a data file, input weights and impacts, and receive the result via email.

## Part I – Command Line Program
The command-line program takes four parameters: the input data file, the weights for each criterion, the impacts (whether a criterion is beneficial or non-beneficial), and the name of the output result file. The program checks for proper input validation, including ensuring that the correct number of arguments are provided, that the input file exists, that numeric columns contain valid numbers, and that the number of weights and impacts matches the number of criteria columns. The program normalizes the data, applies the weights, determines ideal best and worst values for each criterion, calculates distances from the ideals, computes the TOPSIS score, and ranks the alternatives accordingly. The output file contains the scores and ranks for each alternative.

## Part II – Python Package
The TOPSIS functionality has been packaged into a Python package following standard packaging conventions. The package can be installed from PyPI using the command `pip install Topsis-Harseerat-102317191==1.0.0`. The package exposes a command-line interface similar to the standalone program and provides the same functionality. This allows users to perform TOPSIS calculations without needing to directly run the Python script. The package is structured with an `__init__.py` file and a module containing the core TOPSIS functions. Proper packaging allows for easy installation, version management, and reuse in other projects.

## Part III – Web Service (Flask)
A web service has been developed using Flask that enables users to perform TOPSIS calculations through a web interface. Users can upload a CSV file containing alternatives and criteria, input the weights and impacts, and provide an email address. The application validates the inputs, performs the TOPSIS calculation, generates the result file, and sends it automatically to the user’s email. The service handles common input issues such as missing values, non-numeric data, and incorrect formatting of weights or impacts. This provides a user-friendly interface for TOPSIS without requiring users to use the command line or Python environment.

## Input Validation and Error Handling
Across all parts, input validation and error handling are emphasized. The application checks that the number of weights and impacts matches the number of criteria, that impacts are specified correctly as positive or negative, and that the input data contains only numeric values in the criteria columns. Exceptions such as file not found, invalid numeric values, and encoding issues are handled gracefully. For the web service, the email format is validated to ensure that the result can be delivered successfully.

## Dependencies
The project uses standard Python libraries including pandas and numpy for data manipulation, and Flask for the web service. For sending emails in Part III, the smtplib and email libraries are used. All dependencies can be installed via pip.

## Conclusion
This assignment demonstrates the implementation of the TOPSIS method in multiple formats: a command-line tool, a Python package, and a web service. It showcases the ability to handle real-world data validation issues, perform multi-criteria decision-making calculations, and deliver results in multiple user-friendly ways. The project also covers software engineering practices such as packaging, documentation, and web development integration.


