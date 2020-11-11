from instapy import InstaPy
session = InstaPy(username="017_devs", password="fxmy8421")
session.login()




session.like_by_tags(["html", "code","java","python","javascript","css","webdev","kotlin"], amount=25)
session.set_relationship_bounds(enabled=True,delimit_by_numbers=True,max_following=500)
session.set_quota_supervisor(enabled=True,
                                    peak_comments_daily=250,
                                    peak_comments_hourly=25,
                                    peak_likes_daily=250,
                                    peak_likes_hourly=25,
                                 sleep_after=['likes', 'follows'])

session.set_do_comment(True,percentage=100)
session.set_comments(["Hi i have a account named @017_devs and i thought lets support each other by following each other ... hope you would agree  ","hi , i think we should support each others account by following each other "])

session.end()

'''

'''