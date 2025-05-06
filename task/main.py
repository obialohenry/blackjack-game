from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# continue_playing = True

def check_for_ace_in_list(item:list):
    for item_object in item:
        if item_object == 11:
            ace_index = item.index(item_object)
            if sum(item) > 21:
                item[ace_index] = 1

def stand(dealers_cards:list,my_cards:list)->bool:

    check_for_ace_in_list(dealers_cards)
    check_for_ace_in_list(my_cards)

    while sum(dealers_cards) < 17:
        random.shuffle(cards)
        dealers_cards.append(random.choice(cards))
        check_for_ace_in_list(dealers_cards)

    a_players_total_cards = sum(my_cards)
    dealers_total_cards = sum(dealers_cards)
    print(f"Your final hand: {my_cards}, final score: {a_players_total_cards}")
    print(f"Computer's final hand: {dealers_cards},final score: {dealers_total_cards}")
    if a_players_total_cards > 21:
        print("You went over. You lose 😭")
    elif dealers_total_cards > 21:
        print('Opponent went over. You win 😁')
    else:
        if a_players_total_cards > dealers_total_cards:
            if a_players_total_cards == 21:
                print("Win, you have Blackjack 😱")
            else:
                print("You win 😁")
        elif a_players_total_cards == dealers_total_cards:
            print("Draw 🙃")
        else:
            if dealers_total_cards == 21:
                print("Lose, opponent has Blackjack 😱")
            else:
                print("You lose 😤")

    return False


def hit(my_cards:list,dealers_cards:list)-> bool:

    random.shuffle(cards)
    my_cards.append(random.choice(cards))

    check_for_ace_in_list(my_cards)
    players_total_cards = sum(my_cards)

    if players_total_cards > 21:
        print(f"Your final hand: {my_cards}, final score: {players_total_cards}")
        print(f"Computer's final hand: {dealers_cards},final score: {sum(dealers_cards)}")
        print("You went over. You lose 😭")
        return False


    print(f'Your cards: {my_cards}, current score: {players_total_cards}')
    print(f"Computer's first card: {dealers_cards[1]}")
    return True

def black_jack():
    my_cards = []
    dealers_cards = []
    random.shuffle(cards)
    for index in range(0, 2):
        my_cards.append(random.choice(cards))
        dealers_cards.append(random.choice(cards))

    print(f"Your cards: {my_cards}")
    print(f"Computer's first card: {dealers_cards[1]}")
    hit_again = True
    while hit_again:
        player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if player_choice == 'y':
           hit_again =  hit(my_cards=my_cards, dealers_cards=dealers_cards)
        else:
            hit_again = stand( dealers_cards=dealers_cards, my_cards=my_cards)
            # print(f"hit again status after standing: {hit_again}")



play_again = True
while play_again:
    choice_of_playing_blackjack = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if choice_of_playing_blackjack == 'y':
        print("\n" * 20)
        print(logo)
        black_jack()
    else:
        play_again = False





















