#String of text aligned left, right and center
import logging
def text_alignment():
    thickness = int(input())
    c = 'H'
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    # Top Cone
    for i in range(thickness):
        logging.info((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        logging.info((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        logging.info(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
