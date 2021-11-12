import instaloader
account=input("Enter instagram account name copy/paste:")

instaloader.Instaloader().download_profile(account,profile_pic_only=False)
