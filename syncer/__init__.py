import base64
import sqlite3
import time
import sys
import io
import traceback
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from requests import Session

from logger import Logger


class Syncer:
    def __init__(
            self,
            settings: dict,
            LOGGER: Logger
    ):
        self.sessions = {
            "Oiclass": Session(),
            "HydroOJ": Session(),
            "UOJ": Session(),
            "Codeforces": Session()
        }
        self.logan = {
            "Oiclass": False,
            "HydroOJ": False,
            "UOJ": False,
            "Codeforces": False
        }
        self.oiclass_domain = {}
        self.hydrooj_domain = {}
        self.pool = ThreadPoolExecutor(max_workers=4)
        self.settings = settings
        self.LOGGER = LOGGER

    def login(self, site: str):
        match site:
            case "Oiclass":
                self.pool.submit(lambda: self.login_oiclass())
            case "HydroOJ":
                self.pool.submit(lambda: self.login_hydrooj())
            case "UOJ":
                self.pool.submit(lambda: self.login_uoj())
            case "Codeforces":
                self.pool.submit(lambda: self.login_codeforces())

    def check_login(self, site: str) -> bool:
        return self.logan[site]

    def login_oiclass(self):
        if self.check_login("Oiclass"):
            return 1
        self.sessions["Oiclass"].post(url="http://www.oiclass.com/login", data={
            "uname": self.settings["oiclassUsername"],
            "password": self.settings["oiclassPassword"],
            "rememberme": "on"
        })
        page = self.sessions["Oiclass"].get("http://www.oiclass.com/home/domain").text
        soup = BeautifulSoup(features="lxml", markup=page)

        for i in soup.find_all(class_="typo-a", name="a"):
            self.oiclass_domain[i["href"].split("/")[2]] = False

        self.LOGGER.log(20, str(self.oiclass_domain))

        self.logan["Oiclass"] = True
        return 0

    def login_hydrooj(self):
        if self.check_login("HydroOJ"):
            return 1
        self.sessions["HydroOJ"].post(url="https://hydro.ac/login", data={
            "uname": self.settings["hydroojUsername"],
            "password": self.settings["hydroojPassword"],
            "rememberme": "on"
        })

        page = self.sessions["HydroOJ"].get("https://hydro.ac/home/domain").text
        soup = BeautifulSoup(features="lxml", markup=page)

        for i in soup.find_all(class_="typo-a", name="a"):
            self.hydrooj_domain[i["href"].split("/")[2]] = False

        self.LOGGER.log(20, str(self.hydrooj_domain))

        self.logan["HydroOJ"] = True
        return 0

    def login_uoj(self):
        if self.check_login("UOJ"):
            return 1
        self.sessions["UOJ"].post(url="https://uoj.ac/login", data={
            "username": self.settings["uojUsername"],
            "password": self.settings["uojPassword"]
        })
        self.logan["UOJ"] = True
        return 0

    def login_codeforces(self):
        if self.check_login("Codeforces"):
            return 1
        self.sessions["Codeforces"].post(url="https://codeforces.com/enter", data={
            "handleOrEmail": self.settings["codeforcesUsername"],
            "password": self.settings["codeforcesPassword"],
            "remember": "on"
        }, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
        })
        self.logan["Codeforces"] = True

    def sync(self, site: str):
        match site:
            case "Oiclass":
                self.pool.submit(lambda: self.sync_oiclass())
            case "HydroOJ":
                self.pool.submit(lambda: self.sync_hydrooj())
            case "UOJ":
                self.pool.submit(lambda: self.sync_uoj())
            case "Codeforces":
                self.pool.submit(lambda: self.sync_codeforces())

    def sync_oiclass(self, domain: str = "system"):
        page = self.sessions["Oiclass"].get(f"http://www.oiclass.com/d/{domain}/").text
        self.oiclass_domain[domain] = True
        if "Oops!" in page or "앗..!" in page:
            return 0
        try:
            db = sqlite3.connect("data.db")
            if not self.check_login("Oiclass"):
                return 1
            self.LOGGER.log(30, f"Syncing Oiclass - {domain}")
            pg = 0
            record_urls = []
            while True:
                pg += 1
                reach = False
                page = self.sessions["Oiclass"].get(f"http://www.oiclass.com/d/{domain}/record?page="
                                                    f"{pg}&uidOrName={self.settings['oiclassUsername']}&status=1").text
                soup = BeautifulSoup(features="lxml", markup=page)
                for i in soup.find_all(name="a", class_="record-status--text pass"):
                    if "/record/" in i["href"]:
                        record_urls.append(i["href"])
                        reach = True

                if not reach:
                    break

            self.LOGGER.log(10, str(record_urls))
            for i in record_urls:
                self.LOGGER.log(10, f"http://www.oiclass.com{i}")
                page = self.sessions["Oiclass"].get(f"http://www.oiclass.com{i}").text
                if "Oops!" in page or "앗..!" in page:
                    if "View hidden problems" in page:
                        continue
                    else:
                        time.sleep(10)
                        page = self.sessions["Oiclass"].get(f"http://www.oiclass.com{i}").text
                soup = BeautifulSoup(features="lxml", markup=page)
                pid = ""
                for j in soup.find_all(name="a"):
                    if "/p/" in j["href"]:
                        pid = j.text
                        break
                self.LOGGER.log(10, str(pid))
                code = soup.find(name="code")
                if code is not None:
                    code = base64.b32encode(code.text.encode("utf-8")).decode("utf-8")

                    for j in db.execute(
                            f"SELECT count(*) FROM problems WHERE pid='{pid}' AND site='Oiclass - {domain}';"):
                        cnt = j[0]
                    if cnt == 0:
                        self.LOGGER.log(10,
                                        f"INSERT INTO problems (pid, site, code) VALUES ('{pid}', 'Oiclass - {domain}', '{code}');")
                        db.execute(
                            f"INSERT INTO problems (pid, site, code) VALUES ('{pid}', 'Oiclass - {domain}', '{code}');")
                        db.commit()
        except Exception:
            traceback.print_exc()
        self.LOGGER.log(30, f"Done with Oiclass - {domain}")

        for i in self.oiclass_domain:
            if not self.oiclass_domain[i]:
                self.sync_oiclass(domain=i)

    def sync_hydrooj(self, domain: str = "system"):
        page = self.sessions["HydroOJ"].get(f"https://hydro.ac/d/{domain}/").text
        self.hydrooj_domain[domain] = True
        if "Oops!" in page or "앗..!" in page:
            return 0
        try:
            db = sqlite3.connect("data.db")
            if not self.check_login("HydroOJ"):
                return 1
            self.LOGGER.log(30, f"Syncing HydroOJ - {domain}")
            pg = 0
            record_urls = []
            while True:
                pg += 1
                reach = False
                page = self.sessions["HydroOJ"].get(f"https://hydro.ac/d/{domain}/record?page="
                                                    f"{pg}&uidOrName={self.settings['hydroojUsername']}&status=1").text
                soup = BeautifulSoup(features="lxml", markup=page)
                for i in soup.find_all(name="a", class_="record-status--text pass"):
                    if "/record/" in i["href"]:
                        record_urls.append(i["href"])
                        reach = True

                if not reach:
                    break

            self.LOGGER.log(10, str(record_urls))
            for i in record_urls:
                self.LOGGER.log(10, f"https://hydro.ac{i}")
                page = self.sessions["HydroOJ"].get(f"https://hydro.ac{i}").text
                if "Oops!" in page or "앗..!" in page:
                    if "View hidden problems" in page:
                        continue
                    else:
                        time.sleep(10)
                        page = self.sessions["HydroOJ"].get(f"https://hydro.ac{i}").text
                soup = BeautifulSoup(features="lxml", markup=page)
                for j in soup.find_all(name="a"):
                    if "/p/" in j["href"]:
                        pid = j.text
                        break
                self.LOGGER.log(10, str(pid))
                code = soup.find(name="code")
                if code is not None:
                    code = base64.b32encode(code.text.encode("utf-8")).decode("utf-8")

                    for j in db.execute(
                            f"SELECT count(*) FROM problems WHERE pid='{pid}' AND site='HydroOJ - {domain}';"):
                        cnt = j[0]
                    if cnt == 0:
                        self.LOGGER.log(10, f"INSERT INTO problems (pid, site, code) "
                                            f"VALUES ('{pid}', 'HydroOJ - {domain}', '{code}');")
                        db.execute(
                            f"INSERT INTO problems (pid, site, code) VALUES ('{pid}', 'HydroOJ - {domain}', '{code}');")
                        db.commit()
        except Exception:
            traceback.print_exc()
        self.LOGGER.log(30, f"Done with HydroOJ - {domain}")

        for i in self.hydrooj_domain:
            if not self.hydrooj_domain[i]:
                self.sync_hydrooj(domain=i)

    def sync_uoj(self):
        try:
            if not self.check_login("UOJ"):
                return 1
            db = sqlite3.connect("data.db")
            page = self.sessions["UOJ"].get(
                f"https://uoj.ac/submissions?submitter={self.settings['uojUsername']}&min_score=100&max_score=100").text
            soup = BeautifulSoup(features="lxml", markup=page)
            record_urls = []
            for i in soup.find_all(name="a", class_="uoj-score"):
                record_urls.append(i["href"])

            self.LOGGER.log(10, str(record_urls))

            for i in record_urls:
                self.LOGGER.log(10, f"https://uoj.ac{i}")
                page = self.sessions["UOJ"].get(f"https://uoj.ac{i}").text
                soup = BeautifulSoup(features="lxml", markup=page)

                for j in soup.find_all(name="a"):
                    if "/problem/" in j["href"]:
                        pid = j.text
                        break

                self.LOGGER.log(10, pid)
                code = soup.find(name="code")
                if code is not None:
                    code = base64.b32encode(code.text.encode("utf-8")).decode("utf-8")

                    for j in db.execute(f"SELECT count(*) FROM problems WHERE pid='{pid}' AND site='UOJ';"):
                        cnt = j[0]
                    if cnt == 0:
                        self.LOGGER.log(10,
                                        f"INSERT INTO problems (pid, site, code) VALUES ('{pid}', 'UOJ', '{code}');")
                        db.execute(
                            f"INSERT INTO problems (pid, site, code) VALUES ('{pid}', 'UOJ', '{code}');")
                        db.commit()

            self.LOGGER.log(30, "Done with UOJ")
        except Exception:
            traceback.print_exc()

    def sync_codeforces(self):
        try:
            if not self.check_login("Codeforces"):
                return 1
            db = sqlite3.connect("data.db")
            page = self.sessions["Codeforces"].post(
                f"https://codeforces.com/submissions/{self.settings['codeforcesUsername']}", data={
                    "verdictName": "OK",
                }, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
                }).text
            soup = BeautifulSoup(features="lxml", markup=page)
            record_urls = []

            self.LOGGER.log(30, "Syncing Codeforces")

            for i in soup.find_all(name="a"):
                if "/contest/" in i["href"]:
                    record_urls.append(i["href"])

            self.LOGGER.log(10, str(record_urls))

            for i in record_urls:
                self.LOGGER.log(10, f"https://codeforces.com{i}")
                page = self.sessions["Codeforces"].get(f"https://codeforces.com{i}").text
                soup = BeautifulSoup(features="lxml", markup=page)
                pid = ""

                for j in soup.find_all(name="a"):
                    if "/problem/" in j["href"]:
                        pid = j.text
                        break

                self.LOGGER.log(10, pid)
                code = soup.find(name="pre", id="program-source-text")
                if code is not None:
                    code = base64.b32encode(code.text.encode("utf-8")).decode("utf-8")
                    for j in db.execute(f"SELECT count(*) FROM problems WHERE pid='{pid}' AND site='Codeforces';"):
                        cnt = j[0]
                    if cnt == 0:
                        self.LOGGER.log(10, f"INSERT INTO problems (pid, site, code) VALUES ('{pid}', 'Codeforces', '{code}');")
                        db.execute(
                            f"INSERT INTO problems (pid, site, code) VALUES ('{pid}', 'Codeforces', '{code}');")
                        db.commit()

            self.LOGGER.log(30, "Done with Codeforces")
        except Exception:
            traceback.print_exc()
