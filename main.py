import configparser

def oqish():
    config = configparser.ConfigParser()
    config.read('settings.ini')

    print("Settings:")
    for section in config.sections():
        print(f"Section: {section}")
        for key, value in config.items(section):
            print(f"{key} = {value}")

oqish()
