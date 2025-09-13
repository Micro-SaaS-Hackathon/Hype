from google import genai
import json
from utils import parse

from decouple import config

api_key = config("API_KEY")
reserve_api_token = config("RESERVE_API_KEY")

client = genai.Client(api_key=api_key)

def analyse(category, sahe, torpaq, qiymet, iqlim):
    
    data_path = f"static/datas/json_datas/{category}.json"
    
    with open(data_path, "r", encoding="utf-8") as d:
        data = json.load(d)

    with open("utils/prompt.txt", "r", encoding="utf-8") as p:
        prompt = p.read()
        
        if category != "et_ve_et_mehsul" and category != "qoyun_keci":
            final_prompt = prompt.format(
                product_name=category,
                data=json.dumps(data, ensure_ascii=False, indent=4),
                total_area=sahe,
                soil_type=torpaq,
                average_price=qiymet,
                climate_class=iqlim
            )
        else:
            final_prompt = prompt.format(
                product_name=category,
                data=json.dumps(data, ensure_ascii=False, indent=4),
                total_area=sahe,
                soil_type=torpaq,
                average_price=qiymet,
                climate_class=iqlim
            )

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=final_prompt
    )

    with open("utils/ai_answers.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

    parse.parse()
    return response.text
