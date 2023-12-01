import requests
import json


# from JSON_CLASS import JsonData

url = "https://85c600ab5e094a41951e97ed9e5890ad.us-west1.gcp.cloud.es.io:9243/product/_search"

payload = json.dumps({
  "query": {
    "term": {
      "product.itemNumber": {
        "value":"5338249" #"4096438"
      }
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZWxhc3RpYzpNc2xudmdxTXlkbmdweU5pSmN3Um42NmI='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
test = json.loads(response.text)
print(test)

#
# UID,name,itemNumber,modelNumber,productImagePath,link,height,width,depth,etc
# testUID,testName,1234,abc,pic.png,https://www.lowes.com/pd/Miele-W1-front-loading-washing-machine-2-26-cu-ft-High-Efficiency-Stackable-Steam-Cycle-Front-Load-Washer-Lotus-White-ENERGY-STAR/5013768989,-1,-1,-1,NA
# UID2,name2,5678,xyz,image.jpg,link2,-1,-1,-1,NA
