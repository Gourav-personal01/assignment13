# The sort() method specifies the order in which the query returns the matching documents from the given collection


# Example - 

#db.mycol.find({},{"title":1,_id:0}).sort({"title":-1})