from linebot.models import (RichMenu, RichMenuArea,
                            RichMenuBounds, RichMenuSize)
from linebot.models import URIAction, PostbackAction


def font_richmenu():
    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=False,
        name="select font",
        chat_bar_text="Select a font",
        areas=[RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0,
                                  width=1250, height=843//2),
            action=PostbackAction(
                type='postback',
                label='Bold',
                data='MATHEMATICAL_BOLD')
        ),
            RichMenuArea(
            bounds=RichMenuBounds(x=0, y=843//2,
                                  width=1250, height=843//2),
            action=PostbackAction(
                type='postback',
                label='Italic',
                data='MATHEMATICAL_ITALIC')
        ),
            RichMenuArea(
            bounds=RichMenuBounds(x=1250, y=0,
                                  width=1250, height=843//2),
            action=PostbackAction(
                type='postback',
                label='Bold italic',
                data='MATHEMATICAL_BOLD_ITALIC'
            )
        ),
            RichMenuArea(
            bounds=RichMenuBounds(x=1250, y=843//2,
                                  width=1250, height=843//2),
            action=PostbackAction(
                type='postback',
                label='Script',
                data="SCRIPT"
            )
        )
        ]
    )

    return rich_menu_to_create
