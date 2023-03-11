# webdriver-manager
from webdriver_manager.firefox import GeckoDriverManager

# Selenium
from selenium import webdriver

# Native
import configparser
import shutil
import os

from lib.utils import get_config_path 

def set_geckodriver_installation():
    dest_path = "C:\\geckodriver\\"

    try:
        executable_path = GeckoDriverManager().install()
        os.makedirs(dest_path)
        shutil.copy(executable_path, dest_path)

        print("[+] Driver instalado con exito")
    except:
        if not os.path.exists(dest_path + "geckodriver"):
            print("[+] El archivo ya existe.")
        else:
            print("[-] No fue posible configurar driver, configure"
                    "manualmente copiando y pegando el driver a la ruta "
                    "C:\geckodriver\.")

        return 1


def create_config_file():
    # config_path = os.path.join(os.getcwd(), "config", "config.init")
    config_path = get_config_path()
    if not os.path.exists:
        os.makedirs(config_path) 


def set_api_key():
    """
    Check and update the API Key from the config.init file
    """
    # config_path = os.path.join(os.getcwd(), "config", "config.init")
    config_path = get_config_path()

    try:
        config = configparser.ConfigParser()
        config.read(config_path)

        api_virustotal = config.get("VirusTotal", "api_key")
    except (FileNotFoundError):
        print(f"No fue posible encontrar config.ini en ruta \n{config_path}")

    if not api_virustotal:
        new_api = input("[*] Insertar llave API de Virustotal: ") 
        config.set("VirusTotal", "api_key", new_api)

        with open(config_path, "w") as config_file:
            config.write(config_file)
    else:
        print("[+] API configurada con exito.")


def config_checker():
    # config_path = os.path.join(os.getcwd(), "config", "config.init")
    config_path = get_config_path()
    print()
    print(config_path)
    print()

    driver_path = "C:\\geckodriver\\geckodriver.exe"
    if not os.path.exists(config_path) or not os.path.exists(driver_path):
        print("[-] No se han encontrado archivos importantes para el ",
              "funcionanmiento del programa.")
        exit()


def config_arg(optino, opt_str, value, parser):
    """
    Functions wrapper just for arg --config,
    this is not a main function for config.py.
    """
    set_geckodriver_installation()
    create_config_file()
    set_api_key()