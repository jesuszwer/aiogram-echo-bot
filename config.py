from pydantic import BaseModel
from pydantic_settings import BaseSettings

AUTHOR: str = "author"
TOKEN: str = "your_token_bot"  # noqa: S105


class BotSettings(BaseModel):
    token: str = TOKEN


class Constant(BaseModel):
    start_text: str = """
    Привет! 👋 Я эхо-бот. Отправь мне любое сообщение, и я повторю его!  
Но это ещё не всё — ты можешь изменить его с помощью кнопок:  

🔠 <b>"В ВЕРХНИЙ РЕГИСТР"</b> – превращает текст в заглавные буквы.  
🔡 <b>"в нижний регистр"</b> – делает все буквы маленькими.  
🔄 <b>"Развернуть текст"</b> – переворачивает текст задом наперёд.  

Попробуй отправить что-нибудь! 😊
    """
    help_text: str = f"""
    🔹 <b>Помощь по боту</b> 🔹

Я — эхо-бот! 📢 Отправь мне любое сообщение, и я его повторю.  
Но у меня есть ещё несколько полезных функций:  

🔠 <b>"В ВЕРХНИЙ РЕГИСТР"</b> – превращает текст в заглавные буквы.  
🔡 <b>"в нижний регистр"</b> – делает все буквы маленькими.  
🔄 <b>"Развернуть текст"</b> – переворачивает текст задом наперёд.  

👀 Просто отправь мне текст и выбери действие с помощью кнопок!  
Если у тебя возникли вопросы, напиши сюда: @{AUTHOR}  

Приятного использования! 🚀  
    """


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()
    const: Constant = Constant()


settings = Settings()
