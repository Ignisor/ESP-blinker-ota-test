from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/Ignisor/ESP-blinker-ota-test')
    o.download_and_install_update_if_available('wombat_3', 'fantomas')


def start():
    from main.blinker import blink

    blink()


def boot():
    download_and_install_update_if_available()
    start()
