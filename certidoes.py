from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


escolha = 0
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

while (escolha != 9):

    print("\n--------------------------------")
    print("\nEscolha uma opção: \n1 - Inserir dados\n2 - Consultar certidão distribuição civel em geral - 10 anos\n3 - Consultar certidão de distribuição de ações criminais\n4 - Consultar certidão eletrônica de ações trabalhistas\n5 - Consultar certidão negativa de débitos trabalhistas\n6 - Consultar certidão do tribunal regional federal da 3ª região  \n7 - Consultar certidão negativa de débitos tributários não inscritos \n8 - Consultar certidão de débitos relativos a créditos tributários federais e à dívida ativa da união\n9 - Sair do programa")
    print("\n--------------------------------")

    escolha = int(input("\nDigite a opção referente a sua escolha: " ))

    if (escolha == 1):

        docType = input("\nCPF ou CNPJ? ")
        if (docType == "cpf"):
            name = input("Digite o nome completo: ")
            doc = input("Digite o CPF: ")
            rg = input("Digite o RG: ")
            mothersName = input("Digite o nome da mãe: ")
            birthdate = input("Digite a data de nascimento: ")
            email = input("E-mail informado para envio das instruções: ")
        elif (docType == "cnpj"):
            doc = input("Digite o CNPJ: ")
            razao = input("Digite a razão social: ")
            email = input("E-mail informado para envio das instruções: ")
        else:
            print("\nTipo de documento inválido.")
            del docType

    elif (escolha == 2):

        if ('docType' in locals()):
            # browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            browser.get("https://esaj.tjsp.jus.br/sco/abrirCadastro.do")
            browser.maximize_window()
            select = Select(browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[1]/td[2]/select'))
            select.select_by_visible_text("CERTIDÃO DE DISTRIBUIÇÃO CÍVEL EM GERAL - ATÉ 10 ANOS")
            if (docType == "cpf"):
                nameInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[3]/td[2]/input')
                cpfInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[5]/td[2]/input')
                rgInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[6]/td[2]/table/tbody/tr/td/span[1]/input')
                nameInput.send_keys(name)
                cpfInput.send_keys(doc)
                rgInput.send_keys(rg)
            else:
                juridica = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/fieldset/span[2]').click()
                razaoInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[4]/td[2]/input')
                cnpjInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[7]/td[2]/input')
                razaoInput.send_keys(razao)
                cnpjInput.send_keys(doc)

            emailInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[2]/table[2]/tbody/tr[1]/td[2]/input')
            emailInput.send_keys(email)
            confirmButton = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[2]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td/span/label/input').click()
        else:
            print("\nInsira os dados antes de consultar.")

    elif (escolha == 3):

        if ('docType' in locals()):
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            browser.get("https://esaj.tjsp.jus.br/sco/abrirCadastro.do")
            browser.maximize_window()
            select = Select(browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[1]/td[2]/select'))
            select.select_by_visible_text("CERTIDÃO DE DISTRIBUIÇÃO DE AÇÕES CRIMINAIS")
            if (docType == "cpf"):
                nameInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[3]/td[2]/input')
                cpfInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[5]/td[2]/input')
                rgInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[6]/td[2]/table/tbody/tr/td/span[1]/input')
                mothersNameInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[9]/td[2]/input')
                birthdateInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[11]/td[2]/table/tbody/tr/td/span[1]/input')
                nameInput.send_keys(name)
                cpfInput.send_keys(doc)
                rgInput.send_keys(rg)
                mothersNameInput.send_keys(mothersName)
                birthdateInput.send_keys(birthdate)
            else:
                juridica = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/fieldset/span[2]').click()
                razaoInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[4]/td[2]/input')
                cnpjInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[1]/table[2]/tbody/tr[7]/td[2]/input')
                razaoInput.send_keys(razao)
                cnpjInput.send_keys(doc)

            emailInput = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[2]/table[2]/tbody/tr[1]/td[2]/input')
            emailInput.send_keys(email)
            confirmButton = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr/td/form/div[2]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td/span/label/input').click()
        else:
            print("\nInsira os dados antes de consultar.")

    elif (escolha == 4):

        if ('docType' in locals()):
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            browser.get("https://trt15.jus.br/servicos/certidoes/certidao-eletronica-de-acoes-trabalhistas-ceat")
            browser.maximize_window()
            browser.switch_to.frame(browser.find_element_by_tag_name("iframe"));
            docInput = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/div/div/span[2]/input')
            docInput.send_keys(doc)
            includeCheckbox = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div/div[2]/div[2]/div[3]/div/span[2]/input').click()
        else:
            print("\nInsira os dados antes de consultar.")

    elif (escolha == 5):

        if ('docType' in locals()):
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            browser.get("http://www.tst.jus.br/certidao")
            browser.maximize_window()
            browser.switch_to.frame(browser.find_element_by_tag_name("iframe"));
            certificadoButton = browser.find_element_by_xpath('/html/body/form/div/div/div[2]/input[1]').click()
            docInput = browser.find_element_by_xpath('/html/body/form/div/fieldset/div[1]/table/tbody/tr[1]/td[2]/input')
            docInput.send_keys(doc)
        else:
            print("\nInsira os dados antes de consultar.")

    elif (escolha == 6):

        if ('docType' in locals()):
            escolhaAbrangencia = int(input("\nEscolha uma opção: \n1 - Justiça Federal de Primeiro Grau em São Paulo\n2 - Tribunal Regional Federal da 3ª região\n"))
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            browser.get("http://web.trf3.jus.br/certidao/Certidao/Solicitar")
            browser.maximize_window()
            if (escolhaAbrangencia == 1):
                abrangenciaButton = browser.find_element_by_xpath('/html/body/div/div[3]/form/fieldset/p[3]/input[1]').click()
            elif (escolhaAbrangencia == 2):
                abrangenciaButton = browser.find_element_by_xpath('/html/body/div/div[3]/form/fieldset/p[3]/input[3]').click()
            
            nameInput = browser.find_element_by_xpath('/html/body/div/div[3]/form/fieldset/span[2]/p[2]/input')
            docInput = browser.find_element_by_xpath('/html/body/div/div[3]/form/fieldset/span[2]/p[5]/input')

            if (docType == "cpf"):
                nameInput.send_keys(name)
            else:
                docTypeButton = browser.find_element_by_xpath('/html/body/div/div[3]/form/fieldset/span[2]/p[4]/input[2]').click()
                nameInput.send_keys(razao)

            docInput.send_keys(doc)
        else:
            print("\nInsira os dados antes de consultar.")

    elif (escolha == 7):
        if ('docType' in locals()):
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            browser.get("https://www10.fazenda.sp.gov.br/CertidaoNegativaDeb/Pages/EmissaoCertidaoNegativa.aspx")
            browser.maximize_window()

            if (docType == "cnpj"):
                cnpjButton = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[2]/fieldset/div[1]/div[1]/span/input[2]').click()

            docInput = browser.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[2]/fieldset/div[1]/div[2]/div/span[1]/input')
            docInput.send_keys(doc)
        else:
            print("\nInsira os dados antes de consultar.")

    elif (escolha == 8):
        if ('docType' in locals()):
            if (docType == "cnpj"):
                browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                browser.get("https://servicos.receita.fazenda.gov.br/Servicos/certidao/CndConjuntaInter/InformaNICertidao.asp?Tipo=1")
                browser.maximize_window()

                docInput = browser.find_element_by_xpath('/html/body/p/table/tbody/tr/td/p/table/tbody/tr/td/form/input[1]')
                docInput.send_keys(doc)
            else:
                browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                browser.get("http://servicos.receita.fazenda.gov.br/Servicos/certidao/CNDConjuntaInter/InformaNICertidao.asp?tipo=2")
                browser.maximize_window()

                docInput = browser.find_element_by_xpath('/html/body/p/table/tbody/tr/td/p/table/tbody/tr/td/form/input[1]')
                docInput.send_keys(doc)
        else:
            print("\nInsira os dados antes de consultar.")
        
    elif (escolha == 9):
        break


