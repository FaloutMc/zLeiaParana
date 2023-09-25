from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import openai
import os
import pandas as pd
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

vr1 = 21
vr2 = 22
vr3 = 23
vr4 = 24

saida = 0
saida0 = 0

print(15*'-=')
print('''Bem-Vindo ao zLeiaParanaMiner!
By:Arthur Reis\n''')
time.sleep(2)
print('''Este é um programa que te ajuda a ler e responder
os livros e as questões corretamentes, usando a API do Chat Gpt
e usando o Python Selenium!''')
print('\nOBS: Depois de terminar o Livro, fechar o Programa! \n')
time.sleep(5)

usuario=input('Qual é o seu @Escola?: \n').strip()
senha=input('Qual é sua senha? \n')

livro=int(input('''Acesse este link: https://leiaparana-le.odilo.us/clubs/63f558a6d13a030008947f21/contents
em seguida digite em numero, qual livro selecionar (Da lista, de cima para baxo, Ex: 1, 12, 31 etc...) \n''').strip())

while saida !=1:

    print('''Alguns livros podem ter respostas diferentes, e eu não conigo detectar qual é.
    Então se o programa der erro/travar, tente outra opção abaixo (O mais recomendado é o X1,
    se não der certo, tentar o X2, em ultimo caso, usar o X3): 

        [1]- X1
        [2]- X2
        [3]- X3''')

    radio=int(input())

    if radio == 1:
        vr1 = 22
        vr2 = 23
        vr3 = 24
        vr4 = 25
        saida=1

    elif radio == 2:
        vr1 = 21
        vr2 = 22
        vr3 = 23
        vr4 = 24
        saida=1

    elif radio == 3:
        vr1 = 23
        vr2 = 24
        vr3 = 25
        vr4 = 26
        saida=1

    else:
        print('>>> Opção Inválida, Tnte Novamente!')

while saida0 != 1:
    print('''
    [1]- Chrome (Chromium): 
    [2]- FireFox:
    [3]- Safari:
    [4]- Edge: \n''')
    nav = int(input('Selecione a opção acima do seu Navegador:\n'))

    if nav == 1:
        driver = webdriver.Chrome()
        saida0 = 1
    elif nav == 2:
        driver = webdriver.Firefox()
        saida0 = 1
    elif nav == 3:
        driver = webdriver.Safari()
        saida0 = 1
    elif nav == 4:
        driver = webdriver.Edge()
        saida0 = 1
    else:
        print(' >>>Opção Inválida, Tente Novamente!!!')

url0 = 'https://leiaparana-le.odilo.us/clubs/63f558a6d13a030008947f21/contents'

driver.get(url0)
time.sleep(3)
driver.find_element('xpath', '/html/body/app-root/ole-header/div/div/div[3]/ole-button').click()
time.sleep(3)

termo1 = driver.find_element('xpath', '//*[@id="identifierId"]')
termo1.clear()
termo1.send_keys(usuario)

