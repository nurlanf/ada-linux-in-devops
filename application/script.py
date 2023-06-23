from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# initial value
last_text = "No message received yet"

@app.route('/api', methods=['GET'])
def get_text():
    global last_text
    last_text = request.args.get('text', default = 'No message received yet')
    return f"Received: {last_text}"

@app.route('/')
def home():
    return render_template_string("""
        <h1>This is {{MY_ENV}} ENVIRONMENT and last posted text is: {{last_text}}</h1>
        """, MY_ENV=os.environ.get('MY_ENV', 'dev'), 
           last_text=last_text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
