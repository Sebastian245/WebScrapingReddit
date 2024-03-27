from flask import Blueprint, jsonify
from services.WebScrapperService import WebScrapperService 

main = Blueprint('language_blueprint', __name__)

@main.route('/getWebScrapping', methods=['GET'])
def getWebScrapping():
    result, data = WebScrapperService.getWebScrapping()
    return jsonify({"result": result, "data": data})

@main.route('/createWebScrapping', methods=['POST'])
def createWebScrapping():
    result, message = WebScrapperService.createWebScrapping()
    return jsonify({"result": result, "message": message})
