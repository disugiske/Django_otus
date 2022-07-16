import json
from datetime import datetime
from requests_html import HTMLSession

import requests

key = "MjkyYjUzY2YtMDZiZS00MzA2LWEzMGEtYWVjYTRjMzIxZmUw"
keynew = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjUzZDY5MDBjLWNmNzQtNDU3MC1iNGZiLTc2YzMyYWE4YjNkOSJ9.o7UViGGjUnaz3VJy5rlWFbOYNggJNvZ1RT3biLHl_Bs"
key32 = "292b53cf-06be-4306-a30a-aeca4c321fe0"
flag = "1"
date = datetime.now().date()
URL_ORDERS = f"https://suppliers-stats.wildberries.ru/api/v1/supplier/orders?dateFrom={date}&flag={flag}&key={key}"
URL_PAYTABLE = f"https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod?dateFrom=2022-07-01&dateTo={date}&rrdid = 3&key={key}&limit=1000"
URL_STOCKS = f"https://suppliers-stats.wildberries.ru/api/v1/supplier/stocks?dateFrom={date}T00:00:00&key={key}"
URL_ADS = "https://seller.wildberries.ru/ns/campaigns-api/ads/api/v2/search/2117299/placement"
URL_ADS_S = "https://brand-suggestions.wildberries.ru/api/v1/redirect?query=%D1%83%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D0%B0%D1%8F%20%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0"

URL_PLACE = "https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-1282181,-455528&emp=0&lang=ru&locale=ru&pricemarginCoeff=1.0&query=%D1%83%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D0%B0%D1%8F%20%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0&reg=1&regions=68,64,83,4,38,80,33,70,82,86,75,30,69,22,66,31,40,1,48,71&resultset=catalog&sort=popular&spp=17"


def orders():
    orders = requests.get(URL_ORDERS).json()
    dayprise = 0
    for i in orders:
        price = i.get('totalPrice') * (1 - (i.get('discountPercent') / 100))
        print(i.get('date'), i.get('supplierArticle'), i.get('oblast'), price)
        dayprise += price
    print("Сумма заказов за день:", "{:0.1f}".format(dayprise))
    print("Количество заказов за день: ", len(orders))


def paytable():
    data_table = requests.get(URL_PAYTABLE).json()
    for i in data_table:
        date = i.get('order_dt')
        if date[:10] == "2022-07-13":
            print(i.get('sa_name'), i.get('delivery_rub'), i.get('ppvz_for_pay'))


def stocks():
    orders = requests.get(URL_STOCKS).json()
    for i in orders:
        if i.get('quantity') > 0:
            print(i.get('subject'), i.get('quantity'), i.get('supplierArticle'), i.get('lastChangeDate'))


cookie = {
    #"___wbu": "36633f25-61fd-489b-a162-1d941aad319e.1611951648",
    #"_ga": "GA1.2.388453110.1611951600", "_ga_TW9NLWX9V5": "GS1.1.1620811086.77.0.1620811086.60",
    "locale": "ru",
    "_wbauid": "202414401643488243",
    #"_wbauid": "6406108211643733111",
    #"WILDAUTHNEW_V3": "429E6BE3819A5E8AB8F467F3293E1A37F5F0BBFE6D5085DBDA191F270F17EF7840ED38EC9B62E27C480C5066C15F70CD3E0495C2979A6DB143326AB0218676F6ADFA8EC272981D4AEC63C2E64BC9F45E0B7992A94BCC5FF287D33D13C333CE16FDDDFDDF82FAD900136197FE571A104952A64C3DBD836031052BAD75F04B78782305BB8AC716068BBD5887D8B1EAF0B20C24D3F847C423C879EFC8C5EA8EA7CA507A1465B599C024CF4F5EDF17FA89E4C498DD381B1A4424D36006D12C8A987FDD7EE7A84D52BF9A99BA2594BDC2F4D4420C1CE06BE405F357B4651CAF98BA7943EE415F169279A0A1F8AA9244542906CCF09E8606825D1AAF08615D096A017904BBEC902E438DC80A93466172B8A6EDB01D7FFA881DF78249CDEDD9D3201B2B51E6CE2CA926DCE42C6BA95438B7C8BDF99ECDB7B3F8D01D136A88733B675EBE5966BCF5",
    #"_gcl_au": "1.1.74191512.1653477157",
    #"BasketUID": "f3b2dce5-8466-4706-b660-512d039ba057",
    #"_hjSessionUser_1972003": "eyJpZCI6IjZhNWYyZjQyLWQ5ZjYtNWNjOC1hYjliLTgyMzQ1ZTYwMWY0MSIsImNyZWF0ZWQiOjE2NTcyOTMxMDkxMzEsImV4aXN0aW5nIjpmYWxzZX0=",
    "x-supplier-id": "5a7818f9-b504-5e4b-83cb-64c9b5307741",
    #"__bsa": "basket-ru-17",
    "WBToken": "AqX4wgmg-YOtDKC17a0MQuiUy_q1yLTQMA3Rt_KH87vibAZG6f-pW4W2fXnIsOZcM5NyRdbt7wJh7BjsjLoiENDjVdq3Y9wezB53oyIn0MK_ww",
    #"__wbl": "cityId=0&regionId=0&&phone=84957755505&latitude=55,638848&longitude=37,669395&src=1",
    #"__pricemargin": "1.0--",
    #"__cpns": "12_3_18_15_21",
    #"__sppfix": "",
    #"__dst": "-1029256_-102269_-1282181_-455528",
    #"__tm": "1657841833",
    #"___wbs": "8555fd9a-3945-4a26-b2bd-36d2c0100745.1657831033",
    #"um": "uid=w7TDssOkw7PCu8KwwrjCuMK2wrDCsMKxwrg%3d:proc=100:ehash=c24f5e7547846d270bb330d5c50bc831",
    #"_gid": "GA1.2.605694486.1657831025",
}


