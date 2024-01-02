from openai import OpenAI

api_key = "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"
kw = str(input("enter your keyword: "))
faq_prompt = f"Write 5 faqs on {kw} that are highly asked on google. Answer them with the tone of simple, straight, and professional. The answer should be in 25 words"


def oai_ans(prompt):
  client = OpenAI(api_key=api_key)
  response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  faq_list = response.choices[0].text.strip().split("\n")
  dog_faq = {}
  i = 0
  for i in range(0, len(faq_list), 2):
    question = faq_list[i].strip()
    answer = faq_list[i + 1].strip()
    dog_faq[question] = answer
  return dog_faq

x = oai_ans(faq_prompt)
print(x)
