

def bayes(p2g1, p1, p2):
    """Calculates the probability of p1 given p2"""
    topline = p2g1 * p1
    bottomline = p2
    return topline / bottomline


def remove_newlines(file):
    """Takes a string, replaces all newlines with spaces, removes all double spaces"""
    filetext = file
    filelist = filetext.split("\n")
    filetext = " ".join(filelist)
    if "  " in filetext:
        filelist = filetext.split("  ")
        filetext = " ".join(filelist)
    return filetext


def rempunc_tok(token, exceptions=[]):
    """takes a token and list of exceptions. If a punctuation type is not excepted, it is removed from the token if at
       the end and not preceded directly by another un-excepted punctuation type"""
    fixtok = token
    punclist = [".", ",", "!", "?", "…", ";", ":"]
    knownpuncs = ["ó.", ".r.", "rl.", "ɫ.", ".i."]
    if exceptions:
        punclist = [i for i in punclist if i not in exceptions]
    allpunc = True
    for char in fixtok:
        if char not in punclist:
            allpunc = False
    if allpunc:
        fixtok = ""
    elif fixtok in knownpuncs:
        return fixtok
    elif len(fixtok) > 1:
        for punc in punclist:
            if fixtok[-1] == punc:
                if fixtok[-2] not in punclist:
                    fixtok = fixtok[:-1]
    elif len(fixtok) == 1:
        for punc in punclist:
            if punc in fixtok:
                fixtok = fixtok[:-1]
    return fixtok


def space_tokenise(string, puncfilter=False, puncexcept=[]):
    """Takes a string, a true/false value for filtering punctuation and a list of punctuation-filter exceptions.
       Replaces newlines with spaces, tokenises string based on word spacing.
       If filter punctuation is true, each token has any punctuation removed unless that token is excepted."""
    strunaltered = string
    stroneline = remove_newlines(strunaltered)
    strtoklist = stroneline.split(" ")
    if puncfilter:
        newtoklist = []
        for tok in strtoklist:
            tok = rempunc_tok(tok, puncexcept)
            newtoklist.append(tok)
        return newtoklist
    else:
        return strtoklist


def bayesSents(word, textslist, textno, rempunc = False):
    """Takes a word, a list of texts and the number of a given text within that list.
       Uses bayes theorum to estimate the probability of the of a given text given the word's occurrence."""
    pw = ((space_tokenise(" ".join(textslist), rempunc)).count(word)) / (len(space_tokenise(" ".join(textslist), rempunc)))
    ps = 1 / (len(textslist))
    pwgs = ((space_tokenise(textslist[textno], rempunc)).count(word)) / (len(space_tokenise(textslist[textno], rempunc)))
    return bayes(pwgs, ps, pw)


# allwords = ["abacadaeaf", "abbbcbdbeb", "aabbccddee"]
# pl = (("".join(allwords)).count("a")) / (len("".join(allwords)))  # overall probability of a given letter
# pw = 1/(len(allwords))  # probability of a randomly chosen letter being from any of the three words
# plgw = (allwords[0].count("a")) / (len(allwords[0]))  # probability of a given letter given word 1
# print(bayes(plgw, pw, pl))

# allsents = ["Is lámhscríbhinn dhathmhaisithe i Laidin é Leabhar Cheanannais, ina bhfuil ceithre Shoiscéal an Tiomna Nua, mar aon le réamhthéacsanna agus táblaí éagsúla.", "Scríobh manaigh Cheilteacha amach é thart ar an mbliain 800.", "Díorthaíodh téacs na Soiscéal ón Vulgáid den chuid is mó, cé go gcuimsítear roinnt sleachta ó luathleaganacha an Bhíobla ar a ngairtear an Vetus Latina chomh maith.", "Is máistirshaothar é den challagrafaíocht agus seasann sé do bhuaic an dathmhaisithe Oileánaigh.", "Ceaptar go forleathan freisin gurb é an tseoid náisiúnta is fearr in Éirinn é."]
# print(bayesSents("é", allsents, 0))
# print(bayesSents("é", allsents, 0, True))
