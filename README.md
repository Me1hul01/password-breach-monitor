# 🔐 Password Breach Alert System

This project continuously monitors a password against known data breaches using the **Have I Been Pwned API** and automatically sends an email alert **only when a breach is detected**.

The system is designed to run daily using Task Scheduler, making it a simple automated security monitoring tool.

---

## 🚀 Features

* 🔍 Checks password against real-world breach database
* 🔐 Uses SHA-1 hashing for secure API querying
* 📧 Sends email alert **only if breach is detected**
* ⏰ Fully automated using Task Scheduler (runs daily)
* 🧩 Simple Python implementation

---

## 🛠️ How It Works

1. The script runs automatically (via Task Scheduler)
2. Password is converted into SHA-1 hash
3. First 5 characters of the hash are sent to the API
4. API returns matching hashes
5. If the password is found in breaches →
   📧 Email alert is sent to the user
6. If not found → No email is sent

---

## ▶️ How to Run Manually

```bash
python email_alert.py yourpassword
```

---

## ⚠️ Email Configuration (IMPORTANT)

To send emails using Gmail, you **cannot use your normal account password**.

You must generate a **Google App Password**.

### 🔑 Steps to Generate App Password:

1. Go to your Google Account
2. Enable **2-Step Verification**
3. After enabling, go to **App Passwords**
4. Select:

   * App: Mail
   * Device: Other (give any name)
5. Click **Generate**
6. Copy the **16-character password**

👉 Use this generated password in your script instead of your real Gmail password.

---

## ⏰ Automation with Task Scheduler (Windows)

This project is designed to run automatically every day.

### Steps:

1. Open **Task Scheduler**
2. Click **Create Basic Task**
3. Name it: `Password Breach Alert Automation`
4. Choose **Daily**
5. Set your preferred time (e.g., 8:00 AM)

---

### ⚙️ Action Setup

* **Program/script:**

  ```
  C:\Path\To\Python\python.exe
  ```

* **Add arguments:**

  ```
  email_alert.py yourpassword
  ```

* **Start in:**

  ```
  C:\Path\To\Your\Project
  ```

---

### ✅ Result

* Script runs every day automatically
* Email is sent **only if the password is found in a breach**
* No unnecessary emails

---

## 🐧 Alternative: Cron Job (Linux/macOS)

```bash
0 8 * * * python3 /path/to/email_alert.py yourpassword
```

---

## 📁 Project Structure

```
.
├── checker.py
├── email_alert.py
├── Alert.html
├── README.md
```

---

## ⚠️ Notes

* Replace email and password placeholders before running
* Do NOT upload real credentials to GitHub
* Use App Password instead of your actual Gmail password

---

## 📡 API Used

* Have I Been Pwned API

---

## 🙌 Acknowledgement

This project demonstrates a basic automated cybersecurity alert system using Python, APIs, and scheduling tools.

---
## 👤 Author
Mehul Chourasia  
Aspiring Software Developer