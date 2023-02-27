import json

import requests

z = 0
i = 0
first_part = "https://blockchain.info/rawaddr/"
initial_input = input("please type the 'seed' address: ")
initial_req = first_part + initial_input

first_json = (requests.get(initial_req)).json()
graphviz_lines = []

address_list = []
used_address_list = []

address_list.append(initial_input)
used_address_list.append(initial_input)

while i < 6:
    if z == 1:
        initial_req = first_part + address_list[i]
        first_json = (requests.get(initial_req)).json()

    for transaction in first_json["txs"]:
        payer_list = []
        recipient_list = []

        print("\n" + transaction["hash"])

        for item in transaction["inputs"]:
            payer_list.append(item["prev_out"]["addr"])
            if item["prev_out"]["addr"] not in address_list:
                address_list.append(item["prev_out"]["addr"])

        for target in transaction["out"]:
            recipient_list.append(target["addr"])
            if target["addr"] not in address_list:
                address_list.append(target["addr"])

        for payer in payer_list:
            for recipient in recipient_list:
                a = '"' + payer + '"' + " -> " + '"' + recipient + '"' + ";"
                if a not in graphviz_lines:
                    graphviz_lines.append(a)
    i += 1
    z = 1


for t in graphviz_lines:
    print(t)
