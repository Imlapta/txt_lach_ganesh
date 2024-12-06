a
    ”ÿgú6  ã                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dl Z d dlZ	d dl
m
Z
 d dlm
Z
mZmZmZmZ d dlmZ d dlmZ d dl mZ d d lmZ d dlmZmZ d d	lmZ d d
lmZ d d
lm Z  d dl!m"Z" d d
lm#Z#m$Z$ d dl%m&Z& ede
eedZ'e (¡ Z)e)j*ddddd„ ƒZ+dd„ Z,e' -e .dg¡¡eedœdd„ƒZ/e' -e .d¡¡dd„ ƒZ0e' -e .dg¡¡eedœd d„ƒZ/d!d"„ Z1e2d#kre3d$ƒ d%d&„ Z4d'd(„ Z5e 6¡ Z7zFz$e7 8e4ƒ ¡ e7 8e5ƒ ¡ e7 9¡  W n e:yú   Y n0 W e7 ;¡  n
e7 ;¡  0 dS ))é    N)Úprogress_bar)ÚAPI_IDÚAPI_HASHÚ	BOT_TOKENÚ WEBHOOKÚPORT)Ú
ClientSession)Úlisten)Úgetstatusoutput)Úweb)ÚClientÚ filters)Ú Message)Ú	FloodWait)ÚStickerEmojiInvalid)Ú message)ÚInlineKeyboardButtonÚInlineKeyboardMarkup)ÚAshuÚbot)Zapi_idZapi_hashZ	bot_tokenú/T)Z
allow_headc                 Ã   s
   t  d¡S )Nz$https://t.me/chouhanbhai_bot)r
   Z
json_response)Z request© r   úm2.pyÚroot_route_handler!   s    r   c                  Ã   s   t jdd} |  t¡ | S )Ni€ÃÉ)Zclient_max_size)r
   Z
ApplicationZ
add_routesÚroutes)Z web_appr   r   r   Ú
web_server&   s    
r   Ústart©r   Úmc                 Ã   s6   |j tjttdddgtdddggƒdI d H  d S ) Nu5   âœœ á´€sÊœá´œá´›á´sÊœ É¢á´sá´¡á´€á´Éª ðŸ¸ðŸº âœœzhttps://t.me/chouhanbhai_bot)Úurlu+   ðŸ¦‹ ð…ð¨ð¥ð¥ð¨ð° ðŒðž ðŸ¦‹zhttps://t.me/chouhanbhai_bot)Zreply_markup)Ú
reply_textr   Z
START_TEXTr   r   r   r   r   r   Ú
account_login,   s    ÿÿúÿþr!   Ústopc                 Ã   s0   |  dd¡I d H  tjtjtjgtj¢R Ž  d S )Nu$   â™¦ ð’ð­ð¨ð©ð©ðžð­ â™¦T)r    ÚosÚexeclÚsysÚ
executableÚargv)Ú_r   r   r   r   Úrestart_handler=   s    r)   Zuploadc           1      Ã   s¼	  |  d¡I d H }|  |jj¡I d H }| ¡ I d H }| d¡I d H  d|jj› }zjt|dƒ}|  ¡ } W d   ƒ n1 sz0    Y  |  d¡} g }| D ]}	| 	|	 dd ¡¡ q–t
 
|¡ W n(   |  d¡I d H  t
 
|¡ Y d S 0 | d	t
|ƒ› d
¡I d H  |  |jj¡I d H }
|
j}
|
 d¡I d H  | d
