##############################################################################

#   Importing Packages
import random

#   This Package helps us to interact with the app
import pyautogui as pg

import time

#   Edit This  ---> Words you want to send
words = ('elakka','kutty kunjan','elakka kunji')
time.sleep(8)

#   Number of Messages to send
for i in range(100):
    
#   Sending Texts once We press Enter
    
    a=random.choice(words)
    pg.write("Dei "+a)
    pg.press("enter")

    
    
##############################################################################    