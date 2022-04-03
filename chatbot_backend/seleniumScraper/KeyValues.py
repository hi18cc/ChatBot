<<<<<<< HEAD

=======
from seleniumScraper.utils import Utilities
from . import urls
>>>>>>> 185074aa463cc5eddb317427af2dee5191307dd2
class KeyValues:
    GameDay_Keys = [
        ['Saturday, August 6, 2022','9121fc9b-61b8-4be9-ba98-8f17822da322'],
        ['Sunday, August 7, 2022','af512934-abf6-46ab-99ff-258a66bd70c9'],
        ['Monday, August 8, 2022','eb1d3d43-6aba-4730-95c3-70e1073a24c1'],
        ['Tuesday, August 9, 2022','3b285a03-5d46-4ae9-9da9-7eff7bcf6bef'],
        ['Wednesday, August 10, 2022','36c51e37-bf21-4b4b-bc55-88b648314c51'],
        ['Thursday, August 11, 2022','3870d0df-a4d8-4c2c-98cc-009614fb7acc'],
        ['Friday, August 12, 2022','02c9f22e-733b-4532-a4d8-5272dd656e57'],
        ['Saturday, August 13, 2022','536f7480-9075-40c7-9896-513367445479'],
        ['Sunday, August 14, 2022','25889cbc-d1dc-4cd6-9b88-260776fc2e59'],
        ['Monday, August 15, 2022','64664b99-09a3-4a66-8aba-57f7ad0467a9'],
        ['Tuesday, August 16, 2022','20bf6bbf-2c6f-4fa9-b72a-853ec026fb4b'],
        ['Wednesday, August 17, 2022','b1d6793d-b49b-4e56-9f74-068bc5ebb845'],
        ['Thursday, August 18, 2022','ccae595e-95a8-414d-8132-13bf9f10fef2'],
        ['Friday, August 19, 2022','975582e9-ba3a-428c-9971-d83259a87d6f'],
        ['Saturday, August 20, 2022','90946399-c286-462c-a916-e9c6c3ce0982'],
        ['Sunday, August 21, 2022','77aab33c-f5ae-44a3-8396-d111a7a6c48f']
        ]

    Location_Keys = [
        ['Brock University', '37e317dc-35d5-4349-989f-4f7aa5442f86'], 
        ['Brock University- Alumni Field', 'b2bfadc5-e417-4e06-9145-393d0dcc7e83'],
        ['Brock University-Eleanor Misener Aquatics Centre',  'd2978ed3-ba92-4dd1-a1ff-2ab5c1b4503b'],
        ['Canada Games Park', '80524204-14c6-49fa-916a-b5e83ccb4077'],
        ['Etobicoke Olympium', '7702d14e-c8f9-41f0-b8d6-4fef83b93d06'],
        ['Legends on the Niagara', 'd1a65c72-8bbd-4a2a-8359-f6ba189b4113' ],
        ['Meridian Centre', 'd31822f8-7181-4eed-ada0-1e5d4c6cc23a'],
        ['Niagara College - Welland Campus', '56e85cce-950b-4aac-a2b0-21e63b8ef408'],
        ['Niagara-on-the-Lake Sailing Club', '23d4c06b-7197-4278-bb0a-17273ed6226e'],
        ['Niagara-on-the-Lake Tennis Club', 'a2ea8d0c-df9a-4983-848b-28b0fd15e3b9'],
        ['Oakes Park', 'c19ff91c-4cbf-40de-87ef-549a8ab2cce2'],
        ['Port Colborne - H.H. Knoll Lakeview Park', '5ad2ce22-d08e-436b-b333-f391f8a3d002'],
        ['Royal Canadian Henley Rowing Course', '62796dbb-1dbd-4647-8fd0-1caae7cdda92'],
        ['Southward Community Park','d6be5e96-c295-41dc-9cfa-5e513391c764'],
        ['Town of Pelham - Fonthill', '078b0097-a0f2-4168-8770-7426d2d20dbf'],
        ['Twelve Mile Creek', 'd96b02c1-6ca3-4de3-95fd-d9800b4e7779'],
        ['Welland Baseball Stadium', '93cb44b3-7357-4fc5-8fbd-e10a0da0f662'],
        ['Welland International Flatwater Centre ', '82b6f9ef-eb4c-413d-b06a-3d48f641167c'],
        ['Welland Tennis Club', 'b8d33ffe-00e8-41c8-809b-997f10e74ab7'],
        ['Youngs Sportsplex', '91d8b478-e00c-4ec4-9423-70d1d574dc74'],
        ['Athletes Village', '812b4529-d8d8-4336-93f0-c217abf4cc67'],
        ['Queen Victoria Park', '5f989e62-34cf-4e4c-a8a4-8c778771e24f'],
        ['Southward Community Park (Softball)', '8a24aeee-9c99-4d83-a10b-43f0177d05f8']
    ]

    Sport_Keys = [
        ['Athletics','af7cb307-6318-461d-a20b-1c32c5bbb1fd'],
        ['Baseball','35b25447-ede5-4b0e-8622-e0524d90223d'],
        ['Basketball','e64025a2-d870-44f9-9bc1-3d97a3e6e1a3'],
        ['Box Lacrosse','836ff56e-9c0d-4ddb-9a2c-9ce6e873533d'],
        ['Canoe Kayak','c1c327cb-db4a-48f2-9623-279a230b69d8'],
        ['Cycling','eb2b96d2-028b-4712-8797-cbff9e8d724f'],
        ['Diving','b001398d-e27b-43d6-8f19-d1e2d259bdb8'],
        ['Golf','08fe5b12-f64a-44b0-979c-e846b9bcad6d'],
        ['Rowing','12ee766e-693d-4c85-8e3d-7c7f37db288f'],
        ['Rugby Sevens','8f8697e0-5000-46df-97e3-c4fed2cd7f26'],
        ['Sailing','2de0f093-243f-4fb6-9c79-8185394decc0'],
        ['Soccer','5371cd4c-f7a2-4d9b-ab1a-48db2c1c56c3'],
        ['Softball','c8f19df1-6f7a-4b94-a357-4f77c1ee295d'],
        ['Swimming','2cd0bd3b-b77c-48cf-9f5a-17a13db8edf2'],
        ['Tennis','907cca96-457c-4e24-b5b4-d48cbbaafa02'],
        ['Triathlon','c689955c-c6f3-410e-8bc2-27f51986c41b'],
        ['Volleyball','1081694f-f495-490c-acfe-afe64dc91b82'],
        ['Wrestling','aab6e406-c519-48bb-a51c-0ec97413c788']
    ]

    Contingent_Keys = [
        ['Alberta','6590a90a-59f8-48b3-9c1b-7657f6c26878'],
        ['British Columbia','6521e249-0fa5-45f5-b575-c81c1c52a1e8'],
        ['Manitoba','048ef4d0-fc41-4de6-a4d4-d369c8eae16f'],
        ['New Brunswick','57df79bc-0c50-4301-9cac-f17d2c9dcc42'],
        ['Newfoundland and Labrador','f5ec856e-3a70-4555-9f63-050dc7bad87b'],
        ['Northwest Territories','49a7dda0-188c-4e9f-8cbf-75a5273d46f1'],
        ['Nova Scotia','8aab80c2-0b8b-4eee-af43-600838628ca4'],
        ['Nunavut','6850a130-b23f-4a20-bfc8-76f344b4b908'],
        ['Ontario','291d774d-8b97-4946-a0e0-b695fa2a92d6'],
        ['Prince Edward Island','c3b5702a-2580-4f9a-8063-d0189ce33358'],
        ['Quebec','5ade2256-09a7-4d95-b818-bbcf1c2cb51b'],
        ['Saskatchewan','94a3ceab-8e35-4cb5-9332-e0a4a1df8d1f'],
        ['Yukon','1c709ed0-94c5-4ad3-907d-9f8d45a3a61d']
        ]

    def getURL(gameday_key = '', sport_key = '', contingent_key = '' ):
        if(gameday_key != ''):
            gameday_key = '&GameDay_GUID=' + gameday_key
        if(sport_key != ''):
            sport_key = '&Sport_GUID=' + sport_key
        if(contingent_key != ''):
<<<<<<< HEAD
            contingent_key = '&Contingent_GUID=' + contingent_key
=======
            contingent_key = '&Contingent_GUID' + contingent_key
>>>>>>> 185074aa463cc5eddb317427af2dee5191307dd2
        

        url = f'https://cg2022.gems.pro/Result/Calendar.aspx?SetLanguage=en-CA{gameday_key}{sport_key}{contingent_key}&Grouping=DS'
        return url
