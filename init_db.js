
//Connects to the database
const mongo = require('mongodb');
const MongoClient = mongo.MongoClient;

const url = 'mongodb://localhost:27017';

MongoClient.connect(url, { useNewUrlParser: true  }, (err, datab) => {

   
   if (err) throw err;
   var db = datab.db("IReNE")
   datab.close();


   // db.createUser(
   //    {
   //    user: "jainel.torres",
   //    pwd: "Password1", // or cleartext password
   //    roles: [ { role: "userAdminAnyDatabase", db: "IReNEdb" }, "readWriteAnyDatabase" ]
   //    }
   // )
   // db.createUser(
   //    {
   //    user: "alberto.canela",
   //    pwd: "Password1", // or cleartext password
   //    roles: [ { role: "userAdminAnyDatabase", db: "IReNEdb" }, "readWriteAnyDatabase" ]
   //    }
   // )
   // db.createUser(
   //    {
   //    user: "alejandro.vasquez",
   //    pwd: "Password1", // or cleartext password
   //    roles: [ { role: "userAdminAnyDatabase", db: "IReNEdb" }, "readWriteAnyDatabase" ]
   //    }
   // )
   // db.createUser(
   //    {
   //    user: "yomar.ruiz",
   //    pwd: "Password0", // or cleartext password
   //    roles: [ { role: "userAdminAnyDatabase", db: "IReNEdb" }, "readWriteAnyDatabase" ]
   //    }
   // )
   // db.createUser(
   //    {
   //    user: "roberto.guzman",
   //    pwd: "Password1", // or cleartext password
   //    roles: [ { role: "userAdminAnyDatabase", db: "IReNEdb" }, "readWriteAnyDatabase" ]
   //    }
   // )
   

   //Collaborator collection with its attributes and restrictions
   db.createCollection("Collaborator", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: [ "first_name", "last_name", "email", "banned", "approved" ],
            properties: {
               first_name: {
                  bsonType: "string",
                  description: "First Name of Collaborator, must be a string, with a length between 0-30, and is required",
                  pattern: "^[a-zA-Z]{0,30}$"
               },
               last_name: {
                  bsonType: "string",
                  description: "Last Name of Collaborator, must be a string, with a length between 0-30 characters, and is required",
                  pattern: "^[a-zA-Z]{0,30}$"
               },
               email: {
                  bsonType: "string",
                  description: "Collaborator's email, must be a string following the pattern, it is unique, and required",
                  pattern:'(.*)\.(.*)@upr\.edu'
               },
               banned: {
                  bsonType: "boolean",
                  description: "must be a boolean with false as a default."
               },
               approved: {
                  bsonType: "boolean",
                  description: "must be a boolean with false as a default."
               }
            }
         }
      }
   })

   //Admin Collection with its attribute and restrictions
   db.createCollection("Admin", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: [ "username", "password"],
            properties: {
               username: {
                  bsonType: "string",
                  description: "Admin username, must be a string, with a length between 8-20 characters, following the pattern, and is required",
                  pattern: "(^(?=[a-zA-Z0-9])(?=.*[a-z])(?=.*[0-9])(?=.*[\.])(?=.*[A-Z])).*[^.]$"
               },
               password: {
                  bsonType: "string",
                  description: "Admin Password, must be a string, with a length between 8-20 characters, must follow the pattern, and is required",
                  pattern: "(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])"
               }
            }
         }
      }
   })

   //Infrastructure Collection with its attribute and restrictions
   db.createCollection("Infrastructure", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            uniqueItems: true,
            required: [ "infrastructureType"],
            properties: {
               infrastructureType: {
                  bsonType: "string",
                  description: "Infrastructure category, must be a string, with a length between 8-20 characters, following the pattern, and is required",
                  pattern: "^[a-zA-Z]{1,50}$"
               }
            }
         }
      }
   })

   //Damage Collection with its attribute and restrictions
   db.createCollection("Damage", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            uniqueItems: true,
            required: [ "damageType"],
            properties: {
               damageType: {
                  bsonType: "string",
                  description: "Infrastructure category, must be a string, must follow the pattern, and is required",
                  pattern: "^[a-zA-Z]{1,50}$"
               }
            }
         }
      }
   })

   //Tag Collection with its attribute and restrictions
   db.createCollection("Tag", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: [ "tagItem"],
            uniqueItems: true,
            properties: {
               tagItem: {
                  bsonType: "string",
                  description: "Tag category, must be a string, must follow the pattern, and is required",
                  pattern: "^[a-zA-Z]{1,50}$"
               }
            }
         }
      }
   })

   db.createCollection("CityPR",{
      validator: {
         $jsonSchema: {
               bsonType: ["array"],
               uniqueItems: true,
               items: {
                  bsonType: ["object"],
                  description: "locations where that case study takes place, must be a list of string, must follow the pattern, and is required",
                  required: ["city", "latitude","longitude"],
                  properties: {
                     city: {
                        bsonType: "string",
                        description: "Location's address"
                     },
                     latitude: {
                        bsonType: "decimal",
                        description: "Location's latitude"
                     },
                     longitude: {
                        bsonType: "decimal",
                        description: "Location's latitude"
                     }
                  }
                  
               }
         }
      }
   })

   //DocumentCase Collection with its attribute and restrictions
   db.createCollection("DocumentCase", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: [ "creatoriD" , "title", "published", "incidentDate", "creationDate", "lastModificationDate", "infrasDocList", "damageDocList", "author", "actor"],
            properties: {
               creatoriD: {
                  bsonType: "string",
                  description: "Collaborator ID who created the case study, must be a string, and is required"
               },
               title: {
                  bsonType: "string",
                  description: "Title of the case study, must be a string, and is required",
                  pattern: "^[a-zA-Z]{10,250}$"
               },
               description: {
                  bsonType: "string",
                  description: "description of the case study, must be a string",
                  pattern: "^[a-zA-Z]{0,500}$"
               },
               language: {
                  bsonType: "string",
                  description: "Language which the case study is written, must be a string, and is required",
                  pattern: "^[a-zA-Z]$"
               },
               published: {
                  bsonType: "boolean",
                  description: "Must be a boolean with true as default, and is required"
               },
               incidentDate: {
                  bsonType: "string",
                  description: "Date when happened the event that the case study describes, must be a string following the pattern, and is required",
                  pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
               },
               creationDate: {
                  bsonType: "string",
                  description: "Date when case study was created, must be a string following the pattern, and is required",
                  pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
               },
               lastModificationDate: {
                  bsonType: "string",
                  description: "Date when case study was last modified, must be a string following the pattern, and is required",
                  pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
               },
               infrasDocList: {
                  bsonType: ["array"],
                  minItems: 1, 
                  uniqueItems: true,
                  additionalProperties: false,
                  items: {
                     bsonType: ["string"],
                     additionalProperties: false,
                     description: "Infrastructure categories that case study has, must be a list of string, must follow the pattern, and is required",
                     pattern: "^[a-zA-Z]{1,30}$"
                  }
               },
               damageDocList: {
                  bsonType: ["array"],
                  minItems: 1, 
                  uniqueItems: true,
                  additionalProperties: false,
                  items: {
                     bsonType: ["string"],
                     additionalProperties: false,
                     description: "Damage categories that case study has, must be a list of string, must follow the pattern, and is required",
                     pattern: "^[a-zA-Z]{1,30}$"
                  }
               },
               tagsDoc: {
                  bsonType: ["array"],
                  minItems: 0, 
                  uniqueItems: true,
                  additionalProperties: false,
                  items: {
                     bsonType: ["string"],
                     description: "Tags that case study has, must be a list of string, must follow the pattern, and is required",
                     pattern: "^[a-zA-Z]{1,30}$"
                  }
               },
               location: {
                  bsonType: ["array"],
                  minItems: 1, 
                  maxItems: 10,
                  uniqueItems: true,
                  additionalProperties: false,
                  items: {
                     bsonType: ["object"],
                     description: "locations where that case study takes place, must be a list of string, must follow the pattern, and is required",
                     required: ["address", "latitude","longitude"],
                     properties: {
                        address: {
                           bsonType: "string",
                           description: "Location's address"
                        },
                        latitude: {
                           bsonType: "decimal",
                           description: "Location's latitude"
                        },
                        longitude: {
                           bsonType: "decimal",
                           description: "Location's latitude"
                        }
                     }
                     
                  }
               },
               author: {
                  bsonType: ["array"],
                  minItems: 1, 
                  uniqueItems: false,
                  items: {
                     bsonType: ["object"],
                     required: ["author_FN", "author_LN", "author_faculty", "author_email"],
                     description: "Authors who wrote the case study, must be a list of Author objects, must follow the pattern, and is required",
                     properties: {
                           author_FN: {
                              bsonType: "string",
                              description: "Author first name",
                              pattern: "^[a-zA-Z]{1,30}$"
                           },
                           author_LN: {
                              bsonType: "string",
                              description: "Author last name",
                              pattern: "^[a-zA-Z]{1,30}$"
                           },
                           author_faculty: {
                              bsonType: "string",
                              description: "Author faculty",
                              pattern: "^[a-zA-Z]{1,30}$"
                           },
                           author_email: {
                                 bsonType: "string",
                                 description: "Author email, must be a string of length 0-50",
                                 pattern: "(.*)\.(.*)@upr\.edu"
                              }  
                     }

                  }
                  
               },
               actor: {
                  bsonType: ["array"],
                  minItems: 1, 
                  uniqueItems: false,
                  items: {
                     bsonType: ["object"],
                     required: ["actor_FN", "actor_LN", "role"],
                     description: "Actors who play a role in the case study, must be a list of Actor objects, must follow the pattern, and is required",
                     properties: {
                           actor_FN: {
                              bsonType: "string",
                              description: "Actor first name",
                              pattern: "^[a-zA-Z]{1,30}$"
                           },
                           actor_LN: {
                              bsonType: "string",
                              description: "Actor last name",
                              pattern: "^[a-zA-Z]{1,30}$"
                           },
                           role: {
                              bsonType: "string",
                              description: "Actor role",
                              pattern: "^[a-zA-Z]{1,30}$"
                           } 
                     }

                  }
               },
               timeline: {
                  bsonType: ["array"],
                  minItems: 0, 
                  uniqueItems: false,
                  items: {
                     bsonType: ["object"],
                     description: "Timeline of a Case study, must be a list of Actor objects, must follow the pattern",
                     properties: {
                           event: {
                              bsonType: ["string"],
                              description: "Event what happened within the case study",
                              pattern: "^[a-zA-Z]{1,250}$"
                           },
                           eventStartDate: {
                              bsonType: ["string"],
                              description: "Date when event started, must be a string following the pattern",
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                           },
                           eventEndDate: {
                              bsonType: ["string"],
                              description: "Date when event ended, must be a string following the pattern",
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                           } 
                     }

                  }
               },
               section: {
                  bsonType: ["array"],
                  minItems: 0, 
                  uniqueItems: false,
                  items: {
                     bsonType: ["object"],
                     description: "Sections of a Case study, must be a list of Section objects.",
                     properties: {
                           secTitle: {
                              bsonType: ["string"],
                              description: "Title of the section",
                              pattern: "(.){1,250}"
                           },
                           content: {
                              bsonType: ["string"],
                              description: "Content of the section",
                           }
                     }

                  }
               } 
            }
         }
      }
   })

   // db.createView('DocumentCaseView','DocumentCase', [{ $project : { 
   //    "creatoriD": $creatoriD,
   //    "title": $title, 
   //    "description": $description,
   //    "published": $published, 
   //    "incidentDate": $incidentDate, 
   //    "creationDate": $creationDate, 
   //    "lastModificationDate": $lastModificationDate, 
   //    "infrasDocList": $infrasDocList, 
   //    "damageDocList": $damageDocList,
   //    "tagsDoc": $tagsDoc,
   //    "actor": $actor,
   //    "author": $author,
   //    "timeline": $timeline,
   //    "section": $section,
   //    "location": location
   // }}])

});