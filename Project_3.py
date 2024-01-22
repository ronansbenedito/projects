# PASSO A PASSO DO PROJETO 

#https://dlp.hashtagtreinamentos.com/python/intensivao/login

#PASSO 1 - ENTRAR NO SISTEMA DA EMPRESA.

#PASSO 2 - FAZER LOGIN

#PASSO 3 - IMPORTAR A BASE DE DADOS

#PASSO 4 - CADASTRAR UM PRODUTOS

#PASSO 5 - REPETIR ESSE PROCESSO ATÉ O FIM DA BASE DE DADOS

#Principais Comandos
    # clique mouse - pyautogi.clicl
    # escrever - pyautogy.write
    # apertar uma tecla - pyautogui.press
    # atalho - pyautpgui.hotkey ("crtl" , "c")
    # scroll pyautogi.scroll

import pyautogui
import time
import pandas as pd
import numpy

# time.sleep - quantos segundos aquele comando vai esperar para rodar

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")

pyautogui.write("Chrome")

pyautogui.press("Enter")

pyautogui.write(link)

pyautogui.press("Enter")

time.sleep(0.5)
pyautogui.click(x=600,y=380)

pyautogui.write("ronan@benedito.com.br")

pyautogui.press("Tab")

pyautogui.write("123456")

pyautogui.press("Enter")

time.sleep(3)

base = pd.read_csv("produtos.csv")

time.sleep(3)

for linha in base.index:

    
    pyautogui.click(x=489, y=261)
    
    #código

    pyautogui.write(str(base.loc[linha, "codigo"]))
    pyautogui.press("Tab")

    #Marca
   
    pyautogui.write(str(base.loc[linha, "marca"]))
    pyautogui.press("Tab")

    #Tipo
   
    pyautogui.write(str(base.loc[linha, "tipo"]))
    pyautogui.press("Tab")

    #Categoria
   
    pyautogui.write(str(base.loc[linha, "categoria"]))
    pyautogui.press("Tab")

    #Preço Unitário
    
    pyautogui.write(str(base.loc[linha,"preco_unitario"]))
    pyautogui.press("Tab")

    #Custo
    pyautogui.write(str(base.loc[linha,"custo"]))
    pyautogui.press("Tab")

    #OBS
    obs = base.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(base.loc[linha,"obs"])
    pyautogui.press("Tab")

    #Enviar o produto
    pyautogui.press("Enter")

    pyautogui.scroll(5000)