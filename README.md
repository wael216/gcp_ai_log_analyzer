# gcp_ai_log_analyzer
this repo aims to use the openAI API to create a cloud function that :  
- when a 500 error is detected, checks its explanation with chatgpt and show it in a web interface  
- for every new 500 error check if it's new or already analysied, and do the step 1 if it's new
