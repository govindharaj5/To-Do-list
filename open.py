from openai import OpenAI
client = OpenAI()

response = client.completions.create(
    model="gpt-4.1-mini",
    prompt="Write a JavaScript function to find prime numbers.",
    max_tokens=200
)

print(response.choices[0].text)
