import logging
from pathlib import Path
from selenium import undetected_chromedriver as ucd

def define_global_variables():
    global user_data, logger 
    user_data = []

def get_user_data():
    global user_data, logger
    
    f = open("userData.txt", "r")
    lines = f.readlines()
    
    for line in lines:
        variables = line.strip().split(",")
        
        if len(variables) < 2:
            logger.error("There aren't enough variables to process the file")
            break
        elif len(variables) > 2:
            logger.error("There are too many variables to process the file")
            break
        
        username, access_key = variables
        
        data = {
        }
        
        user_data.append(data)

def start_chrome_automation():
    global logger
    
    logger = utility.get_logger("Chrome", "chrome.log")
    logger.info("Starting Chrome automation")
    define_global_variables()
    get_user_data()
    