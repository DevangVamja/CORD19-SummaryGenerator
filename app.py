from flask import Flask, request, jsonify, render_template
from src.components.queryProcessing import QueryProcessor
app = Flask(__name__)

# Replace with your OpenAI API key
# openai.api_key = "your_openai_api_key"

# Route to serve the frontend (GET request)
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")  # Serve the HTML file

# Route to handle chat requests (POST request)
@app.route("/chat", methods=["POST"])
def chat():
    print(request.json.get("message"), type(request.json.get("message")))
    response = qp.process_query(request.json.get("message"))
    

    # # Get user input from the frontend
    # user_input = request.json.get("message")

    # # Call the GPT model
    # response = openai.Completion.create(
    #     engine="text-davinci-003",  # Use the appropriate GPT model
    #     prompt=user_input,
    #     max_tokens=150,
    #     temperature=0.7,
    # )

    # # Extract the generated response
    # bot_response = response.choices[0].text.strip()

    # Return the response to the frontend
    return jsonify({"response": response})

if __name__ == "__main__":
    global qp
    qp = QueryProcessor()
    print("Query Processor Initialized")
    app.run(debug=False)