import re

with open('mbox.txt', 'r') as file:
    mbox = file.read()

formatfind = re.findall('New Revision: ([0-9]+)', mbox)
formattt = [int(item) for item in formatfind]

formattt_sum = sum(formattt) / len(formattt)

print("New Revision 포맷에서 추출한 숫자들의 평균값:", formattt_sum)