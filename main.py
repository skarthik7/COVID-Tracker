from urllib.request import urlopen

def country_summary():
    html = urlopen("https://api.covid19api.com/summary")
    data = html.read()
    data_as_dict = eval(data.decode("UTF-8"))
    x=[]
    input_country = input("Country: ")
    for countries in data_as_dict["Countries"]:
        if countries['Country'] == input_country:
            for info in countries:
                country_data = info,countries[info]
                x.append(country_data)
    return x[4:11]

def main():
    option = 1
    while option == 1:
        result = country_summary()
        for data in result:
            print("{}:".format(data[0]),data[1])

main()