# gcp_ai_log_analyzer
this repo aims to use the openAI API to create a cloud function that :  
- when a 500 error is detected, checks its explanation with chatgpt and show it in a web interface  
- for every new 500 error check if it's new or already analysied, and do the step 1 if it's new

to fulfill this you need to : 

1 - Set up Google Cloud Functions and the required APIs:
Enable the Cloud Functions, Cloud Build, and Cloud Storage APIs in your Google Cloud Platform project.
Install and initialize the Google Cloud SDK on your local machine.

2 - Create a Cloud Function that listens for 500 errors, checks for new errors, and communicates with ChatGPT with the code in the file gcpfunction.py

3 - create a requirements.txt file with what's in here 

4 - deploy the function with these commands : 
gcloud functions deploy analyze_error \
    --runtime python310 \
    --trigger-http \
    --allow-unauthenticated \
    --set-env-vars OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>,ERRORS_BUCKET_NAME=<YOUR_BUCKET_NAME>

5 - Create a simple web interface:
You can create a simple web application using a frontend framework like React, Angular, or Vue.js to call your Cloud Function and display the explanations. When a new 500 error occurs, you can send a request to your Cloud Function using JavaScript's fetch() function, and then update the web interface with the explanation returned by the Cloud Function.
