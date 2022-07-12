from requests.models import PreparedRequest
import requests.exceptions
import pytube
import os

# validate userUrl


def validateUrl(url):
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except requests.exceptions.MissingSchema:
        print("Invalid url. \n")


def menu():
    print("Select 1 for Video Only.")
    print("Select 2 for Audio Only.")
    print("Select 3 for Video and Audio.\n")

# download audio


def audioOnly(userUrl, saveLocation):
    if validateUrl(userUrl):
        audio = pytube.YouTube(userUrl).streams.get_audio_only().download(
            saveLocation)
        base, ext = os.path.splitext(audio)
        # rename file stripping the file extension and replacing it with mp3
        newAudio = base + '.mp3'
        os.rename(audio, newAudio)
        print("Done...\n")

    else:
        validate = input("Try again: ")
        audioOnly(validate, saveLocation)

# download video


def videoOnly(userUrl, saveLocation):
    if validateUrl(userUrl):
        pytube.YouTube(userUrl).streams.get_highest_resolution().download(
            saveLocation)
        print("Done...")

    else:
        validate = input("Try again: ")
        videoOnly(validate, saveLocation)

# download audio  and video


def audioAndVideo(userUrl, saveLocation):
    if validateUrl(userUrl):
        audioOnly(userUrl, saveLocation)
        pytube.YouTube(userUrl).streams.get_highest_resolution().download(
            saveLocation)

    else:
        validate = input("Try again: ")
        audioAndVideo(validate, saveLocation)


menu()

userInput = int(input("Choose an option: "))
saveLocation = "C:"


while True:

    if userInput == 1:
        url = input("Paste Link of the Video: ")
        videoOnly(url, saveLocation)

    elif userInput == 2:
        url = input("Paste Link of the Video: ")
        audioOnly(url, saveLocation)

    elif userInput == 3:
        url = input("Paste Link of the Video: ")
        audioAndVideo(url, saveLocation)

    else:
        userInput = int(input("Invalid option. Try again: "))


# validateUrl("https://youtu.be/MEg-oqI9qmw")