¡I d H  |  |jj¡I d H }|j}
| d¡I d H  | tj¡I d H  |  |jj¡I d H }|j}| d¡I d H  zh|dkr²d
}nT|dkrÂd}nD|dkrÒd}n4|dkrâd}n$|dkròd}n|dkrd}nd}W n ty    d}Y n0 | tj¡I d H  |  |jj¡I d H }|j}| d¡I d H  d}|dkrr|}n|}| tj¡I d H  |  |jj¡I d H  }}|j}| d¡I d H  | ¡ I d H  |j}| d¡sâ| d¡røtd|› dƒ d}n|d k t
|ƒd krd }nt|
ƒ}zRt|d  t
|ƒƒD ]8}	||	 d   d!d"¡ d#d$¡ d%d&¡ d'd&¡}d| }d(|v r:tƒ 4 I d H šœ}|j|d)d*d+d,d+d-d.d/d0d1d2d3d4d5d6œd74 I d H š8}| ¡ I d H }t d8|¡ d ¡}W d   ƒI d H  q
1 I d H s 0    Y  W d   ƒI d H  q1 I d H s.0    Y  nÞd9|v rftjd:|› d;d<id7 ¡ d= }n²d>|v sŽd?|v sŽd9|v sŽd@|v rÎdAd<dBdCdDdEdFdGdHœ}d=|› ff} tjdI|| dJ}!|! ¡ d= }nJdK|v rô| dL¡dM }"dN|" dO }n$dP|v r| dL¡dM }"dQ|" dR }||	 dS  dTd&¡ dUd&¡ dLd&¡ dVd&¡ dWd&¡ dXd&¡ dYd&¡ dZd&¡ d[d&¡ d\d&¡ d]d&¡  ¡ }#t!|ƒ "d^¡› d_|#d d`… › }$da|v r¾db|› dc|› dd}%ndb|› de|› df}%dg|v rôdh|$› di|› dj|› dk }&nÎda|v rdl|› dm|› dn|$› dk }&nªdo|v r<dp|%› dq|› dn|$› dk }&n†drsLds|v rfdp|%› dt|› dn|$› dk }&n\|%dukszdv|v r”dp|%› dt|› dn|$› dk }&n.dws¤dx|v rªdy}&ndp|%› dz|› dn|$› dk }&zJd{t!|ƒ "d^¡› d||#› d}|
› d~|› d{	}'d{t!|ƒ "d^¡› d||#› d|
› d~|› d{	}(d€|v  rÈzLt# ||$¡I d H })| j$|jj|)|(dI d H }*|d 7 }t
 
|)¡ t% &d ¡ W nV t' yÂ }+ z<|  t!|+ƒ¡I d H  t% &|+j(¡ W Y d }+~+W q2W Y d }+~+n
d }+~+0 0 nDdw|v rŽzbdh|$› d‚|› dk}&|&› dƒ},t
 )|,¡ | j$|jj|$› dw|(dI d H }*|d 7 }t
 
