# DJamo Test Entretien

### 1- Cite four HTTP verbs and their use ?
    we have :
        - GET Method : this method is used to read or retrieve information
        - POST Method: it serves us to post information on a specific route
        - DELETE Method : it is used to delete data
        - PUT Method: this method is used to apply modifications 
        - PATCH Method: this method is used to apply partial modifications to a resource

```python 

        import requests

        data = {
            "title": "Titre Test",
            "content": "Entretien à Djamo",
            "authorId": 342,
            "isPublished": True,
        }

        req = requests.post("http://api-server/posts", data=data)

        print(req.status_code)
```

### 2:

    2-a : 

    ```python 

        import requests

        data = {
            "title": "Titre Test",
            "content": "Entretien à Djamo",
            "authorId": 342,
            "isPublished": True,
        }

        req = requests.post("http://api-server/posts", data=data)

        print(req.status_code)
    ```

    2-b: the HTTP method used is the POST method

    2-c