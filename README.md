# LoveNotes Daily 💌

**LoveNotes Daily** is a heartwarming Python automation project designed to send daily romantic messages via email. This project adds a personal touch to brighten your loved one’s day with a random sweet message every morning, and a special heartfelt message on their birthday.

## 🌟 Features
- **Daily Romantic Messages:** Sends a loving message every morning at a scheduled time.
- **Special Birthday Message:** On February 28, a personalized birthday wish is sent automatically.
- **API Integration:** Uses Brevo's SMTP email service to deliver messages reliably.
- **Randomized Content:** Selects a random sweet message from a curated list.
- **Custom Scheduling:** Easily configurable schedule for when messages should be sent.

## 💻 Technologies Used
- Python
- Brevo (SendinBlue) API for email delivery
- `schedule` library for task automation
- `requests` library for HTTP requests

## 📜 How It Works
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/lovenotes-daily.git
    cd lovenotes-daily
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure your API key and sender/recipient details in the script.
4. Run the script:
    ```bash
    python love_notes.py
    ```
5. Sit back and let the love flow!

## 🌹 Customize It
- Update the `messages` list with your own personalized messages.
- Change the recipient email to your loved one’s email address.
- Modify the `schedule` timing to your preferred time of day.

## 📬 Example Email
Subject: **Good Morning, My Love 💖**

Body:
> Good morning, sunshine!  
> Wishing you a day as bright as your smile and as beautiful as your heart.  
> Can’t wait to see you again! 😘  

## 💕 License
This project is licensed under the MIT License. Feel free to use and enhance it for personal projects.
