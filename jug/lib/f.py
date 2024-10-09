# from flask import Flask
# from flask import flask
# import html
# from flask import redirect
# from markupsafe import Markup, escape
from markupsafe import escape
import random
import os

class F():


    def uwsgi_log(msg):

        # log_path = os.getcwd() + "/etc/log/uwsgi.log"
        log_path = os.getcwd() + "/etc/log/debug.log"
        # os.system("echo " + msg + " >> " + log_path)
        os.system(f"echo '--- {msg}' >> {log_path}")


    # escape("<script>alert(document.cookie);</script>")
    # Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')

    def checkPathSlash(url):
        # checks that url ends in slash

        # url2 = url.rstrip('/')  # right-strip;
            # This always makes sure there's no final slash;
        url2 = url.rstrip('/') + "/"
            # This makes usre there is always a final slash;
        if url2 != url:
            # return redirect('/' + url2, code=301)
            # return redirect('/' + url2, code=301)
                # The / makes the redirect at the root; otherwise, will just append the url;
            # return "here"
            # 301 /url2   # Not sure what this is about; doesn't seem to work;
            # if there's a / at url, then redirect to non-slash url;

            # raise redirect_to('/' + url2)

            return '/' + url2
        else:
            # return True
            return False

        # There doesn't seem to be a way to redirect directly from here; have to do a return; very lame!

    def stripJinjaWhiteSpace(pageHtml):
        # pageHtml = pageHtml.replace('\n', '').replace('   ', '').replace('  ', '')
        # # return pageHtml.replace('    ', '')
        # return pageHtml

        return ' '.join(pageHtml.split())
        # Split the string by white spaces and put into a list; then join back using ' ' (space)
        # Supposed to at most leave 1 white space;
        # Not perfect though; see white space between '> <', for instance;
        # Not sure about speed between this and doing replace command;

    def hesc(str):
        # result = flask.escape(str)
          # Not work
        # result = html.escape(str)
          # Works
        result = escape(str)
          # Works
        # return str
        return result


    def cd():
        import os

        cwd = os.getcwd()
        print(cwd)


    def getPop():

        # import math

        # random.seed()
        # num1 = 200 * random.random()
        # num2 = num1 * random.random()
        # num3 = num2 * random.random()
        # pop = num2 * num3 * num1
        # return math.ceil(pop)
        # return randrange(101, 100000)
          # Return a randomly selected element from range(start, stop, step).
        return f"{random.randint(1000, 8000000):,d}"
          # Return a random integer N such that a <= N <= b.
          # Alias for randrange(a, b+1).
          # Also add thousand separator;


    def getMoon(moon_phase=False):
        # moonArr = ['◐', '◑', '◒', '◓', '◔', '◕']
        # return moonArr[random.randrange(0, 6)]
        # return random.choice(moonArr)
          # Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

        # random.randInt(0, 5)  # This returns from 0 to 5, including 5
        # random.randrange(0,6) # This returns from 0 to 5, excludes 6

        moonList_emoji = ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘']
        moonList_str = ["New", "Waxing Crescent", "First Quarter", "Waxing Gibbous", "Full", "Waning Gibbous", "Last Quarter", "Waning Crescent"]


        # Return the emoji and text
        # If no specific moon phase provided, then get random:
        if  moon_phase:
            for index, moon in enumerate(moonList_str):
                if moon_phase.lower() == moon.lower():
                    return [moonList_str[index], moonList_emoji[index]]

        # If still here, then get random moon phase
        max = len(moonList_emoji)
        rnd = random.randrange(0, max)

        return [moonList_str[rnd], moonList_emoji[rnd]]


        # moonDict = {
        #     "New Moon": '🌑',
        #     "Waxing Crescent Moon":'🌒',
        #     "First Quarter Moon":'🌓',
        #     "Waxing Gibbous Moon":'🌔',
        #     "Full Moon":'🌕',
        #     "Waning Gibbous Moon":'🌖',
        #     "Last Quarter Moon":'🌗'
        #     "Waning Crescent Moon":'🌘'
        # }
        # # randomly pop item from dictionary as a list;
        # # Should return as: ["New Moon", "🌑"]

        # moonList = moonDict.popitem()
        # return moonList


    def getAdverb():
        adverbs_list = [
            "Turning",
            "Spinning",
            "Glowing",
            "Whirling",
            "Gyrating",
            "Pivotting",
            "Swiveling",
            "Twisting",
            "Rolling",
            "Smiling",
            "Grinning",
            "Stumbling",
            "Rolicking"
        ]

        rnum = random.randint(0, len(adverbs_list)-1)
        return adverbs_list[rnum]

    def getAdjective():
        adjectives_list = [
            "beautiful",
            "bucolic",
            "decrepit",
            "dilapidated",
            "perilous",
            "friendly",
            "tax-free",
            "high-crime",
            "sinking",
            "modern",
            "floating",
            "callow",
            "guilty",
            "unkempt",
            "maniculred",
            "abandoned",
            "fashionable",
            "gastronomic",
            "landlocked",
            "windy",
            "rainy",
            "snowy",
            "humid",
            "putrid",
            "hilly"
        ]

        rnum = random.randint(0, len(adjectives_list)-1)
        return adjectives_list[rnum]

    def getPronoun():
        pronouns_list = [
            "backwater",
            "backwood",
            "banlieue",
            "boondocks",
            "borough",
            "city",
            "colony",
            "community",
            "district",
            "dukedom",
            "encampment",
            "enclave",
            "ghetto",
            "hamlet",
            "municipality",
            "outpost",
            "plantation",
            "settlement",
            "shtetl",
            "town",
            "village",
        ]

        return pronouns_list[random.randint(0, len(pronouns_list)-1)]

    def getFamousSyn():
        famous_list = [
            "famous",
            "infamous",
            "known",
            "distinguished",
            "notable",
            "celebrated",
            "distinguished",
            "prominent",
            "acclaimed",
            "respected",
            "maligned",
            "besmirched",
            "condemned",
            "vilified",
            "mocked",
            "ridiculed",
            "forgotten",
            "remembered",
            "disgraced"
        ]

        return famous_list[random.randrange(0, len(famous_list))]


    def getFamousFor():
        famous_list = [
            "ankle-breaking rocky hills",
            "smelly fishy lakes",
            "sinewy streams",
            "ham sandwich",
            "ungovernable men",
            "lonely women",
            "nosey grandmothers",
            "fat hamburger",
            "stinky fried rice",
            "green spaghetti",
            "pineapple pizza",
            "bean burritos",
            "seedy nightclubs",
            "fat trees",
            "nine seasons",
            "26 hour sun",
            "pretentious evenings",
            "gossipy citizens",
            "cranky temper",
            "greasy living",
            "feral dogs",
            "flying pigs",
            "lost diamonds",
            "absentee government",
            "quisling politicians",
            "fresh sparkling water",
            "antedeluvian architecture"
        ]

        return famous_list[random.randint(0, len(famous_list)-1)]
