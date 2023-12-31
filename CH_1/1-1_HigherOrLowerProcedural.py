# Higher or lower

import random

suit_tuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
rank_tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

n_cards = 8
score = 50

def shuffle(desk_ls_in: list):
    desk_ls_out = desk_ls_in.copy()
    random.shuffle(desk_ls_out)
    return desk_ls_out

def get_card(desk_ls_in: list):
    my_card = desk_ls_in.pop()
    return my_card


if __name__ == '__main__':
    print('Welcome to Higher and lower')
    print('You have to choose whether the next card to be shown will be higher or lower then the current card')
    print('Getting the right adds 20 points; get it wrong and you lose 15 points.')
    print('You have 50 points to start')

    starting_desk_ls = []
    for suit in suit_tuple:
        for idx, value in enumerate(rank_tuple):
            card_dict = {'rank': value, 'suit': suit, 'value': idx + 1}
            starting_desk_ls.append(card_dict)

    while True:
        print()
        game_deck_ls = shuffle(starting_desk_ls)
        cur_card_dict = get_card(game_deck_ls)
        cur_card_rank = cur_card_dict['rank']
        cur_card_suit = cur_card_dict['suit']
        cur_card_value = cur_card_dict['value']
        print(f'Starting card is: {cur_card_rank} of {cur_card_suit}')
        print()

        for card_num in range(0, n_cards):
            print(f'Round {card_num + 1}')
            answer = input(f'Will the next card is higher or lower than the {cur_card_rank} of {cur_card_suit}?'
                           f'(enter h or l): ')
            answer = answer.casefold()
            next_card_dict = get_card(game_deck_ls)
            next_card_rank = next_card_dict['rank']
            next_card_suit = next_card_dict['suit']
            next_card_value = next_card_dict['value']
            print(f'Next card is {next_card_rank} of {next_card_suit}')

            if answer == 'h':
                if next_card_value > cur_card_value:
                    print('You got it right, it was higher')
                    score += 20
                else:
                    print('Sorry, it was not higher')
                    score -= 15
            elif answer == 'l':
                if next_card_value < cur_card_value:
                    print('You got it right, it was lower')
                    score += 20
                else:
                    print('Sorry, it was not higher')
                    score -= 15

            print(f'Your score is {score}.')
            print()
            cur_card_rank = next_card_rank
            cur_card_value = next_card_value

        go_again = input('To play again press Enter, or \'q\' to leave: ')
        go_again = go_again.casefold()
        if go_again == 'q':
            break
    print('Bye!')
