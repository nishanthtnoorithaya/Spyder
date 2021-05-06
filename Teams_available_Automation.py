# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:44:24 2021

@author: Nishanth T (Junior Python Developer)

"""

import pyautogui as  pg

#print(pg.size())                 # Specifies the complete size of the laptop/Desktop.

pg.moveTo(1167,745, duration = 1)  # This will move cursor to taskbar, where the teams app is present.
pg.click(1167,745)                 # This will click on taskbar teams app

pg.moveTo(1181,5, duration = 2)    # This will move cursor to profile of teams app
pg.click(1203,22)                  # This will click on profile of teams app

pg.moveTo(1130,141, duration = 2)   # This will move cursor to status of teams app.
pg.click(1130,141)                  # This will click on status teams app.

pg.moveTo(885,134, duration = 2)     # This will move cursor to available status of teams app.
pg.click(885,134)                    # This will click on available status teams app.


pg.moveTo(1352,21, duration = 1)      # This will move cursor to close bar of teams app.
pg.click(1352,21)                     # This will click on close bar teams app, hence the teams app is closed from front. But from background it will running. 

#print(pg.position())                 # Prints the current position of mouse pointer. 
