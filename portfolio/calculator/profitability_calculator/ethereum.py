import requests
from requests.exceptions import HTTPError


class Ethereum:
    __instance = None
    block_reward: float
    block_reward_gbp: float
    block_time: float
    blocks_per_month: float
    net_hash: float
    net_hash_khs: float
    net_hash_mhs: float
    net_hash_ghs: float
    price: float

    def __init__(self):
        if Ethereum.__instance is None:
            Ethereum.__instance = self

            with open("api.bin", encoding="utf-8") as binary_file:
                api_key = binary_file.read()
            request_str = "https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms=ETH&tsyms=GBP"
            response = requests.get("%s&api_key{%s}" % (request_str, api_key))
            try:
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Unknown error occurred: {err}')
            else:
                print('API call successful.')

            data = response.json()['Data']['ETH']
            self.price = data['Price']['GBP']
            self.block_time = data['CoinInfo']['BlockTime']
            self.net_hash = data['CoinInfo']['NetHashesPerSecond']
            self.net_hash_khs = self.net_hash / 1000
            self.net_hash_mhs = self.net_hash_khs / 1000
            self.net_hash_ghs = self.net_hash_mhs / 1000
            self.block_reward = data['CoinInfo']['BlockReward']
            self.block_reward_gbp = self.block_reward * self.price
            seconds_in_month = 2628288.0  # number of seconds in an average month
            self.blocks_per_month = seconds_in_month / self.block_time

    @staticmethod
    def get_instance():
        """Static method to get the current instance of the class."""
        if not Ethereum.__instance:
            Ethereum()
        return Ethereum.__instance
