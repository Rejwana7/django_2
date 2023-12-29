from django.shortcuts import render
from post.models import Post


def home(request):
    data= Post.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.catrgory.all():
    #         print(j)
    #     print()    
    return render(request,"home.html",{'data':data})
    
# for post in data:
#     print(f"Post Title: {post.title}")
#     print("Categories:")
#     for category in post.categories.all():
#         print(category.name)
#     print()