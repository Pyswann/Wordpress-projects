import con_all_def as oai
import con_html as wp

kw = "How to clean chainsaw"
title_gen = oai.oai_command(f'Write highly SEO-optimized title on the {kw} keyword. Make sure the heading sound simple and fulfill the user intent. The expression should be like you have used or experienced it before. Must include the keyword on the title and don\'t suggest over-saturated titles and the word count should be 20.')

# intro part
intro_gen = oai.oai_output(f"I Want You To Act As A Content Writer Very Proficient SEO Writer Writes Fluently English. Write a 120-word 100% Unique, SEO-optimized, Human-Written article in English introduction for the keyword {kw}. In the first paragraph (50 words), define the importance of the keyword and highlight potential problems it poses to readers. In the next paragraph (30-35 words), provide a solution based on the issues mentioned. In the last paragraph (30-35 words), explain why the upcoming content on this keyword will be an ideal read.")
ht_intro = wp.w_paragraph(intro_gen)
# print(ht_intro)

# sub heading
sub_heading = oai.oai_command(f"Generate 4 to 5 subheadings on the {kw} keyword. Make sure all the subheadings are relevant to kw, and the reader can get valuable information from them. The tone of the content should be simple, informative, and professional. Divide the paragraphs after the 4th line and then start the new line so that reader can read the content easily. Each of the heading should have at least 120 words lengthy. Here don't add any buttle points, all the text should be in paragraph format. The format should be 'Wordpress Gutenberg' format.")

# split = oai.spliting(sub_heading)
# print(split)
# print(sub_heading)

# ques type subheading
qs_head = oai.oai_chat(f"Generate 2 subheadings on the {kw} keyword. Make sure all the subheadings are relevant to kw, and all of them have the quality to engage the reader and have clarity and simplicity. Don't add any paragraphs under the subheading.")







# dicti = {}
#     x = variable.strip().split("\n\n")
#     if len(x) >= 1:
#         for single_line in x:
#             key = single_line.split("\n")
#             dicti[key[0]] = key[1]
