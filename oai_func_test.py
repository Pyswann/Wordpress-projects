from openai import OpenAI

api_key = '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'

# prompt = 'Generate 4 subheadings on the "how to keep your cat\'s litter box clean" keyword. Make sure all the subheadings are relevant to kw, and the reader can get valuable information from them. Under each subheading provide detailed answers in multiple paragraphs.'
def chat_gpt(prmpt):
    client = OpenAI(api_key=api_key)
    response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prmpt,
    temperature=1,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].text.strip()
x = chat_gpt('Generate 4 subheadings on the "how to keep your cat\'s litter box clean" keyword. Make sure all the subheadings are relevant to kw, and the reader can get valuable information from them. Under each subheading provide detailed answers in multiple paragraphs.')
print(x)