from flask_pymongo import PyMongo


def init_db():
    mongo = PyMongo()
    return mongo


def get_db(app, mongo):
    app.config["MONGO_URI"] = "mongodb+srv://222222222222:222222222222@cluster0.ygblo.mongodb.net/Test1_TMS?retryWrites=true&w=majority"
    # app.config["MONGO_URI"] = "mongodb://tms:remotetms@localhost/tms?authSource=tms"
    mongo.init_app(app)
