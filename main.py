from storage import *
from selenium.webdriver.common.by import By

import os


if __name__ == "__main__":
    try:
        driver.get(url_kufar_videocards)
        sleep_driver(driver, 6)
        
        if not os.path.exists('cookies'):
            save_cookies(driver=driver)
            print("Cookies are saved!")
            exit()
        
        for cookie in pickle.load(open("cookies", "rb")):
            driver.add_cookie(cookie)
            
        sleep_driver(driver, 3)
        driver.refresh()
        sleep_driver(driver, 6)
        
        page = 0
        first_page = True 
        
        all_data = []
        while True:
                
            # all products in one page
            product_list = driver.find_elements(by=By.XPATH, value="//a[@class='styles_wrapper__pb4qU']")
            
            item = 0
            for p in product_list:
                p.click()
                sleep_driver(driver, 3)
                
                driver.switch_to.window(driver.window_handles[1])
                sleep_driver(driver, 3)
                
                product_title = driver.find_element(by=By.XPATH, value='//h1[@class="styles_brief_wrapper__title__x59rm"][@data-name="av_title"]').text
                product_price = driver.find_element(by=By.XPATH, value='//span[@class="styles_price--main__VMpTN"]').text
                product_date = driver.find_element(by=By.XPATH, value='//span[@class="styles_brief_wrapper__date__FfOke"]').text
                product_link = driver.current_url
                
                if DEBUG:
                    print(product_title, '-', product_link)
                    print(product_price)
                    print(product_date)
                    print()
                    
                all_data.append({
                    'title': product_title,
                    'price': product_price,
                    'date': product_date,
                    'link': product_link
                })
                sleep_driver(driver, 3)
                
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                sleep_driver(driver, 1)
                
                if DEBUG:
                    item += 1
                    if item == 2:
                        break
                
        
            if first_page:
                next_page = driver.find_element(by=By.XPATH, value='//a[@class="styles_link__KajLs styles_arrow__fJMcy"]').click()
                if DEBUG: print("First page")
                first_page = False 
            else:
                next_page = driver.find_elements(by=By.XPATH, value='//a[@class="styles_link__KajLs styles_arrow__fJMcy"]')
                if DEBUG: print("Len next page: ", len(next_page))
                next_page[1].click()
            if DEBUG:
                page += 1
                print("Page ", page)
            sleep_driver(driver, 10)
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()