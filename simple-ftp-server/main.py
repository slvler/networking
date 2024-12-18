from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser('john', "123456")
checker.addUser('jane', "123456")
checker.addUser("j","123456")

portal = Portal(FTPRealm("./public", "./mysuers"), [AllowAnonymousAccess(), checker])

factory = FTPFactory(portal)

reactor.listenTCP(21, factory)
reactor.run()