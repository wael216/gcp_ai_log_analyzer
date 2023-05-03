import os
import json
from google.cloud import storage
from openai import OpenAI

# Initialize the OpenAI client with your openai api key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the Google Cloud Storage client
storage_client = storage.Client()
bucket_name = os.environ.get("ERRORS_BUCKET_NAME")
bucket = storage_client.get_bucket(bucket_name)

def analyze_error(request):
    request_json = request.get_json(silent=True)
    
    if not request_json or 'error_message' not in request_json:
        return 'Invalid request payload', 400

    error_message = request_json['error_message']
    
    # Check if the error message is already analyzed
    error_hash = hash(error_message)
    blob = bucket.get_blob(str(error_hash))

    if not blob:
        # Analyze the new error message using ChatGPT
        openai_result = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Explain the following 500 error message in simple terms: {error_message}",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        explanation = openai_result.choices[0].text.strip()
        
        # Save the explanation to Google Cloud Storage
        blob = bucket.blob(str(error_hash))
        blob.upload_from_string(json.dumps({"error_message": error_message, "explanation": explanation}))
    else:
        # Load the explanation for the existing error message
        explanation_data = json.loads(blob.download_as_text())
        explanation = explanation_data['explanation']

    return {'explanation': explanation}, 200
