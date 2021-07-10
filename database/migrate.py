import database as db

db = db.Database("reverse_protocols")
db.setLocalhost("localhost")
db.setUsername("root")
db.setPassword("")
db.createDatabase()

db.setTableName("sequences")
db.createTable()