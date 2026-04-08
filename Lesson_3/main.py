import requests
from colorama import Fore, Back, Style, init
import time
# GH_BRANCH = "pixelrun%2Bserver"
# GH_REPO = "MishaPetrovskui/SFML_MainPlatformer"
# GH_API = f"https://api.github.com/repos/{GH_REPO}/commits?sha={GH_BRANCH}&per_page=1"

# GH_API, { headers: { Accept: "application/vnd.github.v3+json" } }

init(autoreset=True)


repositoryAuthor = input("Author: ") 
repository = input("Repository: ") 

GH_API = f"https://api.github.com/repos/{repositoryAuthor}/{repository}/commits?per_page=1"

response = requests.get(GH_API, headers={ "Accept": "application/vnd.github.v3+json" })



if response.status_code == 200:
    data = response.json()
    lastcommit = data[0]["node_id"]
    print(lastcommit)
    while (True):
        time.sleep(5)
        resp = requests.get(GH_API, headers={ "Accept": "application/vnd.github.v3+json" })
        if resp.status_code == 200:
            if lastcommit != resp.json()[0]["node_id"]:
                print(Fore.RED + "NEW COMMIT!")
                print(resp.json()[0]["node_id"])
                lastcommit = resp.json()[0]["node_id"]
            else:
                print("Nothing was happend!")
else:
    print(response.status_code)



# v 0.1.3

# url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/"
# rate = ""

# first = input("First currency: ")

# response = requests.get(url + first + ".json")

# if response.status_code == 200:
#     data = response.json()
#     rate = data[first]
#     # print(data[first])
#     second = input("Second currency: ")
#     finallRate = rate[second]
#     count = int(input("Count: "))
#     print(Fore.GREEN + str((count * finallRate)))
#     print("information for " + data["date"])
# else:
#     print(response.status_code)



# docker build . -t my-hello-world:0.0.1
# docker run -it my-hello-world
# pip freeze > requirements.txt