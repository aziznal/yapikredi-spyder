# Import your Spyder here

from selenium.webdriver.firefox.options import Options as FirefoxOptions


def make_spyder():
    
    url = ''

    options = FirefoxOptions()
    options.headless = True

    # TODO: replace with an instance of your bank spyder
    spyder = CustomSpyderNameHere(url=url, options=options)

    return spyder
