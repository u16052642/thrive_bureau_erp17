/** @thrive-module **/

export const session = thrive.__session_info__ || {};
delete thrive.__session_info__;
