import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print("hello")

#Following https://realpython.com/python-json/#deserializing-json
# using json_test2.ipynb 