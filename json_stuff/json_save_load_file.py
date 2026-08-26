import json

### Insert Data

with open("data.json", "w") as f:
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

    # f.write(json.dumps(data, indent=4))
    json.dump(data,f)


### Load Data
data_json = None

with open("data.json") as f:
    data_json = f.read()

data = json.loads(data_json)

for course in data["courses"]:
    print("--------------------")
    print(f"Name: {course["name"]}")
    print(f"Score: {course["score"]}")
    print(f"Gheybaaat: {course["absent"]}")