def ads():
    ads = requests.get(URL_ADS, cookies=cookie).json()
    #ads.encoding = 'utf-8'
    print(ads)
def ads2():
    headers = {
        'authority': 'static.wbstatic.net',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=%D1%81%D1%83%D0%BC%D0%BA%D0%B0+%D0%BF%D0%BE%D1%8F%D1%81%D0%BD%D0%B0%D1%8F',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    ads = requests.get('https://static.wbstatic.net/j/spa/modules/catalog/advGoods.min.js?785027beb0d731a0',
                            headers=headers)
    #ads = requests.get(URL_ADS_S2)
    #ads.encoding = 'utf-8'
    print(ads.text)
def place():
    count = 0
    place = requests.get(URL_PLACE).json()
    #print(json.dumps(ads_s, sort_keys = True, indent=2))
    #pprint(place, sort_dicts=True, indent=1)
    data=place['data']
    for i in data['products']:
        count = count+1
        print(f'Место: {count}, Бренд:{i.get("brand")}, Цена: {i.get("salePriceU")//100}')

def asd_price():
    URL_ADS_PRICE = "https://catalog-ads.wildberries.ru/api/v5/search?keyword=%d1%83%d0%bf%d0%b0%d0%ba%d0%be%d0%b2%d0%be%d1%87%d0%bd%d0%b0%d1%8f%20%d0%b1%d1%83%d0%bc%d0%b0%d0%b3%d0%b0"
    count = 1

    page = 0
    ads_data = requests.get(URL_ADS_PRICE).json()
    print(json.dumps(ads_data, sort_keys = True, indent=2))
    #pprint(place, sort_dicts=True, indent=1)
    data=ads_data['adverts']
    positions = ads_data['pages'][page]['positions']
    print(positions)
    print(len(data))
    for i in positions:
        if i <= len(data):
            print(f'Страница: {1}, Место: {count}, Цена позиции :{data[i-1].get("cpm")}, Артикул: {data[i-1].get("id")} ')
            count += 1
        else:
            print(f'Страница: {1}, Место: {count}, Цена позиции :{data[5].get("cpm")}, Артикул: {data[5].get("id")} ')
            count += 1


def pars():
    URL_PARS = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=%D1%83%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0'
    session = HTMLSession()
    r = session.get(URL_PARS)
    r.html.render()
    print(r.html.find('product-card j-card-item j-advert-card-item advert-card-item j-good-for-listing-event'))
if __name__ == "__main__":
    # stocks()
    #place2()
    #asd_price()
    ads2()
    #pars()
    # paytable()eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjUzZDY5MDBjLWNmNzQtNDU3MC1iNGZiLTc2YzMyYWE4YjNkOSJ9.o7UViGGjUnaz3VJy5rlWFbOYNggJNvZ1RT3biLHl_Bs
