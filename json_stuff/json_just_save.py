import json

data = {
    "courses": [
        {
            "name": "Math",
            "score": 20,
            "absent": 2
        },
        {
            "name": "Geo",
            "score": 18,
            "absent": 1
        },
        {
            "name": "Quantum Physics",
            "score": 9.75,
            "absent": 0
        }
    ]

}

file = open("data.json", "w")
json.dump(data, file)

json.load()