from flask import Blueprint, request, jsonify
from ideahub import app
from ideahub.db import db
from ideahub.ideas.models import Ideas

ideas = Blueprint('ideas',__name__,url_prefix='/ideas')



@ideas.route('/add', methods=['Post'])
def addTopic():
    content = request.get_json()
    
    title = content['title']
    description = content['description']
    topic = content['topic']
    posted_by = content['posted_by']

    push = Ideas(title=title,description=description,topic=topic,posted_by=posted_by)

    db.session.add(push)
    db.session.commit()

    return jsonify({"Topic added":content['title']})


@ideas.route('/get', methods=['GET'])
def showAll():
    ideas = Ideas.query.all()

    output = []

    for idea in ideas:
        idea_data = {}

        idea_data['id']=idea.id
        idea_data['title']=idea.title
        idea_data['description']=idea.description
        idea_data['topic']=idea.topic
        idea_data['posted_by']=idea.posted_by

        output.append(idea_data)

    return jsonify({"Ideas":output})    

@ideas.route('/get/<string:title>', methods=['GET'])
def showOne(title):
    idea = Ideas.query.filter_by(title=title).first()


    output = [{"id": idea.id, "title": idea.title, "description": idea.description,"topic": idea.topic ,"posted_by": idea.posted_by}]

    return jsonify({"Idea":output})   

@ideas.route('/update', methods=['PUT'])
def update():
    content = request.get_json()

    title=content['title']
    description=content['description']
    topic=content['topic']
    posted_by=content['posted_by']

    update = Ideas.query.filter_by(title=title).first()

    update.title=title
    update.description=description
    update.topic=topic
    update.posted_by=posted_by

    db.session.commit()

    return jsonify({"Idea Updated":title})




@ideas.route('/delete/<string:title>', methods=['DELETE'])
def delete(title):

    delete=Ideas.query.filter_by(title=title).first()
    db.session.delete(delete)
    db.session.commit()

    return jsonify({"Deleted idea":title})