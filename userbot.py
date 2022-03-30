from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> MUSIC MODULE STARTED')
idle()
app.stop()
print('\n>>> MUSIC MODULE STOPED')