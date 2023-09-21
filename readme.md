Garage - Backend
Project By: Oleh Kravets

Descripton
Introducing Garage: the ultimate car management app. Easily track and catalog your car collection, set maintenance reminders, and connect with fellow car enthusiasts, all in one user-friendly platform. Start managing your automotive passion effortlessly with Garage app.

Link
[Deployment](DEPLOYMENT LINK)

Technologies Used
Django
Postman
Python
JavaScript


Backend Endpoints
ENDPOINT	METHOD	PURPOSE
/garage	GET	return list of cars
/garage/:id	DELETE	delete a car entry from database
/garage/:id	PUT	receive info & update car entry in database
/garage	POST	receive info from new form & create new car entry in database
/garage/:id	GET	render page with the shift entry
ERD