def strong_p(txt):
    codes = f'<!-- wp:paragraph --><p><strong>{txt}</strong></p><!-- /wp:paragraph -->'
    return codes


def para_gen(txt):
    codes = f"<!-- wp:paragraph --><p>{txt}</p><!-- /wp:paragraph -->"
    return codes


def h2_gen(txt):
    codes = f'<!-- wp:heading --><h2 class="wp-block-heading">{txt}</h2><!-- /wp:heading -->'
    return codes

def h3_gen(txt):
    codes = f'<!-- wp:heading --><h3 class="wp-block-heading">{txt}</h3><!-- /wp:heading -->'
    return codes


def table_gen(dict,cap):
    codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dict.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += tr_data
    caption = f'<figcaption class="wp-element-caption">{cap}</figcaption></figure>'
    codes += '</tbody></table></figure><!-- /wp:table -->'+caption
    return codes















