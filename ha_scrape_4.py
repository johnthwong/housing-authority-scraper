#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 13:51:52 2023

@author: John Wong
"""

def scrape(*year_num):
    
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import pandas 
    # import pandas as pd
    import time
    
    years = [str(x) for x in year_num]
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    count_list = pandas.DataFrame(columns = ["year", "month", "count"])
    path = "/Users/john/geckodriver"
    driver = webdriver.Firefox(executable_path=path)
    
    for year in years:
        for month in months:   
            driver.get("https://www.housingauthority.gov.hk/en/home-ownership/hos-secondary-market/transaction-records/index.html")
            select_year_element = driver.find_element(By.CLASS_NAME, "select_dropinner_list.w-dropdown-list")                       

            driver.find_element(By.CLASS_NAME, "selectdrop_inner_select.w-dropdown.transaction-records-selectyear").click()
            
            select_year_element.find_element(By.XPATH, "//*[text()='"+ year +"']").click()
            
            select_month_element = (driver
                                    .find_element(By.CLASS_NAME, "selectdrop_inner_select.w-dropdown.transaction-records-selectmonth")
                                    .find_element(By.CLASS_NAME, "select_dropinner_list.w-dropdown-list"))
            
            driver.find_element(By.CLASS_NAME, "selectdrop_inner_select.w-dropdown.transaction-records-selectmonth").click()
            
            select_month_element.find_element(By.XPATH, "//*[text()='"+ month +"']").click()
            time.sleep(1)
            
            driver.find_element(By.CLASS_NAME, "btn_search.w-button").click()
            
            count = driver.find_element(By.CLASS_NAME, "item__text.item__text-count").text
            dictionary = {"year": [year], "month": [month], "count": [count]}
            count_list = pandas.concat([count_list, pandas.DataFrame(dictionary)],
                                       ignore_index= True)
    df_1 = pandas.DataFrame(count_list)
    df_1.to_csv("ssf_transaction_count.csv")


# select_year = driver.find_element(By.XPATH, "/html/body/div[@id='top'][@class='wrapper']/div[@class='main_section']/div[@class='main_section_left']/div[@class='w-form']")
