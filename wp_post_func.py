from requests import get
from pprint import pprint


def media_from_url(img_src, phone_name):
    codes = (f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} -->'
             f'<figure class="wp-block-image aligncenter size-large"><img src="{img_src}"'f'alt="{phone_name}"/>'
             f'<figcaption class="wp-element-caption"><strong><em>{phone_name}</em></strong></figcaption></figure>'
             f'<!-- /wp:image -->')
    return codes


def table_making(dict,cap):
    codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dict.items():
        table_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += table_data
    caption = f'<figcaption class="wp-element-caption">{cap}</figcaption></figure>'
    codes += '</tbody></table></figure><!-- /wp:table -->' + caption
    return codes


def text_gen(text):
    p_codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return p_codes


def gen_h2s(txt):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{txt}</h2><!-- /wp:heading -->'


def full_content_gen(*args):
    final = ""
    for arg in args:
        final += arg
    return final
