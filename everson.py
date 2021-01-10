from selenium import webdriver
from time import sleep

#Test01 - Validar Autenticação" 
driver = webdriver.Chrome()
driver.get("http://localhost:3000/#/sign_in?last_page=/")

print(driver.current_url)
print(driver.capabilities["browserVersion"])

#Preencher  "Username"
elementuser = driver.find_element_by_id("normal_login_username")
elementuser.click()
elementuser.send_keys("testuser")

#Preencher "Password"
elementpsw = driver.find_element_by_id("normal_login_password")
elementpsw.click()
elementpsw.send_keys("pl123")
elementpsw.submit()
sleep(1)

#Checar se a autenticação funcionou.
assert "Good Luck !!!" in driver.find_element_by_xpath("/html/body/div[1]/div/main/div/h2").text


#Test02 - "Pagina 1, Verifica conteudo da tabela"
driver.find_element_by_xpath("//nav/a[1]").click()
sleep(1)

#Verifica se o terceiro elemento da Coluna 1 da Tabela = "JOE Black"
assert "Joe Black" in driver.find_element_by_xpath("//table/tbody/tr[3]/td").text


#Test03 - "Page 2, Verifica Formulario"
driver.find_element_by_xpath("//nav/a[2]").click()
sleep(1)

#Test - Valida Campo da Pagina 2 "Input"
elementimp = driver.find_element_by_class_name("ant-input")
elementimp.click()
elementimp.send_keys("@@@@..@@@@") #Formulario não esta vericando caracter invalido

#Test04 - Validar Acesso da Pagina 3
driver.find_element_by_xpath("//nav/a[3]").click()
sleep(1)
assert "HOME" in driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div[2]/span[1]/span[1]/a").text

#Test05 Validar "Breadcrumb" - HOME
driver.find_element_by_xpath("//main/div/div[2]/span/span[1]/a").click()
sleep(1)
assert "http://localhost:3000/#/" in driver.current_url

#Test06 de Logout "TU"
elementTU = driver.find_element_by_class_name("ant-dropdown-trigger")
elementTU.click()

#Clica no botao "LogOut"
driver.find_element_by_xpath("//div/div/div/ul/li[3]").click()
sleep(1)
assert "http://localhost:3000/#/sign_in?last_page=/" in driver.current_url


sleep(3)
driver.close()




