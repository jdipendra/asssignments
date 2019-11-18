
#this program will decides whether your friend can have party or not on the basis of money he have in his/her wallet
import sys
money_with_friend = input("Me           :How much money do you have in your wallet my friend?\nMy friend    :I have Rs.")
if int(money_with_friend) > 50:
    print("Me           :Congratulations!!! With Rs.", money_with_friend, ", you have party now.")
else:
    print("Me           :Sorry myan! You can't have party with Rs.", money_with_friend)
sys.exit("\n\nIt was just a computer program.\n**********PROGRAM EXITING**********")