auction_dict={}

while True:
    name=input("what is your name?: ")
    bid=int(input("What is your bid?: $ "))
    
    auction_dict[name]=bid
    continue_input=input("Do you have any other bidders ? Yes or no: ")
    if(continue_input=="no"):
        break

highest_bidder = max(auction_dict, key=auction_dict.get)  # Get the key (name) with the highest value (bid)
highest_bid = auction_dict[highest_bidder]  # Get the highest bid
print(f"The highest bidder is {highest_bidder} with a bid of {highest_bid}.")