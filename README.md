# Plant Parenthood API

Plant Parenthood API is the backend service used by the [Plant Parenthood Application](https://github.com/AlessandroRossi87/plant-parenthood). In order to ensure a smooth 
<hr>
<br>


## Development Goals

The goal of this API is provide a backend service to allow the Plant Parenthood front end application to perform, Create, Read, Update and Delete operations via the user interface.
<hr>
<br>

## Database Design

The database design includes the originally planned "Requests" model and the "plant_children" and "requested_children" from the Plants model. These were excluded in the final version but retained in this README for reference to future implementation.

![Database](https://github.com/AlessandroRossi87/pp-api/blob/main/readmefiles/database.png)


## Security

A permissions class named IsOwnerOrReadOnly has been introduced to ensure that only users who have created the content are granted the ability to edit or delete it.

## Technologies

* Django
    * Main framework used for application creation
* Django REST Framework
    * Framework used for creating API
* Cloudinary
    * Used for static image hosting
* Heroku
    * Used for hosting the application
* Git
    * Used for version control
* Github
    * Repository for storing code base and docs

<hr>
<br>

## Python Packages
<details open>
<summary> Details of packages </summary>

* asgiref==3.7.2
    * ASGI specification (Asynchronous Server Gateway Interface)
* cloudinary==1.36.0
    * Cloudinary integration for image and video storage
* dj-database-url==0.5.0
    * Used to parse the DATABASE_URL connection settings
* dj-rest-auth==2.1.9
    * Used with the authentication system
* Django==3.2.23
    * Main framework used to start the project
* django-allauth==0.44.0
    * Used for authentication
* django-cloudinary-storage==0.3.0
    * Cloudinary storage backend for Django
* django-cors-headers==4.3.1
    * Used for Cross-Origin Resource Sharing (CORS) headers in responses
* django-filter==23.4
    * Used to filter API results in serializers
* djangorestframework==3.14.0
    * Framework used to build API endpoints
* djangorestframework-simplejwt==5.3.0
    * Used with Django Rest Framework to create access tokens for authentication
* gunicorn==21.2.0
    * Used for deployment of WSGI applications
* oauthlib==3.2.2
    * Library for implementing OAuth 1.0 and OAuth 2.0 providers
* Pillow==10.1.0
    * Imaging Library - used for image uploading
* psycopg2==2.9.9
    * PostgreSQL database adapter to allow deployed application to perform CRUD on the PostgreSQL DB
* PyJWT==2.8.0
    * For creating Python JSON Web Tokens for authentication
* python3-openid==3.2.0
    * Python OpenID library
* pytz==2023.3.post1
    * World timezone definitions, modern and historical
* requests-oauthlib==1.3.1
    * OAuthlib integration with Requests
* sqlparse==0.4.4
    * SQL parser for Python
* whitenoise==6.4.0
    * Simplifies serving of static files

</details>
<hr>
<br>

## Testing

**Validator Results**

All folders were run through flake8. XXXXX


**Bugs and their fixes**

XXXXX

<hr>
<br>

## Deployment

## Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

<hr>
<br>

## Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

* Navigate to heroku and create an account
* Click the new button in the top right corner
* Select create new app
* Enter app name
* Select region and click create app
* Click the resources tab and search for Heroku Postgres
* Select hobby dev and continue
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
  * SECRET_KEY: (Your secret key)
  * DATABASE_URL: (This should already exist)
  * ALLOWED_HOST:
  * CLIENT_ORIGIN: url for the client front end react application that wil be making requests to these APIs
  * CLIENT_ORIGIN_DEV: address of the local server used to preview and test UI during development of the front end client application
  * GOOGLE_APPLICATION_CREDENTIALS:
  * GOOGLE_CREDENTIALS: json file with authentication keys and tokens to access the google cloud bucket where images are stored
  * GS_BUCKET_NAME: name of the bucket to upload images to.

* Click the deploy tab
* Scroll down to Connect to GitHub and sign in / authorize when prompted
* In the search box, find the repositoy you want to deploy and click connect
* Scroll down to Manual deploy and choose the main branch
* Click deploy

<hr>
<br>

## Cloudinary Storage

To set up bucket and service account. Please see - [Medium Article](https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f). The service account credentials will be needed for deployment.

**Code** 

Packages needed for deployment:

* django-storages[google]
* Pillow

Create a .profile file with the following line inside:

```echo ${GOOGLE_CREDENTIALS} > /app/ga-creds.json```

This line is used to instruct heroku that the GOOGLE_CREDENTIALS var is called ga-creds.json

**Heroku**

1. Log in to heroku and open the pp-api app
2. Click settings
3. Click Config vars
4. Add the following variables:

    * Key: GOOGLE_APPLICATION_CREDENTIALS -  Value: ga-creds.json
    * Key: GOOGLE_CREDENTIALS - Value: json contents of the service account key
    * Key: GS_BUCKET_NAME - Value: Name of the bucket where files are stored

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

In order to run, you will need to create an env.py file and add the config vars as used in heroku steps above.


**Virtual Environment setup** 

Windows:

```
python -m venv venv \
venv/Scripts/activate \
pip install -r requirements.txt
```

Mac:

```
python -m venv venv \
source venv/bin/activate \
pip install -r requirements.txt
```

### Forking

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

## Credits

### Content:
<br>

