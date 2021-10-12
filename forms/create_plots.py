import base64
import io

import matplotlib.pyplot as plt


def query_set_to_array(query, att):
    query = list(query)
    return [value[att] for value in query]


def queryset_to_img(all_object, att, title):
    fig, ax1 = plt.subplots()
    ax1.hist(query_set_to_array(all_object.values(), att))
    plt.title(title)
    plt.tight_layout()
    uni_plot = img_to_bytes(fig)
    return uni_plot


def img_to_bytes(img):
    buf = io.BytesIO()
    img.savefig(buf, format='png', transparent=True)
    buf.seek(0)
    buffer = b''.join(buf)
    return base64.b64encode(buffer).decode('utf-8')
