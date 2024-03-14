#String of text aligned left, right and center
import logging
def text_alignment():
    thickness = int(input())
    c = 'H'
    result = ""
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    # Top Cone
    for i in range(thickness):
        logging.info((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
        result += (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1) + "\n"
    # Top Pillars
    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        result += (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6) + "\n"

    # Middle Belt
    for i in range((thickness + 1) // 2):
        logging.info((c * thickness * 5).center(thickness * 6))
        result += (c * thickness * 5).center(thickness * 6) + "\n"

    # Bottom Pillars
    for i in range(thickness + 1):
        logging.info((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
        result += (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6) + "\n"

    # Bottom Cone
    for i in range(thickness):
        logging.info(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
        result += ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6) + "\n"
    return result