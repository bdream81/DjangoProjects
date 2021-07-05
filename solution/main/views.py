from django.shortcuts import render
from django.views.generic import View

class AboutView(View):
    def get(self, request):

        data1 = [{"title": "125",
        "text":"Active Projects"}, 
        {"title": "200",
        "text":"Business Growth"},
        {"title": "530",
        "text":"Completed Projects"},
        {"title": "941",
        "text":"Happy Clients"}]

        data2 = [{"img_path": "images/customer1.jpg", 
        "name": "Lica Galli", 
        "position": "Project Manager",
        "definition": "Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat"},
        {"img_path": "images/customer2.jpg", 
        "name": "Missy Limana", 
        "position": "Project Manager",
        "definition":"Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat"},
        {"img_path": "images/customer3.jpg", 
        "name": "Aana Brown", 
        "position": "Project Manager",
        "definition":"Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat"},
        {"img_path": "images/customer3.jpg", 
        "name": "Aana Brown", 
        "position": "Project Manager",
        "definition":"Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat"}, 
        {"img_path": "images/customer3.jpg", 
        "name": "Aana Brown", 
        "position": "Project Manager",
        "definition":"Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat"}]
        
        data3 = [{"img_path": "images/quality-results.png", 
        "name":"Quality Results", 
        "definition": " Aliquam a nisl pulvinar, hendrerit arcu sed, dapibus velit. Duis ac quam id sapien vestibulum fermentum ac eu eros. Aliquam erat volutpat."},
        {"img_path": "images/analytics.png", 
        "name":"Analytics", 
        "definition": " Aliquam a nisl pulvinar, hendrerit arcu sed, dapibus velit. Duis ac quam id sapien vestibulum fermentum ac eu eros. Aliquam erat volutpat."},
        {"img_path": "images/affordable-pricing.png", 
        "name":"Affordable Pricing", 
        "definition": " Aliquam a nisl pulvinar, hendrerit arcu sed, dapibus velit. Duis ac quam id sapien vestibulum fermentum ac eu eros. Aliquam erat volutpat."},
        {"img_path": "images/easy-to-use.png", 
        "name":"Easy To Use", 
        "definition": " Aliquam a nisl pulvinar, hendrerit arcu sed, dapibus velit. Duis ac quam id sapien vestibulum fermentum ac eu eros. Aliquam erat volutpat."}, 
        {"img_path": "images/free-support.png", 
        "name":"Free Support", 
        "definition": " Aliquam a nisl pulvinar, hendrerit arcu sed, dapibus velit. Duis ac quam id sapien vestibulum fermentum ac eu eros. Aliquam erat volutpat."},
        {"img_path": "images/effectively-increase.png", 
        "name":"Effectively Increase", 
        "definition": " Aliquam a nisl pulvinar, hendrerit arcu sed, dapibus velit. Duis ac quam id sapien vestibulum fermentum ac eu eros. Aliquam erat volutpat."}
        ]

        return render(request, template_name="main/about.html",
        context={"data1": data1, "data2": data2, "data3": data3})

class HomeView(View):
    def get(self, request):
        return render(request, template_name="main/home.html")

class ServicesView(View):
    def get(self, request):
        data = [{"img_path": "images/web-design.png",
        "title": "Web Design",
        "text": "Nullam quis libero in lorem accumsan sodales. Nam vel nisi eget."}, 
        {"img_path": "images/marketing.png",
        "title": "Marketing",
        "text": "Nullam quis libero in lorem accumsan sodales. Nam vel nisi eget."}, 
        {"img_path": "images/seo.png",
        "title": "SEO",
        "text": "Nullam quis libero in lorem accumsan sodales. Nam vel nisi eget."},
        {"img_path": "images/graphics-design.png",
        "title": "Graphics Design",
        "text": "Nullam quis libero in lorem accumsan sodales. Nam vel nisi eget."}
        ]
        return render(request, template_name="main/services.html", 
        context={"data": data})

class NewsView(View):
    def get(self, request):
        data = [{"img_path": "images/news1.jpg",
        "header": "Aenean ultrices lorem quis blandit tempor urabitur accumsan.",
        "definition": "Donec non sem mi. In hac habitasse platea dictumst. Nullam a feugiat augue, et porta metus. Nulla mollis lobortis leet. Maecenas tincidunt, arcu sed ornare purusrisus"
        }, 
        {"img_path": "images/news2.jpg",
        "header": "Nam vel nisi eget odio pulvinar iaculis. Fusce aliquet.",
        "definition": "Donec non sem mi. In hac habitasse platea dictumst. Nullam a feugiat augue, et porta metus. Nulla mollis lobortis leet. Maecenas tincidunt, arcu sed ornare purus risus"
        }, 
        {"img_path": "images/news3.jpg",
        "header": "Morbi faucibus odio sollicitudin risus scelerisque dignissim.",
        "definition": "Donec non sem mi. In hac habitasse platea dictumst. Nullam a feugiat augue, et porta metus. Nulla mollis lobortis leet. Maecenas tincidunt, arcu sed ornare purus risus"
        }, 
        {"img_path": "images/news1.jpg",
        "header": "Aenean ultrices lorem quis blandit tempor urabitur accumsan.",
        "definition": "Donec non sem mi. In hac habitasse platea dictumst. Nullam a feugiat augue, et porta metus. Nulla mollis lobortis leet. Maecenas tincidunt, arcu sed ornare purus risus"
        }, 
        {"img_path": "images/news2.jpg",
        "header": "Nam vel nisi eget odio pulvinar iaculis. Fusce aliquet.",
        "definition": "Donec non sem mi. In hac habitasse platea dictumst. Nullam a feugiat augue, et porta metus. Nulla mollis lobortis leet. Maecenas tincidunt, arcu sed ornare purus risus"
        },
        {"img_path": "images/news3.jpg",
        "header": "Morbi faucibus odio sollicitudin risus scelerisque dignissim.",
        "definition": "Donec non sem mi. In hac habitasse platea dictumst. Nullam a feugiat augue, et porta metus. Nulla mollis lobortis leet. Maecenas tincidunt, arcu sed ornare purus risus"
        },  
        ]
        return render(request, template_name="main/news.html",
        context={"data": data})