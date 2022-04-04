if [[ -z "$TELETHON_SESSION" && -z "$PYROGRAM_SESSION" ]]
then
	echo "Add PYROGRAM_SESSION or TELETHON_SESSION first!"
elif [[ -z "$TELETHON_SESSION" ]]
then
	python3 -m tod
elif [[ -z "$PYROGRAM_SESSION" ]]
then
	python -m main.py
else
	python3 -m tod & pythonw -m main.py
	exit 1
fi
