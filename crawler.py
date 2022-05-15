# Fazer um Crawler que entre do site do Tripadvisor e pesqueise sobre o congrsso nacional e extrair as avaliações do site e mostrar no terminal.
#####
# Para isso vamos usar a bibliteca selenium junto com o webdriver para fazer essa extração de dados da página.
#####




#Bibliotecas 
from selenium import webdriver
from turtle import window_width
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Abrir navegador, pesquisar o site e maximixar a tela
navegador = webdriver.Chrome()
url = "https://www.tripadvisor.com.br/"
navegador.get(url);
main_window = navegador.maximize_window()

#Dados ultilizados para a navegação e a extração de dados
delay = 20
xpathBotaoAceitar = '//*[@id="onetrust-accept-btn-handler"]'
xpathInputPesquisa = '/html/body/div[1]/main/div[3]/div/div/div/form/input[1]'
localPesquisa = 'Congresso Nacional - Brasília'
xpathPularConteudoPrincipal = '/html/body/div[1]/div[1]/button/span'
xpathResultadoCongresso = '/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[1]';
xpathQtdAvaliacaoLocal = '//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[1]/div[1]';
xpathQtdAvaliacoes = '//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[1]/div[2]/span';
try:
    #Clica no Botao Aceitar
    WebDriverWait(navegador,delay).until(EC.element_to_be_clickable((By.XPATH,xpathBotaoAceitar))).click();
    #Clica no campo de pesquisa
    WebDriverWait(navegador,delay).until(EC.element_to_be_clickable((By.XPATH,xpathPularConteudoPrincipal))).click();
    WebDriverWait(navegador,delay).until(EC.element_to_be_clickable((By.XPATH,xpathInputPesquisa))).click();
    #Escreve o texto
    WebDriverWait(navegador,delay).until(EC.element_to_be_clickable((By.XPATH,xpathInputPesquisa))).send_keys(localPesquisa);
    #Submete a pesquisa
    WebDriverWait(navegador,delay).until(EC.element_to_be_clickable((By.XPATH,xpathInputPesquisa))).submit();
    #Clica no resultado congresso nacional
    WebDriverWait(navegador,delay).until(EC.element_to_be_clickable((By.XPATH,xpathResultadoCongresso))).click();
    #seleciona a aba que selecionou
    main_window = navegador.window_handles[1]
    navegador.switch_to.window(main_window)
    #selecionar a quantidade de avaliação local
    qtdAvaliacoesLocal = navegador.find_elements_by_xpath(xpathQtdAvaliacaoLocal)
    Avaliacoes = navegador.find_elements_by_xpath(xpathQtdAvaliacoes)
    for value in qtdAvaliacoesLocal:
        qtdAvaliacoesLocal = (value.text)
    for value in Avaliacoes:
        Avaliacoes = (value.text)
        print('## Resultado da coleta de dados ##')
        print('Avaliação do local: {} de {} avaliações.'.format(qtdAvaliacoesLocal,Avaliacoes));
        #Fechar o navegador após executar a tarefa    
        navegador.close()
#caso execeda o tempo aparecera o print da dando tempo esgotado
except TimeoutException:
    print('Tempo esgotado.')
