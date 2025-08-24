import requests #Import requests library to make HTP requests

parameters = {
    "amount": 10,   #Requests 10 questions from the API
    "type": "boolean",      #True/Fals type questions
}


#Sending a GET request to Open Trivia DB API with the parameters
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json() #COnvert the JSON response to a Python dictionary
question_data = data["results"] #Extracts the resulst list which contains questions
