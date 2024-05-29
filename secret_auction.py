from replit import clear 
from auction_art import logo

def highestbidder(bids):
  hbid = 0
  hbidder = ""
  for i in bids:
    if bids[i] > hbid:
      hbid = bids[i]
      hbidder = i 
  print(f"\nHighest Bidder : {repr(hbidder)} ----> Bid Amount : {repr(hbid)}")

bidder = 0
bids = {}
gameon = True

while gameon:
  clear()
  print(logo)
  bidder+=1
  print(f'----> Bidder {bidder} ')
  name = input("Enter Name : ")
  price = int(input("Enter bid amount : $"))
  bids[name] = price 
  choice = input('Is there another bidder ? Y or N : ').upper()
  if choice == 'N':
    clear()
    print(logo)
    print("BIDDING HISTORY")
    count = 0
    for i in bids:
      count+=1
      print(f"{count}. --  {i}  --  {bids[i]}   ")
    highestbidder(bids)
    break


