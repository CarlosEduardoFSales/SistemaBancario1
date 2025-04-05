import pyautogui
import time


pyautogui.click(x=3478, y=714)
time.sleep(1)
pyautogui.write("UFPB - LCC")
time.sleep(1)
pyautogui.click(x=3685, y=723)
time.sleep(2)


#excluir
pyautogui.click(x=3950, y=793)
time.sleep(2)
pyautogui.click(x=3809, y=239)
time.sleep(1)


#Entrando na proxima página

pyautogui.click(x=3416, y=823)
time.sleep(2)

#Mudando nome do time

pyautogui.click(x=3474, y=386)
pyautogui.write("Time Java")
time.sleep(1)
pyautogui.press("Tab")
pyautogui.click()
time.sleep(1)
pyautogui.press("Tab")
pyautogui.click()
time.sleep(1)

pyautogui.press("Tab")
pyautogui.write("Time Python")
time.sleep(1)

pyautogui.click(x=3451, y=810)
pyautogui.write("Time Frontend")
time.sleep(1)


#abrindo roleta

pyautogui.click(x=3545, y=934)
time.sleep(1)

pyautogui.click(x=3595, y=670)
time.sleep(3)

pyautogui.click(x=3595, y=670)
time.sleep(3)

pyautogui.click(x=3595, y=670)
time.sleep(3)

pyautogui.click(x=3639, y=1031)
time.sleep(1)

#Terminar rodada

pyautogui.click(x=3520, y=1003)
time.sleep(1)

pyautogui.click(x=3809, y=234)  
time.sleep(1)

#apagar tabela

pyautogui.click(x=3594, y=1238)
time.sleep(1)
pyautogui.click(x=3821, y=229)
time.sleep(2)

#Voltando 

pyautogui.click(x=3545, y=1053)
time.sleep(1)