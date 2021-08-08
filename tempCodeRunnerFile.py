'play music' in query:
            music_dir = "E:\\SONGS"
            songs = os.listdir(music_dir)
            # random_song = random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[0]))