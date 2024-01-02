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
  return response.choices[0].text.strip().split("\n")

faqs = oai_ans(faq_prompt)
print(faqs[1])









