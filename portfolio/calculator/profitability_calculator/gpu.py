from ethereum import Ethereum
from period import Period

POOL_FEE = 0.01  # placeholder


class GPU:
    efficiency: float  # mhs/w
    epp: float  # Efficiency Per Pound ((price / efficiency)*1000)
    mhs: float
    name: str
    power: int  # in Watts
    price: float
    roi: float  # return on investment in days
    day: Period
    week: Period
    month: Period
    year: Period

    def __init__(self, mhs: float, name: str, power: int, price: float, kwh_price_gbp: float):
        self.name = name
        self.mhs = mhs
        self.power = power
        self.price = price
        self.efficiency = self.mhs / self.power
        self.epp = (self.efficiency / self.price) * 1000
        eth = Ethereum.get_instance()
        gpu_ghs = mhs / 1000
        mine_chance = gpu_ghs / eth.net_hash_ghs  # probability to mine next block

        kwh_day = power * 24 / 1000
        power_cost_day = kwh_day * kwh_price_gbp
        blocks_mined_per_month = mine_chance * eth.blocks_per_month

        self.month = Period(blocks_mined_per_month, (power_cost_day * 30), POOL_FEE, 30)
        self.day = Period((blocks_mined_per_month / 30), power_cost_day, POOL_FEE, 1)
        self.week = Period((self.day.blocks_mined * 7), (power_cost_day * 7), POOL_FEE, 7)
        self.year = Period((self.day.blocks_mined * 365), (power_cost_day * 365), POOL_FEE, 365)

        self.roi = self.price / self.day.profit

    def print_info(self) -> None:
        print(f'Name = {self.name}')
        print(f'Power = {self.power} W')
        print(f'Mh/s = {self.mhs:.2f}')
        print(f'Price = {self.price:.2f} GBP')
        print(f'Efficiency = {self.efficiency:.2f} Mh/W')
        print(f'EPP = {self.epp:.4f}')
        print(f'ROI = {self.roi:.1f} days')
        print(f'Monthly revenue = {self.month.revenue:.2f} GBP')
        print(f'Monthly profit = {self.month.profit:.2f} GBP')
        print(f'Monthly pool fee = {self.month.pool_fee:.2f} GBP')
        print(f'Monthly power cost = {self.month.power_cost:.2f} GBP')


if __name__ == '__main__':
    gpu = GPU(mhs=63.20, name="AMD RX 6800 XT", power=104, price=1000.0, kwh_price_gbp=0.1437)
    gpu.print_info()
