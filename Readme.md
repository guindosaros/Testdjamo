# DJamo Test Entretien

### 1- Cite four HTTP verbs and their use ?
    we have :
        - GET Method : this method is used to read or retrieve information
        - POST Method: it serves us to post information on a specific route
        - DELETE Method : it is used to delete data
        - PUT Method: this method is used to apply modifications 
        - PATCH Method: this method is used to apply partial modifications to a resource

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


### 3:
    3-a: 

        First of all for the implementation, I will first look for the best sms API service among the 3 providers.
        Then use the API of this service that I will implement in my application.
        First, I will start by testing if the API meets my expectations in terms of sending sms if it can send sms to various numbers in the world as the application can be used internationally.
        - then, I put a code in place that each time I want to send an sms to given users in case of worries make sure to retrieve this user in the database then his number and send him an sms.
        - after the implementation of the code make unit tests to see if the code works well and then make real internal tests.


    3-b:
        During my career as a developer I have worked on several internal projects for the different companies I have worked for
        I had implemented a Nannews application which was an information application the role of the application a scraper set up that ran on various African news sites to retrieve articles and store them in our database. And then set up an Api that I had to provide to the frontend
        The technology used for the backend was python and its framework Django. And the architecture is the MVT model ( Models View template )

        Unfortunately, I would not be able to provide the Gitlab repos and the site is no longer online.

        During a freelance mission I also had to write a script to automate the order of sneakers on the following site https://www.nike.com/fr

        Here is the link of the github repos: 

        https://github.com/guindosaros/botnike

        And here is the link of a project to set up an Api for the price list of Moroccan medicines, a project realized with Python/Django 

        https://github.com/guindosaros/pharmaapi