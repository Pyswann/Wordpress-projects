import faq_func as fn
import faq_html as ht

# intro part
kw = "why do budgies bob their heads"
intro = f"generate an SEO-optimized 130 word based intro on the keyword of {kw}. Set the content tone simple, informative, and professional and divide the introduction into multiple paragraphs."
in_res = fn.oai_ans(intro)
ready_in_ht = ht.wp_p(in_res)

# in_wr = fn.write_txt("gg.txt", in_ht)
# print(in_ht)

# sub-heading part
sub_head = f"Generate 4 subheadings on the {kw} keyword. Make sure all the subheadings are relevant to kw, and the reader can get valuable information from them. The tone of the content should be simple, informative, and professional. Each of the heading should have at least 120 words lengthy."
h2_res = fn.oai_ans(sub_head)
div = fn.spliting(h2_res)
ready_sub_h2 = fn.store_k_v(div)

# ques type heading

keys = '\n'.join(map(lambda key: key[0], div.items()))
qus_type_h2 = f"Generate 3 question-type subheadings on the {kw} keyword and make sure they are not repeated as like you provided before {keys}. Make sure all the subheadings are relevant to kw, and the reader can get valuable information from them. The tone of the content should be simple, informative, and professional. Each of the heading should have at least 120 words lengthy."
ques_type_h2 = fn.oai_ans(qus_type_h2)
ques_h2_sp = fn.spliting(ques_type_h2)
ready_ques_h2 = fn.store_k_v(ques_h2_sp)


# faq gen
faq_prmt = f"write 6 faqs on the {kw}. Make sure all the faqs are relevant to kw, and the reader can get valuable information from them."
faq_res = fn.oai_ans(faq_prmt)
div_faq = fn.spliting(faq_res)
ready_faq = fn.store_k_v(div_faq)
# # print(ready_faq)
#
content = f'{ready_in_ht}{ready_sub_h2}{ready_ques_h2}{ready_faq}'
print(content)

