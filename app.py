from flask import Flask, request, jsonify, render_template
from src.components.queryProcessing import QueryProcessor
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")  # Serve the HTML file

# Route to handle chat requests (POST request)
@app.route("/chat", methods=["POST"])
def chat():
    
    # print(request.json.get("message"), type(request.json.get("message")))
    response = qp.process_query(request.json.get("message"))

    return jsonify({"response": response})

if __name__ == "__main__":
    global qp
    qp = QueryProcessor()
    print("Query Processor Initialized")
    app.run(debug=False)

'''
Filename: e:\projects\CORD19-SummaryGenerator\app.py
Path: e:\projects\CORD19-SummaryGenerator
Created Date: Friday, March 7th 2025, 4:08:10 pm
Author: Devang Vamja

Copyright (c) 2025 Your Company
'''
