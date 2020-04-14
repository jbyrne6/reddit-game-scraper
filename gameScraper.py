import sys
# REDDIT API
import praw
# import config
from praw.models import MoreComments
# DATA ANALYSIS
from pandas import DataFrame, read_csv
import pandas as pd
import matplotlib.pyplot as plt
# FUZZY STRING MATCHING
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

reddit = praw.Reddit(client_id='AkouZpPAAAtCSg',
                     client_secret='7Y-aZI9Ragv226fePd4LtXxgPjw',
                     user_agent='Game Ranker by /u/lazy_puggle',
                     username='lazy_puggle',
                     password='Kellogs75')

gameSystem = sys.argv[1]
commentString = ''
gameList = []
mentionList = []
fullCommentList = []
sumbissionNumber = 0
searchTerm = 'best ' + gameSystem.lower().replace(' ', '') + ' games'
# print(searchTerm)
if (len(sys.argv)) == 3:
    postLimit = int(sys.argv[2])
else:
    postLimit = 5

# print("Game System: " + gameSystem)
# print("Post Limit: " + str(postLimit))

for submission in reddit.subreddit('all').search(searchTerm, limit=postLimit):
    sumbissionNumber += 1
    print("{:.2%}".format(sumbissionNumber/postLimit))

    comments = submission.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        commentString += comment.body
        # fullCommentList.append(comment.body.lower())
commentString = commentString.lower()

# WRITE COMMENT DATA TO A TEXT FILE
# text_file = open("CommentInfo.txt", "w")
# text_file.write(commentString)
# text_file.close()

# MAIN PART OF FINDING PARTIAL RATIO FOR ALL COMMENTS TO GAMES
# commentCounter = 0
# df1 = pd.DataFrame(data = gameTextList, columns=['Games'])
# for comment in fullCommentList:
#     commentCounter += 1
#     partialRatioList = []
#     for game in gameTextList:
#         partialRatioList.append(fuzz.partial_ratio(game.rstrip().lower(), comment))  # noqa: E501
#     df1["Comment Ratio " + str(commentCounter)] = partialRatioList
# df1["Sum"] = df1.sum(axis=1)
# df1 = df1.sort_values('Sum', ascending=False)
# df1.to_csv('partialRatioData.csv',index=False,header=False)

# print("\n")
# gameRatingList = []
if gameSystem == "3ds":
    gameSystem = "threeDs"
gameTextList = open("GameLists\\" + gameSystem.lower() + "GameList.txt").readlines()  # noqa: E501

for game in gameTextList:
    game = game.rstrip().lower()

    # ARANGE BY RATING AFTER SUBSTRING SEARCH FOR OCCURANCES
    # gameRating = 0
    # gameStart = game.replace("the", "")[:4]
    # startIndex = 0
    # while startIndex != -1:
    #     startIndex = commentString.find(gameStart, startIndex+1)
    #     chunk = commentString[(startIndex-2):(startIndex+20)]
    #     gameRating += fuzz.ratio(game, chunk)
    # gameRatingList.append(gameRating)
    # gameList.append(game)

    if game in commentString:
        gameList.append(game)
        mentionList.append(commentString.count(game))

    # TRYING TO EXPAND SEARCH TERM
    # nameFlag = "false"
    # mentionCount = 0
    # if game in commentString:
    #     nameFlag = "true"
    #     mentionCount += commentString.count(game)
    # if game.replace(":", "") in commentString:
    #     nameFlag = "true"
    #     mentionCount += commentString.count(game)
    # if nameFlag == "true":
    #     gameList.append(game)


resultList = list(zip(gameList, mentionList))
# resultList = list(zip(gameList,gameRatingList))
# for result in resultList:
#     print(result)

df = pd.DataFrame(data=resultList, columns=['Games', 'Mentions'])
df = df.sort_values('Mentions', ascending=False)
df.to_csv('GameOrders\\' + gameSystem + 'GameOrder.csv', index=False, header=False)  # noqa: E501
