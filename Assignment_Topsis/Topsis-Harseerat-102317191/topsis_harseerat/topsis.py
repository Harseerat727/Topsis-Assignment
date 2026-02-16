import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print("Error:", msg)
    sys.exit(1)

def main():
    if len(sys.argv) != 5:
        error("Usage: topsis <InputFile> <Weights> <Impacts> <OutputFile>")

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.isfile(input_file):
        error("Input file not found")

    try:
        data = pd.read_csv(input_file)
    except:
        error("Unable to read input file")

    if data.shape[1] < 3:
        error("Input file must contain at least 3 columns")

    criteria = data.iloc[:, 1:]

    if not np.all(criteria.applymap(np.isreal)):
        error("Columns 2 to last must contain numeric values only")

    weights = weights.split(',')
    impacts = impacts.split(',')

    if len(weights) != criteria.shape[1]:
        error("Number of weights must match number of criteria")

    if len(impacts) != criteria.shape[1]:
        error("Number of impacts must match number of criteria")

    try:
        weights = np.array(weights, dtype=float)
    except:
        error("Weights must be numeric")

    for i in impacts:
        if i not in ['+', '-']:
            error("Impacts must be either + or -")

    norm = np.sqrt((criteria ** 2).sum())
    normalized = criteria / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    s_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = s_minus / (s_plus + s_minus)

    data['Topsis Score'] = score
    data['Rank'] = score.rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)
    print("TOPSIS completed successfully")

if __name__ == "__main__":
    main()
