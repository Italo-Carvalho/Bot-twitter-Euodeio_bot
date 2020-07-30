# -*- coding: utf-8 -*-
import random, os, sys
from random import randint 
import tweepy
import time
from datetime import datetime

text_file = open("palavras.txt", "r")       #Abrimos a lista de palavras
palavras = text_file.readlines()     #E convertemos numa lista

consumer_secret = " "
consumer_key = " "           #Credencias do twitter dev
access_token = " "
access_token_secret = " "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Autenticando 


aleatorio = (randint(1,28638))
numero = int(palavras[0])  #A palavra atual esta salvo no indice 0 da lista

texto = ""

 
if str(palavras[numero])[0] == '0':
    texto = "Eu odeio "+palavras[numero][1].lower()+"... Vou nem comentar..."
    #Algumas palavras não podem ser chingadas, marcamos elas com um 0
    #O bot so vai postar a primeira letra delas
    
else:
    texto = "Eu odeio " + palavras[aleatorio].lower() 
    #Caso não seja uma palavra marcada o bot diz "Eu odeio + palavra"
    
api.update_status(status=texto) #Então postamos no twitter o texto gerado
palavras[0] = str(numero + 1) + '\n'     #Incrementos o contador

with open('palavras.txt', 'w') as file:
    file.writelines(palavras)       #E salvamos devolta no arquivo
    print(texto) #Mostra no terminal a palavra enviada









