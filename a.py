from flask import Flask, request, render_template_string,render_template
import google.generativeai as genai

app = Flask(__name__)


def buttons():
  
    tx_value = "you are dumb"
    genai.configure(api_key="AIzaSyCDEm8zz2nYtX4ziR5Edl6kzbwcoz-Kvng")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"i want you to tell me if the sentence is  positive or negative or neutral or irrelevant. the sentence is : {tx_value}")
    print(response.text)
    response_message = f" {response.text}"
    print(response_message)
    if(len(tx_value) ==0):
        response_message = f"You are dumb!"
        print(response_message)

buttons()