# import os
# from flask import Flask, request, render_template
# import google.generativeai as genai

# app = Flask(__name__)

# # --- CONFIGURATION ---
# # This correctly loads your API key from the environment variables.
# try:
#     API_KEY = os.environ.get("API_KEY")
#     if not API_KEY:
#         raise ValueError("API_KEY environment variable not set or empty.")
#     genai.configure(api_key=API_KEY)
#     print(f"API Key loaded successfully, starting with: {API_KEY[:4]}...")
# except Exception as e:
#     print(f"!!! FATAL ERROR during initialization: {e} !!!")

# # --- USER FLOW & ROUTES ---

# @app.route("/")
# def index():
#     """
#     Renders the animation.html page, which is the start of the user journey.
#     """
#     return render_template("animation.html")

# @app.route("/buttons", methods=["GET", "POST"])
# def buttons():
#     """
#     Handles both GET and POST requests.
#     - GET: Shows the form for the user to enter their message.
#     - POST: Processes the message, calls the AI, and shows the result.
#     """
#     if request.method == "POST":
#         # --- This block runs when the form is submitted ---
        
#         # Get the text from the form's textarea (which has name="tx")
#         tx_value = request.form.get("tx", "").strip()

#         if not tx_value:
#             response_message = "You submitted an empty message!"
#             return render_template('chat.html', original_message="[Empty]", manipulated_message=response_message)

#         try:
#             # ================================================================= #
#             # === THIS IS THE FINAL, CORRECTED MODEL NAME FROM YOUR LIST      === #
#             # ================================================================= #
#             model = genai.GenerativeModel("models/gemini-pro-latest")

#             # Use the correct function to generate content.
#             prompt = f"Return a single, different sentence that alters the meaning of this one: '{tx_value}'"
#             response = model.generate_content(prompt)
            
#             response_message = response.text.strip()
#             print("Successfully received a response from the API.")

#         except Exception as e:
#             print(f"!!! AN API ERROR OCCURRED: {e} !!!")
#             response_message = "Error: Could not get a response from the AI model. Check server logs for details."
        
#         # Render the chat.html template with the original and new messages.
#         return render_template("chat.html", 
#                                original_message=tx_value, 
#                                manipulated_message=response_message)
    
#     # --- This block runs for a GET request ---
#     return render_template("form.html")

# if __name__ == "__main__":
#     app.run(debug=True)

# import os
# from flask import Flask, request, render_template, jsonify
# import google.generativeai as genai

# app = Flask(__name__)

# # --- CONFIGURATION ---
# try:
#     API_KEY = os.environ.get("API_KEY")
#     if not API_KEY:
#         raise ValueError("API_KEY environment variable not set or empty.")
#     genai.configure(api_key=API_KEY)
#     print(f"API Key loaded successfully, starting with: {API_KEY[:4]}...")
# except Exception as e:
#     print(f"!!! FATAL ERROR during initialization: {e} !!!")

# # --- ROUTES ---

# @app.route("/")
# def index():
#     """Renders the initial animation page."""
#     return render_template("animation.html")

# @app.route("/buttons")
# def buttons():
#     """Serves the form page."""
#     return render_template("form.html")

# @app.route("/chat")
# def chat_page():
#     """
#     INSTANTLY serves the chat page.
#     It takes the original message from the URL parameter to display it immediately.
#     """
#     original_message = request.args.get("original_message", "Error: No message provided.")
#     return render_template("chat.html", original_message=original_message)

# @app.route("/generate", methods=["POST"])
# def generate():
#     """
#     This is now an API endpoint. JavaScript calls this in the background.
#     It does the slow work (calling the AI) and returns ONLY the result as JSON.
#     """
#     data = request.get_json()
#     tx_value = data.get("message", "")

#     if not tx_value:
#         return jsonify({"manipulated_message": "Error: No input text provided."})

#     try:
#         # Using the fast 'Flash' model for speed
#         model = genai.GenerativeModel("models/gemini-2.5-flash")
#         prompt = f"Return a single, different sentence that alters the meaning of this one: '{tx_value}'"
#         response = model.generate_content(prompt)
#         response_message = response.text.strip()
#         print("Successfully generated response.")

#     except Exception as e:
#         print(f"!!! AN API ERROR OCCURRED: {e} !!!")
#         response_message = "Error: Could not get a response from the AI model."
    
#     return jsonify({"manipulated_message": response_message})

# if __name__ == "__main__":
#     app.run(debug=True)



#new code to remove astricks
import os
from flask import Flask, request, render_template, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- CONFIGURATION ---
try:
    API_KEY = os.environ.get("API_KEY")
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set or empty.")
    genai.configure(api_key=API_KEY)
    print(f"API Key loaded successfully, starting with: {API_KEY[:4]}...")
except Exception as e:
    print(f"!!! FATAL ERROR during initialization: {e} !!!")

# --- ROUTES ---

@app.route("/")
def index():
    """Renders the initial animation page."""
    return render_template("animation.html")

@app.route("/buttons")
def buttons():
    """Serves the form page."""
    return render_template("form.html")

@app.route("/chat")
def chat_page():
    """
    INSTANTLY serves the chat page.
    It takes the original message from the URL parameter to display it immediately.
    """
    original_message = request.args.get("original_message", "Error: No message provided.")
    return render_template("chat.html", original_message=original_message)

@app.route("/generate", methods=["POST"])
def generate():
    """
    This is an API endpoint. JavaScript calls this in the background.
    It does the slow work (calling the AI) and returns ONLY the result as JSON.
    """
    data = request.get_json()
    tx_value = data.get("message", "")

    if not tx_value:
        return jsonify({"manipulated_message": "Error: No input text provided."})

    try:
        # Using the fast 'Flash' model for speed
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        
        # ================================================================= #
        # === BACK TO THE SIMPLER, MORE EFFECTIVE PROMPT                  === #
        # ================================================================= #
        prompt = f"Return a single, different sentence that alters the meaning of this one: '{tx_value}'"
        
        response = model.generate_content(prompt)
        
        # First, get the raw text from the AI
        raw_response_text = response.text.strip()
        
        # ================================================================= #
        # === NEW CODE TO RELIABLY REMOVE ASTERISKS                       === #
        # ================================================================= #
        cleaned_response = raw_response_text.replace("**", "")

        print(f"Successfully generated response. Raw: '{raw_response_text}', Cleaned: '{cleaned_response}'")

    except Exception as e:
        print(f"!!! AN API ERROR OCCURRED: {e} !!!")
        cleaned_response = "Error: Could not get a response from the AI model."
    
    return jsonify({"manipulated_message": cleaned_response})

if __name__ == "__main__":
    app.run(debug=True)