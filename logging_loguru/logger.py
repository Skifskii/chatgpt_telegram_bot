from loguru import logger

logger.add('logging_loguru/logfiles/logfile.log', format='{time} :: {level} :: {function} :: {message}', level='INFO', rotation='1 week', compression='zip')
