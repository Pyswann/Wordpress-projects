import base64
from requests import post
wp_user_name = "holasohan14@gmail.com"
wp_pass = "AvbF Mp7u ci29 whKx ykzS D6Hc"
wp_credential = f"{wp_user_name}:{wp_pass}"
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {"Authorization":f"Basic {wp_token.decode("utf-8")}"}

post_url = "http://pysohan.local/wp-json/wp/v2/posts"
post_data = {"title":"Honor View40 Specifications",
             "status":"publish",
             "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
             "category":"3"}

res = post(post_url, data=post_data,headers=wp_headers)
print(res)















