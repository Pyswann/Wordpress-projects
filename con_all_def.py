from openai import OpenAI
api_key = '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'
client = OpenAI(api_key=api_key)


def oai_command(prompt):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


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
    return response.choices[0].message.content.strip()


def spliting(variable):
    dicti = {}
    x = variable.strip().split("\n\n")
    if len(x) >= 1:
        for single_line in x:
            key = single_line.split("\n")
            dicti[key[0]] = key[1]
    return dicti


