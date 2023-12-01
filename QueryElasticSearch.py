import requests
import json
import time
from parsingUtilities import utils

# these values do not change
url = "https://85c600ab5e094a41951e97ed9e5890ad.us-west1.gcp.cloud.es.io:9243/product/_search"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ZWxhc3RpYzpNc2xudmdxTXlkbmdweU5pSmN3Um42NmI='
}

utility = utils()
# read in file containing item #'s
itemNumbersTextFile = open('item_numbers.txt', 'r')
itemNumbers = itemNumbersTextFile.readlines()

productInfo = open("productInfo.csv", "w")
content = ""

#
# stats
missed = []
hit = []
total_time = 0
total = len(itemNumbers)

# try each item number
i = 0
for itemNumber in itemNumbers:
    itemNumber = itemNumber.strip()
    if itemNumber[0] == "#":
        content += "------------" + itemNumber + "------------\n"
        total -= 1
        continue
    t0 = time.time()
    payload = json.dumps({
        "query": {
            "term": {
                "product.itemNumber": {
                    "value": itemNumber
                }
            }
        }
    })
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    if (len(data["hits"]["hits"]) == 0):
        missed.append(itemNumber)
        content += "------------" + itemNumber + "------------\n"
        total_time += time.time() - t0
        continue
    else:
        hit.append(itemNumber)

    # get product info
    product = data["hits"]["hits"][0]["_source"]["product"]
    brand = product["brand"]
    name = product["description"]
    modelNumber = product["modelId"]
    # print(product)
    imagePath = "N/A"
    if('epc' in product):
        if( len(product['epc']["additionalImages"]) >  0):
            imagePath = product['epc']["additionalImages"][0]["baseUrl"]

    specs = "N/A"
    h = w = d =-1
    if ("specs" in product):
        specs = product["specs"]
        h,w,d = utility.parse_specs(specs)
    link = "www.lowes.com" + product["pdURL"]
    print("---------------------------------------------------------")
    print(product)
    print(brand)
    print(name)
    print(imagePath)
    print(link)
    print(specs)
    print(h,w,d)
    print("---------------------------------------------------------")


    content += "UID" + str(i) + "," + brand + "," + name + "," + itemNumber + "," + modelNumber+ "," + imagePath + "," + link + "," + str(h) + "," + str(w) + "," + str(d) +",etc\n"
    i += 1


    total_time += time.time() - t0


t0 = time.time()
productInfo.write(content)
total_time += time.time() - t0

misses = len(missed)
hits = len(hit)
accuracy = hits / total
print("Total number queried:", total)
print("Number of misses:", misses)
print("Number of hits:", hits)
print("Accuracy:", accuracy)
print("Total time:", total_time)
print("Average time:", total_time / total)
