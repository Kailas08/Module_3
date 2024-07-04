def single_root_words(root_world, *other_words):
    same_words = []
    for i in other_words:
        if root_world.lower() in i.lower():
            same_words.append(i)
        if i.lower() in root_world.lower():
            same_words.append(i)
        #print(same_words)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))


