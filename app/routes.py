from flask import request
from app import app
from my_data.datas import car_data

# DB will be set up later
users = []

@app.route("/")
def hello_world():
    first_name = "Steve"
    last_name = "Agboola"
    return f'Hello From: {first_name} {last_name}'

# USER ENDPOINTS 

# Create New User  
# Because we are creating new data and sending info to the server, we need to do a POST
@app.route('/users', methods=['POST'])
def create_user(): # Create function called create_user
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'Your content-type must be application/json'}, 400

    # Get the data from the request body
    data = request.json

    # Validate that the data has all of the required fields
    # We will eventually use react so we will leave this as camel case to get it ready (javascript)
    required_fields = ['firstName', 'lastName', 'username', 'email', 'password']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    
        # Get the values from the data
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check to see if any current users already have that username and/or email
    for user in users:
        if user['username'] == username or user['email'] == email:
            return {'error': 'A user with that username and/or email already exists'}, 400

    # Create a new user dict and append to users list
    new_user = {
        "id": len(users) + 1,
        "firstName": first_name,
        "lastName": last_name,
        "username": username,
        "email": email,
        "password": password
    }
    users.append(new_user)
    return new_user, 201

# Create a route that will get all of the data_list
@app.route('/datas')
def get_datas():
    #Get the car_data
    datas = car_data
    return datas

# Create a route that will get a single data_list by its ID
@app.route('/datas/<int:d_id>')  # default is a get request so we dont have to do method =
def get_d(car_data_id):    # create a function i called d
    # Get the datas data
    datas = car_data
    # Loop through each task
    for d in datas:
        #Chek if "id" key of the task and see if it matches the car_data_id from url
        if d['id'] == car_data_id:
            # Return the datas dictionary
            return d
    # If we loop through all the datas without returning, the datas with the ID does not exist
    return {'error': f'Post with model {car_data_id} does not exist'}, 404

#  Without something like postman, our browser can only make a get request even if we write a post request code
#  So our browser will continue to display our data in datas.py

# Now we want to send resources to the server so we need to do a POST request
# Go to postman and do a post reqest
# Lets create a new datas route
@app.route('/datas', methods=['POST'])
def create_post():  #Create a function I called create_post
     # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'You content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    data = request.json
    # Validate the incoming data
    required_fields = ['model', 'bodyColor', 'interiorColor']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
  

     # Get data from the body
    model = data.get('model')
    bodyColor = data.get('bodyColor')
    interiorColor = data.get('interiorColor')

    new_data = {
        "id": len(car_data) + 1,
        "model": "model",
        "bodyColor": "bodyColor",
        "year": 2099,
        "interiorColor": "interiorColor",
     }
    
    # Add the new data to the list of data
    car_data.append(new_data)
    return new_data, 201

    # Create a new instance of Post which will add to our database
    # new_post = Post(model=model, bodyColor=bodyColor, interiorColor=interiorColor)
    # return new_post.to_dict(), 201


 