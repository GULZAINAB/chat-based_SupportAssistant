#  RAG — Chat-based IT Support Assistant

##  Instructions to Run the Bot

### Prerequisites
- Python 3.8 or higher
- Google API Key for Gemini AI

### Step-by-Step Setup

1. **Clone/Download the Project**
   ```
   Download the project files to your local machine
   Navigate to the project directory: chat-based_SupportAssistant/
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**
   - Create a file named `.env` in the project root directory
   - Add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```
   
   **Note:** Get your free API key from Google AI Studio. Gemini 2.0 is available in Google's free tier - just add a credit card to get sufficient free credits.

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

6. **Access the Bot**
   - The application will automatically open in your browser
   - If not, go to: http://localhost:8501
   - Start asking your IT support questions!

---

##  Sample Prompts and Responses

### Example 1: Network Issue
**User Input:**
```
My Wi-Fi isn't working
```

**Bot Response:**
```
  Detected intent: Network Issue

  Solution:
To troubleshoot your Wi-Fi connection, please try the following steps:
1. Ensure Wi-Fi is turned on.
2. Restart your router and modem.
3. Reconnect to the correct SSID and enter the password again.
4. Run the Windows Network Troubleshooter: Go to Settings > Network & Internet > Status > Network troubleshooter.
5. Check if other devices can connect to the Wi-Fi. If no other devices can connect, please contact your Internet Service Provider (ISP).
```

### Example 2: System Performance
**User Input:**
```
My laptop is frozen
```

**Bot Response:**
```
 Detected intent: General Support

 Solution:
If your laptop is frozen, please try the following steps:
1. Save your work: Ensure that you save any unsaved work before proceeding.
2. Restart your system:
   • Click on the "Start" button.
   • Click on the "Power" icon.
   • Select "Restart."
3. Force Shutdown (if unresponsive): If your system remains unresponsive, press and hold the power button for 10 seconds to force a shutdown. After the system shuts down, power it back on.
```

### Example 3: System Settings
**User Input:**
```
How to change time and date
```

**Bot Response:**
```
Detected intent: System Settings

 Solution:
To set the date and time on your Windows computer, please follow these steps:
1. Open Settings.
2. Go to Time & Language, then select Date & time.
3. Turn off the option labeled "Set time automatically".
4. Click the "Change" button located under "Set the date and time manually" and adjust the date and time as needed.
```

### Example 4: Browser Issues
**User Input:**
```
My browser is running slowly
```

**Bot Response:**
```
 Detected intent: Browser / Cache

 Solution:
To address the slow performance of your browser, please try the following steps:

Clear your browser's cache:
1. Open your Chrome browser.
2. Click on the "More" option (represented by three vertical dots).
3. Go to "More tools" and then select "Clear browsing data."
4. In the "Clear browsing data" window, check the box next to "Cached images and files."
5. Select the desired time range for clearing the cache.
6. Click on "Clear data."
```