driver.find_element('xpath',
                    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
time.sleep(3)
termo2 = driver.find_element('xpath',
                             '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
termo2.clear()
termo2.send_keys(senha)
driver.find_element('xpath', '//*[@id="passwordNext"]/div/button').click()
time.sleep(5)
driver.execute_script("window.open('', '_blank');")
driver.switch_to.window(driver.window_handles[1])
driver.get(url0)
time.sleep(3)

if livro >= 5:
    driver.execute_script("window.scrollBy(0, 900);")

time.sleep(1)
driver.find_element('xpath',f'/html/body/app-root/div/ole-club/div/ole-contents/div/div/div[2]/ole-resources-list/div/div[2]/ul/li[{str(livro)}]').click()
time.sleep(1)
driver.find_element('xpath','/html/body/app-root/div/ole-club/div/ole-contents/div/div/div[1]/div/div[2]/ole-content-actions/div/div[1]/ole-button[1]').click()
time.sleep(1.5)
# Feche a guia anterior somente após interagir completamente com a nova guia
driver.switch_to.window(driver.window_handles[2])
time.sleep(2)
apa = 0
if apa == 0:

    for i in range(300):
        time.sleep(2)

        # Elemento que você deseja clicar
        element = driver.find_element('xpath', '//*[@id="right-page-btn"]')

        # Crie uma espera
        wait = WebDriverWait(driver, 1)

        try:
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            # Elemento que você deseja clicar
            element_to_click = driver.find_element('xpath', '//*[@id="right-page-btn"]')

            # Elemento a ser verificado
            element_to_check = driver.find_elements('xpath', '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/button')

            # Crie uma espera
            wait = WebDriverWait(driver, 1)

            try:
                # Verifique se o elemento a ser verificado não está presente
                if not element_to_check:
                    # Se o elemento não estiver presente, clique no elemento desejado
                    element_to_click.click()
                else:
                    # Se o elemento estiver presente, imprima "Código 911"
                    qt = driver.find_element('xpath', '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/button')
                    qt.click()

                    tc1 = driver.find_element('xpath',
                                              '/html/body/div[4]/md-dialog/form/md-dialog-content/div/pre').get_attribute(
                        'textContent')
                    tc2 = driver.find_element('xpath',
                                              '/html/body/div[4]/md-dialog/form/md-dialog-content/div/div/md-radio-group/div[1]/span').get_attribute(
                        'textContent')
                    tc3 = driver.find_element('xpath',
                                              '/html/body/div[4]/md-dialog/form/md-dialog-content/div/div/md-radio-group/div[2]/span').get_attribute(
                        'textContent')
                    tc4 = driver.find_element('xpath',
                                              '/html/body/div[4]/md-dialog/form/md-dialog-content/div/div/md-radio-group/div[3]/span').get_attribute(
                        'textContent')
                    tc5 = driver.find_element('xpath',
                                              '/html/body/div[4]/md-dialog/form/md-dialog-content/div/div/md-radio-group/div[4]/span').get_attribute(
                        'textContent')
                    tc0 = f'''Chat GPT, me ajude a resolver esta questão, no livro: "Como faziamos sem", me fale qual é a questão correta, responda somente com UMA letra da questão, nada mais,se não o código vai dar erro, Exemplo: B. Ja que esta mensagem é automatica:

                                                {tc1}.

                                                A- {tc2}
                                                B- {tc3}
                                                C- {tc4}
                                                D- {tc5}'''

                    print(tc0)

                    openai.api_key = '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'


                    def get_completion(prompt, model="gpt-3.5-turbo"):
                        messages = [{"role": "user", "content": prompt}]
                        response = openai.ChatCompletion.create(
                            model=model,
                            messages=messages,
                            temperature=0,
                        )
                        return response.choices[0].message["content"]


                    prompt = tc0
                    response = get_completion(prompt)
                    response_re = re.sub(r'\.', '', response).lower().strip()

                    # Defina uma lista com as letras que você deseja verificar
                    letras_alvo = ['a', 'b', 'c', 'd']

                    # Inicialize uma variável para armazenar a primeira letra encontrada (se encontrada)
                    primeira_letra = None

                    # Itere sobre o texto
                    for letra in response_re:
                        if letra in letras_alvo:
                            primeira_letra = letra
                            break  # Saia do loop assim que a primeira letra for encontrada

                    # Verifique se uma das letras foi encontrada e imprima
                    if primeira_letra is not None:
                        pl = primeira_letra
                        print(response)



                        q1 = driver.find_element('xpath', f'//*[@id="radio_{str(vr1)}"]')
                        q2 = driver.find_element('xpath', f'//*[@id="radio_{str(vr2)}"]')
                        q3 = driver.find_element('xpath', f'//*[@id="radio_{str(vr3)}"]')
                        q4 = driver.find_element('xpath', f'//*[@id="radio_{str(vr4)}"]')

                        if pl == 'a':
                            q1.click()
                            time.sleep(0.5)
                            driver.find_element('xpath',
                                                '/html/body/div[4]/md-dialog/form/md-dialog-actions/button[2]').click()
                            driver.find_element('xpath', '/html/body/div[4]/md-dialog/md-toolbar/div/button').click()
                            driver.find_element('xpath', '//*[@id="right-page-btn"]').click()
                            vr1 +=5
                            vr2 +=5
                            vr3 +=5
                            vr4 +=5

                        elif pl == 'b':
                            q2.click()
                            time.sleep(0.5)
                            driver.find_element('xpath',
                                                '/html/body/div[4]/md-dialog/form/md-dialog-actions/button[2]').click()
                            driver.find_element('xpath', '/html/body/div[4]/md-dialog/md-toolbar/div/button').click()
                            driver.find_element('xpath', '//*[@id="right-page-btn"]').click()
                            vr1 += 5
                            vr2 += 5
                            vr3 += 5
                            vr4 += 5


                        elif pl == 'c':
                            q3.click()
                            time.sleep(0.5)
                            driver.find_element('xpath',
                                                '/html/body/div[4]/md-dialog/form/md-dialog-actions/button[2]').click()
                            driver.find_element('xpath', '/html/body/div[4]/md-dialog/md-toolbar/div/button').click()
                            driver.find_element('xpath', '//*[@id="right-page-btn"]').click()
                            vr1 += 5
                            vr2 += 5
                            vr3 += 5
                            vr4 += 5

                        elif pl == 'd':
                            q4.click()
                            time.sleep(0.5)
                            driver.find_element('xpath',
                                                '/html/body/div[4]/md-dialog/form/md-dialog-actions/button[2]').click()
                            driver.find_element('xpath', '/html/body/div[4]/md-dialog/md-toolbar/div/button').click()
                            driver.find_element('xpath', '//*[@id="right-page-btn"]').click()
                            vr1 += 5
                            vr2 += 5
                            vr3 += 5
                            vr4 += 5

                        else:
                            print('ERROR: O Chat GPT Não Achou uma resposta válida: 2! ')


            except Exception as e:
                # Lide com outras exceções, se necessário
                print("Erro:", e)

        except Exception as e:
            # Lide com a exceção (por exemplo, imprima uma mensagem de erro)
            print('ERROR Inesperado.')


        except Exception as e:
            print("Página Concluida.")