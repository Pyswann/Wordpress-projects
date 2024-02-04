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
# x = oai_command("what is love")
# print(x)


def oai_chat(prompt):
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
x = oai_chat("what is love")
print(x)


def spliting(variable):
    dicti = {}
    x = variable.strip().split("\n\n")
    if len(x) >= 1:
        for single_line in x:
            key = single_line.split("\n")
            dicti[key[0]] = key[1]
    return dicti


def create_dictionary(text):
    # Splitting text into paragraphs using '\n\n'
    paragraphs = text.split('\n\n')
    # Creating a dictionary to store key-value pairs
    data_dict = {}
    # Extracting heading and paragraph for each entry
    for paragraph in paragraphs:
        lines = paragraph.split('\n', 1)  # Splitting each paragraph into heading and content
        if len(lines) == 2:
            a = lines.split("\n\n")
            heading, content = a
            data_dict[heading] = content

    return data_dict
