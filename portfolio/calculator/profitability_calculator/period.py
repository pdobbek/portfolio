from ethereum import Ethereum


class Period:
    """
    This class contains information regarding income and expenditure during a certain time period.
    """

    blocks_mined: float
    duration: int  # total duration of the period in days.
    expenditure_total: float  # total expenditure for this period (GBP).
    pool_fee: float  # GBP
    pool_fee_modifier: float  # pool_fee_modifier = 1.0 - pool_fee_percent
    pool_fee_percent: float
    power_cost: float  # cost of electricity for this period.
    profit: float
    revenue: float  # total income for this period (GBP).

    def __init__(self, blocks_mined: float, power_cost: float, pool_fee_percent: float, duration: int):
        eth = Ethereum.get_instance()
        self.blocks_mined = blocks_mined
        self.revenue = blocks_mined * eth.block_reward_gbp
        self.duration = duration
        self.pool_fee_percent = pool_fee_percent
        self.pool_fee_modifier = 1.0 - pool_fee_percent
        self.pool_fee = self.revenue * pool_fee_percent
        self.power_cost = power_cost
        self.expenditure_total = power_cost + self.pool_fee
        self.profit = self.revenue - self.expenditure_total