|$› dw¡ W nV t'yŠ }+ z<|  t!|+ƒ¡I d H  t% &|+j(¡ W Y d }+~+W q2W Y d }+~+n
d }+~+0 0 n~d„|$› d…|› d†|› d‡ }-|  |-¡I d H }.t# *||&|$¡I d H }/|/}0|. d¡I d H  t# +| ||'|0||$|.¡ I d H  |d 7 }t% &d ¡ W nZ t	yh }+ z@|  dˆt!|+ƒ› d‰|$› dŠ|› ¡I d H  W Y d }+~+q2W Y d }+~+n
d }+~+0 0 q2W n6 t	y¦ }+ z|  |+¡I d H  W Y d }+~+n
d }+~+0 0 |  d‹¡I d H  d S )ŒNu(   sá´‡É´á´… á´á´‡ .á´›xá´› Ò“ÉªÊŸá´‡  âTz./downloads/ÚrÚ
z://é   uG   âˆ ðˆð§ð¯ðšð¥ð¢ð ðŸð¢ð¥ðž ð¢ð§ð©ð®ð­.u8   ÉªÉ´ á´›xá´› Ò“ÉªÊŸá´‡ á´›Éªá´›ÊŸá´‡ ÊŸÉªÉ´á´‹ ðŸ”—** **uo   **

sá´‡É´á´… Ò“Ê€á´á´  á´¡Êœá´‡Ê€á´‡ Êá´á´œ á´¡á´€É´á´› á´›á´ á´…á´á´¡É´ÊŸá´á´€á´… ÉªÉ´Éªá´›á´€ÊŸ Éªs 1uz   âˆ ðð¨ð° ðð¥ðžðšð¬ðž ð’ðžð§ð ðŒðž ð˜ð¨ð®ð« ððšð­ðœð¡ ððšð¦ðžZ144Z 256x144Z240Z 426x240Z360Z 640x360Z480Z 854x480Z720Z1280x720Z1080Z	1920x1080ZUNu   ï¸ âªâ¬â®â®â®ZRobinz http://zhttps://zwget 'z' -O 'thumb.jpg'z	thumb.jpgZnoz file/d/zuc?export=download&id=zwww.youtube-nocookie.com/embedzyoutu.bez?modestbranding=1Ú z/view?usp=sharingZ	visioniasz‡text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zen-US,en;q=0.9zno-cachez
keep-alivezhttp://www.visionias.in/ZiframeZnavigatez
cross-siteÚ1zuMozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36z("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android")ZAcceptzAccept-Languagez
Cache-ControlZ
ConnectionZPragmaZ RefererzSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezUpgrade-Insecure-Requestsz
User-Agentz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platform)Ú headersz(https://.*?playlist.m3u8.*?)\"zvideos.classplusappzChttps://api.classplusapp.com/cams/uploader/video/jw-signed-url?url=úx-access-tokenZ\eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r   ztencdn.classplusappz media-cdn-alisg.classplusapp.comzmedia-cdn.classplusappzapi.classplusapp.comzMobile-Androidz1.4.37.1Z18Z5d0d17ac8b3c9f51z(2848b866799971ca_2848b8667a33216c_SDK-30Zgzip)ZHostr0   z
user-agentz
app-versionz
api-versionz	device-idzdevice-detailszaccept-encodingz>https://api.classplusapp.com/cams/uploader/video/jw-signed-url)r/   Úparamsz/utkarshapp.mpdr   éþÿÿÿz$https://apps-s3-prod.utkarshapp.com/z/utkarshapp.comz
/master.mpdz&https://d26g5bnklkwsh4.cloudfront.net/z/master.m3u8r   ú	ú:ú+ú#ú|ú@Ú*Ú.ZhttpsZhttpé   z) é<   Zyoutuz
b[height<=z][ext=mp4]/bv[height<=z!][ext=mp4]+ba[ext=m4a]/b[ext=mp4]z
]/bv[height<=z]+ba/b/bv+baZacecwplyz
yt-dlp -o "z" -f "bestvideo[height<=zQ]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "ú"z yt-dlp -i -f "bestvideo[height<=z=]+bestaudio" --no-keep-video --remux-video mkv --no-warning "z" -o "zplayer.vimeoz
yt-dlp -f "z/+bestaudio" --no-keep-video --remux-video mkv "Zm3u8Z
livestreamz%" --no-keep-video --remux-video mkv "Ú0Ú unknownz.pdfÚdownloadZpdfzC+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "z**z. u   .mkv

Batch Name  Â» u   

Downloaded By Â» u   .pdf

Batch Name  Â» Zdrive)Z chat_idZdocumentZ captionz .pdf" "z -R 25 --fragment-retries 25uZ   **âŠâŸ± ðƒð¨ð°ð§ð¥ð¨ðšðð¢ð§ð  âŸ±âŠ Â»

ðŸ“ ððšð¦ðž Â» u!   
âŒ¨ ðð®ð¥ð¢ð­ð² Â» u   

ðŸ”— ð”ð‘ð‹ Â»** `ú`uZ   âŒ˜ ðƒð¨ð°ð§ð¥ð¨ðšðð¢ð§ð  ðˆð§ð­ðžð«ð®ð©ð­ðžð
u   
âŒ˜ ððšð¦ðž Â» u   
âŒ˜ ð‹ð¢ð§ð¤ Â» uE   âœ… ð’ð®ðœðœðžð¬ð¬ðŸð®ð¥ð¥ð² ðƒð¨ð§ðž),r    r	   ZchatÚidr@   ÚdeleteÚopenÚreadÚsplitÚappendr#   ÚremoveZeditÚlenÚtextr   Z Q1_TEXTÚ	ExceptionZ C1_TEXTZ T1_TEXTÚ
startswithr
   ÚintÚrangeÚ replacer   ÚgetÚreÚsearchÚgroupÚrequestsÚjsonÚstripÚstrÚzfillÚhelperZ
