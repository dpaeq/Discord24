import discord
import asyncio

client = discord.Client()

token = "ODgzNTQ1NzIxMjAxMDk4NzYy.YTLgEw.9KmtXmJdMxCPvvVYDIWLHgRns18"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇 실행 완료')
    game = discord.Game("시비걸기")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.endswith("함"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/함.jpg")
        await message.channel.send(file=file)
        await message.channel.send("그런 함은 침몰하였습니다")
    if message.content.endswith("딱"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/딱지라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("딱지라이더")
    if message.content.endswith("시"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/시계라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("시계라이더")
    if message.content.endswith("자"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/자전거라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("자전거라이더")
    if message.content.endswith("바"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/바이올린라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("바이올린라이더")
    if message.content.endswith("가"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/가면라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("가면라이더")
    if message.content.endswith("빨"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/빨래라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("빨래라이더")
    if message.content.endswith("전"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/전기톱라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("전기톱라이더")
    if message.content.endswith("감"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/감염라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("감염라이더")
    if message.content.endswith("기"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/기타라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("기타라이더")
    if message.content.endswith("히"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/히틀러라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("히틀러라이더")
    if message.content.endswith("오"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/오랜지라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("오랜지라이더")
    if message.content.endswith("야"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/야옹이라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("야옹이라이더")
    if message.content.endswith("좀"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/좀비라이더.jpg")		
        await message.channel.send(file=file)
        await message.channel.send("좀비라이더")
    if message.content.endswith("중"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/중력라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("중력라이더")
    if message.content.endswith("지"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/지나가던라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("지나가던라이더")
    if message.content.endswith("트"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/트럼펫라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("트럼펫라이더")
    if message.content.endswith("신"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/신호등라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("신호등라이더")
    if message.content.endswith("고"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/고자라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("고자라이더")
    if message.content.endswith("짜"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/짜파게티라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("짜파게티라이더")
    if message.content.endswith("도"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/도둑라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("도둑라이더")
    if message.content.endswith("라"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/라디오라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("라디오라이더")
    if message.content.endswith("더"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/더이라면가.jpg")
        await message.channel.send(file=file)
        await message.channel.send("더이라면가")
    if message.content.endswith("아"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/아이라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("아이라이더")
    if message.content.endswith("인"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/인형극라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("인형극라이더")
    if message.content.endswith("굴"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/굴라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("엄마가섬그늘에굴따러가면라이더")
    if message.content.endswith("해"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/해변라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("해변라이더")
    if message.content.endswith("다"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/다람쥐라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("다람쥐라이더")
    if message.content.endswith("만"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/만두라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("만두라이더")
    if message.content.endswith("무"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/무면허라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("무면허라이더")
    if message.content.endswith("엄"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/엄준식라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("엄준식라이더")
    if message.content.endswith("ㅗ"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/ㅗ.jpg")
        await message.channel.send(file=file)
        await message.channel.send("ㅗ")
    if message.content.endswith("왜"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/왜라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("왜!")
    if message.content.endswith("ㅋ"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/ㅋㅋㅋ.jpg")
        await message.channel.send(file=file)
        await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
    if message.content.endswith("요"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/요리사라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("요리사라이더")
    if message.content.endswith("마"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/마법전사유캔도.jpg")
        await message.channel.send(file=file)
        await message.channel.send("마법전사유캔도")
    if message.content.endswith("데"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/데리야끼라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("데리야끼라이더")
    if message.content.endswith("어"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/어부라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("어부라이더")
    if message.content.endswith("한다"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/다이아몬드라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("다이아몬드라이더")
    if message.content.endswith("와"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/와샌즈.jpg")
        await message.channel.send(file=file)
        await message.channel.send("아시는구나!")
    if message.content.endswith("싯팔"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/처신잘해.jpg")
        await message.channel.send(file=file)
        await message.channel.send("욕하다 숨지지 말고")
    if message.content.endswith("져"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/져스티스크래쉬.jpg")
        await message.channel.send(file=file)
        await message.channel.send("JUSTICE CRASH!!!!")
    if message.content.endswith("나"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/나비라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("나비라이더")
    if message.content.endswith("네"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/네코라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("NEKO라이더")
    if message.content.endswith("니"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/니그로라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("니그로라이더")
    if message.content.endswith("두"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/두리안라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("두리안라이더")
    if message.content.endswith("임"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/임영웅.jpg")
        await message.channel.send(file=file)
        await message.channel.send("안녕하세요. 임영웅입니다~")
    if message.content.endswith("애"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/애플라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("애플라이더")
    if message.content.endswith("진"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/진실의방으로.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("등"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/등신대.jpg")
        await message.channel.send(file=file)
        await message.channel.send("뭐? 신?")
    if message.content.endswith("면"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/면발이억수로.jpg")
        await message.channel.send(file=file)
        await message.channel.send("면발이 억수로 부드럽네예~")
    if message.content.endswith("파"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/파돌리기.jpg")
        await message.channel.send(file=file)
        await message.channel.send("아랏 챠챠라 리비다비빔 빠라 린칸덴칸 덴단도")
    if message.content.endswith("와!"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/와.jpg")
        await message.channel.send(file=file)
        await message.channel.send("와ㅏ!")
    if message.content.endswith("ㅈㄹ"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/옘병지랄.jpg")
        await message.channel.send(file=file)
        await message.channel.send("ㅈㄹㅋㅋㅋ")
    if message.content.endswith("뷁"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("뺙"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("삑"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("궭"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("이잉"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("왈"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("왈!"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("왕!"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/개소리야.jpg")
        await message.channel.send(file=file)
    if message.content.endswith("음"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/음악라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("음악라이더")
    if message.content.endswith("대"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/대게라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("대게라이더")
    if message.content.endswith("손"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/손목시계라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("손목시계라이더")
    if message.content.endswith("길"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/길거리라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("길거리라이더")
    if message.content.endswith("후"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/후크라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("후크라이더")
    if message.content.endswith("냐"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/냐옹이라이더.jpg")
        await message.channel.send(file=file)
        await message.channel.send("냐!")
    if message.content.endswith("여"):
        file = discord.File("C:/Users/joo18/Documents/사진짤/여름.jpg")
        await message.channel.send(file=file)
        await message.channel.send("여름이었다.")

client.run(token)