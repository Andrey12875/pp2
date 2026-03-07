    #Extract all prices from the receipt
    #Find all product names
    #Calculate total amount
    #Extract date and time information
    #Find payment method
    #Create a structured output (JSON or formatted text)
import re
import json
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

products = re.findall(r"\d+\.\n+([^\n]+)",text)
prices = re.findall(r"[Сс]тоимость\n+([^\n]+)",text)
date_time = re.findall(r"[Вв]ремя:\s*([^\n]+)",text)
sum = re.findall(r"[Ии][Тт][Оо][Гг][Оо]:\s*([^\n]+)",text)
payment = re.findall(r"(.+[кК]арта|[Нн]аличные|[кК]арта.+)", text)
result = {"product_names":products,
          "product_prices":prices,
          "date_time":date_time,
          "sum":sum[0],
          "payment":payment[0]}

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
