from httpx import get
from pprint import pprint
base_url = "https://www.cocooncityhostel.com/wp-json/wp/v2"
# get post
post_api = f"{base_url}/posts"
res = get(post_api)
# pprint(res.json())

# get page
page_api = f"{base_url}/pages?per_page=20"
res_page = get(page_api).json()
pprint(res_page)

# get post









