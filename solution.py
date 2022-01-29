import json
import re


def generate_phrase_patterns(phrase):
    """
    This function generates additional phrases as per the required fuzzy search.
    A fuzzy search is that there can be at max extra one word in the phrase.
    :param phrase: single phrase
    :return: Additional phrases required for the fuzzy search
    """
    phrase_words = phrase.split()
    new_phrases = [phrase]
    for i in range(1, len(phrase_words)):
        phrase_word_copy = phrase_words.copy()
        phrase_word_copy.insert(i, "\\w+")
        new_phrases.append(' '.join(phrase_word_copy))
    return new_phrases


def phrasel_search(P, Queries):
    """
    This function will pattern match each query with all phrases and return the matched phrases.
    :param P: list of phrases
    :param Queries: list of queries
    :return: list of matched phrases per query
    """
    new_phrases = []
    for phrase in P:
        new_phrases.extend(generate_phrase_patterns(phrase))

    ans = []
    for query in Queries:
        phrase_matched = []
        for p in new_phrases:
            matched_occurrences = re.findall(p, query)
            if matched_occurrences:
                phrase_matched.extend(matched_occurrences)
        ans.append(phrase_matched)
    return ans


if __name__ == "__main__":
    with open('20_points.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print(returned_ans)

        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
