import requests
import pytest


def main():
    # list of US presidents
    presidentList = ["Adams", "Arthur", "Biden", "Buchanan", "Bush", "Carter", "Cleveland", "Clinton", "Coolidge",
                     "Eisenhower", "Fillmore", "Ford", "Garfield", "Grant", "Harding", "Harrison", "Hayes", "Hoover",
                     "Jackson", "Jefferson", "Johnson", "Kennedy", "Lincoln", "Madison", "McKinley", "Monroe", "Nixon",
                     "Obama", "Pierce", "Polk", "Reagan", "Roosevelt", "Taft", "Taylor", "Truman", "Trump", "Tyler",
                     "Van Buren", "Washington", "Wilson"]
    # DuckDuckGo Api Info
    duck_url = "https://api.duckduckgo.com"
    # Getting data from DDG
    response = requests.get(duck_url + "/?q=presidents+of+the+united+states&format=json")
    # Reading data from DDG into the data variable
    data = response.json()
    # Generating the related topics list
    relatedTopicsList = data["RelatedTopics"]

    ListOfPresidents = []
    for name in relatedTopicsList:
        ListOfPresidents.append(name['Text'])
    print(ListOfPresidents)

    # pytest section
    @pytest.mark.parametrize("presidentNameList", presidentList)
    def test_presidents(presidentNameList):
        assert presidentNameList in ListOfPresidents == presidentList


main()
