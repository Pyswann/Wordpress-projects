from openai import OpenAI

api_key = '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'
client = OpenAI(api_key=api_key)
kw = "Rolex vs Titan"


def oai_output(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

x = oai_output(f"Craft a concise, informative, and professional introduction for the keyword {kw}. In the first paragraph (30-35 words), define the importance of the keyword and highlight potential problems it poses to readers. In the next paragraph (30-35 words), provide a solution based on the issues mentioned. In the last paragraph (30-35 words), explain why the upcoming content on this keyword will be an ideal read.")
print(x)