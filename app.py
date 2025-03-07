from flask import Flask, request, jsonify, render_template
import csv
import os

app = Flask(__name__, template_folder=".")

FILE_NAME = "customer_data.csv"

# Ensure CSV file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Email", "Phone", "Smoke", "Drink", 
                        "Exercise", "Diet", "Checkups", "Stress", "Sleep", 
                        "Water", "Medical History", "Tablets", "Health Score", 
                        "Health Status"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_data():
    try:
        data = request.json  # request.get_json() can be replaced with request.json

        if not data:
            return jsonify({"error": "No data received"}), 400

        # Convert data to a list format for CSV
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

        # Append data to the CSV file
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)

        return jsonify({"message": "Data saved successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
