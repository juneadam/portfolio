from flask import Flask, render_template, request, flash, session, redirect, jsonify

app = Flask(__name__)
app.secret_key = 'dev'

@app.route('/')
def render_homepage():
    '''Renders homepage.'''

    return render_template('index.html')


if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)