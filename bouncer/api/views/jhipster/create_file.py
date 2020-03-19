import json

def create_file(raw_data):
        # true = "true"
        # false = "false"
        output = {
                "generator-jhipster": {
                "promptValues": {
                "packageName": "org.jhipster.blog",
                "nativeLanguage": "en"
                },

                }
                }
        for field in raw_data["fields"]:
                if field['name']  == "applicationType" :
                        output["generator-jhipster"]["applicationType"] = field["string"]

                if field['name']  == "baseName" :
                        output["generator-jhipster"]["baseName"] = field["string"]

                if field['name']  == "packageName" :
                        output["generator-jhipster"]["packageName"] = field["string"]

                if field['name']  == "authenticationType" :
                        output["generator-jhipster"]["authenticationType"] = field["string"]
                        
                if field['name']  == "databaseType" :
                        output["generator-jhipster"]["databaseType"] = field["string"]

                if field['name']  == "devDatabaseType" :
                        output["generator-jhipster"]["devDatabaseType"] = field["string"]

                if field['name']  == "prodDatabaseType" :
                        output["generator-jhipster"]["prodDatabaseType"] = field["string"]

                if field['name']  == "buildTool" :
                        output["generator-jhipster"]["buildTool"] = field["string"]
                
                if field['name']  == "clientFramework" :
                        output["generator-jhipster"]["clientFramework"] = field["string"]

                if field["name"] == "progLang":
                        if field["string"] == "Kotlin":
                                output["generator-jhipster"]["otherModules"] =  [
                                {
                                        "name": "generator-jhipster-kotlin",
                                        "version": "1.6.0"
                                }
                                ]
                if field["name"] == "progLang":
                        if field["string"] == "Node":
                                output["generator-jhipster"]["otherModules"] =  [
                                {
                                        "name": "generator-jhipster-node",
                                }
                                ]

        with open('.yo-rc.json', 'w') as outfile:
                json.dump(output, outfile)
        print(output)
        return output