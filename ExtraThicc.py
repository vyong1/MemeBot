map = {
    'a' : '卂',
    'b' : '乃',
    'c' : '匚',
    'd' : '刀',
    'e' : '乇',
    'f' : '下',
    'g' : '厶',
    'h' : '卄',
    'i' : '工',
    'j' : '丁',
    'k' : '长',
    'l' : '乚',
    'm' : '从',
    'n' : '𠘨',
    'o' : '口',
    'p' : '尸',
    'q' : '㔿',
    'r' : '尺',
    's' : '丂',
    't' : '丅',
    'u' : '凵',
    'v' : 'リ',
    'w' : '山',
    'x' : '乂',
    'y' : '丫',
    'z' : '乙',
    ' ' : '  '
}

def thiccify(s):
    s = s.lower()
    s_new = ""
    for c in s:
        if c in map:
            s_new += map[c.lower()]
        else:
            s_new += c
    return s_new