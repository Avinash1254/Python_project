import random
import time
import os

def spin_row():
    symbols = ['✨', '🎈', '🎁', '💎', '👑']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def animate_spin():
    symbols = ['✨', '🎈', '🎁', '💎', '👑']
    print("\n🎡 Spinning...", end="", flush=True)
    for _ in range(10):  # Number of animation frames
        row = [random.choice(symbols) for _ in range(3)]
        print("\r" + " | ".join(row), end="", flush=True)
        time.sleep(0.15)
    print()  # move to new line after animation

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '✨':
            return bet * 2
        elif row[0] == '🎈':
            return bet * 3
        elif row[0] == '🎁':
            return bet * 4
        elif row[0] == '💎':
            return bet * 10
        elif row[0] == '👑':
            return bet * 20
    return 0

def spin_and_payout(bet, is_bonus=False):
    """Perform one spin and return payout amount."""
    if is_bonus:
        print("\n🎁 Bonus Spin Activated! (Free Spin)")
    animate_spin()
    row = spin_row()
    print_row(row)
    payout = get_payout(row, bet)
    if payout > 0:
        print(f"🎉 You won ${payout}!")
    else:
        print("😞 Sorry, you lost this round.")
    return payout

def main():
    balance = 100
    print("🎰 Welcome to Slot Machine 🎰")
    print('=' * 30)
    print("Symbols: ✨  🎈  🎁  💎  👑")
    print('=' * 30)

    while balance > 0:
        print(f"\n💰 Current Balance: ${balance}")
        bet = input("Place your bet amount (or 'q' to quit): ")

        if bet.lower() == 'q':
            print("Thanks for playing! Goodbye 👋")
            break

        if not bet.isdigit():
            print(" Enter a valid number!")
            continue

        bet = int(bet)
        if bet > balance:
            print(" Insufficient balance!")
            continue
        if bet <= 0:
            print(" Bet must be greater than 0!")
            continue 

        balance -= bet
        payout = spin_and_payout(bet)
        balance += payout

        # 🎁 Bonus Spin if win
        while payout > 0:
            print(" You earned a FREE spin!")
            bonus_payout = spin_and_payout(bet, is_bonus=True)
            balance += bonus_payout
            if bonus_payout == 0:
                break
            payout = bonus_payout

    if balance <= 0:
        print("\n Game Over! You’re out of money!")

if __name__ == '__main__':
    main()
