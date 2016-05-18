from lxml import html
import requests

# Global debug variable, turns on several printed tests
debug = False


def search(title):
    # Run search, save results into local variable
    if debug:
        print("search CALLED")  # Debug statement
    search_string = get_search_results(title)

    # Pass resulting search URL into get_html_tree
    movie_tree = get_html_tree(search_string)
    if debug:
        print("search RETURNING")
    return movie_tree


def get_search_results(title):
    search_text = title
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


def get_summary(movie_tree, movie):
    # Grab the summary (returns as string)
    xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="summary_text"]/text()|'
                             '//*[@id="title-overview-widget"]//div[@class="summary_text"]/a/text()')
    # xpath is converted to string via .join()
    summary = ''.join(xpath).strip()
    # Return the string summary or error handler if no summary found
    if summary:
        movie.summary = summary
    else:
        movie.summary = "Summary unavailable for this title."
        return False


def get_misc(movie_tree, movie):
    if debug:
        print("show_misc CALLED")
    rating_xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="subtext"]/meta/@content')
    if rating_xpath:
        movie.rating = ''.join(rating_xpath)
    if debug:
        print("Movie rating:", movie.rating)  # Debug statement

    runtime_xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="subtext"]//'
                                     '*[@itemprop="duration"]/text()')
    if runtime_xpath:
        movie.runtime = ''.join([text.replace('\n', '').strip() for text in runtime_xpath])
        # Credit: Falcon Taylor-Carter
    if debug:
        print("Movie runtime:", movie.runtime)  # Debug statement

    genre_xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="subtext"]//a/'
                                   '*[@itemprop="genre"]/text()')
    if genre_xpath:
        genre_xpath = ''.join([''.join((item + ', ') for item in genre_xpath[0:-1]), genre_xpath[-1]])
        movie.genre = genre_xpath
    if debug:
        print("Movie genre:", genre_xpath)  # Debug statement
    if debug:
        print("show_misc FINISHED")


def get_reviews(movie_tree, movie):
    # Grab the review (returns as string))
    xpath = movie_tree.xpath('//*[@id="title-overview-widget"]//div[@class="imdbRating"]//strong/@title')
    review = ''.join(xpath).strip()
    if review:
        movie.review = review
    else:
        movie.review = "Title has no reviews."


class Movie:
    """Base class for all movies"""
    def __init__(self, title, summary="Summary unavailable", rating="Rating unknown", runtime="Runtime unknown",
                 genre="Genre unknown", review="No user reviews."):  # Change default argument to "unknown"
        self.title = title
        self.summary = summary
        # Next three lines effectively "self.misc"
        self.rating = rating
        self.runtime = runtime
        self.genre = genre
        self.review = review
        self.alpha_title = self.title.lower()
        self.update()
        self.gen_alpha_title()

    def __str__(self):
        return ''.join(string for string in [self.title, '\n', self.summary, '\n', self.rating,
                                             '  |  ', self.runtime, '  |  ', self.genre, '\n', self.review])

    def __repr__(self):
        return 'Movie(' + ''.join([''.join(string for string in ['\"', self.title, '\", \"', self.summary, '\", \"',
                                                                 self.rating, '\", \"', self.runtime, '\", \"',
                                                                 self.genre, '\", \"', self.review, '\")'])])

    def update(self):
        # Can be called using Movie.update() in order to refresh information, which may have changed on IMDB
        movie_tree = search(self.title)
        get_summary(movie_tree, self)
        get_misc(movie_tree, self)
        get_reviews(movie_tree, self)

    def gen_alpha_title(self):
        if "The " in self.title[0:4]:
            self.alpha_title = self.title.replace("The ", '', 1)
            self.alpha_title += ", The"
            self.alpha_title = self.alpha_title.lower()
        else:
            self.alpha_title = self.title.lower()
