from flask import Flask
from flask_cors import CORS
from app.webhook.routes import webhook
from app.config import MONGO_URI
from flask_session import Session
from app.extensions import events_collection

def create_app():

    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
    
    # For adding session

    # app.secret_key = 'super-secret-key'  
    # app.config['SESSION_TYPE'] = 'filesystem'  
    # Session(app)

    app.config["EVENTS_COLLECTION"] = events_collection
   
    app.register_blueprint(webhook)

    
    return app
