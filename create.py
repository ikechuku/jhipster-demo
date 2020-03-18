import json
raw_data = {'fingerprint': 'fb3fd844f6b62eb7bdce363473b92054e567f90b33490a1e2551663092b4e68a', 'fields': [{'name': 'applicationType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '4be5ad95d3006509f40645eb524a918497c2191e2a63256c590fcae4f591dc10', 'slot': 'choice', 'string': 'Monolithic application (recommended for simple projects)', 'value': 'Monolithic application (recommended for simple projects)', 'modified': False, 'reference': 'f69214dfaefe5e172b98a1a611be7040a2fe11f8995b7be84646ae39ab9fca9f', 'time': 1584108057768, 'key': '5d056f7c8ba9bd53e3c4fa2e5151e1b4a517df769c83c9efd885e63ee473f06e'}, {'name': 'Do you want to make it reactive with Spring WebFlux', 'type': 'tripetto-block-yes-no', 'version': '1.0.3', 'node': 'b7e315bc2b3a1dd44b118b59e1fafa980087cae4b28834960f1394d34d4916be', 'slot': 'answer', 'string': 'no', 'value': 'no', 'modified': False, 'time': 1584108059377, 'key': '589f6d728b5aa418ae8d0eed98db8dcb2d2913565566c0a6d00a22c26821d182'}, {'name': 'What is the base name of your application?', 'type': 'tripetto-block-text', 'version': '2.0.0', 'node': 'd67bfb2649835f03a8a1d4d9578e539aee0fb143c9a662c9f8c1323e3564e974', 'slot': 'value', 'string': 'ZEEKARAR', 'value': 'ZEEKARAR', 'modified': False, 'time': 1584108077723, 'key': 'e43ecb8bed20a9f8feb5fd59f6f8e9091284d5442f1ecc6528c13018adb0c1d1'}, {'name': 'What is your default Java package name?', 'type': 'tripetto-block-text', 'version': '2.0.0', 'node': 'd89afe24f07670dabacb69746d4d03b942ef460357cb7a612f07a11ecc6e4007', 'slot': 'value', 'string': 'parallelscore.research.org', 'value': 'parallelscore.research.org', 'modified': False, 'time': 1584108104308, 'key': '3597160feda07174adabab2df2d4196a7cc144f52fa5b083e7d874c8a17c8929'}, {'name': 'Do you want to use JHipster Registry to configure, monitor and scale your application?', 'type': 'tripetto-block-yes-no', 'version': '1.0.3', 'node': 'cfc2cee7def3aa3cbb27d86b28281d2a51cd4704b6f0d30c604f469319025e84', 'slot': 'answer', 'string': 'no', 'value': 'no', 'modified': False, 'time': 1584108107106, 'key': '087348cadbaad83ad1b9f541c702228fc5c1980624d14aef16de6403c84879df'}, {'name': 'authenticationType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': 'e82058214cb9e057eebf6e187c562f52a8a16901552bb55340d2718e98d22698', 'slot': 'choice', 'string': 'OAuth 2.0 / OIDC Authentication (stateful, works with Keycloak and Okta)', 'value': 'OAuth 2.0 / OIDC Authentication (stateful, works with Keycloak and Okta)', 'modified': False, 'reference': '9042517fcfa286e9f655f5b900d0b0f4541a5fe38ec576d04d4d454c8f8f1d89', 'time': 1584108108451, 'key': 'f373f4b70b7c9acabda11c9693ccd5956e3435abb0f13ecc033c46a233ed4332'}, {'name': 'databaseType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '0ea05e2e82c39d2b0f2f995bd0fe69434c793d8673584d5f3ccd1c22c4041ce1', 'slot': 'choice', 'string': 'SQL (H2, MySQL, MariaDB, PostgresSQL, Oracle, MSSQL)', 'value': 'SQL (H2, MySQL, MariaDB, PostgresSQL, Oracle, MSSQL)', 'modified': False, 'reference': '98f329952ce09bd8f75a76ab0f807af035bb24903bf24a165257061b840f107f', 'time': 1584108109709, 'key': '4161a95cfa3a059b11a39e413963c94dff202923166d2033a7cb8db4de7a2a1b'}, {'name': 'devDatabaseType', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '9a3d5596ab96ca1b4af9369ec82a707d5efa22a852c1b1b46e06f63b87139329', 'slot': 'choice', 'string': 'Oracle', 'value': 'Oracle', 'modified': False, 'reference': '4652a0289e91a922cf8c835c87d8d1ec9a688d925d42cf043e6d9fbf523d81e6', 'time': 1584108111327, 'key': 'e32cc5c929adb7be86609802cd49a31f4f65fec62e2deaefe496016090e922d5'}, {'name': 'Which Production database would you like to use?', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': 'fcf3c1440083923c4c930896b51a5a135804629eb37ed9735e93f219e8753a23', 'slot': 'choice', 'string': 'Oracle', 'value': 'Oracle', 'modified': False, 'reference': 'c93c19909cfbc78b735564c458f448d61c5543437efec322ff2e615bab88ce7a', 'time': 1584108112792, 'key': '572d9e694c65f411343c1497c2d697f6396ac9ad4ef3b19dbdb5ecc89fd2526f'}, {'name': 'Do you want to use the Spring cache abstraction?', 'type': 'tripetto-block-yes-no', 'version': '1.0.3', 'node': 'e47622c5466e3f30d954e21aba1f41719538fcb1a8f71ef8fa0155d827109df1', 'slot': 'answer', 'string': 'no', 'value': 'no', 'modified': False, 'time': 1584108114266, 'key': '4566ac94d79579e49aa235c15f5820fe2ab582480e60a567a0cd56c16b807ae9'}, {'name': 'Choice', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '5f08e397e80a1da13a2658bdf380ea9b8233a6f61edabdf41cc3e8084f7b8619', 'slot': 'choice', 'string': '', 'modified': False, 'key': 'bd5136bd63524d90de418f8eaaf8b93f2fb3357f90142fc5cecc626661ba6e38'}, {'name': 'buildTool', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': '49fd63cd9dc34b9ab45760b9a200399a1c2fcad173c0ee0053c8ddb0b8f88376', 'slot': 'choice', 'string': 'Maven', 'value': 'Maven', 'modified': False, 'reference': 'cf223271ee5d9805981544232bd4025703265c6f3cd6f28bc9a2f81eefc2ed9a', 'time': 1584108117864, 'key': '58f3d218804bf53b371a32aa309bd7143b7ef1febbcd32f7d33cdc1da1c07d39'}, {'name': 'clientFramework', 'type': 'tripetto-block-multiple-choice', 'version': '1.0.2', 'node': 'f0a24440a0564da9c0958960b93d66613280162edc196181b5c482eaa6b9bd32', 'slot': 'choice', 'string': 'React', 'value': 'React', 'modified': False, 'reference': '7c88e0b540cfda6da523e82daf2ea441bd37f03be5eb348b21f85893450aa333', 'time': 1584108119507, 'key': '4c9ab1d6b6554e4ec5e957a75f268e8d19ebe320153b1e03fd50d7c43ed94774'}]}
true = "true"
false = "false"
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