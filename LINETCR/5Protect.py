# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from bs4 import BeautifulSoup
from datetime import datetime
#import time,random,sys,json,codecs,threading,glob,re,os,subprocess
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia, google,tempfile,glob,shutil,unicodedata,urllib3
import html5lib
from urllib import urlopen
import requests,tempfile
#from urllib3.contrib import pyopenssl
#from random import randint
from gtts import gTTS

cl = LINETCR.LINE() #Kalani
cl.login(token="En4au0WNUZp9guHbWob6.d0Y8Z+kWn1tqFy24ChaJ9G.9YaRapQlS/0FBeVEX7pXO7uI5YoWM4kSf76K8CwGyh0=")
cl.loginResult()

ki = LINETCR.LINE() #One
ki.login(token="En4au0WNUZp9guHbWob6.d0Y8Z+kWn1tqFy24ChaJ9G.9YaRapQlS/0FBeVEX7pXO7uI5YoWM4kSf76K8CwGyh0=")
ki.loginResult()

kk = LINETCR.LINE() #Two
kk.login(token="En4au0WNUZp9guHbWob6.d0Y8Z+kWn1tqFy24ChaJ9G.9YaRapQlS/0FBeVEX7pXO7uI5YoWM4kSf76K8CwGyh0=")
kk.loginResult()

kc = LINETCR.LINE() #Tree
kc.login(token="En4au0WNUZp9guHbWob6.d0Y8Z+kWn1tqFy24ChaJ9G.9YaRapQlS/0FBeVEX7pXO7uI5YoWM4kSf76K8CwGyh0=")
kc.loginResult()

ks = LINETCR.LINE() #Four
ks.login(token="En4au0WNUZp9guHbWob6.d0Y8Z+kWn1tqFy24ChaJ9G.9YaRapQlS/0FBeVEX7pXO7uI5YoWM4kSf76K8CwGyh0=")
ks.loginResult()

#ka = LINETCR.LINE() #Five
#ka.login(qr=True)
#ka.loginResult()

print "KalaniProtectBot login Success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""●▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬●
       ই✠☪1DaffaN3Kalani☪ইद
   ●▬ஜ۩124D15T1 T34M۩ஜ▬●
●▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬●
●▬ஜ۩Menu publik۩ஜ▬●
[★]Adminlist
[★]Info Group
[★]Welcome
[★]Creator
[★]Bot
[★]Wkwk
[★]Hehehe
[★]Galau
[★]You
[★]Please
[★]Lol
[★]Welcome
[★]Ping
[★]Ini Apa
●▬ஜ۩Menu admin۩ஜ▬●
[★]Status/Set
[★]Cancel
[★]Buka/Tutup qr
[★]Mid Bot
[★]Speed/Sp
[★]Cctv(Ciduk)
[★]Status/Set
[★]Gurl
[★]Tag all/Tagall
[★]Absen/Respon
[★]Banlist
[★]Yt: Text Cari
[★]Pp @Tag
[★]Dp @Tag
[★]Gn Nama Group
[★]Bot? (Mid Bot)
[★]Mid Bot
[★]Me (Cek Mid)
[★]Info Group
[★]Mid @
[★]Ig: Instagram
[★]Pp Group (Nama)
[★]One Piece
●▬ஜ۩Menu Owner۩ஜ▬●
[★]Qr On/Off
[★]Cancel On/Off
[★]Join On/Off
[★]Share On/Off
[★]Add On/Off
[★]Admin add @
[★]Owner add @
[★]Bot add @
[★]Spam Group
[★]Bot 1/10 Rename
[★]/invitemeto:
[★]Masuk
[★]Keluar
[★]Like teman
[★]Bot Like
[★]Ready op(Kickers)
[★]Nk @ Kick
[★]Unban (Share)
[★]List Group
●▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬●
   ●▬ஜ۩124D15T1 T34M۩ஜ▬●
●▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬●
"""

Promo = """╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║  ✰Owner Menu✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔════════════
║╠[1]Status
║╠[2]Bot?
║╠[3]Respon
║╠[4]Cctv→Ciduk
║╠[5]Tagall
║╠[6]Banlist
║╠[7]Youtube:
║╠[8]/music
║╠[9]Me
║╠[10]Info group
║╠[11]Ig: Username
║╠[12]One Piece
║╠[13]SVF
║╠[14]Cancel
║╠[15]Open/Close Qr
║╠[16]Gurl
║╠[17]Gn
║╠[18]Staff add @
║╠[19]Admin add @
║╠[20]Wl add @
║╠[21]Staff remove @
║╠[22]Admin Remove @
║╠[23]Wl remove @
║╠[24]Pp @
║╠[25]Dp @
║╠[26]Mid @
║╠[27]Pp Group
║╠[28]Stafflist
║╠[29]Adminlist
║╠[30]Ownerlist
║╠[31]Whitelist
║╠[32]Nk @
║╠[33]Qr on/off
║╠[34]Cancel on/off
║╠[35]Join on/off
║╠[36]Share on/off
║╠[37]Bot Add @
║╠[38]Mimic on/off
║╠[39]Bc
║╠[40]Spam
║╠[41]Anu @
║╠[42]Bot1/10 rename
║╠[43]Allbio:
║╠[44]Copy←→Backup
║╠[45]List group
║╠[46]/invitemeto:
║╠[47]SpamInvite
║╠[48]Ban all
║╠[49]Clear ban
║╠[50]Like
║╠[51]Like me
║╠[52]Masuk
║╠[53]Keluar
║║★And More★
║╚════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║  124D15T1 T34M
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚═════════════"""

About = """╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║ ✰Admin Menu✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔════════════
║╠[1]Status
║╠[2]Bot?
║╠[3]Respon
║╠[4]Cctv→Ciduk
║╠[5]Tagall
║╠[6]Banlist
║╠[7]Youtube:
║╠[8]/music
║╠[9]Me
║╠[10]Info group
║╠[11]Ig: Username
║╠[12]One Peice
║╠[13]SVF
║╠[14]Cancel
║╠[15]Open/Close Qr
║╠[16]Gurl
║╠[17]Gn
║╠[18]Staff add @
║╠[19]Pp @
║╠[20]Dp @
║╠[21]Mid @
║╠[22]Pp Group
║╠[23]Stafflist
║╠[24]Adminlist
║╠[25]Nk @
║╚════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║ 124D15T1 T34M
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚═════════════"""

KAC=[cl,ki,kk,kc,ks,]
mid = cl.getProfile().mid #One
Amid = ki.getProfile().mid #Two
Bmid = kk.getProfile().mid #Tree
Cmid = kc.getProfile().mid #Four
Dmid = ks.getProfile().mid #Five

Bots=[mid,Amid,Bmid,Cmid,Dmid,]
admin=["u0f4cbccff2b03754d07d8db8707023f6","u577d79f51412f92e7a28d360ca351ae4","u82f7bb98715417c34fe1b7fac263e893"] 
owner=["u0f4cbccff2b03754d07d8db8707023f6","u82f7bb98715417c34fe1b7fac263e893"]
whitelist=["u82f7bb98715417c34fe1b7fac263e893"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"""THANKS FOR ADD ME
🔱RADISTI TEAM PROTECT🔱

ṡȗƿƿȏяṭєԀ ɞʏ SMULE:
  
☆@1DaffaN3Kalani☆
☆@PMDI_SOPOJARWO☆
☆@PMDI_OFICIAL☆
☆#PMDI_BERGOYANG☆
☆ ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ ☆

