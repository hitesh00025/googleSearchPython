import pprint

from googleapiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  # NOTE : use your own KEY and SEARCH KEY
  
  service = build("customsearch", "v1",
            developerKey="AIzaSyAyO9ZSUrVBFbgPhE7_iaXDBRr35F_SdwQ")

  res = service.cse().list(
      q='hitesh kumar merck',
      cx='001651119929652751903:hsy37cecsye',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()
