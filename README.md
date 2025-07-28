# GCP Cloud Developer Guestbook

This is a simple guestbook web application built with Python and Flask. The project serves as a hands-on exercise for learning core concepts of Google Cloud Platform (GCP) development.

The application allows users to leave messages which are stored in a Firestore database and is deployed to Cloud Run.

## Core Technologies

* **Backend:** Python with Flask
* **Database:** Google Cloud Firestore
* **Containerization:** Docker
* **Deployment:** Google Cloud Run
* **CI/CD:** Google Cloud Build

## Running Locally

1.  Create and activate a Python virtual environment.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the application: `flask --app app run`