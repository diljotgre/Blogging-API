from flask import Flask, request, jsonify
from models import Post
from db_operations import add, init, update, delete, get_all
from datetime import datetime

app = Flask(__name__)

init()

@app.route('/')
def test():
    return "<h2>Server is running</h2>"

@app.post('/add')
def create_post():
    data = request.get_json()
    if not data:
        return jsonify({"error":"No JSON Provided"}), 400
    try:
        add(title = data['title'], content = data['content'], category = data['category'], tags = data['tags'], createdAt =datetime.now(), updatedAt= datetime.now())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify("Post Created"), 201

@app.put('/update/<int:id>')
def update_post(id):
    data = request.get_json()
    if not data:
        return jsonify({"error":"No data provided"}), 400
    
    try:
        update(title = data['title'], content = data['content'], category = data['category'], tags = data['tags'], updatedAt=datetime.now(), id = id)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify("Post Updated"), 201

@app.delete('/delete/<int:id>')
def delete_post(id):
    if not id:
        return jsonify({"error": "No id was provided"}), 400

    try:
        delete(id = id)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify("Post Deleted"), 201        
    

@app.get('/getposts')
def get_all():
    try:
        
        get_all()
        
    except Exception as e:
        return jsonify(str(e)), 500
   
    
