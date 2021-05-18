import PythonTelegramWraper.bot as bot
import paho.mqtt.client as mqtt
import threading
import os
import time

class ImpfBot:
    def start(self, update, context):
        cid = bot.chatID(update)
        bot.sendMessage(cid, str(cid))


    def on_message(self, client, userdata, msg):
        message=msg.payload.decode("utf-8")
        print("Message received:",message)
        bot.sendMessage(os.environ.get("CHAT_ID"),message)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def __init__(self):
        bot.addBotCommand("start", self.start)

        self.client = mqtt.Client(client_id="telegramchecker", clean_session=False)
        self.client.on_message = self.on_message
        self.client.on_connect=self.on_connect
        self.client.connect(os.environ.get("MQTT_BROKER_ADRESS"), 1883, 60)
        self.client.subscribe(os.environ.get("TOPIC"))

        thread = threading.Thread(target=bot.startBot, daemon=True)
        thread.start()
        thread = threading.Thread(target=self.loop, daemon=True)
        thread.start()
    
    def loop(self):
        while True:
            self.client.loop()
            time.sleep(1)

ImpfBot()
while True:
    time.sleep(1)