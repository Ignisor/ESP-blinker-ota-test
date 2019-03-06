from ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/Ignisor/ESP-blinker-ota-test')
    o.download_and_install_update_if_available('wombat_3', 'fantomas')


def check_for_updates():
    o = OTAUpdater('https://github.com/Ignisor/ESP-blinker-ota-test')
    OTAUpdater.using_network('wombat_3', 'fantomas')
    o.check_for_update_to_install_during_next_reboot()


def start():
    from main.blinker import blink

    blink()


download_and_install_update_if_available()
check_for_updates()
start()
