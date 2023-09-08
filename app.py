from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necessary for Flask's flash function

@app.route('/')
def home():
    return render_template('home_support.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/ticketing')
def ticketing():
    return render_template('ticketing.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    # Extracting form data
    name = request.form.get('name')
    email = request.form.get('email')
    feedback_text = request.form.get('feedback')

    # For demonstration purposes, print to the console
    print("Name:", name)
    print("Email:", email)
    print("Feedback:", feedback_text)

    # In a real-world scenario, save this data to a database, send as an email, etc.

    # Notify the user and redirect to the feedback page
    flash('Thank you for your feedback!', 'success')  # 'success' is a category to be used for styling
    return redirect(url_for('feedback'))


if __name__ == '__main__':
    # Listen on all network interfaces and on port 80
    app.run(host='0.0.0.0', port=80)
