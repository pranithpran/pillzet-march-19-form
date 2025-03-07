PillZet - Customer Health Data Collection
A Flask-based web application for collecting and analyzing customer health details.

📌 Features
✔ Collect customer health details via a web form.
✔ Store data in customer_data.csv for further analysis.
✔ Automatically updates CSV file with new entries.
✔ Uses Flask as the backend and JavaScript (fetch API) for form submission.

🛠 Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript
Database: CSV file storage
📂 Project Structure
bash
Copy
Edit
/pillzet_project
│── /static              # CSS, JS, Images
│── /templates           # HTML files
│── app.py               # Flask backend
│── customer_data.csv    # Stored customer details
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
🚀 Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/pillzet.git
cd pillzet
2️⃣ Set Up Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
Activate it:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Flask App
bash
Copy
Edit
python app.py
Go to http://127.0.0.1:5000/ in your browser.

📜 API Endpoints
Method	Endpoint	Description
GET	/	Load index.html
POST	/save	Save customer details to CSV
💡 Future Improvements
🔹 Implement a database (MySQL/PostgreSQL) for better scalability.
🔹 Add user authentication.
🔹 Create a dashboard to visualize customer health trends.

📌 Contributing
Fork the repo
Create a new branch (feature-xyz)
Commit your changes
Push and create a PR
📜 License
This project is open-source and free to use under the MIT License.
