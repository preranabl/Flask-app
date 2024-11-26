from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        return f"Form submitted! Name: {name}, Email: {email}, Phone: {phone}, Age: {age}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
