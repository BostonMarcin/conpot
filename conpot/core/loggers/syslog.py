# Copyright (C) 2013  Daniel creo Haslinger <creo-conpot@blackmesa.at>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from logging.handlers import SysLogHandler
import logging; from conpot.core.loggers.utils import create_extra
import socket

# from utils import AppFilter


class SysLogger(object):
    def __init__(self, host, port, facility, logdevice, logsocket):

        logger = logging.getLogger()
        # app_filter = AppFilter()
        # log_format = AppFilter().logformat()
        # formatter = logging.Formatter(log_format)

        if str(logsocket).lower() == 'udp':

            handler = SysLogHandler(address=(host, port),
                                    facility=getattr(SysLogHandler, 'LOG_' + str(facility).upper()),
                                    socktype=socket.SOCK_DGRAM)

        elif str(logsocket).lower() == 'dev':
            handler = SysLogHandler(logdevice)

        # handler.addFilter(app_filter)
        # handler.setFormatter(formatter)
        logger.addHandler(handler)

    def log(self, data):
        # stub function since the additional handler has been added to the root loggers instance.
        pass
