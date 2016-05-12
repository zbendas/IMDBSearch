from lxml import html
import requests


def GetSearchResults():
    # Collect user search input
    SearchText = input("What movie?\n")
    # Format search URL and grab the search results page
    SearchPage = requests.get('http://www.imdb.com/find?q=' + str(SearchText).strip() + '&s=tt')
    # Create an HTML tree using html.fromstring
    SearchTree = html.fromstring(SearchPage.content)
    # Grab the URL of the first movie page in the search results
    SearchResult = SearchTree.xpath('//td[@class="result_text"][1]/a/@href')
    # Return the string that contains the URL, or error handler if it wasn't found
    if SearchResult:
        return SearchResult[0].strip()
    else:
        print("No movies with this title found.")
        return False
    # print "Search result URL: ", SearchResult[0] #Debug statement


def ShowSummary(movielink):
    # Determine if passed value is False (which means null value in previous function)
    if movielink is False:
        return False
    # Passes movielink parameter to requests.get
    MoviePage = requests.get('http://www.imdb.com' + str(movielink))
    # Generate an HTML tree of movie page
    MovieTree = html.fromstring(MoviePage.content)
    # Grab the summary
    summary = MovieTree.xpath('//*[@id="title-overview-widget"]//div[@class="summary_text"]/text()')  # returns as list
    # Strip first item in list of whitespace, saves it back into list.
    summary[0] = summary[0].strip()
    # Return the string summary or error handler if no summary found
    if summary[0]:
        print("Summary:", summary[0])
    else:
        print("Summary unavailable for this title.")
        return False


def SearchIMDB():
    # Run search, save results into local variable
    SearchString = GetSearchResults()
    # Pass resulting search URL into ShowSummary
    ShowSummary(SearchString)

SearchIMDB()
