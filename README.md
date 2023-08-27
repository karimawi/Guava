<h1 align="center"><img src="https://i.imgur.com/v59khn0.png" alt="Guava" width=30 style="vertical-align:top"/> Guava</h1>
<br/>

> ⚠ **[Repository Archived] UPDATE 27th of August 2023:** A couple of days ago Riot Games added a new captcha verification system to their login auth flow, I went back and forth with some tools and libraries trying to find a solution to the problem that doesn't take a full year to login, but unfortunately the best thing I could find is captcha solving services which as you might be thinking are paid API keys that I can't afford, and still they take up to 20 seconds to solve the captcha, so until Riot removes this captcha thing or goes to a different approach that doesn't completely kill my login algorithm, this repository will be archived, I'm very upset writing this since I wrote a ton of new features and UI changes that were very close to being finished and now they're of no use, farewell, Guava. And thank you for using it.
<br/>


> ⚠ **Important Notice 30th of April 2023:** I wrote this program as a "fun" project to practice some Tkinter for our Python course at uni, didn't think it would get any attention or be actually used by people, so I didn't take the time to write it in an organized/object-oriented manner, it's mostly jank and spaghetti so, it's getting a rewrite as soon as possible, all the known bugs will be fixed, the code would be more readable and organized in more than one file, a handful of QoL features will be added like summoner details, login shortcuts, list reorder and much more, I started. Still, it's going to take a while, since I'm most of the time either studying for college or in campus, my free time is limited, but I'll try my best. Thanks for using Guava 💛
<br/>

<p align="center">
  <a href="#" target="_blank">
    <img src="https://img.shields.io/badge/Version-1.0.0%20--%20Beta-yellow?labelColor=1E1E1E&color=B5C531&style=for-the-badge" alt="Version"/>
    </a>
  <a href="https://discord.com/users/609230785769111554" target="_blank">
    <img src="https://img.shields.io/badge/Discord-Profile-Yellow?labelColor=1E1E1E&color=B5C531&style=for-the-badge&logo=discord&logoColor=B5C531" alt="Chat"/>
    </a>
   <a href="https://github.com/karimawii/Guava/releases/" target="_blank">
    <img src="https://img.shields.io/github/downloads/karimawii/Guava/total?labelColor=1E1E1E&color=B5C531&style=for-the-badge&logo=data:image/svg+xml;base64,PCEtLSBVcGxvYWRlZCB0bzogU1ZHIFJlcG8sIHd3dy5zdmdyZXBvLmNvbSwgVHJhbnNmb3JtZWQgYnk6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIHdpZHRoPSIyMHB4IiBoZWlnaHQ9IjIwcHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJub25lIj4KCjxnIGZpbGw9IiNCNUM1MzEiPgoKPHBhdGggZD0iTTguNzUgMS43NWEuNzUuNzUgMCAwMC0xLjUgMHY2LjU5TDUuMyA2LjI0YS43NS43NSAwIDEwLTEuMSAxLjAyTDcuNDUgMTAuNzZhLjc4Ljc4IDAgMDAuMDM4LjAzOC43NDguNzQ4IDAgMDAxLjA2My0uMDM3bDMuMjUtMy41YS43NS43NSAwIDEwLTEuMS0xLjAybC0xLjk1IDIuMVYxLjc1eiIvPgoKPHBhdGggZD0iTTEuNzUgOWEuNzUuNzUgMCAwMS43NS43NXYzYzAgLjQxNC4zMzYuNzUuNzUuNzVoOS41YS43NS43NSAwIDAwLjc1LS43NXYtM2EuNzUuNzUgMCAwMTEuNSAwdjNBMi4yNSAyLjI1IDAgMDExMi43NSAxNWgtOS41QTIuMjUgMi4yNSAwIDAxMSAxMi43NXYtM0EuNzUuNzUgMCAwMTEuNzUgOXoiLz4KCjwvZz4KCjwvc3ZnPg==" alt="Download"/>
  </a>
  <a href="https://github.com/karimawii/Guava/blob/master/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/karimawii/Guava?labelColor=1E1E1E&color=B5C531&style=for-the-badge&logo=data:image/svg+xml;base64,PCEtLSBVcGxvYWRlZCB0bzogU1ZHIFJlcG8sIHd3dy5zdmdyZXBvLmNvbSwgVHJhbnNmb3JtZWQgYnk6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPg0KPHN2ZyANCiAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIg0KICB3aWR0aD0iMjQiDQogIGhlaWdodD0iMjQiDQogIHZpZXdCb3g9IjAgMCAyNCAyNCINCiAgZmlsbD0ibm9uZSINCiAgc3Ryb2tlPSIjQjVDNTMxIg0KICBzdHJva2Utd2lkdGg9IjIiDQogIHN0cm9rZS1saW5lY2FwPSJyb3VuZCINCiAgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCINCj4NCiAgPHBhdGggZD0iTTE2IDE2bDMtOCAzLjAwMSA4QTUuMDAyIDUuMDAyIDAgMDExNiAxNnoiIC8+DQogIDxwYXRoIGQ9Ik0yIDE2bDMtOCAzLjAwMSA4QTUuMDAyIDUuMDAyIDAgMDEyIDE2eiIgLz4NCiAgPHBhdGggZD0iTTcgMjFoMTAiIC8+DQogIDxwYXRoIGQ9Ik0xMiAzdjE4IiAvPg0KICA8cGF0aCBkPSJNMyA3aDJjMiAwIDUtMSA3LTIgMiAxIDUgMiA3IDJoMiIgLz4NCjwvc3ZnPg==" alt="License"/>
  <br/>
  <br/>
  <img width="700" alt="Guava" src="https://i.imgur.com/IFXGuWA.png"/>
  <br/>
  <p align="center">
  An account manager & switcher for <a href="https://www.leagueoflegends.com/">League of Legends</a><br/> built with Python using Tkinter, features a sleek and modern GUI and a ton of functionality.
  <br/>
  <br/>
  <a href="#features">Features</a> |
  <a href="#faq">FAQ</a> |
  <a href="#installation">Installation</a> |
  <a href="#libraries">Libraries</a>
  </p>
  </a>
