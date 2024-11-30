import requests
import schedule
import time
import random
from datetime import datetime

messages = [
    "Good morning, beautiful 😘",
    "Rise and shine, my love! 💖",
    "Good morning! Hope you have a wonderful day ahead 😘",
    "Sending you love and positivity to start your day! 💕",
    "Wishing you a day full of happiness and smiles 🌸",
    "You’re the reason I wake up smiling every morning 😘.",
    "Good morning, sunshine ☀️. I hope your day is as bright as you are.",
    "Waking up thinking of you makes every morning perfect 💖.",
    "May your day be filled with as much joy as you bring to my life 💕.",
    "Hello, gorgeous! Hope today brings you everything you’re hoping for 💫.",
    "Every sunrise is a reminder of how blessed I am to have you 🌅.",
    "You’re my first thought every morning and my last every night 💕.",
    "Good morning, my heart! ❤️ I’m so grateful to have you.",
    "Here’s to another day of me loving you more than yesterday 💖.",
    "Sending hugs and kisses to start your day right 😘.",
    "I hope your coffee’s as sweet as you are ☕💞.",
    "Wishing I could wake up next to you every morning 😘.",
    "Just a reminder that you’re amazing, beautiful, and so loved 💖.",
    "Can’t wait to see that beautiful smile of yours today 🌸.",
    "Morning, babe! 😘 Can’t wait to spend the day with you in my thoughts.",
    "I hope your day is filled with sunshine and joy 🌞💕.",
    "You make every morning feel like a special occasion 💝.",
    "Wishing the most beautiful person a beautiful day 💖.",
    "If I could be with you every morning, I would ❤️.",
    "Starting my day with thoughts of you puts a smile on my face 😘.",
    "I wish you a day full of laughter and love 💖.",
    "Good morning, my love! I hope your day is as bright as your smile 💫.",
    "The world is brighter with you in it 🌎💕.",
    "Nothing feels better than waking up and thinking about you 💖.",
    "You’re my sunshine, my only sunshine 🌞.",
    "Morning, babe! I wish I was there to see that morning glow ☀️.",
    "I’m so lucky to have you in my life. Have a great day 💖.",
    "Just a reminder: you’re beautiful, inside and out 💕.",
    "Sending you love and light to brighten your day 💖.",
    "You make every day better just by being in my life 💫.",
    "I hope your day is as lovely as you are 😘.",
    "Good morning to the one who makes my heart race 💞.",
    "You’re my reason for waking up with a smile every day 😊.",
    "Good morning, sweetheart! 😘 Hope your day is wonderful.",
    "If only I could start every morning by your side 💖.",
    "Thinking of you makes every morning magical ✨.",
    "Just a reminder: you’re amazing, today and every day 💖.",
    "Good morning, love! Hope today is full of joy for you 😘.",
    "May your day be as bright as your smile ☀️💫.",
    "Wishing the world’s most amazing person an amazing day 💖.",
    "Every day with you is a blessing 🌹.",
    "You’re the first thought in my mind and the first smile on my face 😊.",
    "Starting my day with thoughts of you is the best way to begin 💖.",
    "Good morning, love! Sending you all my positive vibes 💕.",
    "Can’t wait to see your smile today 😊.",
    "I wish I could start every morning with a kiss from you 😘.",
    "You’re my reason for waking up with a smile each day 💖.",
    "Good morning, angel! You make my life so much better 💫.",
    "I wish every morning could be spent in your arms 💞.",
    "You’re on my mind and in my heart, always 💖.",
    "Wishing my favorite person a beautiful morning ☀️.",
    "Good morning, my heart! I love you more with each sunrise 💕.",
    "You’re my favorite hello and my hardest goodbye ❤️.",
    "Hope your day is as beautiful as your heart 💖.",
    "Wishing I could wake up beside you every day 😘.",
    "Good morning, my love! May today be as amazing as you are 💫.",
    "Waking up thinking of you is my favorite routine 💖.",
    "Your smile is my favorite part of every day 💕.",
    "Can’t wait to see you again! Have a great day 🌞.",
    "Wishing you a morning full of peace and love 💖.",
    "I hope today is filled with moments that make you smile 😊.",
    "You make my life infinitely better 💖.",
    "Good morning, babe! You’re my favorite thought every morning 💕.",
    "If I could hold you every morning, I’d never let go ❤️.",
    "Wishing I could start the day beside you 😘.",
    "You’re my light on the darkest days 💖.",
    "Good morning to my favorite person in the world 💫.",
    "Your smile brightens up my day, always 💖.",
    "Waking up to your smile would be my dream come true 😘.",
    "Hope your day is full of joy and love 💕.",
    "Thinking of you makes every day brighter ☀️.",
    "I love you more than words can say 💖.",
    "You’re the highlight of my life 🌹.",
    "Good morning, love! Here’s to a day full of smiles 💫.",
    "Can’t wait for the day I wake up next to you 💖.",
    "You make every day better just by being you 💕.",
    "You’re the first thing on my mind every morning 🌞.",
    "Your happiness is my happiness 💖.",
    "Good morning, my sweet love 💫.",
    "You’re my reason for everything 🌹.",
    "Waking up thinking of you is the best way to start the day 😊.",
    "Hope your day is full of beautiful surprises 💖.",
    "You’re my forever and always 💞.",
    "Good morning, my heart 💖.",
    "I wish I could tell you every morning how much you mean to me 😘.",
    "Your love makes every day worth it 💖.",
    "Thinking of you makes me smile every morning 😊.",
    "You’re my one and only, forever 💕.",
    "Can’t wait to spend today thinking of you 💖.",
    "Your love is my favorite part of every day 💫.",
    "Good morning, my love! 💖"
]

