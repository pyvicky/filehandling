Contact Manager API

How to setup Docker container:
1. Build Docker image:
    Go to the folder containing Dockerfile and the source code then try the command: docker build -t firstproj .

2. Run the Docker container:
   Once the image is built, you can run a Docker container based on that image using the command: docker run  -p 8000:8000 firstproj

3. Accessing the API
   After running the Docker container access the app from the Swagger UI using the URL http://localhost:8000/docs

   To ADD a contact:
   > select POST add_contact then click on try it out on the right> under request body enter the name and number and execute it> In responses you can find the contact added message.

   To SHOW all contacts:
   > select get_contacts then click on try it out on the right> In response body you can find the list of contacts were added to the list.

   To DELETE a contact:
   > select delete_contact then click on try it out on the right> under parameter entet the name which you want to delete then hit execute.
