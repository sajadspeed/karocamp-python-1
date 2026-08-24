name = "Roya"

student = {
    "name": name,
    "std_id": 236541213,
    "is_a_good_person": True,
    "friends": [ 
        {
            "name": "Ziba",
        }
     ]
}

print( student["friends"][0] )

for friend in student["friends"]:
    print(friend)
