from flask import Flask, request, jsonify, render_template
import csv
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__, template_folder=".")

# Google Drive Setup
SERVICE_ACCOUNT_FILE = "your-google-drive-key.json"  # Replace with your downloaded JSON file
FOLDER_ID = "your-google-drive-folder-id"  # Replace with your shared Google Drive folder ID

# Authenticate Google Drive API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
client = gspread.authorize(creds)

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
        data = request.json  

        if not data:
            return jsonify({"error": "No data received"}), 400

        print("Received Data:", data)  

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

        print("Data written to CSV")  

        # Upload to Google Drive
        upload_to_drive(FILE_NAME)

        return jsonify({"message": "Data saved and uploaded successfully"}), 200

    except Exception as e:
        print("Error:", str(e))  
        return jsonify({"error": str(e)}), 500

def upload_to_drive(file_name):
    """ Upload CSV file to Google Drive """
    try:
        from pydrive.auth import GoogleAuth
        from pydrive.drive import GoogleDrive

        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(SERVICE_ACCOUNT_FILE)
        drive = GoogleDrive(gauth)

        # Check if file exists in Drive
        file_list = drive.ListFile({'q': f"'{FOLDER_ID}' in parents and title = '{file_name}'"}).GetList()
        if file_list:
            file = file_list[0]  # Get existing file
            file.SetContentFile(file_name)
            file.Upload()
            print("File updated on Drive")
        else:
            file = drive.CreateFile({'title': file_name, 'parents': [{'id': FOLDER_ID}]})
            file.SetContentFile(file_name)
            file.Upload()
            print("File uploaded to Drive")
    
    except Exception as e:
        print("Google Drive Upload Error:", str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
