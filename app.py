from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def de():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    year = request.form['year']

    return render_template('success.html', name=name, email=email, year=year)

if __name__ == "__main__":
    app.run(debug=True, port=5000)