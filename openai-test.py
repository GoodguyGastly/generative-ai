from dotenv import load_dotenv
import os
from openai import OpenAI

# Load API key from .env file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(api_key=openai_api_key)

# Create a chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant."},
        {"role": "user", "content": "Say hello."}
    ]
)

# Print the response
print(completion.choices[0].message.content)
