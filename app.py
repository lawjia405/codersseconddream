from flask import Flask, render_template, request, jsonify
from matchmaking import User, find_best_match, users, calculate_match_score

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    # Extract form data
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    height = request.form['height']
    preferences = request.form.getlist('preferences')
    
    # Create a user instance for the form data
    user = User(name, int(age), gender, int(height), preferences)
    
    # Find the best match
    best_match_user = find_best_match(user, users)
    if best_match_user:
        match_score = calculate_match_score(user, best_match_user)
        match_info = {
            'name': best_match_user.name,
            'age': best_match_user.age,
            'gender': best_match_user.gender,
            'height': best_match_user.height,
            'match_score': match_score
        }
    else:
        match_info = {'error': 'No match found'}
    
    # Return match information
    return jsonify(match_info)

if __name__ == '__main__':
    app.run(debug=True)