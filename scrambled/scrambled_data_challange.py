from collections import Counter
import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
diclst = []
str = ""
try:
    with open("resources/dictionaryfile.txt", "r") as dp:
        Lines = dp.readlines()
        for line in Lines:
            diclst.append(line.rstrip())
    logger.info("the given dictionary are ")
    logger.info(diclst)
except IOError:
    logger.error("Could not read file:dictionaryfile")
try:
    with open("resources/inputfile.txt", "r") as ip:
        str = ip.read()
    logger.info("the given input file is ")
    logger.info(str)
except IOError:
    logger.error("Could not read file:inputfile")


def scramblecount(dictionary, str):
    logger.info("*****************")
    logger.info("finding substring with %s", dictionary)
    MatchStartCharSubStrlst = []
    for i in range(0, len(str)):
        if str[i] == dictionary[0]:
            MatchStartCharSubStrlst.append(str[i:i + len(dictionary)])
    MatchStartAndEndCharSubStrlstlst = []

    for i in MatchStartCharSubStrlst:
        if i.startswith(dictionary[0]) & i.endswith(dictionary[-1]):
            MatchStartAndEndCharSubStrlstlst.append(i)
    logger.info("matching with starting and ending character ")
    logger.info(MatchStartAndEndCharSubStrlstlst)
    finalScrambleSubStrlst = []
    for i in MatchStartAndEndCharSubStrlstlst:
        if Counter(i[1:-1]) == Counter(dictionary[1:-1]):
            finalScrambleSubStrlst.append(i)

    logger.info("number matched scrambles substrs are %d", len(set(finalScrambleSubStrlst)))
    return (len(set(finalScrambleSubStrlst)))


globalcounter = 0
for dic in diclst:
    globalcounter += scramblecount(dic, str)

logger.info("Case #1:%d", globalcounter)
