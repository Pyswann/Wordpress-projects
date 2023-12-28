import wp_post_func as mm
from httpx import get,post
import json
from base64 import b64encode
data_url = "https://mobile-phone-server.vercel.app/phones"
res = get(data_url).json()
phones = res.get("RECORDS")
# collecting all initial datas
for phone in phones:
    name = phone.get("name")
    released_at = phone.get("released_at")
    os = phone.get("os")
    storage = phone.get("storage")
    display_size = phone.get("display_size")
    display_resolution = phone.get("display_resolution")
    camera_pixels = phone.get("camera_pixels")
    ram = phone.get("ram")
    chipset = phone.get("chipset")
    battery_type = phone.get("battery_type")
    battery_size = phone.get("battery_size")
    picture_url = phone.get("picture")
    body = phone.get("body")
    # paragraph
    para = f"The {name} is an {os} smartphone that was released on {released_at}. It has a {display_size} large display with a resolution of {display_resolution}. The phone is powered by a {chipset} chipset . It comes with {ram} GB of RAM and 16 GB of internal storage, which can be expanded using a microSDXC card. The phone has a triple camera setup on the back, with an {camera_pixels} primary camera and two 2 MP cameras, and a 5 MP front-facing camera. The phone is equipped with a {battery_size} {battery_type} battery."
    # table data
    first_table_data = {
        'name': name,
        'released data': released_at,
        'chipset': chipset,
        'body': body
    }
    spec_str = phone.get("specifications")
    data = json.loads(spec_str)
    # all content elements
    first_wp_para = mm.text_gen(para)
    first_img = mm.media_from_url(picture_url,name)
    first_h2 = mm.gen_h2s(name+"overview")
    first_table = mm.table_making(first_table_data,name)
    # specification section
    spec_h2 = mm.gen_h2s(f"{name} Specifications")
    spec_table = mm.table_making(data,f"{name} Specifications")
    # full content generating
    full_content = mm.full_content_gen(first_wp_para,first_img,first_h2,first_table,spec_h2,spec_table)
    print(full_content)
    # hitting all the post to wp
    user_name = "holasohan14@gmail.com"
    password = "AvbF Mp7u ci29 whKx ykzS D6Hc"
    wp_credential = user_name + ":" + password
    wp_token = b64encode(wp_credential.encode())
    wp_headers = {"Authorization": f"Basic {wp_token.decode("utf-8")}"}
    web_url = "http://pysohan.local/wp-json/wp/v2/posts"
    # post structure
    post_data = {"title": f"We have used{name} for 30 Days and That Busted the Myth!",
                 "status": "publish",
                 "content": full_content,
                 "category": "3"}
    res = post(web_url, data=post_data, headers=wp_headers,verify=False)
    print(res)














