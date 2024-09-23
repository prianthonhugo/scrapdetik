import requests

# json_data = requests.get('https://www.floatrates.com/daily/idr.json')
json_data = {"aud":{"code":"AUD","alphaCode":"AUD","numericCode":"036","name":"Australian Dollar","rate":9.7116624623443e-5,"date":"Fri, 20 Sep 2024 23:59:00 GMT","inverseRate":10296.898228057},
             "cad":{"code":"CAD","alphaCode":"CAD","numericCode":"124","name":"Canadian Dollar","rate":8.9747072607516e-5,"date":"Fri, 20 Sep 2024 23:59:00 GMT","inverseRate":11142.424715882},
             "cny":{"code":"CNY","alphaCode":"CNY","numericCode":"156","name":"Chinese Yuan","rate":0.00046653252223494,"date":"Fri, 20 Sep 2024 23:59:00 GMT","inverseRate":2143.4732892992},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.9265426003059e-5,"date":"Fri, 20 Sep 2024 23:59:00 GMT","inverseRate":16873.244106073}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])