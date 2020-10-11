import asterisk.manager

import asterisk.manager

manager = asterisk.manager.Manager()
manager.connect("localhost")
manager.login('pyst2', '5kcn4MCVTk6qCrdq')

assert manager.connected()