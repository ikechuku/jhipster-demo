import json
raw_data =  {'fingerprint': '03a6048328483b1ca8656db79af4d579663efeed4ed032cc77e32e0295796773', 'fields': [{'name': 'applicationType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '4be5ad95d3006509f40645eb524a918497c2191e2a63256c590fcae4f591dc10', 'slot': 'choice', 'string': 'Microservice application', 'value': 'Microservice application', 'modified': False, 'reference': '9042e795361a587fd5b3db31ae65c1c10f8ff18aec6a1e2b48660da7b45accd3', 'time': 1584540960496, 'key': '5d056f7c8ba9bd53e3c4fa2e5151e1b4a517df769c83c9efd885e63ee473f06e'}, {'name': 'Do you want to make it reactive with Spring WebFlux', 'type': 'tripetto-block-yes-no', 'version': '1.0.3', 'node': 'b7e315bc2b3a1dd44b118b59e1fafa980087cae4b28834960f1394d34d4916be', 'slot': 'answer', 'string': 'no', 'value': 'no', 'modified': False, 'time': 1584540963126, 'key': '589f6d728b5aa418ae8d0eed98db8dcb2d2913565566c0a6d00a22c26821d182'}, {'name': 'baseName', 'type': 'tripetto-block-text', 'version': '2.0.0', 'node': 'd67bfb2649835f03a8a1d4d9578e539aee0fb143c9a662c9f8c1323e3564e974', 'slot': 'value', 'string': 'DJango', 'value': 'DJango', 'modified': False, 'time': 1584540966375, 'key': 'e43ecb8bed20a9f8feb5fd59f6f8e9091284d5442f1ecc6528c13018adb0c1d1'}, {'name': 'packageName', 'type': 'tripetto-block-text', 'version': '2.0.0', 'node': 'd89afe24f07670dabacb69746d4d03b942ef460357cb7a612f07a11ecc6e4007', 'slot': 'value', 'string': 'DJnago', 'value': 'DJnago', 'modified': False, 'time': 1584540969382, 'key': '3597160feda07174adabab2df2d4196a7cc144f52fa5b083e7d874c8a17c8929'}, {'name': 'Do you want to use JHipster Registry to configure, monitor and scale your application?', 'type': 'tripetto-block-yes-no', 'version': '1.0.3', 'node': 'cfc2cee7def3aa3cbb27d86b28281d2a51cd4704b6f0d30c604f469319025e84', 'slot': 'answer', 'string': 'no', 'value': 'no', 'modified': False, 'time': 1584540971588, 'key': '087348cadbaad83ad1b9f541c702228fc5c1980624d14aef16de6403c84879df'}, {'name': 'authenticationType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': 'e82058214cb9e057eebf6e187c562f52a8a16901552bb55340d2718e98d22698', 'slot': 'choice', 'string': 'HTTP Session Authentication (stateful, default Spring Security mechanism)', 'value': 'HTTP Session Authentication (stateful, default Spring Security mechanism)', 'modified': False, 'reference': 'c95e64dd6fd590c73cc92e671beda09eddc7466d0715ec7c28132261d21e06a4', 'time': 1584540972992, 'key': 'f373f4b70b7c9acabda11c9693ccd5956e3435abb0f13ecc033c46a233ed4332'}, {'name': 'databaseType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '0ea05e2e82c39d2b0f2f995bd0fe69434c793d8673584d5f3ccd1c22c4041ce1', 'slot': 'choice', 'string': 'Cassandra', 'value': 'Cassandra', 'modified': False, 'reference': 'd8e6ddc52336cb331723a2a01daf30f7f91f9ec90f9e917bb81c6409a6f0a4db', 'time': 1584540974356, 'key': '4161a95cfa3a059b11a39e413963c94dff202923166d2033a7cb8db4de7a2a1b'}, {'name': 'devDatabaseType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '9a3d5596ab96ca1b4af9369ec82a707d5efa22a852c1b1b46e06f63b87139329', 'slot': 'choice', 'string': 'Microsoft SQL Server', 'value': 'Microsoft SQL Server', 'modified': False, 'reference': 'a2252e7a344b7849fa23b445411ea75b55b27eb995cac1978a6697e4a238a0f3', 'time': 1584540975580, 'key': 'e32cc5c929adb7be86609802cd49a31f4f65fec62e2deaefe496016090e922d5'}, {'name': 'prodDatabaseType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': 'fcf3c1440083923c4c930896b51a5a135804629eb37ed9735e93f219e8753a23', 'slot': 'choice', 'string': 'Microsoft SQL Server', 'value': 'Microsoft SQL Server', 'modified': False, 'reference': '91c140082bf5577b64a0da8a0c75e3e1582fbf029e2b9bb04d93609ce3fad9f5', 'time': 1584540977169, 'key': '572d9e694c65f411343c1497c2d697f6396ac9ad4ef3b19dbdb5ecc89fd2526f'}, {'name': 'Do you want to use the Spring cache abstraction?', 'type': 'tripetto-block-yes-no', 'version': '1.0.3', 'node': 'e47622c5466e3f30d954e21aba1f41719538fcb1a8f71ef8fa0155d827109df1', 'slot': 'answer', 'string': 'yes', 'value': 'yes', 'modified': False, 'time': 1584540978508, 'key': '4566ac94d79579e49aa235c15f5820fe2ab582480e60a567a0cd56c16b807ae9'}, {'name': 'Choice', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '5f08e397e80a1da13a2658bdf380ea9b8233a6f61edabdf41cc3e8084f7b8619', 'slot': 'choice', 'string': ' [BETA] Yes, with the Infinispan implementation (hybrid cache, for multiple nodes)', 'value': ' [BETA] Yes, with the Infinispan implementation (hybrid cache, for multiple nodes)', 'modified': False, 'reference': 'b22501a82245f496d55b5e915f7340153d18cdb5f876fcad5a6564217b3e0ae3', 'time': 1584540979793, 'key': 'bd5136bd63524d90de418f8eaaf8b93f2fb3357f90142fc5cecc626661ba6e38'}, {'name': 'buildTool', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '49fd63cd9dc34b9ab45760b9a200399a1c2fcad173c0ee0053c8ddb0b8f88376', 'slot': 'choice', 'string': 'Maven', 'value': 'Maven', 'modified': False, 'reference': 'cf223271ee5d9805981544232bd4025703265c6f3cd6f28bc9a2f81eefc2ed9a', 'time': 1584540981274, 'key': '58f3d218804bf53b371a32aa309bd7143b7ef1febbcd32f7d33cdc1da1c07d39'}, {'name': 'clientFramework', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': 'f0a24440a0564da9c0958960b93d66613280162edc196181b5c482eaa6b9bd32', 'slot': 'choice', 'string': 'React', 'value': 'React', 'modified': False, 'reference': '7c88e0b540cfda6da523e82daf2ea441bd37f03be5eb348b21f85893450aa333', 'time': 1584540982762, 'key': '4c9ab1d6b6554e4ec5e957a75f268e8d19ebe320153b1e03fd50d7c43ed94774'}]}

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


with open('.yo-rc.json', 'w') as outfile:   
    json.dump(output, outfile)