# Special message for her birthday
special_message = "Happy Birthday, my love! 🎉🎂 I hope your day is as beautiful and amazing as you are! 😘💖"

def send_email_via_brevo(message, recipient_email):
    api_key = "your actual brevo API key"  # Replace with your actual API key
    url = "https://api.brevo.com/v3/smtp/email"
    
    headers = {
        "accept": "application/json",
        "api-key": api_key,  
        "content-type": "application/json"
    }
    
    payload = {
    "sender": {"name": "pillu😘", "email": "your_email@yourdomain.com"},
    "to": [{"email": recipient_email}],
    "subject": "Good Morning Message 💖",
    "htmlContent": f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333;">
            <h1 style="color: #FF69B4; text-align: center;">🌞 Good Morning, My Love! 💖</h1>
            <p style="font-size: 18px;">{message}</p>
            <p style="font-style: italic; text-align: center; color: #999;">Have a magical day ahead! 🌸</p>
            <footer style="text-align: center; margin-top: 20px;">
                <p>With all my love,</p>
                <p style="font-size: 16px; color: #FF1493;">Your Pillu 😘</p>
            </footer>
            <footer style="font-family: cursive; text-align: center;">
    <p>“You’re my sunshine on a cloudy day.” 🌤️</p>
</footer>

        </body>
        </html>
    """
}


    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 201:
            print(f"Email sent successfully: {message}")
        else:
            print(f"Failed to send email: {response.status_code}, {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

def job():
   
    current_date = datetime.now()
    
   
    if current_date.month == 2 and current_date.day == 28:
        send_email_via_brevo(special_message, "receptientemail@gmail.com")  # Send special birthday message
    else:
        
        message = random.choice(messages)
        recipient_email = "receptientemail@gmail.com"  # Replace with recipient's email
        send_email_via_brevo(message, recipient_email)

# Schedule the job to run every day at 6 AM
schedule.every().day.at("06:00").do(job)


try:
    
    while True:
        schedule.run_pending()
        time.sleep(60) 
except KeyboardInterrupt:
    print("Program stopped by user.")