CONTACT:
Idline: http://line.me/ti/p/H2VZm0LFeR~ই✠☪1DaffaN3Kalani☪ইद""",
    "lang":"JP",
    "comment":"Thanks for add Me By : ই✠☪1DaffaN3Kalani☪ইद\n\nhttp://line.me/ti/p/H2VZm0LFeR",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "winvite" :False,
    "winvite2" :False,
    "winvite3" :False,
    "winvite4" :False,
    "winvite5" :False,
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":True,
    "Protectcancl":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "status":False,
    "target":{}
    }

settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()
Filter='Filter.txt'

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.displayName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for mm in nama:
     akh = akh + 3
     aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
     strt = strt + 4
     akh = akh + 1
     bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = contact.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
      cl.sendMessage(msg)
    except Exception as error:
       print error
        
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
        
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
        
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Hours %02d Minutes %02d Seconds' % (hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in whitelist:
                pass
              else:
                try:
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  ks.kickoutFromGroup(op.param1,[op.param2])
                 # ka.kickoutFromGroup(op.param1,[op.param2])
                  H = cl.getGroup(op.param1)
                  H.preventJoinByTicket = True
                  cl.updateGroup(H)
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  H = random.choice(KAC).getGroup(op.param1)
                  H.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(H)
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if wait["blacklist"][op.param3] == True:
              cl.sendText(op.param1,cl.getContact(op.param3).displayName + " On Blacklist Boss\nWe Will Cancel Invitation")
              random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
            else:
              pass
        
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots or admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in whitelist:
                pass
              else:
                try:
                  cl.cancelGroupInvitation(op.param1, gMembMids)
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User Finish------#  
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in owner:
                  cl.acceptGroupInvitation(op.param1)
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
              else:
                cl.rejectGroupInvitation(op.param1)
                
            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in owner:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in owner:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in owner:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in owner:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Emid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in owner:
                  ka.acceptGroupInvitation(op.param1)
                else:
                  ka.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                    
        if op.type == 17: #Protect Join
          if wait["Protectjoin"] == True:
            if wait["blacklist"][op.param2] == True:
              cl.sendText(op.param1,cl.getContact(op.param2).displayName + " On Blacklist Boss\nWe Will Kick")
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              cl.sendText(op.param1,cl.getContact(op.param3).displayName + " His Inviting\nWe Will Kick Too")
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
            else:
              pass
  #------Joined User Kick start------#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            try:
              cl.kickoutFromGroup(op.param1,[op.param2])
              ki.kickoutFromGroup(op.param1,[op.param2])
              kk.kickoutFromGroup(op.param1,[op.param2])
              kc.kickoutFromGroup(op.param1,[op.param2])
              ks.kickoutFromGroup(op.param1,[op.param2])
              #ka.kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
        
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or owner:
                try:
                  ks.kickoutFromGroup(op.param1,[op.param2])
                  H = ks.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  ks.updateGroup(H)
                  Ticket = ks.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  H.preventJoinByTicket = True
                  ks.updateGroup(H)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  H = random.choice(KAC).getGroup(op.param1)
                  H.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(H)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  H.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(H)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Amid:
              if op.param2 not in Bots or owner:
                try:
                  G = kk.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kk.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Bmid:
              if op.param2 not in Bots or owner:
                try:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G = kc.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Cmid:
              if op.param2 not in Bots or owner:
                try:
                  G = ks.getGroup(op.param1)
                  ks.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G = ks.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Dmid:
              if op.param2 not in Bots or owner:
                try:
                  G = ka.getGroup(op.param1)
                  ka.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ka.updateGroup(G)
                  Ticket = ka.reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G = ka.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ka.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            elif op.param3 in Emid:
              if op.param2 not in Bots or owner:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G = kb.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kb.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
        if op.type == 19: #admin dan whitelist
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            try:
              if op.param3 in admin:
                if op.param2 not in Bots or owner:
                  if op.param2 in Bots:
                    pass
                  elif op.param2 in owner:
                    pass
                  else:
                    try:
                      cl.kickoutFromGroup(op.param1,[op.param2])
                      ki.kickoutFromGroup(op.param1,[op.param2])
                      kk.kickoutFromGroup(op.param1,[op.param2])
                      kc.kickoutFromGroup(op.param1,[op.param2])
                      ks.kickoutFromGroup(op.param1,[op.param2])
                      ka.kickoutFromGroup(op.param1,[op.param2])
                      cl.inviteIntoGroup(op.param1,[op.param3])
                      ki.inviteIntoGroup(op.param1,[op.param3])
                      kk.inviteIntoGroup(op.param1,[op.param3])
                      kc.inviteIntoGroup(op.param1,[op.param3])
                      ks.inviteIntoGroup(op.param1,[op.param3])
                      ka.inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).getGroup(op.param1)
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    
              elif op.param3 in whitelist:
                if op.param2 not in Bots or owner:
                  try:
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).getGroup(op.param1)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
            except:
              try:
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
      #---------------                      
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            cl.sendMessage(msg)
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + " Kickers")

        if op.type == 11:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in whitelist:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            cl.sendMessage(msg)
            
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[124D15T1 TEAM CHAT] " + "\n" + data['result']['response'].encode('utf-8'))
                                
        if op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param2 not in admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in whitelist:
                pass
              else:
                random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True
                                
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            #print(
            #" TO: {}\n".format(msg.to),
            #"FROM: {}\n".format(msg.from_),
            #"TEXT: {}\n".format(msg.text),
            #"CONTENT TYPE: {}\n".format(msg.contentType),
            #"METADATA: {}\n".format(msg.contentMetadata),
            #"TYPE: {}\n".format(msg.toType),
            #"MESSAGE ID: {}\n".format(msg.id),
            #"DATE: {}\n\n".format(msg.createdTime)
            #)


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
              if wait["winvite"] == True:
                if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = cl.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      cl.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      cl.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        cl.inviteIntoGroup(msg.to,[target])
                        cl.sendText(msg.to,"Already Invited Done✔ 💋: \n➡" + _name)
                        wait["winvite"] = False
                        break
                      except:
                        try:
                          cl.findAndAddContactsByMid(invite)
                          cl.inviteIntoGroup(op.param1,[invite])
                          wait["winvite"] = False
                        except:
                          try:
                            cl.findAndAddContactsByMid(invite)
                            cl.inviteIntoGroup(op.param1,[invite])
                            wait["winvite"] = False
                            cl.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              cl.findAndAddContactsByMid(invite)
                              cl.inviteIntoGroup(op.param1,[invite])
                              wait["winvite"] = False
                              cl.sendText(msg.to,"Done ✔ 💋 \n➡" + _name)
                              break
                            except:
                              cl.sendText(msg.to,"Negative, Error detected")
                              wait["winvite"] = False
                              break
              elif wait["winvite2"] == True:
                if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ki.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ki.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ki.sendText(msg.to,"Remove User From Blacklist Done✔" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ki.findAndAddContactsByMid(target)
                        ki.inviteIntoGroup(msg.to,[target])
                        ki.sendText(msg.to,"Already Invited Done✔💋: \n➡" + _name)
                        wait["winvite2"] = False
                        break
                      except:
                        try:
                          ki.findAndAddContactsByMid(invite)
                          ki.inviteIntoGroup(op.param1,[invite])
                          wait["winvite2"] = False
                        except:
                          try:
                            ki.findAndAddContactsByMid(invite)
                            ki.inviteIntoGroup(op.param1,[invite])
                            wait["winvite2"] = False
                            ki.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ki.findAndAddContactsByMid(invite)
                              ki.inviteIntoGroup(op.param1,[invite])
                              wait["winvite2"] = False
                              ki.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              ki.sendText(msg.to,"Negative, Error detected")
                              wait["winvite2"] = False
                              break
              elif wait["winvite3"] == True:
                if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kk.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kk.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kk.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kk.sendText(msg.to,"Remove User From Blacklist Done✔" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kk.findAndAddContactsByMid(target)
                        kk.inviteIntoGroup(msg.to,[target])
                        kk.sendText(msg.to,"Already Invited Done✔💋: \n➡" + _name)
                        wait["winvite3"] = False
                        break
                      except:
                        try:
                          kk.findAndAddContactsByMid(invite)
                          kk.inviteIntoGroup(op.param1,[invite])
                          wait["winvite3"] = False
                        except:
                          try:
                            kk.findAndAddContactsByMid(invite)
                            kk.inviteIntoGroup(op.param1,[invite])
                            wait["winvite3"] = False
                            kk.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kk.findAndAddContactsByMid(invite)
                              kk.inviteIntoGroup(op.param1,[invite])
                              wait["winvite3"] = False
                              kk.sendText(msg.to,"Done ✔  💋 \n➡" + _name)
                              break
                            except:
                              kk.sendText(msg.to,"Negative, Error detected")
                              wait["winvite3"] = False
                              break
              elif wait["winvite4"] == True:
                if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kc.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kc.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kc.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kc.sendText(msg.to,"Remove User From Blacklist Done✔ !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kc.findAndAddContactsByMid(target)
                        kc.inviteIntoGroup(msg.to,[target])
                        kc.sendText(msg.to,"Already Invited Done✔💋: \n➡" + _name)
                        wait["winvite4"] = False
                        break
                      except:
                        try:
                          kc.findAndAddContactsByMid(invite)
                          kc.inviteIntoGroup(op.param1,[invite])
                          wait["winvite4"] = False
                        except:
                          try:
                            kc.findAndAddContactsByMid(invite)
                            kc.inviteIntoGroup(op.param1,[invite])
                            wait["winvite4"] = False
                            kc.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kc.findAndAddContactsByMid(invite)
                              kc.inviteIntoGroup(op.param1,[invite])
                              wait["winvite4"] = False
                              kc.sendText(msg.to,"Done ✔  💋 \n➡" + _name)
                              break
                            except:
                              kc.sendText(msg.to,"Negative, Error detected")
                              wait["winvite4"] = False
                              break
              elif wait["winvite5"] == True:
                if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ks.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ks.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ks.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ks.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ks.findAndAddContactsByMid(target)
                        ks.inviteIntoGroup(msg.to,[target])
                        ks.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite5"] = False
                        break
                      except:
                        try:
                          ks.findAndAddContactsByMid(invite)
                          ks.inviteIntoGroup(op.param1,[invite])
                          wait["winvite5"] = False
                        except:
                          try:
                            ks.findAndAddContactsByMid(invite)
                            ks.inviteIntoGroup(op.param1,[invite])
                            wait["winvite5"] = False
                            ks.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ks.findAndAddContactsByMid(invite)
                              ks.inviteIntoGroup(op.param1,[invite])
                              wait["winvite5"] = False
                              ks.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              ks.sendText(msg.to,"Negative, Error detected")
                              wait["winvite5"] = False
                              break
              elif wait["winvite6"] == True:
                if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ka.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ka.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ka.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ka.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ka.findAndAddContactsByMid(target)
                        ka.inviteIntoGroup(msg.to,[target])
                        ka.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite6"] = False
                        break
                      except:
                        try:
                          ka.findAndAddContactsByMid(invite)
                          ka.inviteIntoGroup(op.param1,[invite])
                          wait["winvite6"] = False
                        except:
                          try:
                            ka.findAndAddContactsByMid(invite)
                            ka.inviteIntoGroup(op.param1,[invite])
                            wait["winvite6"] = False
                            ka.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ka.findAndAddContactsByMid(invite)
                              ka.inviteIntoGroup(op.param1,[invite])
                              wait["winvite6"] = False
                              ka.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              ka.sendText(msg.to,"Negative, Error detected")
                              wait["winvite6"] = False
                              break
              
              elif wait["wblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  cl.sendText(msg.to,"already")
                  wait["wblack"] = False
                else:
                  wait["commentBlack"][msg.contentMetadata["mid"]] = True
                  wait["wblack"] = False
                  cl.sendText(msg.to,"decided not to comment")
                  
              elif wait["dblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  del wait["commentBlack"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  #ki.sendText(msg.to,"deleted")
                  #kk.sendText(msg.to,"deleted")
                  #kc.sendText(msg.to,"deleted")
                  wait["dblack"] = False

                else:
                  wait["dblack"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  #ki.sendText(msg.to,"It is not in the black list")
                  #kk.sendText(msg.to,"It is not in the black list")
                  #kc.sendText(msg.to,"It is not in the black list")
              elif wait["wblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  cl.sendText(msg.to,"already")
                  #ki.sendText(msg.to,"already")
                  #kk.sendText(msg.to,"already")
                  #kc.sendText(msg.to,"already")
                  wait["wblacklist"] = False
                else:
                  wait["blacklist"][msg.contentMetadata["mid"]] = True
                  wait["wblacklist"] = False
                  cl.sendText(msg.to,"aded")
                #ki.sendText(msg.to,"aded")
                  #kk.sendText(msg.to,"aded")
                  #kc.sendText(msg.to,"aded")

              elif wait["dblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  del wait["blacklist"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  #ki.sendText(msg.to,"deleted")
                  #kk.sendText(msg.to,"deleted")
                  #kc.sendText(msg.to,"deleted")
                  wait["dblacklist"] = False

                else:
                  wait["dblacklist"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  #ki.sendText(msg.to,"It is not in the black list")
                  #kk.sendText(msg.to,"It is not in the black list")
                  #kc.sendText(msg.to,"It is not in the black list")
              elif wait["contact"] == True:
                msg.contentType = 0
                cl.sendText(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                else:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","Setlist","Help"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
              text = msg.text
              if text is not None:
                cl.sendText(msg.to,text)
              else:
                if msg.contentType == 7:
            	    msg.contentType = 7
            	    msg.text = None
            	    msg.contentMetadata = {
            	               "STKID": "6",
            	               "STKPKGID": "1",
            	               "STKVER": "100" }
            	    cl.sendMessage(msg)
                elif msg.contentType == 13:
            	    msg.contentType = 13
            	    msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            	    cl.sendMessage(msg)
            
            elif "Mimic:" in msg.text:
              if msg.from_ in owner:
                cmd = msg.text.replace("Mimic:","")
                if cmd == "on":
                  if mimic["status"] == False:
                    mimic["status"] = True
                    cl.sendText(msg.to,"Mimic On Done✔")
                  else:
                    cl.sendText(msg.to,"Mimic Already On Done✔")
                elif cmd == "off":
                  if mimic["status"] == True:
                    mimic["status"] = False
                    cl.sendText(msg.to,"Mimic Off Done✔")
                  else:
                    cl.sendText(msg.to,"Mimic Already Done✔")
                elif cmd == "list":
                  if mimic["target"] == {}:
                    cl.sendText(msg.to,"No target")
                  else:
                    mc = "Target Mimic\n"
                    mids = []
                    for s in range(len(mimic["target"])):
                        mids.append(mimic["target"][s])
                    cmids = cl.getContacts(mids)
                    for x in range(len(cmids)):
                        mc += "\n["+str(x)+"]"+cmids[x].displayName
                    cl.sendText(msg.to,mc)
                elif "add:" in cmd:
                  target0 = msg.text.replace("Mimic:add:","")
                  target1 = target0.lstrip()
                  target2 = target1.replace("@","")
                  target3 = target2.rstrip()
                  _name = target3
                  gInfo = cl.getGroup(msg.to)
                  targets = []
                  for a in gInfo.members:
                    if _name == a.displayName:
                      targets.append(a.mid)
                  if targets == []:
                    cl.sendText(msg.to,"No targets")
                  else:
                    for target in targets:
                      try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Success added target")
                        cl.sendMessageWithMention(msg.to,target)
                        break
                      except:
                        cl.sendText(msg.to,"Ready To Following Chat From Target Boss")
                        break
                elif "del:" in cmd:
                  target0 = msg.text.replace("Mimic:del:","")
                  target1 = target0.lstrip()
                  target2 = target1.replace("@","")
                  target3 = target2.rstrip()
                  _name = target3
                  gInfo = cl.getGroup(msg.to)
                  targets = []
                  for a in gInfo.members:
                    if _name == a.displayName:
                      targets.append(a.mid)
                  if targets == []:
                    cl.sendText(msg.to,"No targets")
                  else:
                    for target in targets:
                      try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Success deleted target")
                        cl.sendMessageWithMention(msg.to,target)
                        break
                      except:
                        cl.sendText(msg.to,"Im Not Following Again Boss\nTired, Not Get Money")
                        break
                    
            elif msg.text in ["Key2","Setlist2","Help2"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Promo)
                else:
                    cl.sendText(msg.to,Promo)
            elif msg.text in ["Key3","Setlist3","Help3"]:
              if msg.from_ in owner or admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,About)
                else:
                    cl.sendText(msg.to,About)
            elif "Gn " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "One gn " in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif "Two gn " in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif "Tree gn " in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "One kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Two kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Oneinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Zinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Twoinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Sinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Treeinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Uinvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif "Fourinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Cinvite ","")
                ks.findAndAddContactsByMid(midd)
                ks.inviteIntoGroup(msg.to,[midd])
            elif "Fiveinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Finvite ","")
                ka.findAndAddContactsByMid(midd)
                ka.inviteIntoGroup(msg.to,[midd])
            
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            ki.findAndAddContactsByMid(target)
                            kk.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            ks.findAndAddContactsByMid(target)
                            ka.findAndAddContactsByMid(target)
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Already Added Done✔")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                cl.sendText(msg.to,"You Are Not My Boss !!!")
                cl.sendText(msg.to,"Command Denied")
                
            elif "Owner add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner add executing"
                _name = msg.text.replace("Owner add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            ki.findAndAddContactsByMid(target)
                            kk.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            ks.findAndAddContactsByMid(target)
                            ka.findAndAddContactsByMid(target)
                            owner.append(target)
                            cl.sendText(msg.to,"Owner Already Added Done✔")
                        except:
                            pass
                print "[Command]Owner add executed"
              else:
                cl.sendText(msg.to,"You Are Not My Boss !!!")
                cl.sendText(msg.to,"Command Denied")
            
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Deleted")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                cl.sendText(msg.to,"You Are Not My Boss !!!")
                cl.sendText(msg.to,"Command Denied")
            elif "Owner remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner remove executing"
                _name = msg.text.replace("Owner remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.remove(target)
                            cl.sendText(msg.to,"Owner Deleted")
                        except:
                            pass
                print "[Command]Owner remove executed"
              else:
                cl.sendText(msg.to,"You Are Not My Boss!!!")
                cl.sendText(msg.to,"Command Denied")
            
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Please Wait...")
                  mc = "👑 124D15Ti T34M 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in admin:
                      mc += "[★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
                  
            elif msg.text in ["Ownerlist","ownerlist"]:
              if owner == []:
                  cl.sendText(msg.to,"The Owner is empty")
              else:
                  cl.sendText(msg.to,"Please Wait...")
                  mc = "👑 Owner One Piece Bot 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in owner:
                      mc += "[★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Ownerlist executed"
    #--------------- Lawan atau Whitelist -------
            elif "Wl add @" in msg.text:
              if msg.from_ in owner:
                #print "[Command]Staff add executing"
                _name = msg.text.replace("Wl add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   cl.sendText(msg.to,"Orang nya Ga Keliatan Kaya Setan")
                else:
                   for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            ki.findAndAddContactsByMid(target)
                            kk.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            ks.findAndAddContactsByMid(target)
                            ka.findAndAddContactsByMid(target)
                            whitelist.append(target)
                            cl.sendText(msg.to,"Whitelist Already Added")
                        except:
                            pass
                #print "[Command]Kawan add executed"
              else:
                cl.sendText(msg.to,"You Are Not My Boss !!!")
                cl.sendText(msg.to,"Command Denied")
                
            elif "Wl remove @" in msg.text:
              if msg.from_ in owner:
                #print "[Command]Kawan remove executing"
                _name = msg.text.replace("Wl remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   cl.sendText(msg.to,"Orangnya ga ada Lagi Anu")
                else:
                   for target in targets:
                        try:
                            whitelist.remove(target)
                            cl.sendText(msg.to,"Whitelist Deleted")
                        except:
                            pass
                #print "[Command]Kawan remove executed"
              else:
                cl.sendText(msg.to,"You Are Not My Boss !!!")
                cl.sendText(msg.to,"Command Denied")
                
            elif msg.text in ["Whitelist","whitelist"]:
              if whitelist == []:
                  cl.sendText(msg.to,"Whitelist nya Kosong Boss")
              else:
                  cl.sendText(msg.to,"Please Wait...")
                  mc = "👥Whitelist 124D15T1 T34M👥\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in whitelist:
                      mc += "👉 [★]" + cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  #print "[Command]Stafflist executed"
    #--------------------------------------
    #--------------------------------------
    #-------------- Add Friends -----------
            elif "Bot add @" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = ka.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        ka.findAndAddContactsByMid(target)
                        cl.sendText(msg.to,"We Already Added His as a Friends")
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                  
    #-------------=SC AllBio=----------------
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Spam " in msg.text:
              if msg.from_ in owner:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                #Keke cantik <3
                if txt[1] == "on":
                  if jmlh <= 500:
                    for x in range(jmlh):
                      cl.sendText(msg.to, teks)
                  else:
                    cl.sendText(msg.to, "Out of range! ")
                elif txt[1] == "off":
                  if jmlh <= 900:
                    cl.sendText(msg.to, tulisan)
                  else:
                    cl.sendText(msg.to, "Out of range! ")
                    
            elif "Fbc " in msg.text:
              if msg.from_ in owner:
	              print "[Friend Broadcast Excuted]"
	              bctxt = msg.text.replace("Fbc ","")
	              n = cl.getAllContactIds()
                #n = p1.getAllContactIds()
	              for people in n:
	                cl.sendText(people, (bctxt))
                  #p1.sendText(people, (bctxt))
  #-----------------=Selesai=------------------
            elif msg.text in ["Bot?"]:
              if msg.from_ in owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ku.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ko.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid1}
                p1.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid2}
                p2.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid3}
                p3.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid4}
                p4.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Pmid5}
                p5.sendMessage(msg)
            elif msg.text in ["Me"]:
              if msg.from_ in owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
                
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              if msg.from_ in owner:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zcancel","zcancel"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"QR Already Opened")
                    else:
                        cl.sendText(msg.to,"Already Opened Boss")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy buka qr","Luffy open qr"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Plak")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro buka qr","Zorro open qr"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji open qr","Sanji buka qr"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Code QR Already Closed")
                    else:
                        random.choice(KAC).sendText(msg.to,"Already Closed Boss")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy close qr","Luffy tutup qr"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro tutup qr","Zorro close qr"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Plak")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji tutup qr","Sanji close qr"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
              rplace=msg.text.lower().replace("jointicket ")
              if rplace == "on":
                wait["atjointicket"]=True
              elif rplace == "off":
                wait["atjointicket"]=False
                cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
                
            elif '/ti/g/' in msg.text.lower():
              link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
              links = link_re.findall(msg.text)
              n_links=[]
              for l in links:
                if l not in n_links:
                  n_links.append(l)
                for ticket_id in n_links:
                  if wait["atjointicket"] == True:
                    group=cl.findGroupByTicket(ticket_id)
                    cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
                    cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    cl.sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
            elif "My mid" == msg.text:
              random.choice(KAC).sendText(msg.to, msg.from_)
              
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                ki.sendMessage(msg)
                #kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in owner:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Bot1 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot1 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                  profile = cl.getProfile()
                  profile.displayName = string
                  cl.updateProfile(profile)
                  cl.sendText(msg.to,"name " + string + " done")
            elif "Bot2 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot2 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"name " + string + " done")
            elif "Bot3 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot3 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"name " + string + " done")
            elif "Bot4 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot4 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"name " + string + " done")
            elif "Bot5 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot5 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"name " + string + " done")
            elif "Bot6 rename " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot6 rename ","")
                if len(string.decode('utf-8')) <= 6000000000:
                    profile = ka.getProfile()
                    profile.displayName = string
                    ka.updateProfile(profile)
                    ka.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in owner:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                
            elif msg.text in ["Cancelinvite on","cancelinvite on"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == True:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Protect Canceled Invited On")
                  else:
                    cl.sendText(msg.to,"Done")
                else:
                  wait["Protectcancel"] = True
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Protect Canceled Invited On")
                  else:
                    cl.sendText(msg.to,"done")
                    
            elif msg.text in ["Cancelinvite off","cancelinvite off"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == False:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Protect Canceled Invited Off")
                  else:
                    cl.sendText(msg.to,"Done")
                else:
                  wait["Protectcancel"] = False
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Protect Canceled Invited Off")
                  else:
                    cl.sendText(msg.to,"done")
                
            elif msg.text in ["Purge on","purge on","Purge: on","purge: on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"High Protect Activated")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"High Protect Activated")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Purge off","purge off","Purge: off","purge: off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"High Protect Disabled")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"High Protect Disabled")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invitation On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invitation On")
                    else:
                        cl.sendText(msg.to,"done")
              else:
                cl.sendText(msh.to, "This command only for owner")
                
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invitation Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invitation Off")
                    else:
                        cl.sendText(msg.to,"done")
              else:
                cl.sendText(msh.to, "This command only for owner")
                
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
              else:
                cl.sendText(msh.to, "This command only for owner")
                
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
              else:
                cl.sendText(msh.to, "This command only for owner")
                
            elif msg.text in ["Invite off","invite off"]:
              if msg.from_ in owner:
                if wait["winvite"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Dibatalin")
                    else:
                        cl.sendText(msg.to,"Dibatalin")
                else:
                    wait["winvite"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Dibatalin")
                    else:
                        cl.sendText(msg.to,"Dibatalin")
                if wait["winvite2"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Dibatalin")
                    else:
                        ki.sendText(msg.to,"Dibatalin")
                else:
                    wait["winvite2"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Dibatalin")
                    else:
                        ki.sendText(msg.to,"Dibatalin")
                
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in owner:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in owner:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
              if msg.from_ in owner:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in owner:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in owner:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set"]:
              if msg.from_ in admin:
                md = "╔═══════════════\n║⭐Protection Status⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                if wait["Protectgr"] == True: md+="║[•]Protect QR Enable\n"
                else: md+="║[•]Protect QR Disable\n"
                if wait["Protectcancl"] == True: md+="║[•]Protect Invite Enable\n"
                else: md+="║[•]Protect Invite Disable\n"
                if wait["Protectcancel"] == True: md+="║[•]Protect Cancel Enable\n"
                else: md+="║[•]Protect Cancel Disable\n"
                if wait["Protectjoin"] == True: md+="║[•]High protect Enable\n"
                else: md+="║[•]High protect Disable\n"
                if wait["contact"] == True: md+="║[•]Contact ✔\n"
                else: md+="║[•]Contact ✖\n"
                if wait["autoJoin"] == True: md+="║[•]Auto Join ✔\n"
                else: md +="║[•]Auto Join ✖\n"
                if wait["autoCancel"]["on"] == True:md+="║[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+="║[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="║[•]Auto Leave ✔\n"
                else: md+="║[•]Auto Leave ✖\n"
                if wait["timeline"] == True: md+="║[•]Share ✔\n"
                else: md+="║[•]Share ✖\n"
                if wait["autoAdd"] == True: md+="║[•]Auto Add ✔\n"
                else: md+="║[•]Auto Add ✖\n"
                if wait["commentOn"] == True: md+="║[•]Comment ✔\n"
                else: md+="║[•]Comment ✖\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║⭐124D15T1 T34M⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in owner:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in owner:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
              if msg.from_ in owner:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
              if msg.from_ in owner:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
              if msg.from_ in owner:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
              if msg.from_ in owner:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
              if msg.from_ in owner:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    try:
                      ki.findAndAddContactsByMid(msg.from_)
                      ki.inviteIntoGroup(gid,[msg.from_])
                    except:
                      try:
                        kk.findAndAddContactsByMid(msg.from_)
                        kk.inviteIntoGroup(gid,[msg.from_])
                      except:
                        try:
                          kc.findAndAddContactsByMid(msg.from_)
                          kc.inviteIntoGroup(gid,[msg.from_])
                        except:
                          try:
                            ks.findAndAddContactsByMid(msg.from_)
                            ks.inviteIntoGroup(gid,[msg.from_])
                          except:
                            cl.sendText(msg.to,"Mungkin kami tidak di dalaam grup itu")
                    
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in owner:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
              if msg.from_ in owner:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
              if msg.from_ in owner:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in administrator:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
              if msg.from_ in owner:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
              if msg.from_ in owner:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
              if msg.from_ in owner:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in owner:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in owner:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
              if msg.from_ in owner:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
              if msg.from_ in owner:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#
            elif msg.text == "Cctv":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Checking CCTV...")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
            elif msg.text == "Ciduk":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "╔═════════════\n║👀Seen By👀%s\n╠═════[Result]═════\n║👀The Siders👀\n%s║Pray For Sider Sick Strooke\n║[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Type Cctv First Dude\nThen Type Ciduk\nDasar Pikun ♪")
        #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["In","Masuk","Bot in"]:
              if msg.from_ in owner:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                G = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                print "Semua Sudah Lengkap"
                
            elif msg.text in ["Luffy join"]:
              if msg.form_ in owner:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Zorro join"]:
              if msg.from_ in owner:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Sanji join"]:
              if msg.from_ in owner:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Ussop Join"]:
              if msg.from_ in owner:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Keluar","Get out","Out"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Bye zorro"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye sanji"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Ussop"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all","Tagall"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
            elif msg.text in ["Tag"]:
              if msg.from_ in owner:
              elif msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                  summon(msg.to, nama)
                if jml > 100 and jml < 200:
                  for i in range(0, 99):
                    nm1 += [nama[i]]
                  summon(msg.to, nm1)
                  for j in range(100, len(nama)-1):
                    nm2 += [nama[j]]
                  summon(msg.to, nm2)
                if jml > 200  and jml < 500:
                  for i in range(0, 99):
                    nm1 += [nama[i]]
                  summon(msg.to, nm1)
                  for j in range(100, 199):
                    nm2 += [nama[j]]
                  summon(msg.to, nm2)
                  for k in range(200, 299):
                    nm3 += [nama[k]]
                  summon(msg.to, nm3)
                  for l in range(300, 399):
                    nm4 += [nama[l]]
                  summon(msg.to, nm4)
                  for m in range(400, len(nama)-1):
                    nm5 += [nama[m]]
                  summon(msg.to, nm5)
                if jml > 500:
                  print "Terlalu Banyak Men 500+"
                cnt = Message()
                cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
                
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Like Me","like me"]:
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
              else:
                cl.sendText(msg.to,"Command Ini Hanya Untuk Owner\nMaaf yah Ka")
                
            elif msg.text in ["Like","like"]:
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                  cl.sendText(msg.to,"Sudah Selesai Kami Like Boss")
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            
            elif msg.text in ["Bot restart"]:
              if msg.from_ in owner:
    	          cl.sendText(msg.to, "Kami Siap Restart\nWaktu Restart Sekitar 10 Detik ")
                #cl.sendText(msg.to, "Waktu Restart Sekitar 10 Detik")
                  restart_program()
                
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Fvck" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Fvck","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = ka.getGroup(msg.to)
                    cl.sendText(msg.to,"Hello Kk")
                    cl.sendText(msg.to,"One Piece Team Mau Bersih² Group Sampah Nih")
                    cl.sendText(msg.to,"Karna Ini Group Sampah Jadi Mau Di Bersihin Dulu Yah\n★Jangan Baper...\n★Jangan Nangis\n★Jangan Cengeng\nBawa Enjoy Aja Kawan♪")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    cl.sendText(msg.to,"This My Team WAR")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots or owner:
                            if target in owner:
                              pass
                            elif target in admin:
                              pass
                            elif target in Bots:
                              pass
                            elif target in whitelist:
                              pass
                            else:
                              try:
                                klist=[cl,ki,kk,kc,ks,ka]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                              except:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                #random.choice(KAC).kickoutFromGroup(msg.to,[target])
        #----------------Fungsi Kick User Target Start----------------------#
            elif ("Nk " in msg.text):
              if msg.from_ in owner:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"] [0] ["M"]
                for x in key["MENTIONEES"]:
                  targets.append(x["M"])
                #targets = []
                for target in targets:
                  try:
                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                  except:
                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                      
            elif ("Tendang " in msg.text):
               if msg.from_ in owner:
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"] [0] ["M"]
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  #targets = []
                  for target in targets:
                    try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                    except:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Ban " in msg.text:
              if msg.from_ in owner:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                  try:
                    wait["blacklist"][target] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    cl.sendText(msg.to,"Succes Banned")
                  except:
                    pass
                  
            elif ("Jitak " in msg.text):
               if msg.from_ in owner:
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"] [0] ["M"]
                  for x in key["MENTIONEES"]:
                      targets.append(x["M"])
                  for target in targets:
                    try:
                      ki.kickoutFromGroup(msg.to,[target])
                    except:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
          #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        #ki.sendText(msg.to,"Dilarang Banned Bot")
                        #kk.sendText(msg.to,"Dilarang Banned Bot")
                        #kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        #pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not Found.....")
                        #ki.sendText(msg.to,"Tidak Ditemukan.....")
                        #kk.sendText(msg.to,"Tidak Ditemukan.....")
                        #kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "Unban all" in msg.text:
              if msg.from_ in owner:
                print "[Unban]ok"
                gs = cl.getGroup(msg.to)
                targets = wait["blacklist"] 
                if targets == []:
                  cl.sendText(msg.to,"Not found ~")
                else:
                  for target in targets:
                    try:
                      del wait["blacklist"][target]
                      cl.sendText(msg.to,"Sukses Clear ban ~")
                    except:
                      cl.sendText(msg.to,"Error")
                      
            elif msg.text in ["Clear ban"]:
              if msg.from_ in owner:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Succes Clear Blacklist")
                #p1.sendText(msg.to,"Succes Clear Blacklist Boss")
        #----------------Fungsi Unbanned User Target Finish-----------------------#
            elif "Copy @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Copy @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                  if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  sendMessage(msg.to, "Not Found...")
                else:
                  for target in targets:
                    try:
                      cl.CloneContactProfile(target)
                      cl.sendText(msg.to, "Success Copy profile ~")
                    except Exception as e:
                      print e
            elif msg.text in ["Backup","backup"]:
              if msg.from_ in owner:
                try:
                  cl.updateDisplayPicture(backup.pictureStatus)
                  cl.updateProfile(backup)
                  cl.sendText(msg.to, "Backup done")
                except Exception as e:
                  cl.sendText(msg.to, str(e))
            elif "Spam album:" in msg.text:
              if msg.from_ in owner:
                try:
                  albumtags = msg.text.replace("Spam album:","")
                  gid = albumtags[:33]
                  name = albumtags.replace(albumtags[:34],"")
                  cl.createAlbum(gid,name)
                  cl.sendText(msg.to,"We created an album" + name)
                except:
                  cl.sendText(msg.to,"Error")
                    
            elif "Contact bc " in msg.text:
              if msg.from_ in owner:
                bctxt = msg.text.replace("Contact bc ", "")
                t = cl.getAllContactIds()
                #t = p1.getAllContactIds()
                t = 100
                while(t):
                  cl.sendText(msg.to, (bctxt))
                  #p1.sendText(msg.to, (bctxt))
                  t-=1
        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text:
              if msg.from_ in owner:
                bctxt = msg.text.replace("Bc ","")
                a = cl.getGroupIdsJoined()
                a = ki.getGroupIdsJoined()
                a = kk.getGroupIdsJoined()
                a = kc.getGroupIdsJoined()
                a = ks.getGroupIdsJoined()
                a = ka.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
                  ki.sendText(taf, (bctxt))
                  kk.sendText(taf, (bctxt))
                  kc.sendText(taf, (bctxt))
                  ks.sendText(taf, (bctxt))
                  ka.sendText(taf, (bctxt))
            elif "Lbc " in msg.text:
              if msg.from_ in owner:
                bctxt = msg.text.replace("Lbc ","")
                a = cl.getGroupIdsJoined()
                #a = p1.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
                  #p1.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["LG","List Group"]:
              if msg.from_ in owner:
                gids = cl.getGroupIdsJoined()
                h = ""
                for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[★]%s Member\n" % (cl.getGroup(i).name   + "👉" + str(len(cl.getGroup(i).members)))
                cl.sendText(msg.to,"===========[List Group]==========\n"+ h +"Total Group :" + str(len(gids)))
                
            elif msg.text in ["LG1"]:
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]\n%s\n\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["LG2"]:
              if msg.from_ in owner:
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]\n%s\n\n" % (ki.getGroup(i).name,i)
                ki.sendText(msg.to,h)
            elif msg.text in ["LG3"]:
              if msg.from_ in owner:
                gid = kk.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]\n%s\n\n" % (kk.getGroup(i).name,i)
                kk.sendText(msg.to,h)
            elif msg.text in ["LG4"]:
              if msg.from_ in owner:
                gid = kc.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]\n%s\n\n" % (kc.getGroup(i).name,i)
                kc.sendText(msg.to,h)
            elif msg.text in ["LG5"]:
              if msg.from_ in owner:
                gid = ks.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]\n%s\n\n" % (ks.getGroup(i).name,i)
                ks.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bot out","Op bye"]:
              if msg.from_ in owner:
                #gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = ks.getGroupIdsJoined()
                gid = ka.getGroupIdsJoined()
                for i in gid:
                  ka.leaveGroup(i)
                  ks.leaveGroup(i)
                  kc.leaveGroup(i)
                  ki.leaveGroup(i)
                  kk.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sayonara")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#------------------------End---------------------

 #-----------------End-----------
            elif msg.text in ["Op katakan hi"]:
              if msg.from_ in owner:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Welcome"]:
                cl.sendText(msg.to,"Selamat datang di Group Kami")
                cl.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING"]:
              if msg.from_ in owner:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","Absen bot","Stay","Respon"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"すでに保護している86(Already On Protect Group)")
                ki.sendText(msg.to,"すでに保護している86(Already On Protect Group)")
                kk.sendText(msg.to,"すでに保護している86(Already On Protect Group)")
                kc.sendText(msg.to,"すでに保護している86(Already On Protect Group)")
                ks.sendText(msg.to,"すでに保護している86(Already On Protect Group)")
                #ka.sendText(msg.to,"")
                cl.sendText(msg.to,"すでに保護している86 It's Present Done✔ Complete Ready To Protect Group")
    #-------------Fungsi Respon Finish---------------------#   
            elif msg.text in ["Invite"]:
              if msg.from_ in owner:
                wait["winvite"] = True
                cl.sendText(msg.to,"Share contact boss 😎")
                
            elif msg.text in ["2invite"]:
              if msg.from_ in owner:
                wait["winvite2"] = True
                ki.sendText(msg.to,"Share contact boss 😎")
                
            elif msg.text in ["3invite"]:
              if msg.from_ in owner:
                wait["winvite3"] = True
                kk.sendText(msg.to,"Share contact boss 😎")
                
            elif msg.text in ["4invite"]:
              if msg.from_ in owner:
                wait["winvite4"] = True
                kc.sendText(msg.to,"Share contact boss 😎")
                
            elif msg.text in ["5invite"]:
              if msg.from_ in owner:
                wait["winvite5"] = True
                ks.sendText(msg.to,"Share contact boss 😎")
                
            elif msg.text in ["6invite"]:
              if msg.from_ in owner:
                wait["winvite6"] = True
                ka.sendText(msg.to,"Share contact boss 😎")
                
            elif msg.text in ["Invite Group Creator","Invite group creator"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                  ginfo = cl.getGroup(msg.to)
                  gCreator = ginfo.creator.mid
                  try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    cl.sendText(msg.to, "Succes Inv gCreator")
                  except:
                    try:
                      p1.findAndAddContactsByMid(gCreator)
                      p1.inviteIntoGroup(msg.to,[gCreator])
                      p1.sendText(msg.to, "Succes Inv gCreator")
                    except:
                      random.choice(KAC).findAndAddContactsByMid(gCreator)
                      random.choice(KAC).inviteIntoGroup(msg.to,[gCreator])
                      random.choice(KAC).sendText(msg.to, "Succes Inv gCreator")
            
            elif msg.text in ["SpamInvite"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                #siap = cl.getGroup(msg.to)
                  ready = cl.getAllContactIds()
                  targets = []
                  targets.append(ready)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        cl.inviteIntoGroup(msg.to,[target])
                      except:
                        cl.inviteIntoGroup(msg.to,[target])
                        
            elif msg.text == 'Tagall2':
              if msg.from_ in owner:
                group = cl.getGroup(msg.to) 
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                  mention(msg.to, nama)

                elif jml > 100 and jml < 200:
                  for i in range(0,100):
                    nm1 += [nama[i]]
                  mention(msg.to, nm1)
                  for j in range(100, len(nama)-1):
                    nm2 += [nama[j]]
                  mention(msg.to, nm2)
                
                elif jml > 200 and jml < 300:
                  for i in range(0,100):
                    nm1 += [nama[i]]
                  mention(msg.to, nm1)
                  for j in range(100, 200): 
                    nm2 += [nama[j]]
                  mention(msg.to, nm2)
                  for x in range(200, len(nama)-1):
                    nm3 += [nama[x]]
                  mention(msg.to, nm3)
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                random.choice(KAC).sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")
      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "Calculating...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sSeconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#
      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'u0f4cbccff2b03754d07d8db8707023f6'}
              cl.sendText(msg.to,"👇👇👇👇👇👇👇👇👇👇👇👇")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"👆👆👆👆👆👆👆👆👆👆👆👆")
              
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
              quote = ['Apaan sih Ka Kurang Kerjaan Banget','Bodo Amat','Dasar Jones Manggil² Bot','Jones Ya?','Ada Orang kah disini?','Ah Upil Lu','Ada Perawan Nganggur ga Coy?']
              psn = random.choice(quote)
              cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing Banned User")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "→" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
            elif msg.text in ["Cek ban"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            
            elif "Ban all" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Not found ~")
                  else:
                    for target in targets:
                      if target in Bots:
                        pass
                      elif target in admin:
                        pass
                      else:
                        try:
                          wait["blacklist"][target] = True
                          f=codecs.open('st2__b.json','w','utf-8')
                          json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                          cl.sendText(msg.to,"Terbanned ~")
                        except:
                          cl.sendText(msg.to,"Error")
            elif msg.text in ["Tendang ban","Kill ban"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        #random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        #random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        #random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        #random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        #random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        #random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Random " in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    strnum = msg.text.replace("Random ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.00001)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "Fakecat" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
            
            elif "Steal " in msg.text:
              if msg.from_ in owner:
                  nk0 = msg.text.replace("Steal ","")
                  nk1 = nk0.lstrip()
                  nk2 = nk1.replace("@","")
                  nk3 = nk2.rstrip()
                  _name = nk3
                  gs = cl.getGroup(msg.to)
                  targets = []
                  for s in gs.members:
                       if _name in s.displayName:
                           targets.append(s.mid)
                  if targets == []:
                      sendMessage(msg.to,"user does not exist")
                      pass
                  else:
                      for target in targets:
                          try:
                              contact = cl.getContact(target)
                              x = contact.displayName
                              profile = cl.getProfile()
                              profile.displayName = x
                              cl.updateProfile(profile)
                              cl.sendText(msg.to,"Steal Profile Picture Success Boss 😂")
                          except Exception as e:
                              cl.sendText(msg.to,"Fail")
                              print e
            
            elif "Ig: " in msg.text:
              if msg.from_ in admin:
                cari = msg.text.replace("Ig: ","")
                try:
                    response = requests.get("https://www.instagram.com/"+cari+"?__a=1")
                    data = response.json()
                    namaIG = str(data['user']['full_name'])
                    bioIG = str(data['user']['biography'])
                    mediaIG = str(data['user']['media']['count'])
                    verifIG = str(data['user']['is_verified'])
                    usernameIG = str(data['user']['username'])
                    followerIG = str(data['user']['followed_by']['count'])
                    profileIG = data['user']['profile_pic_url_hd']
                    privateIG = str(data['user']['is_private'])
                    followIG = str(data['user']['follows']['count'])
                    text = "==============================\n[Name] : "+namaIG+"\n[Biography] :\n"+bioIG+"\n[Follower] : "+followerIG+"\n[Following] : "+followIG+"\n[Media] : "+mediaIG+"\n[Verified] :"+verifIG+"\n[Private] : "+privateIG+"\n[Username] : "+usernameIG+"\n=============================="
                    cl.sendImageWithUrl(msg.to, profileIG)
                    cl.sendText(msg.to, str(text))
                except Exception as e:
                    cl.sendText(msg.to, str(e))
                    
            elif "Translate-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-eng ","")
                try:
                  translator = Translator()
                  trs = translator.translate(txt,'en')
                  A = trs.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to,A)
                except:
                  cl.sendText(msg.to,'Error.')
                  
            elif "Translate-arab " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-arab ","")
                try:
                  translator = Translator()
                  trs = translator.translate(txt,'ar')
                  A = trs.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to,A)
                except:
                  cl.sendText(msg.to,'Error.')
                    
            elif "Translate-japan " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-japan ","")
                try:
                  translator = Translator()
                  trs = translator.translate(txt,'ja')
                  A = trs.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to,A)
                except:
                  cl.sendText(msg.to,'Error.')
                    
            elif "Say " in msg.text:
              if msg.from_ in admin:
                    say = msg.text.replace("Say ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
            
            elif "Jsay " in msg.text:
              if msg.from_ in admin:
                    say = msg.text.replace("Jsay ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
            
            elif "Isay " in msg.text:
              if msg.from_ in admin:
                    say = msg.text.replace("Isay ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")

                    
            elif '/lyric ' in msg.text.lower():
              if msg.from_ in admin:  
                try:
                    songname = msg.text.lower().replace('/lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Song ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif "Youtube: " in msg.text:
              if msg.from_ in admin:
                query = msg.text.replace("Youtube: ","")
                cl.sendText(msg.to, "Searching...")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'https://www.youtube.com/results'
                    params = {'search_query':query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    loop = 1
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            if loop == 0:
                                cl.sendText(msg.to, a['title']+'\nhttps://www.youtube.com'+a['href'])
                                break
                            else:
                                loop = loop - 1
            elif msg.text.lower() == 'runtime':
              if msg.from_ in admin:
                eltime = time.time() - mulai
                van = "Bot Was Running On "+waktu(eltime)
                cl.sendText(msg.to,van)
            elif 'music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithUrl(msg.to, song[3])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
                    
            elif '/music ' in msg.text.lower():
              if msg.from_ in admin:  
                try:
                    songname = msg.text.lower().replace('/music ','')
                    params = {'songname': songname}
                    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithUrl(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
        
            elif "Pp group " in msg.text:
              if msg.from_ in admin:
                saya = msg.text.replace('Pp group ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                        
            elif "Dp @" in msg.text:
              if msg.from_ in admin:
                print "[Command]dp executing"
                _name = msg.text.replace("Dp @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                  if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  cl.sendText(msg.to,"Contact not found")
                else:
                  for target in targets:
                    try:
                      contact = cl.getContact(target)
                      cu = cl.channel.getCover(target)
                      path = str(cu)
                      cl.sendImageWithUrl(msg.to,path)
                    except Exception as e:
                      raise e
                 
            elif "Stealgroup" in msg.text:
              if msg.from_ in owner:
                group = cl.getGroup(msg.to)
                cl.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + group.pictureStatus)
            
            elif "Pp @" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                if targets == []:
                    cl.sendText(msg.to,"Kontak tidak ditemukan,mungkin kontak yg dituju tidak mempunyai muka")
                else:
                    for target in targets:
                      try:
                        contact = cl.getContact(target)
                        path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithUrl(msg.to, path)
                      except Exception as e:
                        raise e
                        
            elif "Name @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Name @","")
                _nametarget = _name.rstrip(" ")
                gs = cl.getGroup(msg.to)
                for h in gs.members:
                  if _nametarget == h.displayName:
                    cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                  else:
                    pass
                        
            elif "Anu @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Anu @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                  if _nametarget == g.displayName:
                    cl.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ka.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ka.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ki.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kk.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    kc.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ks.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    ka.sendText(g.mid,"QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO.QQ.MM.OO")
                    cl.sendText(msg.to, "Done")
                    
            elif msg.text in ["Simisimi on","Simisimi:on"]:
              if msg.from_ in owner:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
              else:
                cl.sendText(msg.to,"You Are Not My Boss")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
              if msg.from_ in owner:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
              else:
                cl.sendText(msg.to,"You Are Not My Boss")
                
            elif Filter in msg.text:
              if msg.from_ in admin:
                pass
              elif msg.from_ in whitelist:
                pass
              else:
                cl.sendText(msg.to,"Ngomong Kasar Tidak Diperbolehkan Disini\nKick Aja Lah")
                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
#------------ Filter Chat --------------
            elif msg.text in[".qrp on",".kick on","kick on","Kick on","Ready op","Ready Op","Fvck","fvck","Fuck","fuck",".kickall on",".kickall"]:
              if msg.from_ in admin:
                pass
              else:
                try:
                  cl.sendText(msg.to,"Cieee Kickers!!!")
                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                  wait["blacklist"][msg.from_] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  cl.sendText(msg.to,"Bye Bitch")
                  
            elif msg.text in ["Kontol","kontol","Memek","memek","Kntl","kntl","Kntol","kntol"]:
              if msg.from_ in admin:
                pass
              else:
                try:
                  cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                except:
                  cl.sendText(msg.to,"Bye Bitch")
                  
            elif "Kontol" in msg.txt:
              if msg.from_ in admin:
                pass
              else:
                try:
                  cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                except:
                  cl.sendText(msg.to,"Bye Bitch")
            elif "kontol" in msg.txt:
              if msg.from_ in admin:
                pass
              else:
                try:
                  cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                except:
                  cl.sendText(msg.to,"Bye Bitch")
            elif "Memek" in msg.txt:
              if msg.from_ in admin:
                pass
              else:
                try:
                  cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                except:
                  cl.sendText(msg.to,"Bye Bitch")
            elif "memek" in msg.txt:
              if msg.from_ in admin:
                pass
              else:
                try:
                  cl.sendText(msg.to,"Dilarang Ngomong Jorok !!!!")
                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                except:
                  cl.sendText(msg.to,"Bye Bitch")
            
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n╠" + Name
                wait2['ROM'][op.param1][op.param2] = "╠" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          cl.sendText(op.param1, "👥Welcome to the group👥\n" + "👉" + str(ginfo.name) + "👈" + "\n" + "👑Group Owner Is👑" + "\n" + "👉" + ginfo.creator.displayName + "👈" + "\n\n" + "    This Group Has Been Protect By:" + "\n⭐||One Piece Team Protect||⭐")
          random.choice(KAC).sendText(op.param1, "Founder Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
          random.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
          print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if op.param2 in Bots:
            return
          random.choice(KAC).sendText(op.param1, "Innallilahiwainalulahirojiun..Kenapa Tuh Leave?Baper Kayaknya Tu orang cuma Dumay Coyyy😜😜😜")
          print "MEMBER HAS LEFT THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,50):
      hasil = satpam.activity(limit=50)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          #satpam.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #satpam.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by : @ই✠1DaffaN3Kalani☪ইद 􀂳􏿿👈\n\n124D15T1 T34M B0T")
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by : @ই✠1DaffaN3Kalani☪ইद 􀂳􏿿👈\n\n124D15T1 T34M B0T")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          #ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          #kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          #ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ku.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          #ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          #ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ko.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          #k1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #k1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          #satpam.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"=====Ready=====\n[★]Bot Protect Group[★]\n-Registrasi 100K\n-Bulan Selanjutnya 50K/Bulan\nTotal 10 Bot\n\n[★]SelfBot[★]\n- 1 Selfbot 1 Bot Assist = 50K/Bulan\n- 1 Selfbot 2 Bot Assist = 100K/Bulan\n- 1 Selfbot 3 Bot Assist = 150K/Bulan\n- 1 Selfbot 4 Bot Assist = 200K/Bulan\n- 1 Selfbot 5 Bot Assist = 250K/Bulan\nVia :\nBank BCA\nPulsa Telkomsel & Three\n\nBisa Test Terlebih Dahulu Bisa\nMinat??? PM Id Line @hanavy1992\n[★]One Piece Team Protect[★]\nGroup Ga Aman Jaminan Uang Kami Kembalikan")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,50):
        hasil = cl.activity(limit=50)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    #ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    #kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    #ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    #ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    #ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by : O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉\nStatus Boss udah Kami Like\nOwner Kami :\nHanavy Koplaxs")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
                
#def nameUpdate():
    #while True:
        #try:
          #if wait["clock"] == True:
            #now2 = datetime.now()
            #nowT = datetime.strftime(now2,"(%H:%M)")
            #profile = cl.getProfile()
            #profile.displayName = wait["cName"]
            #cl.updateProfile(profile)
            
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
