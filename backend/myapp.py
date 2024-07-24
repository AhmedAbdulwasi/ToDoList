from flask import Flask,jsonify,request
from flask_cors import CORS
from config import config_dict
from models import Tasks,db
import requests
from flask_migrate import Migrate
from datetime import datetime

def create_app(config_name='development'):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_dict[config_name])
    db.init_app(app)
    Migrate(app,db)


    @app.route("/api/showtasks", methods=['GET']) # Get the tasks when requested
    def get_showtasks():
        tasks = Tasks.query.all()
        json_tasks = list(map(lambda x: x.to_json(), tasks)) #basically maping it out and making them json for each tasks.
        return jsonify({"tasks": json_tasks})
    
    @app.route("/api/createtasks", methods=['POST']) # Create the tasks
    def post_createtasks():
        subject = request.json.get("subject")
        description = request.json.get("description")
        completed = request.json.get("completed")
        date_str = request.json.get("date")

        try:
            date = datetime.fromisoformat(date_str)
        except ValueError:
            return jsonify({"message": "Invalid date"}), 400

        if not subject or not description or not date:
            return jsonify({"message":"Subject, description, and date is required."}), 400
        
        newtasks = Tasks(subject=subject,description=description,completed=completed,date=date)

        try:
            db.session.add(newtasks)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": f"Error 400: {str(e)}"}), 400

        return jsonify({"message":"New Task Created!"}),201
    
    @app.route("/api/updatetasks/<int:task_id>", methods=["PATCH"])
    def updatetasks(task_id): # Update the tasks
        task = Tasks.query.get(task_id)

        if not task:
            return jsonify({"message":"No task exists with that task id"}),404
        else:
            data = request.json
            task.subject = data.get("subject", task.subject)
            task.description = data.get("description", task.description)
            task.completed = data.get("completed", task.completed)
            date_str = data.get("date")

            try:
                task.date = datetime.fromisoformat(date_str)
            except ValueError:
                return jsonify({"message": "Invalid date format"}), 400
            db.session.commit()
            return jsonify({"message":"Task updated!"}),200
    

    @app.route("/api/deletetasks/<int:task_id>", methods=["DELETE"]) # Delete tasks
    def deletetask(task_id):
        task = Tasks.query.get(task_id)

        if not task:
            return jsonify({"message":"No task exists with that task id"}),404
        else:
            db.session.delete(task)
            db.session.commit()

            return jsonify({"message":"Task Deleted!"}),200


    return app

    


app = create_app()
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
