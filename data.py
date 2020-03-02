import pypinyin


def pinyin_sort(dic):
    sort_dic = {}
    for name in dic.keys():
        name_pinyin = ''
        name_pinyin_list = pypinyin.lazy_pinyin(name)
        for v in name_pinyin_list:
            name_pinyin += v
        sort_dic[name_pinyin] = [name, dic[name]]

    new_dic = {}
    for pinyin in sorted(sort_dic):
        new_dic[sort_dic[pinyin][0]] = sort_dic[pinyin][1]

    return new_dic
