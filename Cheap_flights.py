from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
import time

import pandas as pd

import smtplib
from email.message import EmailMessage

import schedule

departure_month = "Dec"
departure_date = '11'
arrival_month = "Jan"
arrival_date = '05'
departure_flight_inputs={'Departure': " SHV",
               'Arrival': " ACT",
               'Date': f"{departure_month} {departure_date}, 2024"}

return_flight_inputs={'Departure': " ACT",
               'Arrival': " SHV",
               'Date': f"{arrival_month} {arrival_date}, 2025"}

def find_cheapest_flights(flight_info):
    PATH = 'C:\Users\Patrick .A. Asamoah\Desktop\adwuma\new_life\chromedriver-win64'
    driver = webdriver.Chrome(executable_path=PATH)

    leaving_from = flight_info['Departure']
    going_to = flight_info['Arrival']
    trip_date = flight_info['Date']
    

    driver.get("https://expedia.com")

    flight_xpath = '//a[@aria-controls="search_form_product_selector_flights"]'
    flight_element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, flight_xpath))
        )
    flight_element.click()
    time.sleep(0.2)

    oneway_xpath = '//a[@aria-controls="FlightSearchForm_ONE_WAY"]' 
    one_way_element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, oneway_xpath))
        )
    one_way_element.click()
    time.sleep(0.2)

    leaving_from_xpath = '//button[@aria-label="Leaving from"]'
    leaving_from_element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, leaving_from_xpath))
        )
    leaving_from_element.clear
    leaving_from_element.click()
    time.sleep(1)
    leaving_from_element.send_keys(leaving_from)
    
    time.sleep(1)
    leaving_from_element.send_keys(Keys.DOWN, Keys.RETURN)

    going_to_xpath = '//button[@aria-label="Going to"]'
    going_to_element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, going_to_xpath))
        )
    going_to_element.clear
    going_to_element.click()
    time.sleep(1)
    going_to_element.send_keys(going_to)
    
    time.sleep(1)
    going_to_element.send_keys(Keys.DOWN, Keys.RETURN)

    departing_box_xpath = f'//button[@aria-label="Date {departure_month} {departure_date}"]'
    
    depart_box_element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, departing_box_xpath))
        )
    
    depart_box_element.click()
    time.sleep(2)