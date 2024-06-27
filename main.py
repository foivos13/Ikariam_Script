import json
import requests
from bs4 import BeautifulSoup
import http.cookiejar
import urllib

cookies = {
    'pc_idt': 'ADnn_Bj9N_VO_Nl-J1TGjXZVEF3ZZz_hE-lHYd2bN-zsBGrd413ASAed1cfXTWkrXPOEgFTpE_qiqGHv0NkMQS9bw-lWbv8DJJOhTqqpZ4g2aP_IVe6nzGFMLT9pr5Xm3tQyOhbKcU4ZvT6-Ja2Z2IaxT4FElflNemXELA',
    'gf-token-production': 'f06b38c3-6b45-458f-b77d-cc509113be35',
    'gf_pz_token': '4e6a3543-4ae2-4409-b2cf-8bff08a785e5',
    'gf-cookie-consent-4449562312': '^|7^|1',
    'cf_clearance': 'Xsw1WBsEHfFlHpHfHQOooCLzNezVHnHnFl2veYr6C60-1714608274-1.0.1.1-M6HVJKruZDH4aS9pGoKJAQ0MtBRwXHXQ2xYoxv9PaBqchtGIyiaXPRkn1fvnXJ2oYva8Pk6.sKvk2OT02NLtWA',
    'PHPSESSID': '2bqshgi3584mnjuf6j18pbpug1',
    'ik_video_player': 'volume^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Bpath^%^3D/^%^3Bpath=/',
    'ik_friendslist_105499': 'page^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Dthis.length^%^3Bt--^%^3B^%^29if^%^28this^%^5Bt^%^5D^%^3D^%^3D^%^3De^%^29return^%^210^%^3Breturn^%^211^%^7D^%^3Bpath=/',
    'ikariam_loginMode': '0',
    '__cf_bm': 'JtHcyjh4ecbcaij3GN9AOQlTN40Pr7EknsC9Bb.okQ4-1719322101-1.0.1.1-6uHOlhh.EyZfWQxnzn.duf69Yw9JGqI4gAGqGUcEMvJ241jIv7caunNRaiaQSzc.CI1.HufWwsukGjYfTn0Pcw',
    'ikariam': '105499_ab50e5dce019948e4733f46e526131fc',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Referer': 'https://s56-en.ikariam.gameforge.com/?view=island&oldBackgroundView=city&containerWidth=2560px&containerHeight=600px&worldviewWidth=2560px&worldviewHeight=554px&cityTop=-103px&cityLeft=-1851px&cityRight=&cityWorldviewScale=0.885',
    # 'Cookie': 'pc_idt=AC67gghrk1kl5LQrIcThOf8zz0gzZxBpjSa99ruasa0RvqootnoI4EPrmdZARJdmOXNktqfpAs5N7SdRsXOXnz5NH8pqmpEXM7NvEoMhziFGOsmq7SGwnC7U0lbIOrC7UJQ9a6V74P4qrNRZV3AH8Ax2J27ZF4OEaY_fbA; gf-token-production=f06b38c3-6b45-458f-b77d-cc509113be35; gf_pz_token=4e6a3543-4ae2-4409-b2cf-8bff08a785e5; gf-cookie-consent-4449562312=^|7^|1; cf_clearance=Xsw1WBsEHfFlHpHfHQOooCLzNezVHnHnFl2veYr6C60-1714608274-1.0.1.1-M6HVJKruZDH4aS9pGoKJAQ0MtBRwXHXQ2xYoxv9PaBqchtGIyiaXPRkn1fvnXJ2oYva8Pk6.sKvk2OT02NLtWA; __cf_bm=pjVwQXsSBSFLpL9hVeGMJC96km1ykzgk8TOur.8kLPU-1717613637-1.0.1.1-YJo9VMf11tam94JClo3skism_ZYkwsyH_KQSOhKg9G1yy9G.c_RsGh5jsE5_OBic9DIJ3nA4ba4AATebRsHa3A; PHPSESSID=2bqshgi3584mnjuf6j18pbpug1; ik_video_player=volume^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Bpath^%^3D/^%^3Bpath=/; ik_friendslist_105499=page^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Dthis.length^%^3Bt--^%^3B^%^29if^%^28this^%^5Bt^%^5D^%^3D^%^3D^%^3De^%^29return^%^210^%^3Breturn^%^211^%^7D^%^3Bpath=/; ikariam_loginMode=0; ikariam=105499_f5e5187e8d1379c7d8584e52a4a3d73f',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=1',
}

