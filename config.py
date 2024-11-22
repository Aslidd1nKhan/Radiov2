"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "6272205785")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 20627039))
    CHAT = int(os.environ.get("CHAT", "-1002247685563"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://www.youtube.com/live/36YnV9STBqc")
    API_HASH = os.environ.get("API_HASH", "16778e88a5e553e9c3daf389436c6c45")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7862732765:AAEGFhJGWb26nNy6GKgd1TChHxMoyrq4ZEU") 
    SESSION = os.environ.get("SESSION_STRING", "AgFPgW4ANZGKNDBy4VVuegR7XMKPHnpxtlgdhIXep_ol6N7r74ncE9biyGhqsSZgESJP8k1GstEY8EJQWyj_MHHSAEDgDBaS8nheMpmwfZebs8OFYQWE5K7-N0ajh-xZ2f2qOdWH9ExIRNnJsJ4HL9eQ5s_pabD2ONN06Cc9NttuuSuJT8jlksFxbEevUeVt4Ob_31YulgxfO6h3Zz2jrRwbcuBmFA1-gP5H7YID-kOrw4pTkg1IqywEb3CFKSntQ-8HV8ia0Odi7mCaf70XgfLXcLCb27YMcBcgovhLi9hei-GRzC0gDyTs7oGcYBfG9EziHOAfWQFQhbbkPzCBB0sbArvlUwAAAAGnW8D9AA")

