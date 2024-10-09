from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def test():
    return "<h2>Server is running</h2>"

# @app.post('/posts')
# def create_post():
#     data = request.get_json()
    
#     if not data:
#         return jsonify({"error":"No JSON Provided"}), 400
    
    
    
