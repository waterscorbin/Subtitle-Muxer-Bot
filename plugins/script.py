from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):



    START_TEXT = """
Hey {} 

I am Telegram Most Powerful Subtitle Muxer Bot

I can Mux Any srt or ass File in File or Video

Use Help Command to Know How to Use me

Deployed By π By ΰΌΊπΉπΎοΈπ·π½ π³πΎοΈπ΄ΰΌ»
"""
    HELP_TEXT = """
Recommended
β  Use Hardmux If You Have More Time

Recommended
β  Use Softmux To add Subtitle Fastly in It

Softmux
β  Send /softmux to add Subtitle Softly in it

HardMux
β  Send /hardmux to add Subtitle hardly in it 

Deployed By π By ΰΌΊπΉπΎοΈπ·π½ π³πΎοΈπ΄ΰΌ»
"""
    ABOUT_TEXT = """
 **π€ Bot :** John Doe Subtitle Muxer\n
 **βοΈ Credits :** Everyone in this journey\n
 **π Language :** [Python3](https://python.org)\n
 **π Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
 **π Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('β Help', callback_data='help'),
        InlineKeyboardButton('β Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('π‘ Home', callback_data='home'),
        InlineKeyboardButton('π² About', callback_data='about'),
        InlineKeyboardButton('β Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('π‘ Home', callback_data='home'),
        InlineKeyboardButton('β Help', callback_data='help'),
        InlineKeyboardButton('β Close', callback_data='close')
        ]]
    )
