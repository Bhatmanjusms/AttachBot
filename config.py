#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala

import os

class Config(object):
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5845591450:AAHXINy_Oddhpcf5X88f1zQ_J1VC9NGBqH4")
  #CHANNEL_USERNAME without '@'
  CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "ufyyuvgg7")
  CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001544809913))
