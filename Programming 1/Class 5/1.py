price_app = 3
price_song = 7
funds = int(input('How much money do you wish to prepay? \n'))

max_num_apps = funds // price_app
max_num_songs = funds // price_song
rest_num_apps = (funds - price_song * max_num_songs) // price_app
money_left_apps = funds % price_app
money_left_songs = (funds % price_song) % price_app

if max_num_apps == 1:
    app = 'app'
else:
    app = 'apps'

if max_num_songs == 1:
    song = 'song'
else:
    song = 'songs'

if rest_num_apps == 1:
    app2 = 'app'
else:
    app2 = 'apps'

print(f'With this amount, you will be able to purchase {max_num_apps} {app}.')
print(f'You will then have ${money_left_apps} left as a credit on your account.')
print(f'Alternatively, for this amount, you will be able to purchase {max_num_songs} {song} and {rest_num_apps} {app2}.')
print(f'You will then have ${money_left_songs} left as a credit on your account.')
print(f'Thanks for Shopping at Best Music Store!')
