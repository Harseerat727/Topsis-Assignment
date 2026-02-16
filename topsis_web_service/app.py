from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# -------------------- CLEAN CSV/EXCEL FUNCTION --------------------
def clean_data(file):
    """Clean uploaded CSV or Excel for TOPSIS"""
    try:
        # Try reading CSV
        try:
            df = pd.read_csv(file)
        except UnicodeDecodeError:
            file.seek(0)
            df = pd.read_csv(file, encoding='latin1', engine='python')
    except Exception:
        # Try Excel
        try:
            file.seek(0)
            df = pd.read_excel(file)
        except Exception as e:
            raise ValueError(f"Failed to read file: {e}")

    # Strip spaces from headers
    df.columns = [col.strip() for col in df.columns]

    # Strip spaces from string data
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # First column = alternatives, rest = numeric criteria
    numeric_cols = df.columns[1:]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill missing numeric values with column mean
    if df[numeric_cols].isnull().sum().sum() > 0:
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Ensure at least 3 columns
    if df.shape[1] < 3:
        raise ValueError("File must have at least 3 columns")

    return df

# -------------------- TOPSIS FUNCTION --------------------
def topsis(data, weights, impacts):
    norm_data = data / np.sqrt((data**2).sum())
    weighted = norm_data * weights

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

    dist_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    return score

# -------------------- EMAIL FUNCTION --------------------
def send_email(to_email, file_path):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'TOPSIS Result'
        msg['From'] = 'harseeratk2005@gmail.com'
        msg['To'] = to_email
        msg.set_content('Please find attached TOPSIS result.')

        with open(file_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename='result.csv')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('harseeratk2005@gmail.com', 'xqsh omft nlnq iiyr')  # App password
            server.send_message(msg)
        return True, ""
    except Exception as e:
        return False, str(e)

# -------------------- FLASK ROUTE --------------------
@app.route('/topsis', methods=['POST'])
def run_topsis():
    # -------------------- CHECK FILE --------------------
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    # -------------------- CLEAN THE DATA --------------------
    try:
        df = clean_data(file)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    alternatives = df.iloc[:, 0]
    data = df.iloc[:, 1:]

    # -------------------- WEIGHTS & IMPACTS --------------------
    try:
        weights = list(map(float, request.form['weights'].split(',')))
        impacts = request.form['impacts'].split(',')
    except:
        return jsonify({"error": "Invalid weights/impacts format"}), 400

    if len(weights) != len(impacts):
        return jsonify({"error": "Number of weights and impacts do not match"}), 400
    if len(weights) != data.shape[1]:
        return jsonify({"error": "Number of weights/impacts must match number of criteria columns"}), 400
    if not all(i in ['+', '-'] for i in impacts):
        return jsonify({"error": "Impacts must be '+' or '-'"}), 400

    # -------------------- CALCULATE TOPSIS --------------------
    scores = topsis(data, weights, impacts)
    df['Topsis Score'] = scores
    df['Rank'] = df['Topsis Score'].rank(ascending=False, method='min')

    output_file = "result.csv"
    df.to_csv(output_file, index=False)

    # -------------------- SEND EMAIL --------------------
    email = request.form['email']
    success, msg = send_email(email, output_file)
    if not success:
        return jsonify({"error": f"Failed to send email: {msg}"}), 500

    return jsonify({"message": "Result sent to email successfully!"})

# -------------------- RUN APP --------------------
if __name__ == '__main__':
    app.run(debug=True)
