# excluirmemoriatemporaria
exclui arquivos da memoria ram do pc. 
import pyautogui
import time
import win32com.client as win32

pyautogui.alert('depois que clicar no ok, vai abrir uma janela e vai apagar arquivos (TEMPORARIOS) do seu computador.')
pyautogui.hotkey('win','r')
time.sleep(2)
pyautogui.write('prefetch')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('ctrl','a')
time.sleep(2)
pyautogui.hotkey('win','delete')
pyautogui.press('up')
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('right')
pyautogui.press('enter')
pyautogui.alert('Otimização concluida!')
