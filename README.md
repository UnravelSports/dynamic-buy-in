## Fantasy Premier League Dynamic Buy-in Payout Calculator
This project helps to calculate FPL (or any similarly structured) competitions' payout structure when using a dynamic buy-in structure inspired by poker side-pot calculations.

A dynamic buy-in structure means each player plays for the total part of the prize pool that is covered by their buy-in. 

#### Example 0
If 8 players decide to play, 5 of which enter for 50$ and 3 enter for 200$. All 8 players will play for a 8*50$=400$ price pool, but the 3 players that entered for more will play for an additional 3*150$=450$ prize pool.

#### Important things to note:
- Each player plays for the total part of the prize pool that is covered by their buy-in. 
- The `src.config.payouts_in_money_group` function needs to be updated according to your own specifications. Currently, it's set to pay:
  - 50%, 30%, 20% for sub-groups with more than 12 players
  - 70%, 30% for sub-groups with more than or equal to 5 players
  - 100% for sub-groups with less than 5 players
- The `buy_ins` variable needs to be updated to include Player names or Player/Team IDs with their associated buy-in. It currently consists of dummy values.
- Current dummy calculations are done by setting the `numpy.seed()` and shuffling the buy_in dataframe to create an artificial rank inside `src.config.add_ranking`. This needs to be updated when the new FPL season gets under way.

#### Example 1 (seed = 42)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>rank</th>
      <th>player</th>
      <th>buy_in</th>
      <th>50.0_prize</th>
      <th>75.0_prize</th>
      <th>100.0_prize</th>
      <th>200.0_prize</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Player B</td>
      <td>50.0</td>
      <td>280.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>280.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Player F</td>
      <td>100.0</td>
      <td>120.0</td>
      <td>87.5</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>282.5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Player A</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Player H</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>37.5</td>
      <td>0.0</td>
      <td>200.0</td>
      <td>237.5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Player C</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Player E</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Player D</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Player G</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

#### Example 2 (seed = 36)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>rank</th>
      <th>player</th>
      <th>buy_in</th>
      <th>50.0_prize</th>
      <th>75.0_prize</th>
      <th>100.0_prize</th>
      <th>200.0_prize</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Player C</td>
      <td>50.0</td>
      <td>280.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>280.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Player F</td>
      <td>100.0</td>
      <td>120.0</td>
      <td>87.5</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>282.5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Player A</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Player D</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>37.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>37.5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Player G</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>200.0</td>
      <td>200.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Player H</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Player E</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Player B</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

#### Example 3 (seed = 35)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>rank</th>
      <th>player</th>
      <th>buy_in</th>
      <th>50.0_prize</th>
      <th>75.0_prize</th>
      <th>100.0_prize</th>
      <th>200.0_prize</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Player C</td>
      <td>50.0</td>
      <td>280.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>280.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Player F</td>
      <td>100.0</td>
      <td>120.0</td>
      <td>87.5</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>282.5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Player A</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Player D</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>37.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>37.5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Player G</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>200.0</td>
      <td>200.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Player H</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Player E</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Player B</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

#### Installation
`pip install -r requirements.txt`

