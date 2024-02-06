from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Mock database of user credentials
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'], chat=True)
    else:
        return render_template('index.html', chat=False)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if username exists and passwords match
    if username in users and users[username] == password:
        session['username'] = username  # Create session for authenticated user
        return jsonify({'success': True, 'message': 'Login successful!'})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password.'})

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user session
    return redirect(url_for('index'))


from flask import Flask, render_template, request
import re

app = Flask(__name__)

def simple_chatbot(user_input):
    patterns = {
        r"(hello|hi|hey|greetings)": "Hello! How can I help you?",
        r"I need help with solving an issue on SBV Trinity, will you be able to help": "Yes, i am happy to help!",
        r"what are SBV working hours|What time does SBV close|Can i find SBV open on Weekends|does SBV open on weekends": "SBV is functional 24/7, if you need to reach to them, you can always do so by calling their Support Office on: +27 11 283 2000 or e-mail:supportoffice@sbv.co.za.",
        r"(bye|goodbye)": "Goodbye! Have a great day!",
        r"(\bthanks\b|\bthank you\b)": "You're welcome!",
        r"(.*)": "I'm not sure how to respond to that. Can you please ask something else?"
    }

    for pattern, response in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = simple_chatbot(user_input)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
