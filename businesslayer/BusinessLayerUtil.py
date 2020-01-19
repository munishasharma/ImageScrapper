# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:23:02 2020

@author: Munisha.Sharma
"""

from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    
    keyword = ""
    fileLoc=""
    image_name=""
    header=""
    
    def downloadImages(keyword , header):
        imgScrapper = ScrapperImage
        url = imgScrapper.createImageUrl(keyword)
        rawHtml = imgScrapper.scrap_html_data(url , header)
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList , keyword , header)
        return masterListOfImages
    