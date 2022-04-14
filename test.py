import requests
import requests_to_curl


data = {
    "title": "Titre Test",
    "content": "Entretien à Djamo",
    "authorId": 342,
    "isPublished": True,
}

req = requests.post("http://api-server/posts", data=data)

test = requests_to_curl.parse(req)

print(test)
