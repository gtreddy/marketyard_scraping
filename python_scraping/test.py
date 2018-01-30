from webScraping import  HTMLTableParser
hp=HTMLTableParser()
table=hp.parse_url("http://www.puneapmc.org/history.aspx?id=Rates3144")
table.head()
