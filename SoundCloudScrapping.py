"""
//Created on Tue Aug 20 04:10:12 PM 2019

// satyadeep singh
"""
from selenium import webdriver
import requests
import bs4
import os

# New, top, mix, track & artists URL
top_url = "https://soundcloud.com/charts/top"
new_url = "https://soundcloud.com/charts/new"
track_url = "https://soundcloud.com/search/sounds?q="
artist_url = "https://soundcloud.com/search/people?q="
mix_url_end = "&filter.duration=epic"


def main_menu(browser):
    print('\n\n || Welcome to SoundCloud || \n\n')
    print()

    while True:
        print("\n\n*** Menu ***\n\n")
        print("1. Search for a track")
        print("2. Search for an artist")
        print("3. Search for a mix")
        print("4. Top Charts")
        print("5. New & Hot Charts")
        print("0. Exit")
        print()

        choice = int(input("Your Choice: "))

        if choice == 0:
            browser.quit()
            break
        print()

        # Search for a track
        if choice == 1:
            name = input("Name of the track: ")
            print()
            "%20".join(name.split(' '))
            browser.get(track_url + name)
            continue

        # Search for an artist
        if choice == 2:
            name = input("Name of the artist: ")
            print()
            "%20".join(name.split(' '))
            browser.get(artist_url + name)
            continue

        # Search for a mix
        if choice == 3:
            name = input("Name of a mix: ")
            print()
            "%20".join(name.split(' '))
            browser.get(track_url + name + mix_url_end)
            continue

        # get the top 50 tracks for a genre
        if choice == 4:
            rq = requests.get(top_url)
            soup = bs4.BeautifulSoup(rq.text, 'lxml')

            while True:
                print("Genres Available: ")
                print()

                genres = soup.select("a[href*=genre]")[2:]
                genre_links = []

                # print all available genres
                for index, genre in enumerate(genres):
                    print(str(index) + ": " + genre.text)
                    genre_links.append(genre.get("href"))

                print()

                choice = input("Your choice (x to go back to main menu): ")

                if choice == 'x':
                    break
                else:
                    choice = int(choice)

                url = "https://soundcloud.com" + genre_links[choice]
                rq = requests.get(url)
                soup = bs4.BeautifulSoup(rq.text, 'lxml')

                tracks = soup.select('h2')[3:]
                track_links = []
                track_names = []

                for index, track in enumerate(tracks):
                    track_links.append(track.a.get('href'))
                    track_names.append(track.text)
                    print(str(index) + ": " + track.text)

                # song selection loop
                while True:
                    choice = input(
                        'Your choice (x to re-select a new genre): ')
                    print()

                    if choice == 'x':
                        break
                    else:
                        choice = int(choice) - 1

                    print("Now playing: " + track_names[choice])
                    print()

                    browser.get('https://soundcloud.com' + track_links[choice])

        # get the new and hot tracks for a genre
        if choice == 5:
            rq = requests.get(new_url)
            soup = bs4.BeautifulSoup(rq.text, 'lxml')
            # print(rq.text)
            while True:
                print("Genres Available: ")
                print()

                genres = soup.select("a[href*=genre]")[2:]
                genre_links = []

                # print all available genres
                for index, genre in enumerate(genres):
                    print(str(index) + ": " + genre.text)
                    genre_links.append(genre.get("href"))

                print()

                choice = input("Your choice (x to go back to main menu): ")

                if choice == 'x':
                    break
                else:
                    choice = int(choice)

                url = "https://soundcloud.com" + genre_links[choice]
                rq = requests.get(url)
                soup = bs4.BeautifulSoup(rq.text, 'lxml')

                tracks = soup.select('h2')[3:]
                track_links = []
                track_names = []

                for index, track in enumerate(tracks):
                    track_links.append(track.a.get('href'))
                    track_names.append(track.text)
                    print(str(index) + ": " + track.text)

                # song selection loop
                while True:
                    choice = input(
                        'Your choice (x to re-select a new genre): ')
                    print()

                    if choice == 'x':
                        break
                    else:
                        choice = int(choice) - 1

                    print("Now playing: " + track_names[choice])
                    print()

                    browser.get('https://soundcloud.com' + track_links[choice])

    print()
    print("Goodbye!")
    print()


def main():
    # create the selenium browser
    browser = webdriver.Firefox(executable_path = "C:\|Users\\satyadeep singh\\Desktop\\geckodriver.exe")
    browser.get('https://soundcloud.com')
    main_menu(browser)


if __name__ == '__main__':
    main()

