from flask import Blueprint, request, jsonify
from ideahub import app
from ideahub.db import db
from ideahub.topic.models import IdeaTopic

topic = Blueprint('topic',__name__,url_prefix='/topic')

@topic.route('/add', methods=['Post'])
def addTopic():
    content = request.get_json()
    id = content['id']
    title = content['title']
    description = content['description']
    posted_by = content['posted_by']

    push = IdeaTopic(title=title,description=description,posted_by=posted_by)

    db.session.add(push)
    db.session.commit()

    return jsonify({"Topic added":content['title']})


@topic.route('/get', methods=['GET'])
def showAll():
    topics = IdeaTopic.query.all()

    output = []

    for topic in topics:
        topic_data = {}

        topic_data['id']=topic.id
        topic_data['title']=topic.title
        topic_data['description']=topic.description
        topic_data['posted_by']=topic.posted_by

        output.append(topic_data)

    return jsonify({"Topics":output})    

@topic.route('/get/<string:title>', methods=['GET'])
def showOne(title):
    topic = IdeaTopic.query.filter_by(title=title).first()


    output = [{"id": topic.id, "title": topic.title, "description": topic.description, "posted_by": topic.posted_by}]

    return jsonify({"Topics":output})   

@topic.route('/update', methods=['PUT'])
def update():
    content = request.get_json()

    title=content['title']
    description=content['description']
    posted_by=content['posted_by']

    update = IdeaTopic.query.filter_by(title=title).first()

    update.title=title
    update.description=description
    update.posted_by=posted_by

    db.session.commit()

    return jsonify({"Topic Updated":title})




@topic.route('/delete/<string:title>', methods=['DELETE'])
def delete(title):

    delete=IdeaTopic.query.filter_by(title=title).first()
    db.session.delete(delete)
    db.session.commit()

    return jsonify({"Deleted Topic":title})