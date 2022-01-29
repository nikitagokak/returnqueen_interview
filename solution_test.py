import unittest
from solution import phrasel_search

class MyTestCase(unittest.TestCase):
    def test_something(self):
        phrases = [
            "balance goodbye lot forget",
            "health contact ever big",
            "business become for chap",
            "approach field",
            "else after blow inform",
            "around egg expect learn",
            "add bad",
            "increase accept",
            "close box",
            "afford bad"
          ]
        query = ["close box son add bad strong afford down bad middle"]
        answer = phrasel_search(phrases, query)
        assert len(answer[0]) == 3
        assert answer[0].count("close box") == 1
        assert answer[0].count("add bad") == 1
        assert answer[0].count("afford down bad") == 1

    def test_20point_sample(self):
        phrases = [
            "almost brother",
            "important let",
            "invest improve",
            "express a",
            "food economy fine fortune",
            "drink feel",
            "bad forward buy apparent",
            "improve both major as",
            "identify budget",
            "hold awful",
            "attend die",
            "assume although"
            ]
        query = ["assume although sign"]
        answer = phrasel_search(phrases, query)
        assert len(answer[0]) == 1
        assert answer[0].count("assume although") == 1

    def test_30point_sample(self):
        phrases = [
            "fund environment document king",
            "field example",
            "club achieve commit happy",
            "fit amount any converse",
            "happy appear heavy listen",
            "danger care",
            "bad eat hear final",
            "cost green",
            "about consult",
            "hell interest colour force",
            "dead light",
            "area english",
            "deal green",
            "also jump",
            "cup apart for fund",
            "garden cold",
            "fish fight call compare",
            "bill have",
            "difference buy",
            "local involve certain design",
            "during he",
            "environment hate london care",
            "elect for",
            "educate allow job another",
            "general into function hang",
            "base if lunch husband",
            "do count end idea",
            "let all",
            "hullo because hard happy",
            "during budget commit likely",
            "economy eat fair certain",
            "force game divide horse",
            "appropriate blue",
            "doctor cheap corner fly",
            "die lad boat bring",
            "educate for city exercise",
            "enjoy laugh",
            "bar by direct day",
            "bed detail after bottle",
            "instead agent",
            "basis detail",
            "car king approach during",
            "get any appropriate force",
            "electric bar",
            "allow centre",
            "general field know invest",
            "cost accept learn divide",
            "clear absolute leg care",
            "district finance again agent",
            "bed guy cost enjoy",
            "join eat extra feed",
            "answer doctor",
            "be increase council hospital",
            "grant germany free by",
            "contract even",
            "imagine able car luck",
            "live britain",
            "bear let grow holiday",
            "especial appoint long by",
            "into garden authority from",
            "detail friend",
            "boat little county due",
            "cake fun",
            "main early look art",
            "large during",
            "basis land full have",
            "hullo comment",
            "inside bloke",
            "lose king hall college",
            "floor bad",
            "body consider lot hear",
            "continue debate",
            "inside laugh except body",
            "laugh cut base at",
            "have encourage drop foot",
            "link hear charge hot",
            "fact boat",
            "argue already",
            "christmas eight",
            "benefit close condition across",
            "cake close",
            "father hell cheap compute",
            "give local",
            "deal hand judge before",
            "friday a few elect",
            "garden dog",
            "great less fall be",
            "forward approach due effect",
            "beat as",
            "community down current lead",
            "age condition",
            "county early",
            "build job foot experience",
            "early equal",
            "break front bring flat",
            "door great group definite",
            "let improve",
            "exist birth college chairman",
            "city how",
            "lead dead girl exist",
            "client how affect along",
            "best he",
            "ball include",
            "down achieve ask learn",
            "guy express",
            "corner hullo",
            "child board coffee actual",
            "far food",
            "converse kitchen by general",
            "because course interest imagine",
            "age life early cent",
            "fire exercise",
            "all child",
            "fortune age",
            "client few character cold",
            "income bloke in leg",
            "dad body alright main",
            "ask compare exist a",
            "grand document",
            "any garden every kind"
        ]
        query = ["about consult quick dad body alright main very field example responsible"]
        answer = phrasel_search(phrases, query)
        assert len(answer[0]) == 3
        assert answer[0].count("about consult") == 1
        assert answer[0].count("dad body alright main") == 1
        assert answer[0].count("field example") == 1

    def test_50point_empty_ans(self):
        phrases = [
            "else although",
            "major affect",
            "catch bit",
            "lock improve drop america",
            "elect live exercise large",
            "invest away experience affect",
            "bring committee kid care",
            "form apply brilliant fish",
            "doctor absolute",
            "act father"
        ]
        query = ["air million"]
        answer = phrasel_search(phrases, query)
        assert len(answer[0]) == 0








if __name__ == '__main__':
    unittest.main()
