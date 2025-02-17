import logging
import settings
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
)

from get_cv import cv_handler

from filter_cv import filter_handler
from personal_area import personal_area_handler

from handlers import (
    find_work,
    message_if_wrong,
    start,
    # find_worker,
    delete_from_base,
)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': settings.PROXY_url,
#     'urllib3_proxy_kwargs': {
#         'username': settings.PROXY_username,
#         'password': settings.PROXY_pass
#     }
# }

logger = logging.getLogger(__name__)


def main() -> None:
    mybot = Updater(settings.API_KEY, use_context=True)  # request_kwargs=PROXY
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(find_work, pattern='^' + 'Найти работу' + '$'))
    dp.add_handler(CallbackQueryHandler(delete_from_base, pattern='^' + 'удалить запись' + '$'))
    dp.add_handler(cv_handler)
    dp.add_handler(filter_handler)
    dp.add_handler(personal_area_handler)
    dp.add_handler(MessageHandler(Filters.text | Filters.photo, message_if_wrong))
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