send_documentÚtimeÚsleepr   ÚxÚsystemZdownload_videoZsend_vid)1r   r   ZeditableÚinputr\   ÚpathÚfZ contentZlinksÚiZinput0Zraw_textZinput1Z	raw_text0Zinput2Z	raw_text2ÚresZinput3Z	raw_text3Z
highlighterZMRZinput6r   Z	raw_text6ZthumbÚcountÚVr   Z sessionZresprJ   r/   r1   ZresponserB   Zname1ÚnameZytfÚcmdZccZcc1ZkaÚcopyÚeZdownload_cmdZShowÚprogZres_fileÚfilenamer   r   r   r!   C   sÎ   &

ÿ








ÿþýüÿ 
òþÿb
ÿþûÿþýü ø
ý

ÿþýüûú ùø	÷
ö
õÿ 



((

ÿ
*


ÿ(ÿ
,&c                  Ã   sV   t rRtƒ I d H } t | ¡}| ¡ I d H  t |dt¡}|  ¡ I d H  tdt› ƒ d S )Nz 0.0.0.0zWeb server started on port )	r   r   r
   Z	AppRunnerZsetupZ TCPSiter    r   Úprint)ZappZrunnerZsiter   r   r   Úmain@  s    
rl   Ú__main__u¶  
    â–ˆâ–‘â–ˆâ–‘â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–„â€ƒâ–ˆâ–€â–€â€ƒâ–ˆâ–€â–ˆâ€ƒâ–„â–€â–ˆâ€ƒâ–ˆâ–€â–€â€ƒâ–€â–ˆâ–€â€ƒ â€ƒ â€ƒâ–„â–€â–ˆâ€ƒâ–ˆâ–€â€ƒâ–ˆâ–‘â–ˆâ€ƒâ–ˆâ–‘â–ˆâ€ƒâ–€â–ˆâ–€â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â€ƒâ–ˆâ–‘â–ˆâ€ƒ â€ƒ
    â–€â–„â–€â–„â–€â€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–„â–ˆâ€ƒâ–ˆâ–„â–€â€ƒâ–ˆâ–„â–„â€ƒâ–ˆâ–€â–„â€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–€â–‘â€ƒâ–‘â–ˆâ–‘â€ƒ â€ƒ â€ƒâ–ˆâ–€â–ˆâ€ƒâ–„â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒâ–ˆâ–„â–ˆâ€ƒâ–‘â–ˆâ–‘â€ƒâ–ˆâ–„â–ˆâ€ƒâ–„â–ˆâ€ƒâ–ˆâ–€â–ˆâ€ƒc                   Ã   s   t  ¡ I d H  d S ©N)r   r   r   r   r   r   Ú	start_botS  s    ro   c                   Ã   s   t ƒ I d H  d S rn   )rl   r   r   r   r   Ú	start_webV  s    rp   )<r#   rQ   r%   rU   rZ   Z asynciorT   Ú
subprocessZcorerY   Zutilsr   Úvarsr   r   r   r   r    Z aiohttpr   Z pyromodr	   r
   r
   Zpyrogramr   r
   Zpyrogram.typesr   Zpyrogram.errorsr   Z*pyrogram.errors.exceptions.bad_request_400r   Z!pyrogram.types.messages_and_mediar   r   r   Zstyler   r   Z
RouteTableDefr   rP   r   r   Z
on_messageZ commandr!   r)   rl   Ú__name__rk   ro   rp   Zget_event_loopZloopZ
create_taskZ
run_foreverÚKeyboardInterruptr"   r   r   r   r   Ú<module>   s`   

 }

ÿ 
