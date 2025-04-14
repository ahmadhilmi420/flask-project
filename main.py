from flask import Flask, request, render_template, jsonify

app = Flask(__name__) 

# dummy_db = {
#     "users": {
#         "ahmad@gmail.com": {
#             "password": "123456",
#             "first_name": "ahmad",
#             "last_name": "hilmi",
#             "email": "ahmad@gmail.com"
#         }
#     }
# }
dummy_db = {
    'users': {
        'ahmadhilmi@gmail.com': {
            'password': 'langitke1', 
            'first_name': 'ahmad', 
            'last_name': 'hilmi', 
            'full_name': 'ahmad hilmi', 
            'email': 'ahmadhilmi@gmail.com'
        },
        
        'rizaldibanyu@gmail.com': {
            'password': 'kakiku', 
            'first_name': 'rizaldi', 
            'last_name': 'banyu', 
            'full_name': 'rizaldi banyu', 
            'email': 'rizaldibanyu@gmail.com',
        },
    }
    
}


# def main():
#     print("Hello from milestone-3-ahmadhilmi420!") 
def all_user_repoitory() -> dict:
    return dummy_db.copy()

def create_user_repository(email: str, user_data: dict):
    dummy_db["users"][email] = user_data
    

def get_all_users():
    users = all_user_repoitory()["users"]
    formated_responses = []
    for email, user_data in users.items():
        user_data.pop("password")
        user_data.pop("full_name")
        user_data.pop("last_name")
        formated_responses.append(user_data)
    return formated_responses

def create_users(data_masuk: dict) -> str:
    email = data_masuk.get("email")	
    password = data_masuk.get("password")
    first_name = data_masuk.get("first_name")
    last_name = data_masuk.get("last_name")
    full_name = f"{first_name} {last_name}"
    if not email:
        return jsonify({"data": {"message": "Email is required"}, "success": False}), 400
    if not password:
        return jsonify({"data": {"message": "Password required"}, "success": False}), 400
    if not first_name:
        return jsonify({"data": {"message": "First name is required"}, "success": False}), 400
    if not last_name:
        return jsonify({"data": {"message": "Last name is required"}, "success": False}), 400
    data_masuk["full_name"] = full_name
    create_user_repository(data_masuk.get("email"), data_masuk)
    return email

@app.route("/")
def index():
    return render_template("index.html")



    # dummy_db["users"].update (user_data)
    # return jsonify(
    #     {"data": {"massage": f"{email} is registered"}, "success": True}
    #     ), 201

@app.route("/users", methods=["GET", "POST", "PUT", "DELETE"])
def get_users():
    print("=" * 10,"METHOD -> ",request.method,"=" * 10)
    match request.method.lower():
        case "get":
            response = get_all_users()
            return jsonify({"data": response, "success": True}), 200
        case "post":
            email = create_users(request.json)
            return jsonify({"data": {"massage": f"{email} is registered"}, "success": True}), 201
        case "put":
            pass
        case "delete":
            pass
