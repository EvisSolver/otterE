#ROADMAP_TO_PROXY_APP

## Optimize code to working with a lot servers
    - process = await asynci.create_subprocess_shell(command, stdout = asynci.subprocess.PIPE)
    
    - async-requests(aiohttp)
    - task-limiter(asyncio.Semaphore)

## Windows Support
    - need to all modules works stability in main dir(change "~/" on "home/") #DONE
    - docker #+-(pyinstaller)
    - requirements.txt(to it downloaded all necessary-library's) #DONE

## MVP GUI
    - QT6 how to works
    - design