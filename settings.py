MONGO_URI = 'mongodb://localhost:27017/eve-course'

RESOURCE_METHODS = ['GET','POST','DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

people_schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30
    },
    'lastname': {
        'type': 'string',
        'maxlength': 50,
        'required': True,
        'unique': True
    },
    'born': {'type': 'datetime'},
    'age': {
        'type': 'integer',
        'coerce': int
        },
    'email': {
        'type': 'string',
        'regex': r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'                # regex not working
    },
    'middle_name': {
        'dependencies': ['firstname', 'lastname']
    },
    'role': {
        'type': 'list',
        'allowed': ['author', 'contributor', 'copy'],
        'default': ['author']
    },
    'location': {
        'type': 'dict',
        'required': True,
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string', 'required': True}
        },
    },
}

works = {
    
    'title': {
        'type': 'string',
        'required': True
    },
    'description': {
        'type': 'string'
    },
    'owner': {
        'type': 'objectid',
        'required': True,

        'data_relation': {
            'resource': 'people',
            'embeddable': True
        }

    }
}

DOMAIN = {
    'people': {
        'schema': people_schema
    },
    'works': {
        'schema': works
    }
}