from openai import OpenAI

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key= "" #wont work as i dont have its subscription
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant name Jarvis who is best in performing general tasks same as alexa but best."},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message)

# THE API KEY IS PAID
