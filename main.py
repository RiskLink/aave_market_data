
import requests
import json
from utils import check_dir, create_csv


def get_aave_market_data():
    url = f"https://aave-api-v2.aave.com/data/markets-data"
    response = requests.get(url)
    data = response.json()
    return data


def get_all_asset_list_of_mainnet():
    url = f"https://aave.github.io/aave-addresses/mainnet.json"
    response = requests.get(url)
    data = response.json()
    all_list = list()
    all_list.extend(data['proto'])
    all_list.extend(data['amm'])
    return all_list


def main():

    csv_file_name = "ethereum_assets.csv"


    """
        read all assets list
    """

    f = open('mainnet.json')
    data = json.load(f)
    all_asset_dict = data

    all_asset_list = []

    all_asset_list.extend(all_asset_dict['proto'])
    all_asset_list.extend(all_asset_dict['amm'])


    # print(all_asset_list)


    """
        fetch all market data
    """
    data = get_aave_market_data()['reserves']
    
    # print(data)

    master_list =  list()

    for item in data:
        data_dict = dict()

        for item2 in all_asset_list:
            print(item2)
            if item2['address'].lower() == item['underlyingAsset'].lower():
                if len(item['id'].split("-")) ==1: 
                    data_dict['contract address'] = item['underlyingAsset']
                    data_dict['Symbol'] = item['symbol']
                    data_dict['Total Liquidity'] = item['totalLiquidityUSD']
                    data_dict['Total Borrows'] = item['totalBorrowsUSD']

                    master_list.append(data_dict)
                    break
        
    create_csv("CSV/{}".format(csv_file_name), master_list)
    print("\n***************** Script Ended *******************\n")


if __name__ == "__main__":
    check_dir("CSV")
    main()
