person={
    "name":"sita",
    "age":"20",
    "hobby":(
        "watching tv",
        "playing music"
    ),
    "family_member":[
        {
            "relation":"mother",
            "name":"abc",
            "age":"40"
        },
          {
            "relation":"father",
            "name":"bwc",
            "age":"45"
        },
    ]
        
    
}


# print(person['name'])
# print(person['hobby'][0])
print(person['family_member'][0]['name'])


print(person['family_member'][1]['name'][::-1])    #reverse the string