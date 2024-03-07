from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"title": "1: Airpods pro", 
     "description": "[Apple MFi Certified] AirPods Pro Wireless Earbuds Bluetooth in Ear Light-Weight Headphones Built-in Microphone, with Touch Control, Noise Cancelling, Charging case",
     "price": "$199.99", "image": "airpods pro.jpg", "rating":"4.5"},
    {"title": "2: Amazon Echo Dot (4th Gen)", "description": "Echo Dot (4th Gen) | Smart speaker with Alexa | Twilight Blue", "price": "$129.99", "image": "echodot.jpg", "rating":"4.5"},
    {"title": "3: Samsung 65-Inch QLED 4K TV", "description": "SAMSUNG 55-Inch Class QLED Q70A Series - 4K UHD Quantum HDR Smart TV with Alexa Built-in (QN55Q70AAFXZA)", "price": "$199.99", "image": "samsung.jpg", "rating":"4.5"},
    {"title": "4:  Nintendo Switch", "description": "Nintendo Switch with Gray Joy‑Con", "price": "$298.00", "image": "nintendo.jpg", "rating":"4.5"},
    {"title": "5:  Fitbit Charge 4", "description": "Fitbit Charge 4 Fitness and Activity Tracker with Built-in GPS, Heart Rate, Sleep & Swim Tracking, Black/Black, One Size (S &L Bands Included)", "price": "$119.99", "image": "fitbit.jpg", "rating":"4.5"},
    {"title": "6: Logitech MX Master 3", "description":"Logitech MX Master 3S Wireless Mouse with Black Mousepad and Microfiber Cloth - Logitech MX Master 3 S Mouse for Mac OS Windows Chrome Linux - 8000 DPI, 90 Faster Scrolling, Quiet Clicks (Graphite)", "price": "$99.99", "image": "logitech.jpg", "rating":"4.5"},
    {"title": "7: Sony WH-1000XM4", "description": "Sony WH-1000XM4 Wireless Premium Noise Canceling Overhead Headphones with Mic for Phone-Call and Alexa Voice Control, Black WH1000XM4", "price": "$248.00", "image": "sony.jpg", "rating":"4.5"},
    {"title": "8: Ring Video Doorbell Pro", "description": "18V Doorbell Transformer, Power Supply Adapter Compatible with Nest Hello Doorbell,Video Doorbell, Video Doorbell Pro , WR2112", "price": "$9.99", "image": "ring.jpg", "rating":"4.5"}, 
    {"title": "9: DJI Mavic Air 2", "description": "Mavic Air 2 Waterproof Case-Carrying Case Hard Shell Professional for DJI Mavic Air 2 Fly More Combo and Drone Accessories", "price": "$37.99", "image": "mavic.jpg", "rating":"4.5"},
    {"title": "10: Instant Pot Duo 7-in-1", "description": "Instant Pot Duo 7-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 6 Quart", "price": "$99.95", "image": "pot.jpg", "rating":"4.5"},
    {"title": "11:Bose SoundLink Revolve+", "description": "Bose SoundLink Revolve+ II Bluetooth Speaker, Triple Black with Charging Cradle", "price": "$258.00", "image": "bose.jpg", "rating":"4.5"},
    {"title": "12: Oculus Quest 2", "description": "Replacement Kit for Oculus Quest 2 Controller/Meta Quest 2 Controller (13-in-1), DUXICEPIN Joysticks, Thumbstick, Screwdriver, Tweezer & Pry Tool-Ultimate Meta Quest 2 Controller Accessories", "price": "$24.98", "image": "oculus.jpg", "rating":"4.5"},
    {"title": "13: WD 5TB Elements Portable", "description": "WD 5TB Elements Portable HDD, External Hard Drive, USB 3.0 for PC & Mac, Plug and Play Ready - WDBU6Y0050BBK-WESN", "price": "$129.99", "image": "Wd.jpg", "rating":"4.5"},
    {"title": "14: GoPro HERO9 Black", "description": "GoPro HERO9 Black - Waterproof Action Camera with Front LCD and Touch Rear Screens, 5K Ultra HD Video, 20MP Photos, 1080p Live Streaming, Webcam, Stabilization", "price": "$212.99", "image": "gopro.jpg", "rating":"4.5"},
    {"title": "15: Philips Hue White and Color Ambiance", "description": "Philips Hue Smart Recessed 6 Inch LED Downlight - White and Color Ambiance Color-Changing Light - 6 Pack - 1100LM - Indoor - Control with Hue App - Works with Alexa, Google Assistant and Apple Homekit", "price": "$327.99", "image": "phillips.jpg", "rating":"4.5"},
    {"title": "16:  Anker PowerCore 10000", "description": "Hermitshell Hard Travel Case for Anker Portable Charger 313 Power Bank (PowerCore Slim 10K) 10000mAh Battery Pack/Anker 523 Power Bank (PowerCore Slim 10K PD)", "price": "$11.99", "image": "anker.jpg", "rating":"4.5"},
    {"title": "17:  Kindle Paperwhite", "description": "Case for All-New Kindle Paperwhite (11th Generation, 2021 Release) - Slim Fit TPU Gel Protective Cover Case for All-New Kindle Paperwhite E-Reader 6.8 Yellow", "price": "$14.99", "image": "kindle.jpg", "rating":"4.5"},
    {"title": "18: Apple Watch Series 6", "description": "Apple Watch SE (2nd Gen) [GPS 40mm] Smartwatch with Midnight Aluminum Case with Midnight Sport Band S/M. Fitness & Sleep Tracker, Crash Detection, Heart Rate Monitor", "price": "$145.99", "image": "apple.jpg", "rating":"4.5"},
    {"title": "19: Google Nest Learning Thermostat", "description": "Google Nest Learning Thermostat - Programmable Smart Thermostat for Home - 3rd Generation Nest Thermostat - Works with Alexa - Stainless Steel", "price": "$199.99", "image": "google.jpg", "rating":"4.5"},
    {"title": "20:Razer BlackWidow Elite", "description": "Razer BlackWidow TE Chroma v2 TKL Tenkeyless Mechanical Gaming Keyboard: Yellow Key Switches, Linear & Silent, Chroma RGB Lighting, Magnetic Wrist Rest, Programmable Macros, Classic Black", "price": "$109.99", "image": "razer.jpg", "rating":"4.7"}
    
]
@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/prices')
def prices():
    return render_template('prices.html', products=products)

@app.route('/details')
def details():
    return render_template('details.html', products=products)





if __name__ == '__main__':
    app.run(debug=True)
