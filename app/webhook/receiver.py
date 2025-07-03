from flask import request, current_app, jsonify
from datetime import datetime, timezone

def handle_webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event', '')
    print(f" event_type:{event_type}")
    if not data:
        return jsonify({"error": "No data received"}), 400

    events_collection = current_app.config["EVENTS_COLLECTION"]
    event_main=event_type
    if event_type == "push":
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]
        timestamp = datetime.now().strftime("%#d %B %Y - %#I:%M %p UTC")
        message = f"{author} pushed to {to_branch} on {timestamp}"

    elif event_type == "pull_request":
        action = data['action']
        author = data['pull_request']['user']['login']
        from_branch = data['pull_request']['head']['ref']
        to_branch = data['pull_request']['base']['ref']
        timestamp =  datetime.now().strftime("%#d %B %Y - %#I:%M %p UTC")

        if action == "opened":
            message = f"{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}"
        elif action == "closed" and data['pull_request']['merged']:
            event_main="merge"
            message = f"{author} merged branch {from_branch} to {to_branch} on {timestamp}"
        else:
            return jsonify({"message": "ignored"}), 200
    else:
        return jsonify({"message": "unsupported event"}), 200

    events_collection.insert_one({
        "event_type": event_main,
        "message": message,
        "timestamp": datetime.now(timezone.utc)
    })

    return jsonify({"message": "event stored"}), 200
