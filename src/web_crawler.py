import urllib.request as request

def get_page(page):
    """ Takes a valid page url and returns page contents """
    return request.urlopen(page).read()


def main():
    pass

if __name__ == '__main__':
    main()
