from django.shortcuts import render
import requests
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def home(request):
  if request.method == "POST":
    search = request.POST.get('search')
    print(search)
    url = 'https://forkify-api.herokuapp.com/api/search?&q=%s' % search
    print(url)
    response = requests.get(url)
    searchdata = response.json()
    
    recipes = searchdata['recipes']
    #posts = []
    #publishers = []
    #for k in recipes:
        #print(k['title'])
        #posts.append(k['title'])
        #publishers.append(k['publisher'])  
    

    #for x in range(len( posts)): 
        #print (posts[x])   
       
    #resc = recipe[count-2]
    #print(resc)
    #res = resc['title']
    #print(res)
    #print(recipe[2]['title'])
    

    return render(request , 'customer\PrimeP.html' , { 'recipes': recipes , 'search':search  } )
  else:
    return render(request , 'customer\PrimeP.html')

def home2(request):
    response = requests.get('https://forkify-api.herokuapp.com/api/search?&q=pizza')
    searchdata = response.json()
    print(searchdata.recipes)
    return render(request , 'customer\PrimeP.html' , {'count':searchdata['count'] , 'recipes':searchdata['title']})