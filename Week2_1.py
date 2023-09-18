# 과제 1

def rev_str(str):
    if len(str) == 1:
        return str
    else:
        a = str[-1]
        str = str[:-1]
        return a + rev_str(str)

if __name__ == '__main__':
    print(rev_str("ABCDE"))
    print(rev_str("Come again, Forever young!"))
    print(rev_str("Amore, Roma"))