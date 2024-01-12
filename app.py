from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def show():
    return render_template("index.html")


@app.route('/check_password', methods = ['POST'])
def check_password():
    name = request.form.get('username')
    password = request.form.get('password')
    print({name}, {password})

    return f'username and password is received'


if __name__ == "__main__":
    app.run(host = '0.0.0.0')