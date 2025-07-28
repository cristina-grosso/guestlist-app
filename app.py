import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import firestore

# Initialize Flask App
app = Flask(__name__)

# Initialize Firestore Client
db = firestore.Client()

@app.route("/", methods=["GET"])
def index():
    """Fetch guestbook entries from Firestore and display them."""
    messages_ref = db.collection("messages").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(10)
    messages = messages_ref.stream()
    
    # We need to convert the generator to a list to render it
    message_list = [message.to_dict() for message in messages]
    
    return render_template("index.html", messages=message_list)

@app.route("/add", methods=["POST"])
def add_message():
    """Handle form submission and write a new entry to Firestore."""
    author = request.form.get("author", "Anonymous")
    message_text = request.form.get("message")
    
    if message_text:
        # Create a new document in the 'messages' collection
        doc_ref = db.collection("messages").document()
        doc_ref.set({
            "author": author,
            "message": message_text,
            "timestamp": datetime.now()
        })
        
    return redirect(url_for("index"))

if __name__ == "__main__":
    # This is used for local development.
    # Gunicorn is used in production.
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))