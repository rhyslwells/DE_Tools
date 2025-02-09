import json 

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)

json_string = json.dumps(data)
# print(json_string)
# print(json.dumps(data, indent=4))

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

# print(encoded_hand)

# blackjack_hand == decoded_hand

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)

# print(data)


