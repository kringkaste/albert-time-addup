# -*- coding: utf-8 -*-

"""
Add up time ranges into a floating-point number of hours.
"""

import os
import time
import locale
from albert import *
from pathlib import Path

md_iid = '2.0'
md_version = '1.0'
md_name = 'Time addup'
md_description = 'Add up time ranges into a floating-point number of hours.'
md_license = 'MIT'
md_url = 'https://github.com/kringkaste/albert-time-addup'


class Plugin(PluginInstance, GlobalQueryHandler):

    def __init__(self):
        GlobalQueryHandler.__init__(self,
                                    id=md_id,
                                    name=md_name,
                                    description=md_description,
                                    defaultTrigger='t ')
        PluginInstance.__init__(self, extensions=[self])


    def calc(self, string):
        tokens = string.split()

        startDate = None
        endDate = None
        sumTime = 0
        for token in tokens:
            if "m" in token:
                value = token.replace("m", "").replace("+", "").replace("-", "")
                try:
                    minutes = int(value)
                    if "-" in token:
                        sumTime = sumTime - (int(value) * 60)
                    else:
                        sumTime = sumTime + (int(value) * 60)
                except:
                    pass                    
            elif startDate == None:
                try:
                    startDate = time.strptime(token, "%H:%M")
                except:
                    startDate = None
            else:
                try:
                    endDate = time.strptime(token, "%H:%M")
                    diff = time.mktime(endDate) - time.mktime(startDate)
                    sumTime = sumTime + diff
                    startDate = None
                    endDate = None
                except:
                    pass

        sumTime = sumTime / 60 / 60
        result = locale.format_string("%.2f", sumTime)
        
        return result


    def handleGlobalQuery(self, query):
        plugin_dir = Path(__file__).parent
        rank_items = []
        s = query.string.strip()
        if s:
            result = self.calc(s)
            rank_items.append(
                RankItem(
                    StandardItem(
                        id="timeaddup",
                        text=result,
                        iconUrls=["file:" + str(plugin_dir / "clock.svg")],
                        actions=[
                            Action(
                                "Clip",
                                "Copy to clipboard",
                                lambda clip=result: setClipboardText(clip),
                            )
                        ],
                    ),
                    1
                )
            )

        
        return rank_items
