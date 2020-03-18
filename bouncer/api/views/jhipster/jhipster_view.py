import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class JhipsterView(APIView):
    def post(self, request):
        raw_data = request.data
        try:

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


                with open('.yo-rc.json', 'w') as outfile:   
                    json.dump(output, outfile)


            return Response(data  )
        except:
            return Response(dict(error="I couldn't get valid data"), status=status.HTTP_400_BAD_REQUEST)
