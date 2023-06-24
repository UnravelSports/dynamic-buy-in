from src.config import *
from src.pay_outs import *

# some dummy buy-in values
buy_ins = {
    "Player A": 50.00,
    "Player B": 50.00,
    "Player C": 50.00,
    "Player D": 75.00,
    "Player E": 75.00,
    "Player F": 100.00,
    "Player G": 200.00,
    "Player H": 200.00,
}


if __name__ == '__main__':
    df = buy_in_dataframe(buy_ins)
    standings = add_ranking(df)

    final = compute_payouts(standings=standings)
    print(final.to_html(index=False))





