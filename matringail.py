import random

AVG_GAMES_FOR_TEST_MONEY_BALANCE = 1000
GAMES_COUNT_STATS = 100
FUNDS_FOR_EACH_PLAYER = 100000
MIN_BET = 2000
MAX_BET = 200000
STOP_COUNT = 200000

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES)


def play_martingail(*, start_funds: int, min_bet: int, max_bet: int) -> int:
    step_to_loose = 0
    current_funds = start_funds
    current_bet = min_bet
    max_winner_funds = start_funds

    while current_funds > 0:
        # print("=========================")

        step_to_loose += 1
        current_funds -= current_bet

        if flip_coin() == HEADS:
            current_funds += current_bet * 2
            # print(f"WIN! Funds: {current_funds}, win bet: {current_bet}")
            current_bet = min_bet

            if current_funds > max_winner_funds:
                max_winner_funds = current_funds
                if max_winner_funds > STOP_COUNT:
                    return -1

        else:
            # print(f"LOOSE! Funds: {current_funds}, loose bet: {current_bet}")
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    # print(f"Max winner funds was {max_winner_funds}$")
    return step_to_loose


def average_bigdata_martingale_game_simulation(*, games_count: int, individual_funds: int, min_bet: int, max_bet: int) -> int:
    step_to_loose_avg = 0
    win_count = 0

    for i in range(games_count):
        current_step_to_loose = play_martingail(
            start_funds=individual_funds,
            min_bet=min_bet,
            max_bet=max_bet)
        if current_step_to_loose == -1:
            # print(f"Игрок условно выиграл удвоив свои деньги")
            win_count += 1

        # print(f"Player #{i}: steps to loose {current_step_to_loose}")

    return (win_count * FUNDS_FOR_EACH_PLAYER) - (FUNDS_FOR_EACH_PLAYER * (GAMES_COUNT_STATS - win_count))


total_balance = 0
for i in range(AVG_GAMES_FOR_TEST_MONEY_BALANCE):
    balance = average_bigdata_martingale_game_simulation(
        games_count=GAMES_COUNT_STATS,
        individual_funds=FUNDS_FOR_EACH_PLAYER,
        max_bet=MAX_BET,
        min_bet=MIN_BET)
    total_balance += balance
total_balance = total_balance // AVG_GAMES_FOR_TEST_MONEY_BALANCE


print(f"Average balance for {AVG_GAMES_FOR_TEST_MONEY_BALANCE} times of {
      GAMES_COUNT_STATS} players games is {total_balance} rubles")
