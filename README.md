![image](https://user-images.githubusercontent.com/7946482/225440356-c10feccb-24ef-412a-b696-9275a6fd896c.png)

## Description
This simple project leverages the OpenAI GPT-3 and Twilio SMS APIs to:
1. Generate a sweet, short poem
2. Send that poem via SMS

It is intended to be used in combination with Amazon Lambda and Amazon EventBridge. Amazon Lambda runs this code in a serverless container, triggered on a regular interval (e.g. once a day) by Amazon EventBridge.

The required libraries (contained in the `/package/` directory) and the `config.py` and `lambda_function.py` files get zipped together into a .zip file named `my-deployment-package.zip` with the following commands in Terminal:
```bash
cd package
zip -r ../my-deployment-package.zip .
cd ..
zip my-deployment-package.zip config.py lambda_function.py
```

## Requirements:
To run, program requires a file named `config.py` formatted with:
```python
TWILIO_SID = "Your Twilio SID as a string"
TWILIO_TOKEN = "Your Twilio token as a string"

OPENAI_ORG = "Your OpenAI org as a string"
OPENAI_KEY = "Your OpenAI key as a string"

GIRLFRIEND_NAME = "Your girlfriend's name"
GIRLFRIEND_NUMBER = "Your girlfriend's phone number, formatted with country code, as a string"
YOUR_NUMBER = "Your phone number on Twilio, formatted with country code, as a string"
```
