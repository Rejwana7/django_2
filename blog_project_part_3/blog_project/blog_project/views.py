from django.shortcuts import render
from post.models import Post
from catagories.models import Catagory


def home(request,category_slug=None):
    data= Post.objects.all()
    if category_slug is not None:
        category=Catagory.objects.get(slug = category_slug) #category wise slug
        # slug je field model e likhechilam seta = amader category slug kore dilam taile ekhn kon category er slug seia category object peye jabo
        data=Post.objects.filter(category=category) 
         # post er category te category object bosiye filter korlam, ager data er sathe overright hoye jabe
    categories=Catagory.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.catrgory.all():
    #         print(j)
    #     print()    
    return render(request,"home.html",{'data':data,'category':categories})
    
# for post in data:
#     print(f"Post Title: {post.title}")
#     print("Categories:")
#     for category in post.categories.all():
#         print(category.name)
#     print()