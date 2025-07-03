from app import create_app
from flask import jsonify

app = create_app()
# @app.route('/',methods=["GET"])
# def get_landing():
#     return jsonify({"message": "nothing"})


if __name__ == '__main__': 
    app.run(debug=True)
