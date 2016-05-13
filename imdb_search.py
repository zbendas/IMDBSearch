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


def misc_format(rating_xpath, runtime_xpath, genre_xpath, sep="  |  "):  # sep has formatting intricacies...
    misc_formatted = []
    if rating_xpath:
        if rating_xpath[-1] is not "rating":
            misc_formatted.append("Rating not found" + sep)  # Using this wording as a debug
        else:
            misc_formatted.append(rating_xpath[0] + sep)
    elif not rating_xpath:
        misc_formatted.append("Not yet rated" + sep)

    if runtime_xpath:
        if runtime_xpath[-1] is not "runtime":
            misc_formatted.append("Runtime not found" + sep)  # Using this wording as a debug
        else:
            misc_formatted.append(runtime_xpath[0] + sep)
    elif not runtime_xpath:
        misc_formatted.append("Runtime unknown" + sep)

    if genre_xpath:
        if genre_xpath[-1] is not "genre":
            misc_formatted.append("Genre not found")  # Using this wording as a debug
        else:
            genre_list = [(item + ', ') for item in genre_xpath[0:-2]]
            genre_list.append(genre_xpath[-2])
            for item in genre_list:
                misc_formatted.append(item)
    elif not genre_xpath:
        misc_formatted.append("Genre unknown")
    return misc_formatted


def show_summary(movie_tree, movie):
    # Grab the summary (returns as list)
    xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="summary_text"]/text()|'
                             '//*[@id="title-overview-widget"]//div[@class="summary_text"]/a/text()')
    # xpath is converted to string via .join()
    summary = ''.join(xpath).strip()
    movie.summary = summary
    # Return the string summary or error handler if no summary found
    if summary:
        print("Summary:", summary)
    else:
        print("Summary unavailable for this title.")
        return False


def show_reviews(movie_tree, movie):
    # Grab the review (returns as list)
    xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="imdbRating"]//strong/@title')
    review = ''.join(xpath)
    review = review.strip()
    if review:
        print(review, ".", sep='')
    else:
        print("Title has no reviews.")


def show_misc(movie_tree, movie):
    rating_xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="subtext"]/meta/@content')
    if rating_xpath:
        rating_xpath.append("rating")
    # print(rating_xpath)  # Debug statement

    runtime_xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="subtext"]//'
                                     '*[@itemprop="duration"]/text()')
    if runtime_xpath:
        runtime_xpath.append("runtime")
    # print(runtime_xpath)  # Debug statement
    runtime_xpath = [text.replace('\n', '').strip() for text in runtime_xpath]  # Credit: Falcon Taylor-Carter

    genre_xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="subtext"]//a/'
                                   '*[@itemprop="genre"]/text()')
    if genre_xpath:
        genre_xpath.append("genre")
    # print(genre_xpath)  # Debug statement
    misc = ''.join(misc_format(rating_xpath, runtime_xpath, genre_xpath))
    print(misc)


def search_imdb(override="", print_summary=True, print_misc=True, print_reviews=True):
    # Run search, save results into local variable
    search_string = get_search_results(override)
    movie = Movie(override)
    # Pass resulting search URL into get_html_tree
    movie_tree = get_html_tree(search_string)
    if print_summary:
        show_summary(movie_tree, movie)
    if print_misc:
        show_misc(movie_tree, movie)
    if print_reviews:
        show_reviews(movie_tree, movie)
    print('\n', end='')


class Movie:
    """Base class for all movies"""
    def __init__(self, title, summary='', rating=None, runtime=None, genre=None):
        self.title = title
        self.summary = summary
        self.rating = rating
        self.runtime = runtime
        self.genre = genre

    def __str__(self):
        return self.title

