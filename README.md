# OctoPrint-CICD_Playground
## Playground for CI/CD tests
### How to use it:

- Login to Github and check that you have a "Personal Accesstoken". This token is needed, so that travis could push the zip-file to your githib-release.
Go to "Settings / Developer Settings / Personal access tokens"
    
    Activate the scope "repo"

- Go to your Github-Project and activate the travis-webhook (Settings/Webhooks)
    
    Payload URL: https://notify.travis-ci.org

    Content type: application/x-wwww.form-urlencoded
    
    Individual events: Just the push event


- Go to Travis-Page / Settings and select your Repository 

- Add the "Personal access token" as an "Environment Variable" to your repo, like this
    GITHUB_TOKEN = 483f7219e9e15d70....

- Copy .travis.yml to your Octoprint root folder (no changes needed)

- Add the "badge-icons" to your readme as follows (replace CICD_Playground with your repositoriy-url):
```
[![Version](https://img.shields.io/badge/dynamic/json.svg?color=brightgreen&label=version&url=https://api.github.com/repos/OllisGit/OctoPrint-CICD_Playground/releases&query=$[0].name)]()
[![Released](https://img.shields.io/badge/dynamic/json.svg?color=brightgreen&label=released&url=https://api.github.com/repos/OllisGit/OctoPrint-CICD_Playground/releases&query=$[0].published_at)]()
![GitHub Releases (by Release)](https://img.shields.io/github/downloads/OllisGit/OctoPrint-CICD_Playground/latest/total.svg)
```


# OctoPrint-Playground Plugin
[![Version](https://img.shields.io/badge/dynamic/json.svg?color=brightgreen&label=version&url=https://api.github.com/repos/OllisGit/OctoPrint-CICD_Playground/releases&query=$[0].name)]()
[![Released](https://img.shields.io/badge/dynamic/json.svg?color=brightgreen&label=released&url=https://api.github.com/repos/OllisGit/OctoPrint-CICD_Playground/releases&query=$[0].published_at)]()
[![Download-Statisic](https://img.shields.io/badge/dynamic/json.svg?color=brightgreen&label=downloads&query=%24%5B0%5D.assets%5B0%5D.download_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FOllisGit%2FOctoPrint-CICD_Playground%2Freleases)]()

Orig. Shields.io ![GitHub Releases (by Release)](https://img.shields.io/github/downloads/OllisGit/OctoPrint-CICD_Playground/latest/total.svg)

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OllisGit/OctoPrint-CICD_Playground/releases/latest/download/master.zip

