from lxml import html
import requests


def get_search_results(override=""):
    if override is not "":
        search_text = override
    else:
        # Collect user search input
        search_text = input("What title?\n")
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


def get_html_tree(movie_link):
    # Determine if passed value is False (which means null value in previous function)
    if movie_link is False:
        return False
    # Passes movie_link parameter to requests.get
    movie_page = requests.get('http://www.imdb.com' + str(movie_link))
    # Generate an HTML tree of movie page
    movie_tree = html.fromstring(movie_page.content)
    return movie_tree


def trimmer(xpath):
    i = 0
    while i < (len(xpath)-1):
        print(i, xpath[i], 'END')
        xpath[i] = xpath[i].replace('\n', '')
        xpath[i] = xpath[i].strip()
        print(i, xpath[i], 'END\n----------')
        i += 1
    # This still returns a list
    return xpath


def show_summary(movie_tree):
    # Grab the summary (returns as list)
    xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="summary_text"]/text()|'
                             '//*[@id="title-overview-widget"]//div[@class="summary_text"]/a/text()')
    # xpath is converted to string via .join()
    summary = ''.join(xpath)
    summary = summary.strip()
    # Return the string summary or error handler if no summary found
    if summary:
        print("Summary:", summary)
    else:
        print("Summary unavailable for this title.")
        return False


def show_reviews(movie_tree):
    # Grab the review (returns as list)
    xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="imdbRating"]//strong/@title')
    review = ''.join(xpath)
    review = review.strip()
    if review:
        print(review, ".", sep='')
    else:
        print("Title has no reviews.")


def show_misc(movie_tree):
    xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="title_wrapper"]/div[@class="subtext"]'
                             '/child::text()|'
                             '//*[@id="title-overview-widget"]//div[@class="title_wrapper"]/div[@class="subtext"]'
                             '//*[@itemprop]/text()')
    print("Untrimmed: \n", xpath)
    xpath = trimmer(xpath)
    misc = ''.join(xpath)
    print("Final: \n", misc, sep='')


def search_imdb(override="", print_summary=True, print_misc=True, print_reviews=True):
    # Run search, save results into local variable
    search_string = get_search_results(override)
    # Pass resulting search URL into get_html_tree
    movie_tree = get_html_tree(search_string)
    if print_summary:
        show_summary(movie_tree)
    if print_misc:
        show_misc(movie_tree)
    if print_reviews:
        show_reviews(movie_tree)
    print('\n', end='')
