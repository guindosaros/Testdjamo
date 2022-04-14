import requests


data = {
    "title": "Titre Test",
    "content": "Entretien à Djamo",
    "authorId": 342,
    "isPublished": True,
}

req = requests.post("http://api-server/posts", data=data)

print(req.status_code)
