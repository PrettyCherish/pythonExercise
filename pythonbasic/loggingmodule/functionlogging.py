# coding=utf-8
import logging


# 1.创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 2.创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

# 3.再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# 4.定义handler的输出格式（formatter）
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 5.给handler添加formatter
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 6.给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

# 记录异常traceback
try:
    open('luanluan.txt')
except(SystemExit, KeyboardInterrupt):
    raise
except FileNotFoundError as e:
    logger.error('Failed to open file', exc_info=False)

logger.debug("1")
logger.info("2")
logger.warning("3")
logger.error("4")
logger.critical("5")

'''
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息

'''