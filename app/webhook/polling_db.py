from flask import jsonify, current_app
from datetime import datetime, timedelta

last_fetch = None  

def get_events():
    global last_fetch
    events_collection = current_app.config["EVENTS_COLLECTION"]
    now = datetime.now() 

    if last_fetch is None:
 
        events = events_collection.find().sort("timestamp", -1)
    else:
      
        events = events_collection.find({
            "timestamp": {"$gte": last_fetch}
        }).sort("timestamp", -1)


    last_fetch = now

    result = [{"message": e["message"], "timestamp": e["timestamp"]} for e in events]
    print(f"Fetched {len(result)} events since {last_fetch}")
    return jsonify(result)
