import itchatmp
import wechat_bot_account
import naips_bot, naips_account

itchatmp.update_config(itchatmp.WechatConfig(
    token = wechat_bot_account.wechat_token,
    appId = wechat_bot_account.wechat_mp_appid,
    appSecret = wechat_bot_account.wechat_mp_appkey,
    encryptMode = itchatmp.content.SAFE,
    encodingAesKey = wechat_bot_account.wechat_mp_aeskey))


@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    msg_str = msg['Content']
    naips_str = naips_bot.get_met_briefing("YMML", naips_bot.napis_user_login(naips_bot.get_initial_cookie(), naips_account.naips_username, naips_account.naips_password))

    if "ymml atis" or "YMML ATIS" or "ymml" or "YMML" in msg_str:

        itchatmp.send({
            'MsgType': itchatmp.content.IMAGE,
            'FileDir': 'test.jpg' }, msg["FromUserName"])


itchatmp.run(port=80, debug=True)