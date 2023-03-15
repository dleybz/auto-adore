from twilio.rest import Client
import openai
import config

openai.organization = config.OPENAI_ORG
openai.api_key = config.OPENAI_KEY

account_sid = config.TWILIO_SID
auth_token = config.TWILIO_TOKEN

gf_number = config.GIRLFRIEND_NUMBER
your_number = config.YOUR_NUMBER

gf_name = config.GIRLFRIEND_NAME

client = Client(account_sid, auth_token)

def lambda_handler(event = None, context = None):
  message = client.messages.create(
    from_=your_number,
    body=generate_message(),
    to=gf_number
  )
  return(None)

def generate_message():
  '''Generates today's poem using OpenAI's GPT-3 API'''
  openai_response = openai.Completion.create(
      engine="text-davinci-003",
      prompt="Here's a 4 line poem that I wrote for my beautiful girlfriend " + gf_name + " about how amazing she is and how I hope she has a great day:",
      temperature=0.7,
      max_tokens=100,
  )
  return openai_response.choices[0].text


