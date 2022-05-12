from flask import *

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['logemail']

        if email == None: ##Sign Up
            name = request.form['signname']
            email = request.form['signemail']
            password = request.form['signpass']

            '''
            INSERT INTO 
                user_det (user_name, user_email, password)
            VALUES
                (name, email, password)
            '''
        else: ##Login
            password = request.form['logpass']

            response = None
            '''
            SELECT
                user_name
            FROM
                user_det
            WHERE
                user_det.user_email = email AND
                user_det.password = password
            '''
            if response: #LogIn Successful
                return "<script>window.location.href='main.html';</script>"
            else:
                return '<alert>Invalid Credentials</alert>'


if __name__ == '__main__':
    app.run('localhost', 8080)