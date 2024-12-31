from django import template


register=template.Library()


@register.filter(name="blogsize")
def blogsize(list,size):
    blog_size=[]
    i=0
    for value in list:
        blog_size.append(value)
        i += 1
        if i == size:
            yield blog_size
            i=0
            blog_size=[]
    if blog_size:
        yield blog_size
