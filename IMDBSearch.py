from lxml import html
import requests


def get_search_results():
    # Collect user search input
    search_text = input("What movie?\n")
    # Format search URL and grab the search results page
    search_page = requests.get('http://www.imdb.com/find?q=' + str(search_text).strip() + '&s=tt')
    # Create an HTML tree using html.fromstring
    search_tree = html.fromstring(search_page.content)
    # Grab the URL of the first movie page in the search results
    search_result = search_tree.xpath('//td[@class="result_text"][1]/a/@href')
    # Return the string that contains the URL, or error handler if it wasn't found
    if search_result:
        return search_result[0].strip()
    else:
        print("No movies with this title found.")
        return False
    # print "Search result URL: ", search_result[0] #Debug statement


def show_summary(movie_link):
    # Determine if passed value is False (which means null value in previous function)
    if movie_link is False:
        return False
    # Passes movie_link parameter to requests.get
    movie_page = requests.get('http://www.imdb.com' + str(movie_link))
    # Generate an HTML tree of movie page
    movie_tree = html.fromstring(movie_page.content)
    # Grab the summary
    summary = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="summary_text"]/text()')  # returns as list
    # Strip first item in list of whitespace, saves it back into list.
    summary[0] = summary[0].strip()
    # Return the string summary or error handler if no summary found
    if summary[0]:
        print("Summary:", summary[0])
    else:
        print("Summary unavailable for this title.")
        return False


def search_imdb():
    # Run search, save results into local variable
    search_string = get_search_results()
    # Pass resulting search URL into ShowSummary
    show_summary(search_string)

search_imdb()
