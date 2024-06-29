from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods =["GET"])
def get_contacts():
    contacts = Contact.query.all()
    #it is pytjon object but we can not return pytjon objects so we need to convert them to json.
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts}), 200

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("last_name")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}), 
            400,
        )
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        #staging area not written to the database yet.
        db.session.add(new_contact)
        #written into the database permanently.
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
        


#if we import this main.py file don't do this otherwise run
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True) 