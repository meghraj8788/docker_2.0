from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <html>
    <head>
        <title>DevOps Zero To Hero</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
                padding-top: 80px;
            }
            h1 {
                font-size: 52px;
                margin-bottom: 10px;
            }
            h2 {
                font-size: 28px;
                color: #00e6e6;
                margin-bottom: 30px;
            }
            p {
                font-size: 20px;
                margin: 10px 0;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                width: 60%;
                margin: auto;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            }
            .footer {
                margin-top: 40px;
                font-size: 14px;
                color: #cccccc;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 DevOps Zero To Hero</h1>

            <p>🔧 Automating Everything</p>
            <p>☁️ Cloud • CI/CD • Containers</p>
            <p>📦 Docker • Kubernetes • AWS</p>
            <p>📈 Monitoring • Logging • Scaling</p>

            <p><b>Status:</b> Application is live and running successfully ✅</p>
        </div>

        <div class="footer">
            <p>Built with ❤️ using Flask | DevOps Learning Project</p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return 'Server is up and running'
