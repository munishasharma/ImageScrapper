# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:45:31 2020

@author: Munisha.Sharma
"""

from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request, jsonify
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer
import os 

# import request

# initialising the flask app with the name "app"
app= Flask(__name__)

#reponse = 'Welcome'

@app.route('/') # route for redirection of the home page

@cross_origin()

def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayImages():
    list_images= os.listdir('static')
    print(list_images)
    
    try:
        if(len(list_images)>0):
            return render_template('showImage.html' , user_images=list_images)
        else:
            return "image not present"
    except Exception as e:
       print("No images found" , e)
       return "please try the different search keyword"

@app.route('/searchImages' , methods =['Get' , 'POST'])
def searchImage():
    if request.method == "POST":
        search_term = request.form['keyword'] #assignign the value of input keyword to the variable keyword
    
    else:    
        print("Please enter something else")
        
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    
    
    imagescrapperutil = BusinessLayer 
    imagescrapper = ScrapperImage()
    list_images = os.listdir('static')
    imagescrapper.delete_downloaded_images(list_images)
    
    image_name = search_term.split()
    image_name = '+'.join(image_name)
    
    lst_images = imagescrapperutil.downloadImages(search_term , header)
    
    return displayImages()
    
    
         
    
        


if __name__ == "__main__":
    app.run(host = '127.0.0.1' , port = 8000) # port to run on local machine
    
