import pytube

url = input("Enter video url: ")

path = "D:"

pytube.YouTube(url).streams.get_highest_resolution().download(path)

print("\n\tSucessfully!")
print("\nPlease access disc D to check the downloaded file!\n")