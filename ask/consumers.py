from channels import Group
import json


def ws_connect(message, pk):
    print '--ws connected to {0}'.format('answers_{0}'.format(pk))
    message.reply_channel.send({"accept": True})
    Group('answers_{0}'.format(pk)).add(message.reply_channel)


def ws_disconnect(message, pk):
    Group('answers_{0}'.format(pk)).discard(message.reply_channel)
