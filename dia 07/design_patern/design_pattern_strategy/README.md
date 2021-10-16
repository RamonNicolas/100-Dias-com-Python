# O mais importante ao estudar padrões de projeto é entender qual a real motivação do padrão, e quando ele deve ser aplicado. 
#   As implementações são menos importantes, pois eles podem variar. O importante é resolver o problema de
# maneira elegante, usando a ideia por trás do padrão como um guia na implementação.E eles também servem para comunicar soluções entre desenvolvedores.

# O padrão Strategy é muito útil quando temos um conjunto de algoritmos similares, e precisamos alternar entre eles em diferentes pedaços da aplicação. 
# No exemplo do vídeo, temos diferentes maneira de calcular o imposto, e precisamos alternar entre elas.
# O Strategy nos oferece uma maneira flexível para escrever diversos algoritmos diferentes, e de passar esses algoritmos para classes 
# clientes que precisam deles. Esses clientes desconhecem qual é o algoritmo "real" que está sendo executado, e apenas manda o algoritmo rodar. 
#     Isso faz com que o código da classe cliente fique bastante desacoplado das implementações dos algoritmos, 
# possibilitando assim com que esse cliente consiga trabalhar com N diferentes algoritmos sem precisar alterar o seu código.