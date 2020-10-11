import asterisk.manager

import asterisk.manager

manager = asterisk.manager.Manager()
manager.connect("172.25.0.101")
manager.login('pyst2', '5kcn4MCVTk6qCrdq')

assert manager.connected()