</p>

---

## Features

**Modern, Easy to Use GUI Where You Can:**
  - Add as many accounts as you want
  - Edit or delete them whenever
  - Import & Export Accounts
  - Easily Copy Account Credentials To Send Anywhere
  
**Everything is locally stored on your device, you can take a look at the code.**

<br/>
<br/>

## FAQ

**Does Guava Support Valorant?** <br/>
Unfortunately, my pc (which is a laptop) is really crap, I can't install or run the game, and I can't do it without having the game even if both games have the same client, some elements are different, like the Valorant Riot Client is all red, also I would want to kill existing processes of the game and for that I'd need to actually run it to get all of the processes names, tl;dr I'll add it once I have proper testing setup for it, whether I upgrade my device or use someone else's, but until that, Guava just supports League of Legends.

**Is Guava secure?** <br/>
As far as the code goes, there's nothing malicious, you can check it for yourself or ask someone who knows if you don't know how, as far as getting banned in game or smth like that, don't worry, it's far from possible to get banned from something like an account switcher, it does read your screen and is a script so you'd wonder it would get detected by league and you get banned, but the image recognition part pretty much ends right after the main client opens, and if you want you can also set Guava to exit itself after logging in.
<br/>
<br/>

## Installation 

These will link you to the latest builds found in the [releases](https://github.com/karimawii/Guava/releases/) tab of this repository,
you can then find the .msi installer.

as for manual installation, just download the source code, install the modules and run the Python file.

<br/>

> ⚠ This project is made to work for Windows computers, it will not work as intended on any other OS.<br/>
<br/>

> ⚠ Guava is still in beta, it's expected to have some bugs, please let me know if you encounter any by opening an [issue](https://github.com/karimawii/Guava/issues/new/choose)

<br/>
<br/>

## Libraries

GUI:
- [Tkitner](https://github.com/python/cpython/tree/main/Lib/tkinter)
- [TkExtraFont](https://github.com/TkinterEP/python-tkextrafont)
- [EasyGUI](https://github.com/robertlugg/easygui)
- [notify-py](https://github.com/ms7m/notify-py)

DB:
- [TinyDB](https://github.com/msiemens/tinydb)
- [wget](https://github.com/steveeJ/python-wget)

User Input Simulation:
- [AHK Python Wrapper](https://github.com/spyoungtech/ahk)
- [AppOpener](https://github.com/athrvvvv/AppOpener)
- [Pyperclip](https://github.com/asweigart/pyperclip)
