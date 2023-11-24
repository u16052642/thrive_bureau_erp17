# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import win32print

from thrive.addons.hw_drivers.interface import Interface

class PrinterInterface(Interface):
    _loop_delay = 30
    connection_type = 'printer'

    def get_devices(self):
        printer_devices = {}
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)

        for printer in printers:
            identifier = printer[2]
            handle_printer = win32print.OpenPrinter(identifier)
            win32print.GetPrinter(handle_printer, 2)
            printer_devices[identifier] = {
                'identifier': identifier,
                'printer_handle': handle_printer,
            }
        return printer_devices
