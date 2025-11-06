from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.minsize(1200,1000)
root.title("news paper")

haddin = Label(text="Hindustan", font="cursiv 30 bold")
haddin.pack()

date = Label(text="21/08/2025", fg="white",font=" normal 20", bg="red",pady=10)
date.pack(side=LEFT ,anchor="ne" )
# usa news peragrsph  nkfbjfb fb f j j vfvbrsp fbvfb 
usa_image = Image.open("images/news.jpg")
usa_photo = ImageTk.PhotoImage(usa_image)
usa_label = Label(root, image=usa_photo)
usa_label.pack()
news_usa_label = Label(text="The U.S. Commerce Department has launched a national security probe into imported wind turbines and components. This follows the inclusion of wind turbines on a 50% tariff list under Section 232. The investigation, initiated on August 13, was made public only recently and may lead to even higher tariffs. Approximately two-thirds of a wind turbine's value is imported, with Europe leading exports, followed by Mexico and India" ,font="normal 10 ",wraplength=1000,justify=CENTER,)
news_usa_label.pack()
# criket news  fdmdk;mdknknfbfnbvfsbvfjlbfsjbfnsvjfnbfj  fvhfd fdbfdrbfngjfdbre fd bf 
criket_image = Image.open("images/criket.jpg")
criket_photo = ImageTk.PhotoImage(criket_image)
criket_label = Label(root, image=criket_photo)
criket_label.pack()

news_cri_label = Label(text='''Cricket is a bat-and-ball game that is played between two teams of eleven players on a field, at the centre of which is a 22-yard (20-metre; 66-foot) pitch with a wicket at each end, each comprising two bails (small sticks) balanced on three stumps. Two players from the batting team, the striker and nonstriker, stand in front of either wicket holding bats, while one player from the fielding team, the bowler, bowls the ball toward the striker's wicket from the opposite end of the pitch. The striker's goal is to hit the bowled ball with the bat and then switch places with the nonstriker, with the batting team scoring one run for each of these swaps. Runs are also scored when the ball reaches the boundary of the field or when the ball is bowled illegally.

The fielding team aims to prevent runs by dismissing batters (so they are "out"). Dismissal can occur in various ways, including being bowled (when the ball hits the striker's wicket and dislodges the bails), and by the fielding side either catching the ball after it is hit by the bat but before it hits the ground, or hitting a wicket with the ball before a batter can cross the crease line in front of the wicket. When ten batters have been dismissed, the innings (playing phase) ends and the teams swap roles. Forms of cricket range from traditional Test matches played over five days to the newer Twenty20 format (also known as T20), in which each team bats for a single innings of 20 overs (each "over" being a set of 6 fair opportunities for the batting team to score) and the game generally lasts three to four hours.''',font="normal 10 " ,wraplength=1000,justify=CENTER,)
# pickbleball news peragraph    fgf frnvnfjf ni4fehvloe9fvjwegvgtvmdmgt kevbrvd kfksdk 

pick_image = Image.open("images/pickleball.jpg")
pick_photo = ImageTk.PhotoImage(pick_image)
pick_label = Label(root, image=pick_photo)
pick_label.pack()

news_pick_label = Label(text='''Pickleball is a racket or paddle sport in which two or four players use a smooth-faced paddle to hit a perforated, hollow plastic ball over a 34-inch-high (0.86 m) net (until one side is not able to return the ball or commits a rule infraction). Pickleball is played indoors and outdoors. It was invented in 1965 as a children's backyard game in the United States, on Bainbridge Island in Washington State. In 2022, pickleball was named the official state sport of Washington.[1]

Aspects of the sport resemble tennis and table tennis played on a doubles badminton court, but pickleball has specific scoring rules, paddles, balls and court lines. On each side of the net is a 7-foot area (2.1 m) known as the non-volley zone (or kitchen); a player standing there may not strike the ball before it has bounced. The hard plastic pickleball produces less bounce than a tennis ball. The limited bounce, non-volley zones, and underhand stroke, with which all serves must be made, give the game a dynamic pace.[2] Slow soft shots in the non-volley zone, called dinks, are used to limit the opponent's ability to attack, while balls that are returned too high might be struck with a powerful drive or overhead smash shot.

After its introduction in 1965, pickleball became a popular sport in the Pacific Northwest and gradually grew in popularity elsewhere. For four years in a row, 2021 through 2024, the sport was named the fastest-growing sport in the United States by the Sports and Fitness Industry Association.[3] By 2024, it was estimated there were 19.8 million participants in the United States, a 311% growth since 2021.[4]

Two professional tours were established in the United States in 2019 and shortly thereafter two professional leagues were established. Pickleball is also growing in popularity outside the United States with two professional leagues and one professional tour operating in Australia, and others being developed in Asia. More than 90% of professional pickleball players have a background in tennis.[5]''',font="normal 10 ",wraplength=1000,justify=CENTER,)
news_pick_label.pack()

root.mainloop()