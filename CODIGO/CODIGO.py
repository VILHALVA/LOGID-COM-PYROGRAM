from pyrogram import Client, filters

# Usando a sessão salva "my_account.session"
app = Client("my_account")

@app.on_message(filters.private)
async def log_message(client, message):
    # Obtém o ID do usuário que enviou a mensagem
    user_id = message.from_user.id
    
    # Obtém o conteúdo da mensagem
    text = message.text
    
    # Imprime no console o ID do usuário e a mensagem recebida
    print(f"Usuário ID: {user_id} | Mensagem: {text}")
    
    # Responde ao usuário com uma mensagem de confirmação
    await message.reply("Mensagem recebida. Seu ID foi registrado no log!")

app.run()
