from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        content = request.form['content']  # Extract text from form data
        # For now, let's just print the submitted content
        print(content)
        return 'Form submitted successfully!'
    return 'This route is for form submissions only.'

if __name__ == '__main__':
    app.run(debug=True)