# IReNE-Database

For a Technical documentacion of the main files of this repository, follow this path
Documentation -> _build -> html -> index.html
Run index.html in a brower

## How to initialize the database

1. First download the following mongodb library:
    - `npm install mongodb --save`
2. Run the init_db.js file where it will initialize db with its collections & restrictions.
    - `node init_db.js`
3. Open another terminal window and go back to the database repository.
4. Run predefined_data.py to fill the database with all the predefined data that it's going to have.
    - `python3 predefined_data.py`
5. Run mock_data.py to fill the database with mock data of collaborators & documents
    - `python3 mock_data.py`


## Database schema

1. Document Class for Collaborators. 
    - Collaborators are the users that will Create/Edit Case Studies.
        - List of attributes:
            - first_name: <String> Collaborator's first name.
                - min_length: 1, max_length: 30, required
                - attribute follows this regex: '^([a-z A-Z \-]*)$'
            - last_name: <String> Collaborator's last name.
                - min_length: 1, max_length: 30, required
                - attribute follows this regex: '^([a-z A-Z \-]*)$'
            - email: <String> Collaborator's email. It must be a @upr.edu email.
                - min_length: 9, max_length: 50, required, unique
                - attribute follows this regex: '.*(@upr\.edu)$'
            - banned: <Boolean> <Default=False> When set to true, the Collaborator looses access to Tellspace service.
                - required
            - approved: <Boolean> <Default=False>  When set to true, the Collaborator gains access to Tellspace service.   
                - required

2. Document Class for Admin. 
    - Admin are the users that will have access to the Admin Dashboard.
        - List of attributes:
            - username: <String>  Admin's username.
                - min_length: 8, max_length: 20, unique, required
                - username attribute follows this regex: '(^[^.]([a-zA-Z0-9]*)[\.]([a-zA-Z0-9]*))[^.]$' 
            - password: <String> Admin's  password.
                - min_length: 8, max_length: 20, unique, required
                - password attribute follows this regex: '(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z]))'
3. Document Class for Tag. 
    - Tag are the tags available for used as keywords for the DocumentCase. There will be some pre-defined by the Team and/or Admin, and the majority will be created by the Collaborators.
        - List of attributes:
            - tagItem: <String>  Tag that can be used in a DocumentCase.
                - min_length: 1, max_length: 50, unique, required 
                - attribute has the following regex '^([a-z A-Z / & , \- ]*)$'
4. Document Class for Infrastructure. 
    - These are going to be the categories available for the description of the infrastructure in the DocumentCase. All of them will be pre-defined by the Team and/or Admins.
        - List of attributes:
            - infrastructureType: <String>  category that can be used in a DocumentCase.
                - min_length: 1, max_length: 50, unique, required
                - attribute has the following regex '^([a-z A-Z / & , \- ]*)$' 
5. Document Class for Damage. 
    - These are going to be the categories available for the description of the Damage in the DocumentCase. All of them  will be pre-defined by the Team and/or Admins.
        - List of attributes:
            - damageType: <String>  category that can be used in a DocumentCase.  
                - min_length: 1, max_length: 50, unique, required
                - attribute has the following regex '^([a-z A-Z / & , \- ]*)$'
6. Document Class for CityPR. 
    - These are going to be the list of cities of Puerto Rico for the use of selection location for DocumentCase & as a filter list for a visualization. All of them  will be pre-defined by the Team.
        - List of attributes:
            - damageType: <String>  category that can be used in a DocumentCase. 
                - min_length: 1, max_length: 50, unique, required 
7. EmbeddedDocument Class for Author. 
    - These are going to be the authors of a DocumentCase, the ones who wrote it.
        - List of attributes:
            - author_FN: <String>  Author's First Name.
                - min_length: 1, max_length: 30, required 
                - attribute follows this regex: '^([a-z A-Z \-]*)$'
            - author_LN: <String>  Author's Last Name.
                - min_length: 1, max_length: 30, required
                - attribute follows this regex: '^([a-z A-Z \-]*)$'
            - author_email: <String>  Author's Email.
                - min_length: 9, max_length: 50, required 
                - email attribute follows this regex: '.*(@upr\.edu)$'
            - author_faculty: <String>  Author's Faculty. 
                - min_length: 9, max_length: 30, required
