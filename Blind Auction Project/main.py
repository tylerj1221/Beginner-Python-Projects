import art
print(art.logo)

bidding = True
bidders = {}

def highest_bidder(end_bidders):
    highest_bidder_name = ""
    highest_bidder_bid = 0

    for bidder in end_bidders:
        if end_bidders[bidder] > highest_bidder_bid:
            highest_bidder_name = bidder
            highest_bidder_bid = end_bidders[bidder]

    print(f"The highest bidder was {highest_bidder_name} with £{highest_bidder_bid}")

while bidding:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    bidders[name] = bid

    if input("Are there any other bidders?\n") == "yes":
        print("\n" * 30)
        bidding = True
    else:
        bidding = False
        highest_bidder(bidders)