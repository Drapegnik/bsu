from matplotlib import colors, pyplot as plt

def draw(X, y, label=None):
    plt.figure(figsize=(20, 5))
    p = plt.scatter(X[:,0], X[:,1], c=y)
    if label:
        plt.xlabel(label, fontsize=14)
    plt.show()
    return p

def draw_few(data):
    _, axarr = plt.subplots(nrows=1, ncols=len(data), figsize=(16, 4))
    for i, (X, y, label) in enumerate(data):
        axarr[i].scatter(X[:,0], X[:,1], c=y)
        axarr[i].set_title(label)
    plt.show()

def hex_from_index(p, index, l):
    return colors.to_hex(p.get_cmap().colors[256 // l * index])

def colored_text(text, color):
    return '<font color={}><strong>{}</strong></font>'.format(color, text)
