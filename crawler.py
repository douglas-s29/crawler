# Fazer um Crawler que entre do site do Tripadvisor e pesqueise sobre o congrsso nacional e extrai as avaliações do site e mostre no terminal.
#####

# Para isso vamos usar a bibliteca selenium junto com o webdriver para fazer essa extração de dados da página.

# A biblioteca time é para dar tempo da pagina carregar e aceitar os cookies de pagina para fazer a pesquisa.
#####




#Bibliotecas 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Comandos para abrir o navegador; pesquisar o site; esperar 5s para aceitar os cookies da pagina; aceitar os cookies; esperar 2 segundos; Clicar em pesquisa e pesquisar Congresso nacional
navegador = webdriver.Chrome()
navegador.get("https://www.tripadvisor.com.br/");
sleep(5);
navegador.find_element_by_xpath ('//*[@id="onetrust-accept-btn-handler"]').click();
sleep(6)
navegador.find_element_by_xpath('//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]').click();
sleep(3)
navegador.find_element_by_xpath('//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]').send_keys('paris');
sleep(3)
navegador.find_element_by_xpath('//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]').submit();
