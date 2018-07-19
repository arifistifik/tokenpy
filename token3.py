from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse


token = LINE() 
token.log("Auth Token : " + str(token.authToken)) 
token.log("Timeline Token : " + str(token.tl.channelAccessToken)) 

token1 = LINE() 
token1.log("Auth Token : " + str(token1.authToken)) 
token1.log("Timeline Token : " + str(token1.tl.channelAccessToken)) 

token2 = LINE() 
token2.log("Auth Token : " + str(token2.authToken)) 
token2.log("Timeline Token : " + str(token2.tl.channelAccessToken)) 

token = token
oepoll = OEPoll(token)
All = [token1,token2,token3,token4]
mid = token.profile.mid
Amid = token1.getProfile().mid
Bmid = token2.getProfile().mid
Cmid = token3.getProfile().mid
Dmid = token4.getProfile().mid
ARBots = [mid,Amid,Bmid,Cmid,Dmid]
ARSelf = ["u0849bd9c038b7e176e02fdbf83c37363"]
ARifistifik = ARSelf + ARBots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    token.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)


def bot(op):
    try:
        if op.type == 5:
            if Setmain["ARautoadd"] == True:
                ra = token.getContact(op.param1)
                token.findAndAddContactsByMid(ra.mid)
                token.sendMessageWithMention(op.param1, op.param1,"Hai","\nsudah ku addback ya\n\n{}".format(str(Setmain["ARmessage"])))
                
        if op.type == 22:
            if mid in op.param3:
                if Setmain["ARautojoin"] == True:
                    cl.leaveRoom(op.param1)        
                
        if op.type == 13:
            if mid in op.param3:
                if Setmain["ARautojoin"] == True:
                    if Setmain["ARbatas"]["on"] == True:
                        G = token.getGroup(op.param1)
                        if len(G.members) > Setmain["ARbatas"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            ra = token.getGroup(op.param1)
                            token.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["ARbatas"]["members"]))
                            token.leaveGroup(op.param1)
                        else:
                            token.acceptGroupInvitation(op.param1)
                            ra = token.getGroup(op.param1)
                            token.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :)")
                            
            if Amid in op.param3:
                if Setmain["ARautojoin"] == True:
                    if Setmain["ARbatas"]["on"] == True:
                        G = token1.getGroup(op.param1)
                        if len(G.members) > Setmain["ARbatas"]["members"]:
                            token1.acceptGroupInvitation(op.param1)
                            ra = token1.getGroup(op.param1)
                            token1.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["ARbatas"]["members"]))
                            token1.leaveGroup(op.param1)
                        else:
                            token1.acceptGroupInvitation(op.param1)
                            ra = token1.getGroup(op.param1)
                            token1.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :)")
                            
            if Bmid in op.param3:
                if Setmain["ARautojoin"] == True:
                    if Setmain["ARbatas"]["on"] == True:
                        G = token2.getGroup(op.param1)
                        if len(G.members) > Setmain["ARbatas"]["members"]:
                            token2.acceptGroupInvitation(op.param1)
                            ra = token2.getGroup(op.param1)
                            token2.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["ARbatas"]["members"]))
                            token2.leaveGroup(op.param1)
                        else:
                            token2.acceptGroupInvitation(op.param1)
                            ra = token2.getGroup(op.param1)
                            token2.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam kenal yah :)")
                            
            if Cmid in op.param3:
                if Setmain["ARautojoin"] == True:
                    if Setmain["ARbatas"]["on"] == True:
                        G = token3.getGroup(op.param1)
                        if len(G.members) > Setmain["ARbatas"]["members"]:
                            token3.acceptGroupInvitation(op.param1)
                            ra = token3.getGroup(op.param1)
                            token3.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["ARbatas"]["members"]))
                            token3.leaveGroup(op.param1)
                        else:
                            token3.acceptGroupInvitation(op.param1)
                            ra = token3.getGroup(op.param1)
                            token3.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :)")
                            
            if Dmid in op.param3:
                if Setmain["ARautojoin"] == True:
                    if Setmain["ARbatas"]["on"] == True:
                        G = token4.getGroup(op.param1)
                        if len(G.members) > Setmain["ARbatas"]["members"]:
                            token4.acceptGroupInvitation(op.param1)
                            ra = token4.getGroup(op.param1)
                            token4.sendText(op.param1,"Sorry jumlah member\n " + str(ra.name) + " lebih dari " + str(Setmain["ARbatas"]["members"]))
                            token4.leaveGroup(op.param1)
                        else:
                            token4.acceptGroupInvitation(op.param1)
                            ra = token4.getGroup(op.param1)
                            token4.sendMessageWithMention(op.param1, ra.creator.mid,"Haii","\nSalam Kenal yah :).")
                            
        if op.type == 46:
            if op.param2 in ARBots:
                token1.removeAllMessages()
                token2.removeAllMessages()
                token3.removeAllMessages()
                token4.removeAllMessages() 
                
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            #receiver = msg.to
            #sender = msg._from
            if msg.toType == 2:
                if msg.contentType == 13:
                    if Setmain["ARautoscan"] == True:
                        msg.contentType = 0
                        token.sendText(msg.to,msg.contentMetadata["mid"])
                        
                elif msg.contentType == 0:
                    if Setmain["ARautoread"] == True:
                        token.sendChatChecked(msg.to, msg_id)
                        token1.sendChatChecked(msg.to, msg_id)
                        token2.sendChatChecked(msg.to, msg_id)
                        token3.sendChatChecked(msg.to, msg_id)
                        token4.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menu":
                            md = "ARIFISTIFIK\n\n"
                            md += " cek「@」\n"
                            md += " gid\n"
                            md += " yid\n"
                            md += " me\n"
                            md += " spb\n"
                            md += " tag\n"
                            md += " set\n"
                            md += " rebot\n"
                            md += " rc\n"
                            md += " cekmid 「on/off」\n"
                            md += " autoread 「on/off」\n"
                            md += " in\n"
                            md += " out\n"
                            md += " kis「@」\n"
                            token.sendText(msg.to, md)
                            
                        elif text.lower() == "set":
                            if msg._from in ARSelf:
                                md = "ARIFISTIFIK\n\n"
                                if Setmain["ARautoscan"] == True: md+="✅ Cekmid\n"
                                else: md+="🍁 Cekmid\n"
                                if Setmain["ARautoread"] == True: md+="✅ Autoread\n"
                                else: md+="🍁 Autoread\n"
                                token.sendText(msg.to, md)
                                
            #---------------------- On/Off Command -------------------# 
            
                        elif text.lower() == "autoread on":
                            if msg._from in ARSelf:
                                if Setmain["ARautoread"] == False:
                                    Setmain["ARautoread"] = True
                                    token.sendMessageWithMention(msg.to,msg._from,"","Auto Read Di Aktifkan")
                                else:
                                    token.sendMessageWithMention(msg.to,msg._from,"","Auto Read Sudah Aktif")
                                    
                        elif text.lower() == "autoread off":
                            if msg._from in ARSelf:
                                if Setmain["ARautoread"] == True:
                                    Setmain["ARautoread"] = False
                                    token.sendMessageWithMention(msg.to,msg._from,"","Auto Read Di Matikan")
                                else:
                                    token.sendMessageWithMention(msg.to,msg._from,"","Auto Read Sudah Di Matikan")
                                    
                        elif text.lower() == "cekmid on":
                            if msg._from in ARSelf:
                                if Setmain["ARautoscan"] == False:
                                    Setmain["ARautoscan"] = True
                                    token.sendMessageWithMention(msg.to,msg._from,"","Cekmid diaktifkan")
                                else:
                                    token.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == "cekmid off":
                            if msg._from in ARSelf:
                                if Setmain["ARautoscan"] == True:
                                    Setmain["ARautoscan"] = False
                                    token.sendMessageWithMention(msg.to,msg._from,"","Cekmid dinonaktifkan")
                                else:
                                    token.sendMessageWithMention(msg.to,msg._from,"","Sudah off")            
                            
            #---------------- Fungsi Command ------------------#
            
                        elif "cek" in text.lower():
                            key = eval(msg.contentMetadata["MENTION"])
                            keys = key["MENTIONEES"][0]["M"]
                            ra = cl.getContact(keys)
                            try:
                                token.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                token.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                            except:
                                pass
                            
                        elif text.lower() == "gid":
                            token.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            token.sendText(msg.to,msg.to)
                            
                        elif text.lower() == "yid":
                            token.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                            token.sendText(msg.to,msg._from)
                        
                        elif text.lower() == "me":
                            token.sendMessageWithMention(msg.to,msg._from,"Hay","\nada apa?")
                            
                        elif text.lower() == "spb":
                            start = time.time()
                            token.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start
                            token.sendText(msg.to, "%s " % (elapsed_time))
                            
                            start2 = time.time()
                            token1.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start2
                            token1.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start3 = time.time()
                            token2.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start3
                            token2.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start4 = time.time()
                            token3.sendMessage("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start4
                            token3.sendText(msg.to, "%s" % (elapsed_time))
                                
                            start5 = time.time()
                            token4.sendText("u3b07c57b6239e5216aa4c7a02687c86d", '.')
                            elapsed_time = time.time() - start5
                            token4.sendText(msg.to, "%s" % (elapsed_time))
                            
                        elif text.lower() == "tag":
                            group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//100
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*100 : (a+1)*100]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Sange \n'
                                token.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                
                        elif text.lower() == "rebot":
                            if msg._from in ARSelf:
                                token.sendMessageWithMention(msg.to,msg._from,"","Tunggu Sebentar..")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)
                                
                        elif text.lower() == "rc":
                            if msg._from in ARSelf:
                                try:
                                    token1.removeAllMessages(op.param2)
                                    token2.removeAllMessages(op.param2)
                                    token3.removeAllMessages(op.param2)
                                    token4.removeAllMessages(op.param2)
                                    token1.sendMessageWithMention(msg.to,msg._from,"","Sudah Di Bersihkan")
                                except:
                                    pass        
                            
                        elif text.lower() == "in":
                            if msg._from in ARSelf:
                                G = token.getGroup(msg.to)
                                ginfo = token.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                token.updateGroup(G)
                                invsend = 0
                                Ticket = token.reissueGroupTicket(msg.to)
                                token1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                token2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                token3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                token4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = token.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                token.updateGroup(G)
                                G.preventedJoinByTicket(G)
                                token.updateGroup(G)
                        
                        elif text.lower() == "out":
                            if msg._from in ARSelf:
                                ra = token1.getGroup(msg.to)
                                token1.sendMessageWithMention(msg.to,ra.creator.mid,"Haii Semunya 😯","\nAku ijin baper 😢 bye")
                                token1.leaveGroup(msg.to)
                                token2.sendMessageWithMention(msg.to,ra.creator.mid,"Haii Semunya 😯","\nAku ijin baper 😢 bye")
                                token2.leaveGroup(msg.to)
                                token3.sendMessageWithMention(msg.to,ra.creator.mid,"Haii Semunya 😯","\nAku ijin baper 😢 bye")
                                token3.leaveGroup(msg.to)
                                token4.sendMessageWithMention(msg.to,ra.creator.mid,"Haii Semunya 😯","\nAku ijin baper 😢 bye")
                                token4.leaveGroup(msg.to)
                                
                        elif "kis" in text.lower():
                            if msg._from in ARSelf:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in ARifistifik:
                                        pass
                                    else:
                                        try:
                                            token1.sendMessageWithMention(msg.to,target,"Sorry Bro","Aku kick anda karna anda jelek makasih")
                                            klist = [token1,token2,token3,token4]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass        
                                
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in ARSelf:
                                link_re = re.compile('(?:line\:\/|line\me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["ARautojoin"] == True:
                                        ra = token.findGroupByTicket(ticket_id)
                                        token.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        token1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        token1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        token1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        token1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
                                    else:    
                                        token1.sendMessageWithMention(msg.to,msg._from,"Kalau mau Auto Join","\naktifkan auotojoin dulu")

    except Exception as error:
        print (error)
        
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)