8. EmbeddedDocument Class for Actor. 
    - These are going to be the Actor of a DocumentCase, the ones having a role in the DocumentCase.
        - List of attributes:
            - actor_FN: <String>  Actor's First Name. 
                - min_length: 1, max_length: 30, required
                - attribute follows this regex: '^([a-z A-Z \-]*)$'
            - actor_LN: <String>  Actor's Last Name.
                - min_length: 1, max_length: 30, required
                - attribute follows this regex: '^([a-z A-Z \-]*)$'
            - role: <String>  Actor's role in the DocumentCase.
                - min_length: 1, max_length: 30, required
9. EmbeddedDocument Class for Timeline. 
    - These will consist of the Timeline of a DocumentCase, describing the events followed.
        - List of attributes:
            - event: <String>  Event happend within the DocumentCase.
                - min_length: 10, max_length: 100, required 
            - eventStartDate: <String>  Date when the event started, it has to have the following format: 'YYYY-MM-DD'.
                 - eventStartDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                 - min_length: 9, max_length: 11, required 
            - eventEndDate: <String>  Date when the event ended, it has to have the following format: 'YYYY-MM-DD'.
                - eventEndDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                - min_length: 9, max_length: 11, required 
10. EmbeddedDocument Class for Section. 
    - These are going to be the body of the Document Case.
        - List of attributes:
            - secTitle: <String>  Section's title. 
                - min_length: 1, max_length: 100, required
            - content: <String>  Section's body.
                - min_length: 1, required
11. EmbeddedDocument Class for Location. 
    - These are going to be the body of the Document Case.
        - List of attributes:
            - address: <String>  Location's address. 
                - min_length: 1, required
            - latitude: <Number>  Location's latitude.
                - min_value: 17.68, max_length: 18.54, required
            - longitude: <Number> Location's Longitude.  
                - min_value: -67.29, max_length: -65.22, required

12. Document Class for DocumentCase. 
    - DocumentCase will consist of a Case Study created by a Collaborator.
        - List of attributes:
            - creatoriD: <String>  the Collaborator's id which created the Case study.
                - min_length: 1, required
            - title: <String> The case study's title .
                - min_length: 10, max_length: 100, required, unique
            - language: <String> The language which the case study is written.
                - min_length: 1, required
            - description: <String> Case study's description.
                - min_length: 1, max_length: 500, required
            - published: <Boolean> <Default=False> When set to true, the case study will be visible in SearchSpace service.
            - incidentDate: <String>  Date when the incident happened, it has to have the following format: 'YYYY-MM-DD'.
                - min_length: 9, max_length: 11, required
                - incidentDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            - creationDate: <String>  Date when the case study was created, it has to have the following format: 'YYYY-MM-DD'.
                - min_length: 9, max_length: 11, required
                - creationDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]' 
            - lastModificationDate: <String>  Last date when the case study was modified, it has to have the following format: 'YYYY-MM-DD'.
                - min_length: 9, max_length: 11, required
                - lastModificationDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'  
            - tagsDoc: List<String> of tags from the case study. 
                - For string: min_length: 0, max_length: 50, not required, unique
                - For List: not required, max_length: 10
            - infrasDocList: List<String> of infrastructure categories from the case study. 
                - For string: min_length: 0, max_length: 50, required, unique
            - damageDocList: List<String> of damage categories from the case study. 
            - location: List<Location> of addresses where the case study took place.
                - For List: max_length: 5, not required
            - author: List<Author> of author objects, the ones who wrote the case study.
                - For List: max_length: 10, required
            - actor: List<Actor> of actor objects, the ones who plays a role in the case study.
                - For List: max_length: 5, required
            - section: List<Section> of section objects, this will consist the body of the case study.
                - For List: max_length: 10, not required
            - timeline: List<Timeline> of timeline objects, this will consist of the events that happened within the case study.
                - For List: max_length: 5, not required
             



