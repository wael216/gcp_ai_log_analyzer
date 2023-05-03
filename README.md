# gcp_ai_log_analyzer

## Description
This repo aims to use the openAI API to create a cloud function that:
- When a 500 error is detected, checks its explanation with ChatGPT and shows it in a web interface
- For every new 500 error, checks if it's new or already analyzed, and does the step 1 if it's new

To fulfill this, you need to:

1. Set up Google Cloud Functions and the required APIs:
   - Enable the Cloud Functions, Cloud Build, and Cloud Storage APIs in your Google Cloud Platform project.
   - Install and initialize the Google Cloud SDK on your local machine.

2. Create a Cloud Function that listens for 500 errors, checks for new errors, and communicates with ChatGPT with the code in the file `gcpfunction.py`.

3. Create a `requirements.txt` file with the dependencies listed in the repository.

4. Deploy the function with these commands:

``` 
gcloud functions deploy analyze_error \
 --runtime python310 \
 --trigger-http \
 --allow-unauthenticated \
 --set-env-vars OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>,ERRORS_BUCKET_NAME=<YOUR_BUCKET_NAME>

```

5. Create a simple web interface:
- You can create a simple web application using a frontend framework like React, Angular, or Vue.js to call your Cloud Function and display the explanations.
- When a new 500 error occurs, you can send a request to your Cloud Function using JavaScript's `fetch()` function, and then update the web interface with the explanation returned by the Cloud Function.

## Dependencies
List of dependencies can be found in the `requirements.txt` file.

## License
This project is licensed under the [LICENSE NAME] license. See the `LICENSE.md` file for details.
