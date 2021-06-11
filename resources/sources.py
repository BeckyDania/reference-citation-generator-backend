import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

sources = Blueprint('sources', 'sources')

@sources.route('/', methods=['GET'])
def sources_index():

	sources_dicts = [model_to_dict(source) for source in models.Source.select()]

	return jsonify(
		data = sources_dicts,
		message= f"Successfully found {len(sources_dicts)} sources",
		status= 200
	), 200  

@sources.route('/', methods=['POST'])
def create_source():
	payload = request.get_json()
	print(payload)
	new_source = models.Source.create(
		style=payload['style'], 
		source=payload['source'], 
		lastname=payload['lastname'], 
		firstname=payload['firstname'], 
		title=payload['title'], 
		publisher=payload['publisher'], 
		date=payload['date'], 
		website=payload['website'], 
		volume=payload['volume'], 
		issue=payload['issue'], 
		pages=payload['pages']
		)



	print(new_source)

	source_dict = model_to_dict(new_source)

	return jsonify(
		data=source_dict,
		message = "Successfully created source",
		status=201
	), 201

@sources.route('/<id>', methods = ['GET'])
def get_one_source(id):
	source = models.Source.get_by_id(id)

	return jsonify(
		data = model_to_dict(source),
		message = "Successfully created source", 
		status=201
	), 201

#PUT UPDATE ROUTE
#PUT api/v1/sources/<id>
@sources.route('/<id>', methods = ['PUT'])
def update_source(id):
	payload = request.get_json()
	models.Source.update(**payload).where(models.Source.id == id).execute()
	return jsonify(
		data = model_to_dict(models.Source.get_by_id(id)),
		status=200,
		message="Source updated Successfully"
	), 200

#DELETE ROUTE
#DELETE api/v1/sources/<id>

@sources.route('/<id>', methods=["DELETE"])
def delete_source(id):
	models.Source.delete().where(models.Source.id==id).execute()
	return jsonify(
		data = None,
		status = 200,
		message = "Source DELETED successfully"
	), 200