params = {
    'view': 'island',
    'oldBackgroundView': 'island',
    'containerWidth': '2543px',
    'containerHeight': '600px',
    'worldviewWidth': '2543px',
    'worldviewHeight': '554px',
    'islandTop': '-247px',
    'islandLeft': '-1790px',
    'islandRight': '',
    'islandWorldviewScale': '1',
}






# ------------------ ISLAND ID OF 1ST CITY TO INITIATE THE GAME ------------------

response = requests.get('https://s56-en.ikariam.gameforge.com/', params=params, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

island_id = soup.find("input", {"name":"currentIslandId"}).get("value")




# ------------------ CITY LIST ------------------
params = {
    'view': 'palace',
    'cityId': '6294',
    'currentCityId': '6294',
    'ajax': '1',
}
response = requests.post('https://s56-en.ikariam.gameforge.com/', params=params, cookies=cookies, headers=headers).json()

city_list = {}
cities = response[0][1]["headerData"]['cityDropdownMenu']
filtered_cities = {key: value for key, value in cities.items() if isinstance(value, dict)}

for i in filtered_cities:
    city_list[filtered_cities[i]["name"]] = filtered_cities[i]["id"]
print(list(city_list)[3])
print(list(city_list.values())[3])




# INSERT BOX FOR TOWN SELECT
# MAYBE INSERT OPTION TO RAID FROM A DIFFERENT VILLAGE



# ------------------ BARBARIAN RAID ------------------
cookies_raid = {
    "__cf_bm": "PZYOcNoIs0A3Ft7lMR97l3yibfCaIrbmwRbzeA3mq8s-1717614694-1.0.1.1-cd5FFHG2qhSpxq3gIXUf3U9sKCWYCJ2gumGAgCt3w1OlNJIfkdXdsoLKv6P3cso5Yu.ixNpF8UafA1TqEO4frg",
    'pc_idt': 'AC67gghrk1kl5LQrIcThOf8zz0gzZxBpjSa99ruasa0RvqootnoI4EPrmdZARJdmOXNktqfpAs5N7SdRsXOXnz5NH8pqmpEXM7NvEoMhziFGOsmq7SGwnC7U0lbIOrC7UJQ9a6V74P4qrNRZV3AH8Ax2J27ZF4OEaY_fbA',
    'gf-token-production': 'f06b38c3-6b45-458f-b77d-cc509113be35',
    'gf_pz_token': '4e6a3543-4ae2-4409-b2cf-8bff08a785e5',
    'gf-cookie-consent-4449562312': '^|7^|1',
    'cf_clearance': 'Xsw1WBsEHfFlHpHfHQOooCLzNezVHnHnFl2veYr6C60-1714608274-1.0.1.1-M6HVJKruZDH4aS9pGoKJAQ0MtBRwXHXQ2xYoxv9PaBqchtGIyiaXPRkn1fvnXJ2oYva8Pk6.sKvk2OT02NLtWA',
    'PHPSESSID': '2bqshgi3584mnjuf6j18pbpug1',
    'ik_video_player': 'volume^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Bpath^%^3D/^%^3Bpath=/',
    'ik_friendslist_105499': 'page^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Dthis.length^%^3Bt--^%^3B^%^29if^%^28this^%^5Bt^%^5D^%^3D^%^3D^%^3De^%^29return^%^210^%^3Breturn^%^211^%^7D^%^3Bpath=/',
    'ikariam_loginMode': '0',
    'ikariam': '105499_f5e5187e8d1379c7d8584e52a4a3d73f',
}

headers_raid = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://s56-en.ikariam.gameforge.com',
    'Connection': 'keep-alive',
    'Referer': 'https://s56-en.ikariam.gameforge.com/?view=island&oldBackgroundView=island&containerWidth=2560px&containerHeight=739px&worldviewWidth=2560px&worldviewHeight=693px&islandTop=-473px&islandLeft=-1700px&islandRight=&islandWorldviewScale=0.95',
    'Cookie': 'pc_idt=AC67gghrk1kl5LQrIcThOf8zz0gzZxBpjSa99ruasa0RvqootnoI4EPrmdZARJdmOXNktqfpAs5N7SdRsXOXnz5NH8pqmpEXM7NvEoMhziFGOsmq7SGwnC7U0lbIOrC7UJQ9a6V74P4qrNRZV3AH8Ax2J27ZF4OEaY_fbA; gf-token-production=f06b38c3-6b45-458f-b77d-cc509113be35; gf_pz_token=4e6a3543-4ae2-4409-b2cf-8bff08a785e5; gf-cookie-consent-4449562312=^|7^|1; cf_clearance=Xsw1WBsEHfFlHpHfHQOooCLzNezVHnHnFl2veYr6C60-1714608274-1.0.1.1-M6HVJKruZDH4aS9pGoKJAQ0MtBRwXHXQ2xYoxv9PaBqchtGIyiaXPRkn1fvnXJ2oYva8Pk6.sKvk2OT02NLtWA; __cf_bm=pjVwQXsSBSFLpL9hVeGMJC96km1ykzgk8TOur.8kLPU-1717613637-1.0.1.1-YJo9VMf11tam94JClo3skism_ZYkwsyH_KQSOhKg9G1yy9G.c_RsGh5jsE5_OBic9DIJ3nA4ba4AATebRsHa3A; PHPSESSID=2bqshgi3584mnjuf6j18pbpug1; ik_video_player=volume^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Bpath^%^3D/^%^3Bpath=/; ik_friendslist_105499=page^%^3D0^%^3Bcontains^%^3Dfunction^%^28e^%^29^%^7Bfor^%^28var^%^20t^%^3Dthis.length^%^3Bt--^%^3B^%^29if^%^28this^%^5Bt^%^5D^%^3D^%^3D^%^3De^%^29return^%^210^%^3Breturn^%^211^%^7D^%^3Bpath=/; ikariam_loginMode=0; ikariam=105499_f5e5187e8d1379c7d8584e52a4a3d73f',
    "Host": "",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=1',
}

data_raid = {
    'action': 'transportOperations',
    'function': 'attackBarbarianVillage',
    'actionRequest': '9f21e0915129ddcb93c295509487139f',
    'islandId': '383',
    'destinationCityId': '0',
    "cargo_army_302_upkeep": "4",
    "cargo_army_302": "0",
    "cargo_army_303_upkeep": "3",
    "cargo_army_303": "30",
    "cargo_army_306_upkeep": "25",
    "cargo_army_306": "6",
    "cargo_army_311_upkeep": "20",
    "cargo_army_311": "0",
    "cargo_army_312_upkeep": "10",
    "cargo_army_312": "0",
    'transporter': '20',
    'barbarianVillage': '1',
    'backgroundView': 'island',
    'currentIslandId': '383',
    'templateView': 'plunder',
    'ajax': '1',
}

plunder = response = requests.post('https://s56-en.ikariam.gameforge.com/index.php', cookies=cookies, headers=headers, data=data_raid)

print(plunder.json())
# soup2 = BeautifulSoup(plunder[1][1][1], "html.parser")
# barbarian_level = soup2.find(id="js_islandBarbarianLevel")
# print(barbarian_level.text)






















