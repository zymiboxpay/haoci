import re
reg = u'.*?(?:！|。|？|(?:：“)|(?:[！。？]”))'
with open('weicheng_no_space.txt', 'r') as f:
    with open('weicheng_sentences.txt', 'w') as outfile:
        for line in f:
            for sentence in re.findall(reg, line):
                sentence = sentence.strip()
                if len(sentence) > 1:
                    outfile.write(sentence + '\n')