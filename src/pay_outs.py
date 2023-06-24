import pandas as pd

from src.config import *


def payouts_in_money_group(group_rank, players_in_money_group):
    if players_in_money_group >= 13:
        pay_pct = {1: 0.5, 2: 0.3, 3: 0.2}
    elif players_in_money_group >= 5:
        pay_pct = {1: 0.70, 2: 0.30}
    else:
        pay_pct = {1: 1.0}

    return pay_pct.get(group_rank, 0)


def buy_in_dataframe(buy_ins: dict) -> pd.DataFrame:
    df = pd.Series(buy_ins).to_frame().reset_index()
    df.columns = ['player', 'buy_in']
    df.sort_values(by='buy_in', inplace=True)
    return df


def add_ranking(df: pd.DataFrame) -> pd.DataFrame:
    # artificially create a rank
    rank = df.sample(frac=1).reset_index(drop=True).reset_index()
    rank['rank'] = rank['index'] + 1
    del rank['index']
    return rank


def compute_payouts(standings: pd.DataFrame) -> pd.DataFrame:
    sz = standings.groupby('buy_in').size().reset_index().rename(columns={0: 'count'})
    sz['players_in_money_group'] = sz['count'][::-1].cumsum()[::-1]
    sz['additional_price_money'] = sz['buy_in'] - sz['buy_in'].shift().fillna(0)

    rank = pd.merge(standings, sz, on=['buy_in'], how='left')

    columns = list()

    # some quick and dirty calculation to find the prize pool per sub-group
    for i, row in sz.iterrows():
        buy_in = row['buy_in']
        rank[buy_in] = np.where(rank['buy_in'] >= buy_in, 1, 0)
        rank[f"{buy_in}_size"] = rank[buy_in].sum()
        rank[f"{buy_in}_pool"] = rank[f"{buy_in}_size"] * sz[sz['buy_in'] == buy_in]['additional_price_money'].iloc[0]
        rank[f"{buy_in}_rank"] = rank[buy_in].cumsum()
        rank[f"{buy_in}_rank"] = np.where(rank[buy_in] == 0, 0, rank[f"{buy_in}_rank"])

        # include money group rank
        rank[f"{buy_in}_pay_pct"] = rank.apply(lambda x: payouts_in_money_group(
            group_rank=x[f"{buy_in}_rank"],
            players_in_money_group=x[f"{buy_in}_size"]
        ), axis=1)

        rank[f'{buy_in}_prize'] = rank[f"{buy_in}_pay_pct"] * rank[f"{buy_in}_pool"]
        columns.extend([f'{buy_in}_prize'])

    final = rank[['rank', 'player', 'buy_in'] + columns]
    final['total'] = final[columns].sum(axis=1)
    return final
