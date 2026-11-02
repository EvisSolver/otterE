import json

link_json = '''{"outbounds":[{"protocol":"vless","sendThrough":"","settings":{"address":"lgdf.z9rkv4mqpx.com","email":"","encryption":"none","flow":"xtls-rprx-vision","id":"3171f8e0-8463-4d72-a277-004e66cbf0c8","level":0,"port":443,"seed":"","testpre":0},"streamSettings":{"network":"tcp","port":0,"realitySettings":{"fingerprint":"qq","limitFallbackDownload":{"AfterBytes":0,"BurstBytesPerSec":0,"BytesPerSec":0},"limitFallbackUpload":{"AfterBytes":0,"BurstBytesPerSec":0,"BytesPerSec":0},"masterKeyLog":"","maxClientVer":"","maxTimeDiff":0,"minClientVer":"","mldsa65Seed":"","mldsa65Verify":"","password":"Q6glPwZOhnjHTPtRJUTFgJOBQGgJGTprQfCf_NpOsTc~","privateKey":"","publicKey":"Q6glPwZOhnjHTPtRJUTFgJOBQGgJGTprQfCf_NpOsTc~","serverName":"lgdf.z9rkv4mqpx.com","shortId":"","show":false,"spiderX":"","type":"","xver":0},"security":"reality"},"tag":"falcon-copper","targetStrategy":""}]}'''
link = json.loads(link_json)

for type, value in link['outbounds'][0].items():
    print(f"{type}{value}\n")