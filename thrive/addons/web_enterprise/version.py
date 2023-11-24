# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import thrive

# ----------------------------------------------------------
# Monkey patch release to set the edition as 'enterprise'
# ----------------------------------------------------------
thrive.release.version_info = thrive.release.version_info[:5] + ('e',)
if '+e' not in thrive.release.version:     # not already patched by packaging
    thrive.release.version = '{0}+e{1}{2}'.format(*thrive.release.version.partition('-'))

thrive.service.common.RPC_VERSION_1.update(
    server_version=thrive.release.version,
    server_version_info=thrive.release.version_info)
