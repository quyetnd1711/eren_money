import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def gold(request):
    page_url = "https://sjc.com.vn/giavang/textContent.php"
    page = requests.get(page_url)
    beautifulSoup = BeautifulSoup(page.content, 'html.parser')
    # Cập nhập lúc
    date_update = beautifulSoup.find_all(class_='w350 m5l float_left red_text bg_white')[0].text
    # Giá vàng
    data_gold = []
    n = 0
    for _ in range(len(beautifulSoup.find_all(class_="br bb ylo2_text p12")) - 1):
        row = beautifulSoup.table.find_all("tr")[n + 1]
        type_gold = row.find_all("td")[0].text
        buy = row.find_all("td")[1].text
        sale = row.find_all("td")[2].text
        if "0.5 chỉ" in type_gold:
            type_gold = type_gold[:38]
        data = {
            "type": type_gold,
            "buy": buy,
            "sale": sale
        }
        data_gold.append(data)
        n += 1
    content = {
        "date_update": date_update,
        "data_gold": data_gold
    }
    return render(request, "gold/gold.html", content)
