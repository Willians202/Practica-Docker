from database import mydb

restaurants = mydb['restaurants']
openings = mydb['restaurantsOpening']

def Con1():
    result = restaurants.aggregate([
    {
        '$group': {
            '_id': {
                'sector': '$borough', 'cuisine': '$cuisine'
            }, 
            'count': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'count': -1
        }
    }
])
    return list(result)

def Con2():
  result = restaurants.aggregate([
  {
        '$project': {
            '_id': 1, 
            'name': 1, 
            'grades': 1
        }
    }, {
        '$unwind': '$grades'
    }, {
        '$group': {
            '_id': '$name', 
            'avg_rating': {
                '$avg': '$grades.score'
            }
        }
    }, {
        '$sort': {
            'avg_rating': -1
        }
    }, {
        '$limit': 5
    }
])
  return list(result)

def Con3():
  result = restaurants.aggregate([
  {
        '$unwind': {
            'path': '$grades'
        }
    }, {
        '$group': {
            '_id': '$name', 
            'avg_rating': {
                '$avg': '$grades.score'
            }
        }
    }, {
        '$project': {
            '_id': 1, 
            'name': 1, 
            'avg_rating': 1, 
            'score': {
                '$switch': {
                    'branches': [
                        {
                            'case': {
                                '$gte': [
                                    '$avg_rating', 20
                                ]
                            }, 
                            'then': 'A'
                        }, {
                            'case': {
                                '$and': [
                                    {
                                        '$gte': [
                                            '$avg_rating', 13
                                        ]
                                    }, {
                                        '$lt': [
                                            '$avg_rating', 20
                                        ]
                                    }
                                ]
                            }, 
                            'then': 'B'
                        }, {
                            'case': {
                                '$lt': [
                                    '$avg_rating', 13
                                ]
                            }, 
                            'then': 'C'
                        }
                    ], 
                    'default': 'No scores found.'
                }
            }
        }
    }, {
        '$sort': {
            'avg_rating': -1
        }
    }, {
        '$limit': 50
    }
])
  return list(result)

def Con4(): 
  result = openings.aggregate([
  {
        '$project': {
            '_id': 0, 
            'reviews': 1
        }
    }, {
        '$unwind': {
            'path': '$reviews'
        }
    }, {
        '$group': {
            '_id': '$reviews.name', 
            'review_date': {
                '$min': '$reviews.date'
            }
        }
    }, {
        '$limit': 1
    }
])
  return list(result)

def Con5(): 
  result = openings.aggregate([
  {
        '$unwind': {
            'path': '$operating_hours'
        }
    }, {
        '$project': {
            '_id': 0, 
            'name': 1, 
            'closed': {
                '$switch': {
                    'branches': [
                        {
                            'case': {
                                '$eq': [
                                    '$operating_hours.Monday', 'Closed'
                                ]
                            }, 
                            'then': 'Monday'
                        }, {
                            'case': {
                                '$eq': [
                                    '$operating_hours.Tuesday', 'Closed'
                                ]
                            }, 
                            'then': 'Tuesday'
                        }, {
                            'case': {
                                '$eq': [
                                    '$operating_hours.Wednesday', 'Closed'
                                ]
                            }, 
                            'then': 'Wednesday'
                        }, {
                            'case': {
                                '$eq': [
                                    '$operating_hours.Thursday', 'Closed'
                                ]
                            }, 
                            'then': 'Thursday'
                        }, {
                            'case': {
                                '$eq': [
                                    '$operating_hours.Friday', 'Closed'
                                ]
                            }, 
                            'then': 'Friday'
                        }, {
                            'case': {
                                '$eq': [
                                    '$operating_hours.Saturday', 'Closed'
                                ]
                            }, 
                            'then': 'Saturday'
                        }, {
                            'case': {
                                '$eq': [
                                    '$operating_hours.Sunday', 'Closed'
                                ]
                            }, 
                            'then': 'Sunday'
                        }
                    ], 
                    'default': 'Open Everyday'
                }
            }
        }
    }
])
  return list(result)
