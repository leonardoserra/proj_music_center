# Questa è un app per gestire un negozio di musica
## Avrà entita: 
```py
User(id:int, username:str, password:str)
Instrument(id:int, name:str, price:float, type:str):class 
Concert(id:int, name:str, date:object, price:float):class
contert_group(id_concerto, id_gruppo) #tabella relazione
Group(id:int, name:str, group_members:list[Person]):class
GroupMember(id:int, name:str, surname:str, instrument:str, group_id:int):class
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
