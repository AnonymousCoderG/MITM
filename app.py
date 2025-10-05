from flask import Flask, request, render_template_string,render_template
import google.generativeai as genai

app = Flask(__name__)

@app.route('/buttons', methods = ['GET','POST'])
def buttons():
    if request.method == 'POST':
        tx_value = request.form.get('tx')
        genai.configure(api_key="AIzaSyAEV9JLqXIyMvWCtWZrfcuc6L1ZoaKa93M")
        #model = genai.GenerativeModel("gemini-1.5-flash")
        model = genai.GenerativeModel("gemini-1.5-pro")
        
        response = model.generate_content(f"just return one sentence which is different from this sentence so that i can demonstrate that someone is manipulating my messages {tx_value}")
        print(response.text)
        response_message = f" {response.text}"
        if(len(tx_value) ==0):
            response_message = f"You are dumb!"
    
        
        return render_template('chat.html', 
                           original_message=tx_value, 
                           manipulated_message=response_message,
                           original_message_label="Original Message",
                           manipulated_message_label="Manipulated Message")

        return render_template_string('''
            <form action="/buttons" method="POST">
                <textarea name="tx"></textarea>
                <button type="submit" class="button">
                    <center>Submit</center>
                </button>
            </form>
            <h1>{{ message }}</h1>
        ''', message=response_message)
    #return render_template('animation.html')
    # return render_template_string('''
    #     <form action="/buttons" method="POST">
    #         <textarea name="tx"></textarea>
    #         <button type="submit" class="button">
    #             <center>Submit</center>
    #         </button>
    #     </form>
    # ''')
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Styled Form</title>
            <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@500&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'IBM Plex Sans', sans-serif;
                    background: #000;
                    color: #10d210;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .form-container {
                    background: #0f0;
                    color: #000;
                    border-radius: 10px;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                    width: 300px;
                    text-align: center;
                }
                textarea {
                    width: 100%;
                    height: 100px;
                    background: #000;
                    color: #10d210;
                    border: 1px solid #10d210;
                    border-radius: 5px;
                    padding: 10px;
                    box-sizing: border-box;
                    resize: none;
                    font-family: 'IBM Plex Sans', sans-serif;
                    font-size: 16px;
                }
                button {
                    background: #10d210;
                    color: #000;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }
                button:hover {
                    background: #0c8c0c;
                }
                button:focus {
                    outline: none;
                }
            </style>
        </head>
        <body>
            <div class="form-container">
                <form action="/buttons" method="POST">
                    <textarea name="tx" placeholder="Enter your message here..."></textarea>
                    <button type="submit">
                        Submit
                    </button>
                </form>
            </div>
        </body>
        </html>
    ''')



@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     tx_value = request.form.get('tx')
    #     genai.configure(api_key="AIzaSyCDEm8zz2nYtX4ziR5Edl6kzbwcoz-Kvng")
    #     model = genai.GenerativeModel("gemini-1.5-flash")
    #     response = model.generate_content(f"just return one sentence which is different from this sentence so that i can demonstrate that someone is manipulating my messages {tx_value}")
    #     print(response.text)
    #     response_message = f" {response.text}"
    #     return render_template_string('''
    #         <form action="/" method="POST">
    #             <textarea name="tx"></textarea>
    #             <button type="submit" class="button">
    #                 <center>Submit</center>
    #             </button>
    #         </form>
    #         <h1>{{ message }}</h1>
    #     ''', message=response_message)
    return render_template('animation.html')
    # return render_template_string('''
    #     <form action="/" method="POST">
    #         <textarea name="tx"></textarea>
    #         <button type="submit" class="button">
    #             <center>Submit</center>
    #         </button>
    #     </form>
    # ''')

if __name__ == '__main__':
    app.run(debug=True)
