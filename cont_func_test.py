from httpx import post, get
from pprint import pprint
import content_post_func as mm
import json
import textwrap

data_url = "https://mobile-phone-server.vercel.app/phones"
res = get(data_url).json()
phones_record = res.get('RECORDS')
for phone in phones_record:
    name = phone.get("name")
    picture = phone.get("picture")
    released_at = phone.get("released_at")
    body = phone.get("body")
    os = phone.get("os")
    storage = phone.get("storage")
    display_size = phone.get("display_size")
    camera_pixels = phone.get("camera_pixels")
    video_pixels = phone.get("video_pixels")
    ram = phone.get("ram")
    chipset = phone.get("chipset")
    battery_size = phone.get("battery_size")
    battery_type = phone.get("battery_type")
    specifications = phone.get("specifications")
    spec_data = json.loads(specifications)
    table = mm.table_gen(spec_data,name)
    # making intro part with these info
    intro_txt = f"Looking for a smartphone that delivers the essentials without breaking the bank? Look no further than the {name}. Released in {released_at}, this device packs a punch with its large display, decent camera setup, and long-lasting battery, all wrapped in a lightweight and slim design."
    str_txt = f"Here's a quick look at what the {name} has to offer:"
    list_txt = f"Spacious Display: Enjoy your content on a vibrant {display_size} screen, perfect for immersive viewing experiences.\n" \
               f"Triple Camera Versatility: Capture memorable moments with its {camera_pixels} triple rear camera, ready to handle various photo and video scenarios.\n" \
               f"Smooth Performance: Powered by a {chipset} chipset and {ram} of RAM, the {name} ensures seamless multitasking and smooth app experiences.\n" \
               f"All-Day Power: Stay connected and entertained with a {battery_size} {battery_type} battery that supports hours of use.\n" \
               f"Modern Operating System: Experience the latest features and security updates with {os}."
    last_intro = f"Whether you're browsing the web, streaming videos, capturing photos, or staying in touch with loved ones, the {name} is ready to handle your daily needs with style and efficiency. Scroll down for more details and a closer look at this budget-friendly smartphone."
    list_txt = f"Spacious Display: Enjoy your content on a vibrant {display_size} screen, perfect for immersive viewing experiences.\n" \
               f"Triple Camera Versatility: Capture memorable moments with its {camera_pixels} triple rear camera, ready to handle various photo and video scenarios.\n" \
               f"Smooth Performance: Powered by a {chipset} chipset and {ram} of RAM, the {name} ensures seamless multitasking and smooth app experiences.\n" \
               f"All-Day Power: Stay connected and entertained with a {battery_size} {battery_type} battery that supports hours of use.\n" \
               f"Modern Operating System: Experience the latest features and security updates with {os}."
    list_of_lines = list_txt.split('\n')
    for line in list_of_lines:
        x = mm.list_gen(line)
        print(x)







