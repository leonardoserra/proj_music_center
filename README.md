# Questa è un app per gestire un negozio di musica
## Avrà entita: 
```py
Prodotto(id:int, nome:str, prezzo:float, tipo:object|str):class 
Concerto(nome:str, data:object, prezzo:float, gruppi:list[Gruppo]):class
Gruppo(nome:str,membri:list[Persona]):class
```
## db:
tabella prodotti
tabella gruppi 
TODO
## templates:
```py 
'base.html' # template base
  'index.html' # homepage dove vengono mostrate blocchi diversi:

               '/home o / ' # lista strumenti e lista concerti
               '/strumenti' # lista strumenti 
               '/concerti' # lista concerti 
  '/strumenti/chitarre' # lista chitarre 
  '/strumenti/batterie' # lista batterie 
  '/strumenti/bassi' # lista bassi 
  
  'show.html' # estende base.html ma mostra solo uno strumento quindi il blocco sarà:
              '/concerti/<int:id>'  #blocco concerto
              '/strumenti/chitarre/<int:id>'  #blocco della chitarra
              '/strumenti/batterie/<int:id>'  #blocco della batteria
              '/strumenti/bassi/<int:id>' #blocco del basso
  'login.html'# avrà il form per il login una volta loggato porta a '/home' ma da loggato.
              '/login, methods=["GET", "POST"]'
``` 

```py
#routes:  
'/home' oppure '/' #homepage che mostra qualche strumento random (o i piu venduti o gli ultimi arrivi) e i prox concerti
'/login' (get e post) #per entrare come admin e modificare

'/strumenti'  #tutti gli strumenti
'/concerti'  #lista concerti
'/strumenti/chitarre' #da lista chitarre  
'/strumenti/batterie'  #da lista batterie
'/strumenti/bassi'  # da lista bassi

'/concerti/<int:id>'  #show concerto
'/strumenti/chitarre/<int:id>'  #show della chitarra
'/strumenti/batterie/<int:id>'  #show della batteria
'/strumenti/bassi/<int:id>' #show del basso
 ``` 