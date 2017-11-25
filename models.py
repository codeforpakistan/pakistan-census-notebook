from mongoengine import *

# to be changed to azure conn string once deployed to production
connect('mongodb://pakistancensus:CwTZjX2WgUICeQbc7zUPBCiP9JlDe7AfD9Qe6u9XYeW4jLKdMOXuF5qzrNYATiMKkCylsigwnNY4lAlN9e9eBA==@pakistancensus.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')


class Measurement(EmbeddedDocument):
    areaType = StringField() # rural or urban area type
    year = IntField()
    households =  IntField()
    male = IntField()
    female = IntField()
    transgenders = IntField()



class District(Document):
    name = StringField(required = True)
    latitude = FloatField()
    longitude = FloatField()
    measurements = ListField(EmbeddedDocumentField(Measurement))

    meta = {
        'indexes': [
            'name',
            '$name'
        ]
    }
    
class Province(Document):
    name = StringField(required = True)
    latitude = FloatField()
    longitude = FloatField()
    measurements = ListField(EmbeddedDocumentField(Measurement))

    meta = {
        'indexes': [
            'name',
            '$name'
        ]
    }