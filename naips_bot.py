#coding=utf-8
import urllib.parse
import sys
import urllib.request
from bs4 import BeautifulSoup
import http.cookiejar
import naips_account


def get_initial_cookie(url = "https://www.airservicesaustralia.com/naips/Account/LogOn"):

    init_cookiejar = http.cookiejar.CookieJar()
    init_cookiehandler = urllib.request.HTTPCookieProcessor(init_cookiejar)
    http_opener = urllib.request.build_opener(init_cookiehandler)

    # Air Service Australia need these two header segments to login, otherwise it will return 401 or 500 response.
    # But I still added a custom "OzAtisBot" User-Agent to notice that I'm a bot lol (to make it fair)
    http_opener.addheaders = [
        ("Referrer","https://www.airservicesaustralia.com/naips/"),
        ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36 OzAtisBot/1.0")]

    # Perform request and return the cookies with cookiejar
    urllib.request.install_opener(http_opener)
    urllib.request.urlopen(url)
    return init_cookiejar


def napis_user_login(cookiejar, username, password, url = "https://www.airservicesaustralia.com/naips/Account/LogOn"):

    login_cookiejar = cookiejar
    login_cookiehandler = urllib.request.HTTPCookieProcessor(login_cookiejar)
    http_opener = urllib.request.build_opener(login_cookiehandler)

    login_post_data = urllib.parse.urlencode(
    {
        "UserName":username,
        "Password":password
    }).encode("utf-8")

    http_opener.addheaders = [
        ("Referrer","https://www.airservicesaustralia.com/naips/"),
        ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36 OzAtisBot/1.0")
    ]

    # Perform login with the cookies, then retrieve some new cookies with login token and return
    login_request = urllib.request.Request(url,login_post_data)
    urllib.request.urlopen(login_request)

    return login_cookiejar



def get_met_briefing(query_location, cookiejar, url = "https://www.airservicesaustralia.com/naips/Briefing/Location"):

    # Handle the cookiejar where it gets from previous login page
    briefing_cookiejar = cookiejar,
    briefing_cookiehandler = urllib.request.HTTPCookieProcessor(briefing_cookiejar)
    http_opener = urllib.request.build_opener(briefing_cookiehandler)

    # Create a POST request template
    query_post_data = urllib.parse.urlencode(
        {
            "DomesticOnly": "false",
            "Locations[0]": query_location,
            "Locations[1]": "",
            "Locations[2]": "",
            "Locations[3]": "",
            "Locations[4]": "",
            "Locations[5]": "",
            "Locations[6]": "",
            "Locations[7]": "",
            "Locations[8]": "",
            "Locations[9]": "",
            "Met": "true",
            "NOTAM": "false",
            "HeadOfficeNotam": "false",
            "Validity": "1",
            "SEGMET": "false"

        }).encode("utf-8")

    # Append a fake header, otherwise it will return 401 or 500 response.
    http_opener.addheaders = [
        ("Referrer", "https://www.airservicesaustralia.com/naips/"),
        ("User-Agent",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36 OzAtisBot/1.0")
    ]

    # Perform POST
    login_request = urllib.request.Request(url, query_post_data)
    result_html = urllib.request.urlopen(login_request)

    # Parse the result by BeautifulSoup
    html_parser = BeautifulSoup(result_html, "lxml")
    met_str = html_parser.find_all("pre", {"class": "briefing"})[0].string

    # Return a trimmed result
    return str(met_str).split("-------------------\n\n")[1]     # Remove headers

# ...do a fake "unit test" if this script is executed directly lol...
if __name__ == "__main__":
    print(get_met_briefing("YMML", napis_user_login(get_initial_cookie(), naips_account.naips_username, naips_account.naips_password)))

