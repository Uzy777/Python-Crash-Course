# 8-8. User Albums:     Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's artist and title. Once you have that information,
#                       all make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'title': album_title}
    return album

while True:
    print("Please enter the details of the album")
    print("(enter 'q' at any time to quit)")

    artist_n = input("Artist Name: ")
    if artist_n == 'q':
        break

    album_t = input("Album Title: ")
    if album_t == 'q':
        break

    final = make_album(artist_n.title(), album_t)
    print(final)