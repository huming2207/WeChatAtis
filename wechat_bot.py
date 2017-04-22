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
    msg_str = str(msg['Content']).upper().split(" ")

    if "ATIS" in msg_str[0]:
        if len(msg_str[1]) == 4 and msg_str[1].isalpha():

            copyright_msg = "Data sourced from Airservice Australia NAIPS system," \
                            "for personal research or educational uses only.\n" \
                            "DO NOT USE IT FOR REAL FLIGHTS!!\n\n"

            naips_str = copyright_msg + str(naips_bot.get_met_briefing(msg_str[1],
                                                   naips_bot.napis_user_login(naips_bot.get_initial_cookie(),
                                                                              naips_account.naips_username,
                                                                              naips_account.naips_password)))
            return naips_str

        else:
            return str("Wrong airport code, please check again. Your message is: " + msg['Content'])





itchatmp.run(port=80, debug=True)