"""Datavisualization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import charts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', charts, name='charts')
]


# <script type="application/json" id="mis">
#   { "nodes": [{"value": "Myriel", "name": "Myriel", "group": 1 },{ "name": "OldMan", "group": 2 }, { "name": "Labarre", "group": 3 }, { "name": "Valjean", "group": 4 }, { "name": "Marguerite", "group": 5 }, { "name":
#   "Mme.deR", "group": 6 }, { "name": "Isabeau", "group": 7 }, { "name": "Gervais", "group": 8 }], "links": [{ "source": 1, "target": 2 ,"value": 5 }, { "source": 1, "target": 0, "value": 8 }, { "source": 0, "target": 2, "value": 8 }] }

# </script>


# var mis = document.getElementById('mis').innerHTML;
# graph = JSON.parse(mis);