def solve(alice_cards, bob_cards, first_player):
  
    alice_turn = first_player == "Alice"
    alice_cards.sort(reverse=True)
    bob_cards.sort(reverse=True)

    while alice_cards and bob_cards:
        if alice_turn:
            alice_card = alice_cards.pop(0)
            if alice_card > bob_cards[0]:
                bob_cards.pop(0)

            else:
                return "Bob"
            alice_turn = False
        else:
            bob_card = bob_cards.pop(0)
            if bob_card > alice_cards[0]:
                alice_cards.pop(0)
            else:
                return "Alice"
            alice_turn = True

    if alice_cards:
        return "Alice"
    else:
        return "Bob"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    winner_if_alice_first = solve(a, b,'Alice')
    winner_if_bob_first = solve(a,b,'Bob')

    print(winner_if_alice_first)
    print(winner_if_bob_first)