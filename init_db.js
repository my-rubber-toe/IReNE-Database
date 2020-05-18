(function main() {
   //Connects to the database
   const mongo = require('mongodb');
   const MongoClient = mongo.MongoClient;

   const url = 'mongodb://localhost:27017';

   const client = new MongoClient(url, {useUnifiedTopology: true}) 

   client.connect(function (error, client, ) {
      
      process.on('unhandledRejection', error => {
         console.log('unhandledRejection', error.message);
       });
       
      new Promise((_, reject) => reject(new Error())).
         catch(error => {
           console.log(error.message);
      });

      var db = client.db("IReNEdb");

      setupCollections(db, () => {
         client.close()
      })
   });

   function setupCollections(db, callback) {
      /*
       * Collaborator schema definition with its attributes, limits & regex
       *    These are going to be the users who will create Case Studies
       */
      db.createCollection("collaborator", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               required: ["first_name", "last_name", "email", "banned", "approved"],
               properties: {
                  first_name: {
                     bsonType: "string",
                     description: "First Name of Collaborator, must be a string, with a length between 0-30, and is required",
                     minLength: 1,
                     maxLength:30,
                     pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'
                  },
                  last_name: {
                     bsonType: "string",
                     description: "Last Name of Collaborator, must be a string, with a length between 0-30 characters, and is required",
                     minLength: 1,
                     maxLength:60,
                     pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'
                  },
                  email: {
                     bsonType: "string",
                     description: "Collaborator's email, must be a string following the pattern, it is unique, and required",
                     minLength: 9,
                     maxLength:70,
                     pattern: '^[\.a-z0-9]*(@upr\.edu)$'
                  },
                  banned: {
                     bsonType: "bool",
                     description: "must be a bool with false as a default."
                  },
                  approved: {
                     bsonType: "bool",
                     description: "must be a bool with false as a default."
                  }
               }
            }
         }
      })


      /*
       * Admin schema definition with its attributes, limits & regex
       *    These are the users who will use the Admin Dashboard
       */
      db.createCollection("admin", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               required: ["username", "password"],
               properties: {
                  username: {
                     bsonType: "string",
                     description: "Admin username, must be a string, with a length between 8-20 characters, following the pattern, and is required",
                     minLength: 6,
                     maxLength:20,
                     pattern: "(^[^.]([a-zA-Z0-9]*)[.]{0,1}([a-zA-Z0-9]*))[^.]$"
                  },
                  password: {
                     bsonType: "string",
                     description: "Admin Password, must be a hashed string",
                  }
               }
            }
         }
      })

      /*
       * Infrastructure schema definition with its attributes, limits & regex
       *    These will be the different categories based on Infrastructure types
       *       All of them will be defined by the team/admins
       */
      db.createCollection("infrastructure", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               uniqueItems: true,
               required: ["infrastructureType"],
               properties: {
                  infrastructureType: {
                     bsonType: "string",
                     description: "Infrastructure category, must be a string, with a length between 8-20 characters, following the pattern, and is required",
                     minLength: 1,
                     maxLength:30,
                     pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"
                  }
               }
            }
         }
      })

      /*
       * Damage schema definition with its attributes, limits & regex
       *    These will be the different categories based on Damage types
       *       All of them will be defined by the team/admins
       */
      db.createCollection("damage", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               uniqueItems: true,
               required: ["damageType"],
               properties: {
                  damageType: {
                     bsonType: "string",
                     description: "Infrastructure category, must be a string, must follow the pattern, and is required",
                     minLength: 1,
                     maxLength:30,
                     pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                  
                  }
               }
            }
         }
      })

      /*
       * Tag schema definition with its attributes, limits & regex
       *    These will be the different tags available for the document
       *       Some will be defined by the team/admins and the majority of them will
       *       be defined by the Collaborators
       */
      db.createCollection("tag", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               required: ["tagItem"],
               uniqueItems: true,
               properties: {
                  tagItem: {
                     bsonType: "string",
                     description: "Tag category, must be a string, must follow the pattern, and is required",
                     minLength: 1,
                     maxLength:30,
                     pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                  
                  }
               }
            }
         }
      })

      /*
       * City_PR schema definition with its attributes, limits & regex
       *    These are the addresses, with coordinates, of all the municipalities of Puerto Rico
       */
      db.createCollection("city_pr", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               uniqueItems: true,
               required: ["city", "latitude", "longitude"],
               description: "locations where that case study takes place, must be a list of string, must follow the pattern, and is required",
               properties: {
                  city: {
                     bsonType: "string",
                     minLength: 7,
                     maxLength:50,
                     description: "Location's address",
                     pattern: "^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$"
                  },
                  latitude: {
                     bsonType: "double",
                     minimum:17.87,
                     maximum:18.53,
                     description: "Location's latitude"
                  },
                  longitude: {
                     bsonType: "double",
                     minimum:-67.28,
                     maximum:-65.23,
                     description: "Location's latitude"
                  }
               }
            }
         }
      })

      /*
       * Document Case schema definition with its attributes, limits & regex
       *    These are the Case Studies which are made by the collaborators in TellSpace
       */
      db.createCollection("document_case", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               required: ["creatoriD", "title", "published", "incidentDate", "creationDate", "lastModificationDate", "infrasDocList", "damageDocList", "author", "actor"],
               properties: {
                  creatoriD: {
                     bsonType: "objectId",
                     description: "Collaborator ID who created the case study, must be a string, and is required"
                  },
                  title: {
                     bsonType: "string",
                     description: "Title of the case study, must be a string, and is required",
                     minLength: 10,
                     maxLength: 50,
                     pattern: "^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$"
                  },
                  description: {
                     bsonType: "string",
                     description: "description of the case study, must be a string",
                     minLength: 1,
                     maxLength: 500
                  },
                  language: {
                     bsonType: "string",
                     description: "Language which the case study is written, must be a string, and is required",
                     minLength:1,
                     maxLength:20,
                     pattern: "^[A-Z][a-z]*$"
                  },
                  published: {
                     bsonType: "bool",
                     description: "Must be a bool with true as default, and is required"
                  },
                  incidentDate: {
                     bsonType: "string",
                     description: "Date when happened the event that the case study describes, must be a string following the pattern, and is required",
                     minLength:9,
                     maxLength: 11,
                     pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                  },
                  creationDate: {
                     bsonType: "string",
                     description: "Date when case study was created, must be a string following the pattern, and is required",
                     minLength:9,
                     maxLength: 11,
                     pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                  },
                  lastModificationDate: {
                     bsonType: "string",
                     description: "Date when case study was last modified, must be a string following the pattern, and is required",
                     minLength:9,
                     maxLength: 70,
                     pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                  },
                  infrasDocList: {
                     bsonType: ["array"],
                     minItems: 1,
                     uniqueItems: false,
                     additionalProperties: false,
                     items: {
                        bsonType: "string",
                        additionalProperties: false,
                        description: "Infrastructure categories that case study has, must be a list of string, must follow the pattern, and is required",
                        minLength: 1,
                        maxLength:30,
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                     
                     }
                  },
                  damageDocList: {
                     bsonType: ["array"],
                     minItems: 1,
                     uniqueItems: false,
                     additionalProperties: false,
                     items: {
                        bsonType: "string",
                        additionalProperties: false,
                        description: "Damage categories that case study has, must be a list of string, must follow the pattern, and is required",
                        minLength: 1,
                        maxLength:30,
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                     
                     }
                  },
                  tagsDoc: {
                     bsonType: "array",
                     minItems: 0,
                     maxItems:10,
                     uniqueItems: false,
                     additionalProperties: false,
                     items: {
                        bsonType: "string",
                        description: "Tags that case study has, must be a list of string, must follow the pattern, and is required",
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$",                       
                         minLength: 1,
                        maxLength:30
                     }
                  },
                  location: {
                     bsonType: ["array"],
                     minItems: 0,
                     maxItems: 5,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "locations where that case study takes place, must be a list of string, must follow the pattern, and is required",
                        properties: {
                           address: {
                              bsonType: "string",
                              minLength: 7,
                              maxLength:50,
                              description: "Location's address",
                              pattern: "^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$"
                           },
                           latitude: {
                              bsonType: "double",
                              minimum:17.87,
                              maximum:18.53,
                              description: "Location's latitude"
                           },
                           longitude: {
                              bsonType: "double",
                              minimum:-67.28,
                              maximum:-65.23,
                              description: "Location's latitude"
                           }
                        }

                     }
                  },
                  author: {
                     bsonType: ["array"],
                     minItems: 1,
                     maxItems:10,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        required: ["author_FN", "author_LN", "author_faculty", "author_email"],
                        description: "Authors who wrote the case study, must be a list of Author objects, must follow the pattern, and is required",
                        properties: {
                           author_FN: {
                              bsonType: "string",
                              description: "Author first name",
                              minLength:2,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           author_LN: {
                              bsonType: "string",
                              description: "Author last name",
                              minLength:2,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           author_faculty: {
                              bsonType: "string",
                              description: "Author faculty",
                              minLength:1,
                              maxLength:30,
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z:0-9À-ÿ]$"
                           },
                           author_email: {
                              bsonType: "string",
                              description: "Author email, must be a string of length 0-50",
                              minLength:9,
                              maxLength:70,
                              pattern: "^[.a-z0-9]*(@upr\.edu)$"
                           }
                        }

                     }

                  },
                  actor: {
                     bsonType: ["array"],
                     minItems: 1,
                     maxItems: 5,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        required: ["actor_FN", "actor_LN", "role"],
                        description: "Actors who play a role in the case study, must be a list of Actor objects, must follow the pattern, and is required",
                        properties: {
                           actor_FN: {
                              bsonType: "string",
                              description: "Actor first name",
                              minLength:1,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           actor_LN: {
                              bsonType: "string",
                              description: "Actor last name",
                              minLength:1,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           role: {
                              bsonType: "string",
                              description: "Actor role",
                              minLength:1,
                              maxLength:30,
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z:0-9À-ÿ]$"
                           }
                        }

                     }
                  },
                  timeline: {
                     bsonType: ["array"],
                     minItems: 0,
                     maxItems:5,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "Timeline of a Case study, must be a list of Actor objects, must follow the pattern",
                        properties: {
                           event: {
                              bsonType: "string",
                              description: "Event what happened within the case study",
                              minLength:1,
                              maxLength:50,
                           },
                           eventStartDate: {
                              bsonType: "string",
                              description: "Date when event started, must be a string following the pattern",
                              minLength:9,
                              maxLength: 11,
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                           },
                           eventEndDate: {
                              bsonType: "string",
                              description: "Date when event ended, must be a string following the pattern",
                              minLength:9,
                              maxLength: 11,
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"   
                           }
                        }

                     }
                  },
                  section: {
                     bsonType: ["array"],
                     minItems: 0,
                     maxItems:10,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "Sections of a Case study, must be a list of Section objects.",
                        properties: {
                           secTitle: {
                              bsonType: "string",
                              description: "Title of the section",
                              minLength: 1,
                              maxLength:50,
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$"
                           },
                           content: {
                              bsonType: "string",
                              description: "Content of the section",
                              minLength: 1
                           }
                        }

                     }
                  }
               }
            }
         }
      })

      /*
       * Creation_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems for creating a document
      */
      db.createCollection("creation_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               properties: {
                  creatoriD: {
                     bsonType: "objectId",
                     description: "Collaborator ID who created the case study, must be a string, and is required"
                  },
                  title: {
                     bsonType: "string",
                     description: "Title of the case study, must be a string, and is required",
                     minLength: 10,
                     maxLength: 50,
                     pattern: "^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$"
                  },
                  description: {
                     bsonType: "string",
                     description: "description of the case study, must be a string",
                     minLength: 1,
                     maxLength: 500
                  },
                  language: {
                     bsonType: "string",
                     description: "Language which the case study is written, must be a string, and is required",
                     minLength:1,
                     maxLength:20,
                     pattern: "^[A-Z][a-z]*$"
                  },
                  published: {
                     bsonType: "bool",
                     description: "Must be a bool with true as default, and is required"
                  },
                  incidentDate: {
                     bsonType: "string",
                     description: "Date when happened the event that the case study describes, must be a string following the pattern, and is required",
                     minLength:9,
                     maxLength: 11,
                     pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                  },
                  creationDate: {
                     bsonType: "string",
                     description: "Date when case study was created, must be a string following the pattern, and is required",
                     minLength:9,
                     maxLength: 11,
                     pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                  },
                  lastModificationDate: {
                     bsonType: "string",
                     description: "Date when case study was last modified, must be a string following the pattern, and is required",
                     minLength:9,
                     maxLength: 70,
                     pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                  },
                  infrasDocList: {
                     bsonType: ["array"],
                     minItems: 1,
                     uniqueItems: false,
                     additionalProperties: false,
                     items: {
                        bsonType: "string",
                        additionalProperties: false,
                        description: "Infrastructure categories that case study has, must be a list of string, must follow the pattern, and is required",
                        minLength: 1,
                        maxLength:30,
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                     
                     }
                  },
                  damageDocList: {
                     bsonType: ["array"],
                     minItems: 1,
                     uniqueItems: false,
                     additionalProperties: false,
                     items: {
                        bsonType: "string",
                        additionalProperties: false,
                        description: "Damage categories that case study has, must be a list of string, must follow the pattern, and is required",
                        minLength: 1,
                        maxLength:30,
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                     
                     }
                  },
                  tagsDoc: {
                     bsonType: "array",
                     minItems: 0,
                     maxItems:10,
                     uniqueItems: false,
                     additionalProperties: false,
                     items: {
                        bsonType: "string",
                        description: "Tags that case study has, must be a list of string, must follow the pattern, and is required",
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$",                        
                        minLength: 1,
                        maxLength:30
                     }
                  },
                  location: {
                     bsonType: ["array"],
                     minItems: 0,
                     maxItems: 5,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "locations where that case study takes place, must be a list of string, must follow the pattern, and is required",
                        properties: {
                           address: {
                              bsonType: "string",
                              minLength: 7,
                              maxLength:50,
                              description: "Location's address",
                              pattern: "^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$"
                           },
                           latitude: {
                              bsonType: "double",
                              minimum:17.87,
                              maximum:18.53,
                              description: "Location's latitude"
                           },
                           longitude: {
                              bsonType: "double",
                              minimum:-67.28,
                              maximum:-65.23,
                              description: "Location's latitude"
                           }
                        }

                     }
                  },
                  author: {
                     bsonType: ["array"],
                     minItems: 1,
                     maxItems:10,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "Authors who wrote the case study, must be a list of Author objects, must follow the pattern, and is required",
                        properties: {
                           author_FN: {
                              bsonType: "string",
                              description: "Author first name",
                              minLength:2,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           author_LN: {
                              bsonType: "string",
                              description: "Author last name",
                              minLength:2,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           author_faculty: {
                              bsonType: "string",
                              description: "Author faculty",
                              minLength:1,
                              maxLength:30,
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z:0-9À-ÿ]$"
                           },
                           author_email: {
                              bsonType: "string",
                              description: "Author email, must be a string of length 0-50",
                              minLength:9,
                              maxLength:70,
                              pattern: "^[\.a-z0-9]*(@upr\.edu)$"
                           }
                        }

                     }

                  },
                  actor: {
                     bsonType: ["array"],
                     minItems: 1,
                     maxItems: 5,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "Actors who play a role in the case study, must be a list of Actor objects, must follow the pattern, and is required",
                        properties: {
                           actor_FN: {
                              bsonType: "string",
                              description: "Actor first name",
                              minLength:1,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                          
                           },
                           actor_LN: {
                              bsonType: "string",
                              description: "Actor last name",
                              minLength:1,
                              maxLength:30,
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           role: {
                              bsonType: "string",
                              description: "Actor role",
                              minLength:1,
                              maxLength:30,
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z:0-9À-ÿ]$"
                           }
                        }

                     }
                  },
                  timeline: {
                     bsonType: ["array"],
                     minItems: 0,
                     maxItems:5,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "Timeline of a Case study, must be a list of Actor objects, must follow the pattern",
                        properties: {
                           event: {
                              bsonType: "string",
                              description: "Event what happened within the case study",
                              minLength:1,
                              maxLength:50,
                           },
                           eventStartDate: {
                              bsonType: "string",
                              description: "Date when event started, must be a string following the pattern",
                              minLength:9,
                              maxLength: 11,
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                           },
                           eventEndDate: {
                              bsonType: "string",
                              description: "Date when event ended, must be a string following the pattern",
                              minLength:9,
                              maxLength: 11,
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"   
                           }
                        }

                     }
                  },
                  section: {
                     bsonType: ["array"],
                     minItems: 0,
                     maxItems:10,
                     uniqueItems: false,
                     items: {
                        bsonType: "object",
                        description: "Sections of a Case study, must be a list of Section objects.",
                        properties: {
                           secTitle: {
                              bsonType: "string",
                              description: "Title of the section",
                              minLength: 1,
                              maxLength:50,
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$"
                           },
                           content: {
                              bsonType: "string",
                              description: "Content of the section",
                              minLength: 1
                           }
                        }

                     }
                  }
               }
            }
         }
      })

      
      db.createCollection("title_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               properties: {
                  title: {
                     bsonType: "string",
                     description: "Infrastructure category, must be a string, must follow the pattern, and is required",
                     minLength: 1,
                     maxLength:50,
                     pattern: "^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$"
                  }
               }
            }
         }
      })

      db.createCollection("description_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               properties: {
                  description: {
                     bsonType: "string",
                     description: "Infrastructure category, must be a string, must follow the pattern, and is required",
                     minLength: 1,
                     maxLength:500
                  }
               }
            }
         }
      })

      db.createCollection("infrastructure_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               minItems: 1,
               properties: {
                  infrasDocList: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "string",
                        additionalProperties: false,
                        description: "Infrastructure categories that case study has, must be a list of string, must follow the pattern, and is required",
                        minLength: 1,
                        maxLength:30,
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                     
                     }
                  }
               }
            }
         }
      })

      db.createCollection("damage_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               minItems: 1,
               properties: {
                  damageDocList: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "string",
                        additionalProperties: false,
                        description: "Infrastructure categories that case study has, must be a list of string, must follow the pattern, and is required",
                        minLength: 1,
                        maxLength:30,
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                     
                     }
                  }
               }
            }
         }
      })

      /*
       * Tag_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems regarding with the tags of the case study
      */
      db.createCollection("tag_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               minItems: 1,
               maxItems:10,
               properties: {
                  tagsDoc: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "string",
                        additionalProperties: false,
                        description: "Infrastructure categories that case study has, must be a list of string, must follow the pattern, and is required",
                        minLength: 1,
                        maxLength:30,
                        pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$"                     
                     }
                  }
               }
            }
         }
      })

      /*
       * Timeline_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems regarding with the timeline of the case study
      */
      db.createCollection("timeline_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               minItems: 0,
               maxItems:5,
               uniqueItems: false,
               properties: {
                  timeline: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "object",
                        description: "Timeline of a Case study, must be a list of Actor objects, must follow the pattern",
                        properties: {
                           event: {
                              bsonType: "string",
                              description: "Event what happened within the case study",
                              minLength: 1,
                              maxLength:50
                           },
                           eventStartDate: {
                              bsonType: "string",
                              description: "Date when event started, must be a string following the pattern",
                              minLength: 9,
                              maxLength:11,
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                           },
                           eventEndDate: {
                              bsonType: "string",
                              description: "Date when event ended, must be a string following the pattern",
                              minLength: 9,
                              maxLength:11,
                              pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                           }
                        }
            
                     }
                  }
               }
            }
         }
      })

      /*
       * Section_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems regarding with the sections of the case study
      */
      db.createCollection("section_embedded", {
         validator: {
            $jsonSchema: {
               bsonType:  "object",
               minItems: 0,
               maxItems:10,
               uniqueItems: false,
               properties: {
                  section: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "object",
                        description: "Sections of a Case study, must be a list of Section objects.",
                        properties: {
                           secTitle: {
                              bsonType: "string",
                              description: "Title of the section",
                              minLength: 1,
                              maxLength:50,
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$"
                           },
                           content: {
                              bsonType: "string",
                              description: "Content of the section",
                              minLength: 1
                           }
                        }
                     }
                  }
               }
            }
         }
      })

      /*
       * Actor_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems regarding with the actors of the case study
      */
      db.createCollection("actor_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               minItems: 0,
               maxItems:5,
               uniqueItems: false,
               properties: {
                  actor: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "object",
                        required: ["actor_FN", "actor_LN", "role"],
                        description: "Actors who play a role in the case study, must be a list of Actor objects, must follow the pattern, and is required",
                        properties: {
                           actor_FN: {
                              bsonType: "string",
                              description: "Actor first name",
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           actor_LN: {
                              bsonType: "string",
                              description: "Actor last name",
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$'                           
                           },
                           role: {
                              bsonType: "string",
                              description: "Actor role",
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z:0-9À-ÿ]$"
                           }
                        }
                     }
                  }
               }
            }
         }
      })

      /*
       * Author_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems regarding with the authors of the case study
      */
      db.createCollection("author_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               minItems: 0,
               maxItems:10,
               uniqueItems: false,
               properties: {
                  author: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "object",
                        required: ["author_FN", "author_LN", "author_faculty", "author_email"],
                        description: "Authors who wrote the case study, must be a list of Author objects, must follow the pattern, and is required",
                        properties: {
                           author_FN: {
                              bsonType: "string",
                              description: "Author first name",
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$',                             
                              minLength:2,
                              maxLength:30
                           },
                           author_LN: {
                              bsonType: "string",
                              description: "Author last name",
                              pattern: '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$',                              
                              minLength:2,
                              maxLength:30
                           },
                           author_faculty: {
                              bsonType: "string",
                              description: "Author faculty",
                              pattern: "^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z:0-9À-ÿ]$",
                              minLength:1,
                              maxLength:30
                           },
                           author_email: {
                              bsonType: "string",
                              description: "Author email, must be a string of length 0-50",
                              minLength:9,
                              maxLength:70,
                              pattern: "^[\.a-z0-9]*(@upr\.edu)$"
                           }
                        }
                     }
                  }
               }
            }
         }
      })

      /*
       * Location_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems regarding with the location of the case study
      */
      db.createCollection("location_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               minItems: 0,
               maxItems:10,
               uniqueItems: false,
               properties: {
                  location: {
                     bsonType: ["array"],
                     items: {
                        bsonType: "object",
                        description: "locations where that case study takes place, must be a list of string, must follow the pattern, and is required",
                        required: ["address", "latitude", "longitude"],
                        properties: {
                           address: {
                              bsonType: "string",
                              minLength: 7,
                              maxLength:50,
                              description: "Location's address",
                              pattern: "^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$"
                           },
                           latitude: {
                              bsonType: "double",
                              minimum:17.87,
                              maximum:18.53,
                              description: "Location's latitude"
                           },
                           longitude: {
                              bsonType: "double",
                              minimum:-67.28,
                              maximum:-65.23,
                              description: "Location's latitude"
                           }
                        }
                     }
                  }
               }
            }
         }
      })

      /*
       * Incident_Embedded schema definition with its attributes, limits & regex
       *    This will be the revision schems regarding with the incident date of the case study
      */
      db.createCollection("incident_embedded", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               properties: {
                  incidentDate: {
                     bsonType: "string",
                     description: "Tag category, must be a string, must follow the pattern, and is required",
                     minLength: 9,
                     maxLength:11,
                     pattern: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                  }
               }
            }
         }
      })

      /*
       *  Document_case_revisionschema definition with its attributes, limits & regex
       *    This will be the document for whenever a change is made on a document
      */
      db.createCollection("document_case_revision", {
         validator: {
            $jsonSchema: {
               bsonType: "object",
               properties: {
                  creatorId: {
                     bsonType: "objectId",
                     description: "Collaborator who made the change."
                  },
                  docId: {
                     bsonType: "objectId",
                     description: "Document where the change was made."
                  },
                  creator_name: {
                     bsonType: "string",
                     description: "Collaborator who made the changes",
                     minLength:2,
                     maxLength:90
                  },
                  creator_email:{
                     bsonType: "string",
                     description: "Collaborator who made the email",
                     minLength: 9,
                     maxLength:70,
                     pattern: '^[\.a-z0-9]*(@upr\.edu)$'
                     
                  },
                  document_title:{
                     bsonType: "string",
                     description: "Document's title",
                     minLength:10,
                     maxLength:50,
                     pattern: "^[A-ZÁÉÍÓÚ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9áéíóú]$"
                  },
                  revision_type:{
                     bsonType: "string",
                     minLength:2,
                     maxLength:20,
                     description: "Which attribute was updated",
                     pattern: '^[a-z A-Z À-ÿ]*[a-záéíóúñü]$'
                  },
                  revision_number:{
                     bsonType: "int",
                     minimum:0,
                     description: "id of the change made in a specific document"
                  },
                  revision_date:{
                     bsonType: "string",
                     description: "Revision date",
                     minLength:9,
                     maxLength:11,
                     pattern: "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
                  },
                  field_changed:{
                     bsonType: "object",
                     minItems: 1,
                     uniqueItems: false,
                     items: {
                        bsonType: ["array"],
                        properties: {
                           bsonType: "object",
                           new: {
                              bsonType: "object",
                              description: "New changes"
                           },
                           old: {
                              bsonType: "object",
                              description: "Old changes"
                           }
                        }
                     }
                  }
               }
            }
         }
      })
  
   }
})()
