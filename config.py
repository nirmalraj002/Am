"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

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
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "24401235")
        self.API_HASH: str = os.environ.get("API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22")
        self.SESSION: str = os.environ.get("SESSION", "BQF0VVMAWuGDiIeWtLh05Gm4G4pDPqkKwmIMlZt4YM_Aw8fGLOB4708EtEbXGnH9BY6rDpWSBpy42RajnLQsD0gd3KopQAdSBzPF5k9ZOfiNbxgSs2qSUaDoS8OV2oOTkaQd0wfEXzFDdJPNfQazEV2otte9NcBT68R72rMADL3jjQ3nI1zwC8ECPngdSL_QknDk2EGEga3XSKTyNcr6d0ZMQuGVKQHJ1kocXNGCJtmrpGcS7WYo_r2NBbJBvePi9ZoOe4p7BcXv5oCadPlLeOCfX6PdKMfq0N-rCz8eKtPSo6wQwC4IrEtefcbn3UZMDO2ZR6eNUmlh8gue0MhnroBHlezJSAAAAAGwd90wAA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "6111967692:AAFEXQo6_5LyA9GNJz-m233iS_57eWr1aBk")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "1556830659").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
