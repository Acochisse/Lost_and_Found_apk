#!/usr/bin/python3
from auth_data import *
import mechanicalsoup
import cookielib


class BaseParse(object):
    """BaseParse class
    Contains read json data, and parsed html data for the scrapers
    to use. Also contains general methods to initialize the scrape.
    Args:
        link (str): link to the project page to scrape
    Attributes:
        json_data (dict): read json data from auth_data.json
        soup (obj): BeautifulSoup obj containing parsed link
        dir_name (str): directory name of the link
    """

    def __init__(self, link=""):
        self.htbn_link = link
        self.json_data = self.get_json()
        self.soup = self.get_soup()
        self.dir_name = self.find_directory()

    @property
    def htbn_link(self):
        return self.__htbn_link

    @htbn_link.setter
    def htbn_link(self, value):
        """Setter for htbn link
        Must contain holberton's url format for projects.
        Args:
            value (str): comes from argv[1] as the project link
        """
        valid_link = "https://intranet.hbtn.io/dashboards/my_planning"
        ##while not (valid_link in value):
          ##  print("[ERROR] Invalid link (must be to project on intranet.hbtn.io)")
            ##value = raw_input("Enter link to project: ")
        self.__htbn_link = valid_link

    def get_json(self):
        """Method that reads auth_data.json.
        Sets json read to `json_data`
        """
        super_path = os.path.dirname(os.path.abspath(__file__))
        try:
            with open("{}/auth_data.json".format(super_path.rsplit("/", 1)[0]), "r") as json_file:
                return json.load(json_file)
        except IOError:
            print("[ERROR] Please run ./setup.sh to setup your auth data...")
            sys.exit()

    def get_soup(self):
        """Method that parses the `htbn_link` with BeautifulSoup
        Initially logs in the intranet using mechanize and cookiejar.
        Then requests for the html of the link, and sets it into `soup`.
        Returns:
            soup (obj): BeautifulSoup parsed html object
        """
        login = "https://intranet.hbtn.io/auth/sign_in"
        cj = cookielib.CookieJar()
        br = mechanicalsoup.Browser()

        sys.stdout.write("  -> Logging in... ")
        try:
            br.set_cookiejar(cj)
            br.open(login)
            br.select_form(nr=0)
            br.form['user[login]'] = self.json_data["intra_user_key"]
            br.form['user[password]'] = self.json_data["intra_pass_key"]
            br.submit()
            page = br.open(self.__htbn_link)
        except AttributeError:
            print("[ERROR] Login failed - are your auth_data credentials correct?")
            sys.exit()

        print("done")
        self.soup = BeautifulSoup(page, 'html.parser')
        br.close()
        del page
        return self.soup

if __name__ == "__main__":
    login_browser_run()
