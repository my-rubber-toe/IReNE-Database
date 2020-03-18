db.createUser(
	{	user: "Jaits13",
		pwd: "Gamerchik13",
		roles: [
			{
				role: "readWrite",
				db: "IReNEdb"
			}
		]
	}
)


db.createCollection( "Collaborator", {
	DocumentsID: [1],
	First_Name: "Jai",
	Last_Name: "T",
	Email: "jt@gmail.com",
	Banned: FALSE,
	Faculty: "Icom",
	Status: FALSE
})

db.createCollection( "Admin",{
    UserName: "user_name",
    Password: "pass"
})

db.createCollection( "Session", {
	SessionToken: "djocnh8wj",
	StartDate: "2012-04-23",
	EndDate: "2012-04-23"
})

db.createCollection( "Infrastructure",{
	InfrastructureType: "building"
})

db.createCollection( "Damage", {
	DamageType: "flooding"
})

db.createCollection("TagList", {
	TagItem: "build"
})

db.createCollection("DocumentCase", {
	Title: "The great flooding",
	Description: "it was bad",
	Published: FALSE,
	IncidentDate: "2012-04-23",
	CreationDate: "2012-04-23",
	Location: ["Coamo"],
    Language: "Español",
	Authors: [
		{   First_Name: "j" , 
            Last_Name: "t",
            Email: "jt@yahoo.com", 
            Faculty: "ICOM"
        }],
	Actor:  [
		{   First_Name: "j" , 
            Last_Name: "t",
            Role: "govenor"
        }],
    Timeline: [
		{   Event: "this happen the flooding",
		    EventDate: "2012-04-23"
		}],
	Section: [
		{   Title: "Introduction",
		    Content: "The flooding was bad"
		}],
    TagDocList: ["Flood"],
    InfrastructureDocList: ["building"],
    DamageDocList: ["flooding"]
})








