from YapiKrediSpyder import YapiKrediSpyder
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def make_spyder():

    url = 'https://www.yapikredi.com.tr/yatirimci-kosesi/doviz-bilgileri'

    options = FirefoxOptions()
    options.headless = True

    # TODO: replace with an instance of your bank spyder
    spyder = YapiKrediSpyder(url=url, options=options)

    return spyder
