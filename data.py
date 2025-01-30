import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

quote_dict = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
quote_dict.raise_for_status()
data = quote_dict.json()
question_data = data["results"]
