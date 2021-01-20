# Demo-api
used for serving api on frontend.

# to build the image

1. Clone the repository

2. To build the image on local machine
```
docker build -t web:latest .
```
3. To run the image on container
```
docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
```
(set debug enviornment as per you choice)

4. To stop the container

```
docker stop django-heroku
```

5. To remove the container

```
docker rm django-heroku
```

6. Server will run on : **http://localhost:8007/**
   
   (by default debug=0 check on http://localhost:8007/admin)

## Note 
1. Whenenver any change is made please do 4 and 5 step first then build and run again

2. set debug=1 in 3rd step of build the image for checking apis. 


