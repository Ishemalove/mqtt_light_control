# 💡 IoT Light Control Over MQTT

A web-based application that allows users to **remotely switch a light ON/OFF** over MQTT. This project includes a **beautiful web UI** and a **simulated IoT device** (ESP8266) using Python.  

## 🌟 Features
- 🖥 **Modern Web Interface** (Dark theme, neon colors, stylish animations)
- 🌍 **MQTT Communication** via WebSockets
- 💡 **Real-Time Light Control** (Turn ON/OFF remotely)
- 🐍 **Simulated IoT Device** in Python (Prints light status)

---

## 📺 Project Structure
```
💃 mqtt-light-control/
│── 📄 index.html          # Stylish Web UI for MQTT light control
│── 📄 script.py           # Python script simulating ESP8266
│── 📄 README.md           # Documentation
```

---

## 🚀 Getting Started

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- **Python 3**  
- **Paho MQTT library** (`pip install paho-mqtt`)  
- **Web Browser** (Chrome, Firefox, Edge, etc.)

---

### **2️⃣ Setting Up the Web UI**
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/mqtt-light-control.git
   cd mqtt-light-control
   ```
2. **Open `index.html`** in a web browser.
3. **Click "Turn ON" or "Turn OFF"** to send MQTT messages.

---

### **3️⃣ Running the Simulated IoT Device**
1. Open a terminal and navigate to the project folder.
2. Run the Python script:
   ```sh
   python script.py
   ```
3. The script will **listen for MQTT messages** and print:
   ```
   💡 Light is TURNED ON
   💡 Light is TURNED OFF
   ```

---

## 💻 MQTT Setup
- **Broker:** `wss://test.mosquitto.org:8081/mqtt` *(Public MQTT Broker)*
- **Topic:** `/student_group/light_control`
- **Messages:** `ON` / `OFF`

---

## 🖼 UI Preview
![UI Screenshot](https://your-image-link.com) *(Upload an image and add the link)*

---

## 🛠 Technologies Used
- **Frontend:** HTML, CSS, JavaScript (MQTT.js)
- **Backend:** Python (Paho MQTT)

---

## 🏆 Future Improvements
- ✅ Add real ESP8266 support
- ✅ Store and display historical light status
- ✅ Mobile-friendly UI enhancements

---

## 💡 Credits
Developed by **[Your Name]** 🚀  
Inspired by IoT and smart home automation.

---

## 🐟 License
This project is **open-source** under the **MIT License**. Feel free to contribute! 🎉

