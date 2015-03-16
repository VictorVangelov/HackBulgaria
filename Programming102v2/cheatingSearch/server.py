from flask import Flask
from flask import request
from flask import render_template
from functools import reduce
from website import Spider

app = Flask(__name__)


@app.route('/search/')
def search():
    query = request.args.get('query', '')
    results = list(get_all_searched_results(query))

    return render_template("result.html", SEARCH_TERMS_GO_HERE=query,
     results= results)



prepositions = ["abaft", "abeam", "aboard", "about", "above", 'absent',
                'across', "afore", "after", "against", "along", "alongside",
                "amid", "amidst", "among", "amongst", "anenst", "apropos",
                "apud", "around", "as", "aside", "astride", "at", "athwart",
                "atop", "barring", "before", "behind", "below", "beneath",
                "beside", "besides", "between", "beyond", "but", "by",
                "chez", "concerning", "despite", "down", "during",
                "except", "excluding", "failing", "following", "for",
                "forenenst", "from", "given", "including", "inside",
                "into", "like", "minus", "modulo", "in", "near",
                "next", "of", "off", "on", "onto", "opposite", "the",
                "out", "outside", "over", "pace", "past", "per",
                "plus", "pro", "qua", "regarding", "round", "sans",
                "save", "since", "than", "through", "thru", "an",
                "throughout", "till", "until", "times", "to",
                "toward", "towards", "under", "underneath", "a",
                "unlike", "until", "unto", "up", "upon", "versus",
                "vs", "via", "vice", "with", "within", "without", "worth"]


def is_specific_word(word):
    return not word.lower() in prepositions


def get_specific_words(query):
    search_words = query.split()
    # specific_words = list(filter(is_specific_word, search_words))
    return  (item for item in search_words if is_specific_word(item))


def get_non_specific_words(query):
    search_words = query.split()
    return (item for item in search_words if not is_specific_word(item))


def get_all_searched_results(query):
    all_words = query.split()
    specific_words = get_specific_words(query)
    non_specific_words = get_non_specific_words(query)
    sites_with_all_query = Spider.sorter(get_full_query_sites(all_words))
    sites_with_specific_words = Spider.sorter(get_sites_with_specific_words(specific_words))
    all_combinations_sites = Spider.sorter(get_all_combinations_sites(query))
    all_sites_together = Spider.sorter(all_separated_query_results(query))
    all_sites = [sites_with_all_query, sites_with_specific_words,
     all_combinations_sites, all_sites_together]
    all_results = []
    for list_of_sites in all_sites:
        all_results.extend(list_of_sites)
    return all_results


def get_full_query_sites(all_words):
    return list(map(sort_sites, all_words))

def get_sites_with_specific_words(specific_words):
    return list(map(sort_sites, specific_words))

def get_all_combinations_sites(query):
    specific_words = get_specific_words(query)
    non_specific_words = get_non_specific_words(query)
    all_other_sites = []
    temp_sites = []
    for specific_word in specific_words:
        for non_specific_word in non_specific_words:
            temp_sites = [specific_word, non_specific_word]
            all_other_sites.append(sort_sites(temp_sites))
    return all_other_sites

def all_separated_query_results(query):
    all_words = query.split()
    return list(map(Spider.search_word, all_words))


@app.route('/')
def index():
    # query = request.args.get('query', '')
    return render_template('wsc.html')


def inters(x, y):
    return x & y


def sort_sites(specific_words):
    return Spider.sorter(list(reduce(inters, list(map(Spider.search_word, specific_words)))))


if __name__ == '__main__':
    app.run(debug)
    # app.run()
    # s1 = some_sites
    # s2 = another_sites
    # s3 = dif_s
    # array = [set(s1), set(s2), set(s3)]
    # asd = (reduce(inters, array))
    # print (asd)

    # u = set.intersection((map(list_to_set, array)))
    # print("\n".join(u))
    # search_words = ["asd", "of"]
    # specific_words = list(filter(is_specific_word, search_words))
    # prepositions = list(filter(isnt_specific_word, search_words))
    # print(specific_words)
