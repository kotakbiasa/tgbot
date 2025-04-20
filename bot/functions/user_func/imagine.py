from time import time
from telegram import Update
from telegram.ext import ContextTypes
from bot.modules import llm

async def func_imagine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    effective_message = update.effective_message
    prompt = " ".join(context.args)

    if not prompt:
        await effective_message.reply_text("Use <code>/imagine prompt</code>\nE.g. <code>/imagine A cat and a dog playing</code>")
        return
    
    sent_message = await effective_message.reply_text("🎨 Generating...")

    start_time = time()
    response = await llm.imagine(prompt)
    response_time = f"{(time() - start_time):.2f}s"

    if not response:
        await context.bot.edit_message_text("Oops! Something went wrong!", chat.id, sent_message.id)
        return
    
    caption = (
        f"<blockquote>Prompt: {prompt}</blockquote>\n"
        f"<b>Process time:</b> <code>{response_time}</code>\n"
        f"<b>User:</b> <code>@{user.username}</code>"
    )

    await context.bot.delete_message(chat.id, sent_message.id)
    await effective_message.reply_photo(response, caption)
