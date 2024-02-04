from openai import OpenAI
import faq_html as ht

api_key ='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'
client = OpenAI(api_key=api_key)

def oai_ans(prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
      "role": "user",
      "content": prompt
    }
    ],
    temperature=1,
    max_tokens=2056,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].message.content


def add_backslash_before_single_quotes(paragraph):
    updated_paragraph = paragraph.replace("'", "\\'")
    return updated_paragraph


def spliting(txt):
    d = {}
    a = txt.strip().split("\n\n")
    con = ""
    if len(a) >= 2:
        for single_line in a:
            b = single_line.split("\n")
            d[b[0]] = b[1]
    return d


def write_txt(f_name, txt):
    with open(f_name, "w") as wt:
        wt.write(txt)


def append_txt(f_name, txt):
    with open(f_name, 'a') as at:
        at.write(txt)


def para(txt):
    single_para = txt.split("\n\n")
    # print(single_para)
    for each in single_para:
        gen = ht.wp_p(each)
        print(gen)


def store_k_v(txt):
    result = ""
    for key, value in txt.items():
        ht_h2 = ht.wp_h2(key).title()
        ht_v = ht.wp_p(value)
        temp = f'{ht_h2}{ht_v}'
        result += temp
    return result




