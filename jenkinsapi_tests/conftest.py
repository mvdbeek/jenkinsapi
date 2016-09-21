import logging


logging.basicConfig(
    format='%(module)s.%(funcName)s %(levelname)s: %(message)s',
    level=logging.INFO
)

modules = ['urllib3']
for module_name in modules:
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.WARNING)
