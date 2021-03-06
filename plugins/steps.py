# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  steps.py importado.{/cyan}'))

hideBoard = types.ReplyKeyboardHide()

reply_to_msg = list()
send_msg = list()


@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'start')
def step_start(m):
    cid = m.chat.id
    if m.content_type == 'text':
        if m.text == 'ESPAÑOL':
            users[str(cid)] = {"lang":"es", "banned": False, "notify": True}
        elif m.text == 'ENGLISH':
            users[str(cid)] = {"lang":"en", "banned": False, "notify": True}
        elif m.text == 'ITALIANO':
            users[str(cid)] = {"lang":"it", "banned": False, "notify": True}
        elif m.text == 'POLSKI':
            users[str(cid)] = {"lang":"pl", "banned": False, "notify": True}
        elif m.text == 'DEUTSCH':
            users[str(cid)] = {"lang":"de", "banned": False, "notify": True}
        elif m.text == 'FRANÇAIS':
            users[str(cid)] = {"lang":"fr", "banned": False, "notify": True}
        elif m.text == 'PERSIAN':
            users[str(cid)] = {"lang":"fa", "banned": False, "notify": True}
        elif m.text == 'PORTUGUÊS':
            users[str(cid)] = {"lang":"pt", "banned": False, "notify": True}
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message( cid, responses['lang_error'][lang(cid)]%( m.text, m.text), parse_mode="Markdown")
            return None
        with open( 'usuarios.json', 'w') as f:
            json.dump( users, f)
        for id in admins:
            bot.send_chat_action(cid, 'typing')
            bot.send_message( id, "Nuevo usuario\n\nNombre: " + str(m.from_user.first_name) + "\nAlias: @" + str(m.from_user.username) + "\nID: " + str(cid))
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['start_2'][lang(cid)], reply_markup=hideBoard)
        userStep[cid] = 0

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'all')
def step_all(m):
    cid = m.chat.id
    save = list()
    delete = list()
    aux = str()
    if m.content_type == 'text':
        userStep[cid] = 0
        for uid in users:
            if users[str(uid)]['notify'] and not is_banned(uid):
                try:
                    bot.send_chat_action( int(uid), 'typing')
                    bot.send_message( int(uid), m.text)
                except:
                    delete.append(uid)
                    #users.pop(uid)
                else:
                    save.append(uid)
        cont = 1
        aux = "Conservados:"
        for x in save:
            aux += "\n\t" + str(cont) + ') '+ x
            cont += 1
        aux += "\nEliminados:"
        cont = 1
        for x in delete:
            users.pop(x)
            aux += "\n\t" + str(cont) + ') '+ x
            cont += 1
        with open('tmp.txt','w') as f:
            f.write(aux)
        bot.send_chat_action(cid, 'typing')
        bot.send_document( cid, open('tmp.txt' ,'rt'))

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'contact')
def step_contact(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        for x in admins:
            bot.send_chat_action( x, 'typing')
            bot.send_message( x, contact_format(m), parse_mode="Markdown")
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['contact_2'][lang(cid)])

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'lang')
def step_lang(m):
    cid = m.chat.id
    if m.content_type == 'text':
        if m.text == 'ESPAÑOL':
            users[str(cid)]['lang'] = 'es'
        elif m.text == 'ENGLISH':
            users[str(cid)]['lang'] = 'en'
        elif m.text == 'ITALIANO':
            users[str(cid)]['lang'] = 'it'
        elif m.text == 'POLSKI':
            users[str(cid)]['lang'] = 'pl'
        elif m.text == 'DEUTSCH':
            users[str(cid)]['lang'] = 'de'
        elif m.text == 'FRANÇAIS':
            users[str(cid)]['lang'] = 'fr'
        elif m.text == 'PERSIAN':
            users[str(cid)]['lang'] = 'fa'
        elif m.text == 'PORTUGUÊS':
            users[str(cid)]['lang'] = 'pt'
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message( cid, responses['lang_error'][lang(cid)]%( m.text, m.text), parse_mode="Markdown")
            return None
        userStep[cid] = 0
        with open('usuarios.json', 'w') as f:
            json.dump( users, f)
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['lang_2'][lang(cid)], reply_markup=hideBoard)

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'update_rotation_text')
def step_update_rotation_text(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        with open('extra_data/rotation.txt','w') as f:
            f.write(m.text)
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['update_rotation_text_2'])

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'update_rotation_pic', content_types=['photo'])
def step_update_rotation_pic(m):
    cid = m.chat.id
    userStep[cid] = 0
    file_info = bot.get_file(m.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('extra_data/rotation.jpg','wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_chat_action(cid, 'typing')
    bot.send_message( cid, responses['update_rotation_pic_2'])

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'update_sale_text')
def step_update_sale_text(m):
    cid = m.chat.id
    if m.content_type == 'text':
        userStep[cid] = 0
        with open('extra_data/sale.txt','w') as f:
            f.write(m.text)
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['update_sale_text_2'])

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) == 'update_sale_pic', content_types=['photo'])
def step_update_sale_pic(m):
    cid = m.chat.id
    userStep[cid] = 0
    file_info = bot.get_file(m.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('extra_data/sale.jpg','wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_chat_action(cid, 'typing')
    bot.send_message( cid, responses['update_sale_pic_2'])

@bot.message_handler(func=lambda msg: next_step_handler(msg.chat.id) in ['patch_es','patch_en','patch_it','patch_pl','patch_fr','patch_de','patch_pt','patch_fa'] )
def step_update_patch(m):
    cid = m.chat.id
    if m.content_type == 'text':
        with open('extra_data/patch_' + userStep[cid].split('_')[1] + '.txt','w') as f:
            f.write(m.text)
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, "Actualizado *patch_" + userStep[cid].split('_')[1] + ".txt*", parse_mode="Markdown")
        userStep[cid] = 0
