from flask import Blueprint
from .receiver import handle_webhook
from .polling_db import get_events

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


webhook.add_url_rule('/receiver', view_func=handle_webhook, methods=['POST'])
webhook.add_url_rule('/events', view_func=get_events, methods=['GET'])
