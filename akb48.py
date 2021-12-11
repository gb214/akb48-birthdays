from selenium import webdriver
from time import sleep

#SETUP
path = './chromedriver.exe'
driver = webdriver.Chrome(path)

# LET'S START NOW

class girl: #CLASS
    def __init__(self, name, age):
        self.name = name
        self.age = age

girls = []  #LIST OF GIRLS

def search_first_result():
    driver.get("https://dgg.gg")
    print(driver.title)
    print(driver.current_url)

    sleep(2)

    #Google search
    barra_de_pesquisa = driver.find_element_by_name('q')
    barra_de_pesquisa.click()
    barra_de_pesquisa.send_keys('list of akb48 members')
    barra_de_pesquisa.submit()
    sleep(1.5)
    print(driver.current_url)

    #CLICKING

    try:
        clickable_link = driver.find_element_by_css_selector('#r1-0 > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1)')
        clickable_link.click()
        sleep(1)
        print(driver.title)
    except:
        print('clicking failed')

driver.get('https://en.wikipedia.org/wiki/List_of_AKB48_members')
print(driver.title)

table = '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/tbody'
#Finding the amount of tables
tables = '/html/body/div[3]/div[3]/div[5]/div[1]/table'
tabelas = driver.find_elements_by_xpath(tables)
print(len(tabelas))

#Iterating over tables:
for t in range(1, len(tabelas)+1):
    print('\nTABLE NUMBER ' + str(t))
    entries = driver.find_elements_by_xpath(tables + '[' +str(t) + ']/tbody/tr')
    print(len(entries))
    for e in range(1, len(entries)+1):
        nome = tables + '[' + str(t) + ']/tbody/tr[' + str(e) + ']/td[1]'
        birthday = tables + '[' + str(t) + ']/tbody/tr[' + str(e) + ']/td[2]'
        try:
            a = driver.find_element_by_xpath(nome)
            b = driver.find_element_by_xpath(birthday)
            #print(a.text + b.text) #List each of them
            girls.append(girl(a.text, b.text.replace(',','').split()))
        except:
            print('Couldnt find the xpath')

print(len(girls))
for i in girls:
    if i.name == '' or i.age == []:
        girls.remove(i)
print(len(girls))



#Counting:
calendar = [[] for i in range(12*31)]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for member in girls:
    for month in months:
        try:
            if month in member.age:
                calendar[months.index(month)*31 + int(member.age[1])-1].append(member)
        except:
            print('no date available')

for i in calendar:
    if len(i)>1:
        for member in i:
            print(member.name + ' ' + member.age[0] + ' ' + member.age[1])

#Fim
sleep(2)
driver.quit()

