"""
Definition of views.
"""

import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime

def drones(request):
    return HttpResponse(
    
    '''
    <html>
    <head>
    <title>Drone Loan</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"></script>
    </head>
    <body>


    <style>
    .jumbotron {
    position: relative;
    overflow: hidden;
    background-color: black;
}

    .jumbotron video {
    position: absolute;
    z-index: 1;
    top: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.5;
}

    .jumbotron .container {
    z-index: 2;
    position: relative;
}
    </style>

    <div class="jumbotron jumbotron-fluid">

    <video autoplay muted loop poster="https://dummyimage.com/900x400/000/fff">
    <source src="http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4" type="video/mp4">
    </video>
         <center><h1>www.DroneIt.Com</h1>
        <p>Where Will You Go Today?</p></center> 
    </div>
  
    <div class="container">
    <div class="row">
    <div class="col-sm-4">
      <h3>Rent A Drone</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>Your Drone = $$$$$$$</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>BUY A DRONE!</h3>        
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
      </div>
     </div>
    </div>

</body>
</html>


    '''
    
    #<a href="artists/u2">U2</a>
    );

def artistdetails(request, name):
    output = '<html><head><title>' + name
    output += '</title></head><body><h1>' + name
    output += '<h1/></body></html>'
    return HttpResponse(output); 


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )



