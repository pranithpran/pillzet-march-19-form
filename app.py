from flask import Flask, request, jsonify, render_template
import requests
import csv
import os

app = Flask(__name__, template_folder=".")

# Local CSV File (Backup Storage)
FILE_NAME = "customer_data.csv"

# Ensure CSV file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Email", "Phone", "Smoke", "Drink", 
                         "Exercise", "Diet", "Checkups", "Stress", "Sleep", 
                         "Water", "Medical History", "Tablets", "Health Score", 
                         "Health Status"])

# Google Form URL (Replace YOUR_FORM_ID with actual ID)
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/YOUR_FORM_ID/formResponse"

# Google Form Field Entry IDs (Replace with actual IDs)
FORM_FIELDS = {
    "name": "entry.1234567890",
    "age": "entry.2345678901",
    "email": "entry.3456789012",
    "phone": "entry.4567890123",
    "smoke": "entry.5678901234",
    "drink": "entry.6789012345",
    "exercise": "entry.7890123456",
    "diet": "entry.8901234567",
    "checkups": "entry.9012345678",
    "stress": "entry.0123456789",
    "sleep": "entry.1122334455",
    "water": "entry.2233445566",
    "medicalHistory": "entry.3344556677",
    "tablets": "entry.4455667788",
    "healthScore": "entry.5566778899",
    "healthStatus": "entry.6677889900"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_data():
    try:
        data = request.json  # Receiving JSON data

        if not data:
            return jsonify({"error": "No data received"}), 400

        # Convert to CSV row
        row = [
            data.get("name", ""),
            data.get("age", ""),
            data.get("email", ""),
            data.get("phone", ""),
            data.get("smoke", ""),
            data.get("drink", ""),
            data.get("exercise", ""),
            data.get("diet", ""),
            data.get("checkups", ""),
            data.get("stress", ""),
            data.get("sleep", ""),
            data.get("water", ""),
            data.get("medicalHistory", ""),
            data.get("tablets", ""),
            data.get("healthScore", ""),
            data.get("healthStatus", "")
        ]

        # Append to local CSV file
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)

        # Send data to Google Form
        form_data = {FORM_FIELDS[key]: value for key, value in data.items() if key in FORM_FIELDS}
        response = requests.post(GOOGLE_FORM_URL, data=form_data)

        if response.status_code == 200:
            return jsonify({"message": "Data saved successfully to Google Sheets"}), 200
        else:
            return jsonify({"error": "Failed to save data to Google Sheets"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
