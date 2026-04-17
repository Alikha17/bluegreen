from flask import Flask, render_template_string
import os

app = Flask(__name__)

# These variables allow us to change the app's look via environment variables
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_COLOR = os.getenv("APP_COLOR", "blue") # This will be 'blue' or 'green'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>ArgoCD Blue-Green Demo</title>
    <style>
        body { 
            background-color: {{ color }}; 
            color: white; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            height: 100vh; 
            font-family: sans-serif; 
        }
        .box { 
            padding: 20px; 
            border: 5px solid white; 
            border-radius: 15px; 
            text-shadow: 2px 2px 4px #000;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>Status: {{ color | upper }} ENVIRONMENT</h1>
        <h2>Version: {{ version }}</h2>
        <p>Managed by Argo CD & Argo Rollouts</p>
    </div>
</body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(HTML_TEMPLATE, color=APP_COLOR, version=APP_VERSION)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
