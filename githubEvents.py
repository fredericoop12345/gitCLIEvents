import requests
import sys

def displayFetchedActivities(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        for events in data:
            type=events.get("type")
            print(type)
            repos=events.get("repo")
            print(repos)
    except requests.exceptions.RequestException as e:
        print("Error :",e)

def main():
    if len(sys.argv)<2:
        print("Command should be of the form 'github-activity <username>' where you input your corresponding username")
    else:
        username=sys.argv[1]
        fullURL="https://api.github.com/users/"+str(username)+"/events"
        displayFetchedActivities(fullURL)


if __name__=="__main__":
    main()
