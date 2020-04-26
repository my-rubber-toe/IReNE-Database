
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
         required: [ "infrastructureType"],
         properties: {
            infrastructureType: {
               bsonType: "string",
               description: "Infrastructure category, must be a string, with a length between 8-20 characters, following the pattern, and is required",
               pattern: "^[a-zA-Z]{1,30}$"
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
         required: [ "damageType"],
         properties: {
            damageType: {
               bsonType: "string",
               description: "Infrastructure category, must be a string, must follow the pattern, and is required",
               pattern: "^[a-zA-Z]{1,30}$"
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
         properties: {
            tagItem: {
               bsonType: "string",
               description: "Tag category, must be a string, must follow the pattern, and is required",
               pattern: "^[a-zA-Z]{1,30}$"
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
         required: [ "creatoriD, title, published, incidentDate, creationDate, lastModificationDate, infrasDocList, damageDocList"],
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
            // infrasDocList: {
            //    bsonType: ["string"],
            //    description: "Infrastructure categories that case study has, must be a list of string, must follow the pattern, and is required",
            //    pattern: "^[a-zA-Z]{1,30}$"
            // }
         }
      }
   }
})