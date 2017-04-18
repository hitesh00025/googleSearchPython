# googleSearchPython

1. Setup Google API Key: 
   Go to : https://console.developers.google.com/apis/credentials?project=test-search-164923
   
   create Creditionals >> API KEYS >> Create.
   
2. Setup custom search engine
   go to : https://cse.google.com/cse/
   
   createsearchEngine >> Add a dummy URL >> Delete the URL after its created.
   
   
3. Install Google API client for Python
   Command : pip install google-api-python-client
   
   
4. Enable Custom Search API DISABLE from https://console.developers.google.com/


5. Run code : python googleSearchAPI.py

Output :

{u'context': {u'title': u'Testgooglesearch'},
 u'items': [{u'displayLink': u'www.linkedin.com',
             u'formattedUrl': u'https://www.linkedin.com/in/hiteshkumar0025',
             u'htmlFormattedUrl': u'https://www.linkedin.com/in/<b>hiteshkumar</b>0025',
             u'htmlSnippet': u'View <b>Hitesh Kumar&#39;s</b> professional profile on LinkedIn. ... In current role at <b>Merck</b>, I <br>\nam working on JavaScript full stack with Node.js, MongoDb and Express on&nbsp;...',
             u'htmlTitle': u'<b>Hitesh Kumar</b> | LinkedIn',
             u'kind': u'customsearch#result',
             u'link': u'https://www.linkedin.com/in/hiteshkumar0025',
             u'pagemap': {u'cse_image': [{u'src': u'https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAl9AAAAJDhjY2UxODI0LTcyMTctNDAwNC1iMTIyLTQ4MWQ3OWFiZDViNA.jpg'}],
                          u'cse_thumbnail': [{u'height': u'160',
                                              u'src': u'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQHe-1FAiBXK2tziVclwqWN0HtxEHHsWq6fFMzyFCfKdYoR9CrpdNamNeQ',
                                              u'width': u'160'}],
                          u'hcard': [{u'fn': u'Hitesh Kumar',
                                      u'photo': u'https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAl9AAAAJDhjY2UxODI0LTcyMTctNDAwNC1iMTIyLTQ4MWQ3OWFiZDViNA.jpg',
                                      u'title': u'MEAN Stack | Full Stack Developer at Merck'}],
                          u'metatags': [{u'application-name': u'LinkedIn',
                                         u'appname': u'chrome',
                                         u'detectadblock': u'//platform.linkedin.com/js/px.js',
                                         u'globaltrackingappid': u'webTracking',
                                         u'globaltrackingappname': u'chrome',
                                         u'globaltrackingurl': u'//www.linkedin.com/mob/tracking',
                                         u'lnkd-track-json-lib': u'https://static.licdn.com/scds/concat/common/js?h=2jds9coeh4w78ed9wblscv68v-ebbt2vixcc5qz0otts5io08xv',
                                         u'msapplication-tilecolor': u'#0077B5',
                                         u'msapplication-tileimage': u'https://static.licdn.com/scds/common/u/images/logos/linkedin/logo-in-win8-tile-144_v1.png',
                                         u'og:description': u"View Hitesh Kumar\u2019s professional profile on LinkedIn. LinkedIn is the world's largest business network, helping professionals like Hitesh Kumar discover inside connections to recommended job candidates, industry experts, and business partners.",
                                         u'og:image': u'https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAl9AAAAJDhjY2UxODI0LTcyMTctNDAwNC1iMTIyLTQ4MWQ3OWFiZDViNA.jpg',
                                         u'og:title': u'Hitesh Kumar | LinkedIn',
                                         u'og:url': u'https://www.linkedin.com/in/hiteshkumar0025?trk=public_profile_card_url',
                                         u'pageimpressionid': u'9efc68c4-657e-4b27-8411-e93e544da190',
                                         u'pagekey': u'public_profile_v3_desktop',
                                         u'referrer': u'origin',
                                         u'remotenavjscontentbaseurl': u'https://static.licdn.com/scds/concat/common/js?v=0.1.253',
                                         u'treeid': u'uML+2XlVshTAWLfk9SoAAA==',
                                         u'twitter:card': u'summary',
                                         u'twitter:site': u'@LinkedIn'}],
                          u'person': [{u'location': u'Greater New York City Area',
                                       u'org': u'Merck',
                                       u'role': u'MEAN Stack | Full Stack Developer at Merck'}]},

   
