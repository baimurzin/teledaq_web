from pyrogram import Client
from time import time, sleep
from random import random
import settings


app = Client(
    "my_account",
    api_id=settings.api_id,
    api_hash=settings.api_hash
)

CHANNELS = [dict(login="proxyme"),
            dict(link="AAAAAEK5OzbJ5eZsr34hCQ"),
            dict(login="temablog"),
            dict(login="breakingmash"),
            dict(link="AAAAAErpUE2JD_l8FpW8Hg"),
            dict(link="AAAAAEOzOEPpWs_SjppyzQ")]

with open("_speed_stats.txt", "w") as file:
    file.write("")


with app:
    a = time()
    for channel_code in CHANNELS:
        channel_code = channel_code["login"] if channel_code.get("login") else channel_code["link"]
        try:
            finded_chat = app.join_chat(channel_code)
            chat = app.get_chat(finded_chat.id)
            with open("{}.txt".format(chat.title), "w") as file:
                file.write("{title} @{username}\n".format(
                    title=chat.title if chat.title else "NoTitle",
                    username=chat.username if chat.username else "NoLogin"
                ))
            chat_messages = app.iter_history(chat_id=chat.id)
            messages_count = 0
            for message in chat_messages:
                messages_count += 1
                # if messages_count > 500:
                #     break
                sleep(random()/77.7)
                with open("{}.txt".format(chat.title), "a") as file:
                    if message.text:
                        file.write("<message views='{}'>\t{}\n".format(message.views, " ".join(message.text.splitlines())))
                    elif message.media:
                        file.write("<media_m views='{}'>\t{}\n".format(message.views, " ".join(message.caption.splitlines()) if message.caption else ""))
                    else:
                        continue
                        # file.write("<s_fuck>\t{}\n".format(str(message)))
            app.leave_chat(channel_code)
            b = time()
            with open("_speed_stats.txt", "a") as file:
                file.write("{\n\t")
                file.write("\n\t".join([chat.title, "{}s {}ms".format(int(b - a), int((b - a)*1000)%1000), "{} messages".format(messages_count)]))
                file.write("\n}\n\n")
            # print(chat.title, "{}s".format(b - a), messages_count)
        except Exception as e:
            with open("_speed_stats.txt", "a") as file:
                file.write("notfound '{}'\n\n".format(channel_code))
            # print("{} doesn't not exists at this point".format(channel_code))
            print(Exception(e))
