Testing APIs using Cypress Testing Framework and JavaScript.

This small app was created with express BE framework and was created only for testing purposes.
It includes mainly registration & login API (focusing on Auth).
Database that was used is MongoDB.

To run the server:
``
npm start
``

You can manully test the endpoint to make sure everything works for you, by running:

register endpoint:

``
curl -d '{"name": "Static Tester", "email": "static@test.io", "password": "simplepass"}' -H "Content-Type: application/json" http://localhost:3000/api/user/register
``

login endpoint:

``
curl -d '{"email": "static@test.io", "password": "simplepass"}' -H "Content-Type: application/json" http://localhost:3000/api/user/login 
``

Users on MongoDB
![7645D753-D483-4792-B9F7-48308A3968BE](https://user-images.githubusercontent.com/83350680/191087374-5e05d8b6-c5b0-4706-942c-c4856002ff69.jpeg)



To run tests:
``
npm test
``


login spec:

![E62E1D03-E54D-49EB-BB51-3B1CEA362F2A](https://user-images.githubusercontent.com/83350680/191088279-6bb19b69-6bf0-4354-99c4-08ece316fa43.jpeg)

register spec:

![BA7A3231-A3B1-4917-8C4B-766ADFDB4A6B](https://user-images.githubusercontent.com/83350680/191088312-76a48269-703e-41cf-aee7-5be1963670bb.jpeg)

summary:

![85B5AB8F-C9CF-4A6C-8CB2-8BA9998E1C79_4_5005_c](https://user-images.githubusercontent.com/83350680/191088369-19a49e8a-a24b-4fc0-8142-6b7560f2601e.jpeg)
