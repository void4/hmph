import actors
import builtin
import envs
import registry

L5 = envs.Env(parent=None)
L4 = envs.Env(parent=L5)
L39 = actors.Script(next_serial_id=1,
                    elements=[actors.Method(selector='send:',
                                            parameters=['message'],
                                            body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                   inner_map={}),
                                            serial_id=0)])
L44 = actors.Script(next_serial_id=3,
                    elements=[actors.Method(selector='first',
                                            parameters=[],
                                            body=actors.Expression(text='inbox get at: 1',
                                                                   inner_map={}),
                                            serial_id=0),
                              actors.Method(selector='removefirst',
                                            parameters=[],
                                            body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                   inner_map={}),
                                            serial_id=1),
                              actors.Method(selector='sender',
                                            parameters=[],
                                            body=actors.Expression(text='sender',
                                                                   inner_map={}),
                                            serial_id=2)])
L3 = actors.Actor(env=L4,
                  script=actors.Script(next_serial_id=1,
                                       elements=[actors.Method(selector='run',
                                                               parameters=[],
                                                               body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                      inner_map={'sender': L39,
                                                                                                 'mailbox': L44}),
                                                               serial_id=0)]))
L2 = actors.ActorEditor(actor=L3,
                        editable=True)
L56 = builtin.Stamp()
L55 = actors.ActorEditor(actor=L56,
                         editable=False)
L58 = actors.Script(next_serial_id=0,
                    elements=[])
L32 = builtin.MailDirectory(env=envs.Env(parent=L5))
L60 = actors.ActorEditor(actor=L32,
                         editable=False)
L63 = builtin.String(str='Is it a cat?')
L62 = actors.ActorEditor(actor=L63,
                         editable=False)
L65 = actors.Script(next_serial_id=0,
                    elements=[])
L68 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                           elements=[actors.Method(selector='not',
                                                                   parameters=[],
                                                                   body=actors.Expression(text='true',
                                                                                          inner_map={}),
                                                                   serial_id=0),
                                                     actors.Method(selector='iftrue:iffalse:',
                                                                   parameters=['truevalue',
                                                                               'falsevalue'],
                                                                   body=actors.Expression(text='falsevalue',
                                                                                          inner_map={}),
                                                                   serial_id=1)]),
                      value=False)
L67 = actors.ActorEditor(actor=L68,
                         editable=False)
L75 = actors.Script(next_serial_id=1,
                    elements=[actors.Method(selector='on:',
                                            parameters=['box'],
                                            body=actors.Expression(text='(box get) on: box',
                                                                   inner_map={}),
                                            serial_id=0)])
L85 = envs.Env(parent=None)
L84 = envs.Env(parent=L85)
L83 = envs.Env(parent=L84)
L82 = envs.Env(parent=L83)
L81 = envs.Env(parent=L82)
L269 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='question',
                                             parameters=[],
                                             body=actors.Expression(text='query',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='yes',
                                             parameters=[],
                                             body=actors.Expression(text='onyes\r\n',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='no',
                                             parameters=[],
                                             body=actors.Expression(text='onno\r\n',
                                                                    inner_map={}),
                                             serial_id=2)])
L79 = actors.Actor(env=envs.Env(parent=L81),
                   script=L269)
L282 = builtin.String(str='Thanks, I will remember.')
L96 = builtin.BoxMaker()
L284 = actors.ActorEditor(actor=L96,
                          editable=False)
L110 = envs.Env(parent=L84)
L141 = envs.Env(parent=L110)
L182 = envs.Env(parent=L141)
L181 = envs.Env(parent=L182)
L289 = envs.Env(parent=L181)
L155 = actors.Script(next_serial_id=3,
                     elements=[actors.Text(body="I'm out of ideas about your animal -- please tell me its name and a question to ask in the future, such that yes is the right answer for it.",
                                           serial_id=0),
                               actors.Method(selector='name:question:',
                                             parameters=['animal',
                                                         'question'],
                                             body=actors.Expression(text="node <- (makebranch on: question ifyes: (makebox holding: (makeguess for: animal)) ifno: (makebox holding: guessernode)).\r\n'Thanks, I will remember.'",
                                                                    inner_map={}),
                                             serial_id=2)])
L148 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='question',
                                             parameters=[],
                                             body=actors.Expression(text="'Is it a ' + animal + '?'",
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='yes',
                                             parameters=[],
                                             body=actors.Expression(text="'Wavy!'",
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='no',
                                             parameters=[],
                                             body=actors.Expression(text='make terminus',
                                                                    inner_map={'terminus': L155}),
                                             serial_id=2)])
L287 = actors.Actor(env=envs.Env(parent=L289),
                    script=L148)
L286 = actors.ActorEditor(actor=L287,
                          editable=True)
L86 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                           elements=[actors.Method(selector='not',
                                                                   parameters=[],
                                                                   body=actors.Expression(text='true',
                                                                                          inner_map={}),
                                                                   serial_id=0),
                                                     actors.Method(selector='iftrue:iffalse:',
                                                                   parameters=['truevalue',
                                                                               'falsevalue'],
                                                                   body=actors.Expression(text='falsevalue',
                                                                                          inner_map={}),
                                                                   serial_id=1)]),
                      value=False)
L108 = builtin.Box(initial_value=L86)
L293 = builtin.BoxMaker()
L292 = actors.ActorEditor(actor=L293,
                          editable=False)
L297 = envs.Env(parent=None)
L296 = envs.Env(parent=L297)
L343 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L347 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L331 = actors.Script(next_serial_id=0,
                     elements=[])
L351 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L331}),
                      serial_id=4)
L354 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L356 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L358 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L360 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L365 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L368 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L373 = actors.Example(expression=actors.Expression(text="maildirectory at: 'alice' put: mailbox sender",
                                                   inner_map={}),
                      serial_id=17)
L295 = actors.Actor(env=L296,
                    script=actors.Script(next_serial_id=18,
                                         elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L343,
                                                   L347,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L351,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L354,
                                                   L356,
                                                   L358,
                                                   L360,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L365,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L368,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15),
                                                   actors.Text(body="maildirectory at: 'alice' put: mailbox sender",
                                                               serial_id=16),
                                                   L373]))
L16 = builtin.BoxMaker()
L376 = actors.ActorEditor(actor=L16,
                          editable=False)
L379 = builtin.BoxMaker()
L378 = actors.ActorEditor(actor=L379,
                          editable=False)
L386 = envs.Env(parent=None)
L385 = envs.Env(parent=L386)
L384 = envs.Env(parent=L385)
L453 = actors.Script(next_serial_id=2,
                     elements=[actors.Method(selector='show',
                                             parameters=[],
                                             body=actors.Expression(text='name htmlescaped + \'="\' +value htmlescaped + \'"\'',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Text(body='XXX need to html-escape the strings',
                                           serial_id=1)])
L450 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='name:value:',
                                             parameters=['name',
                                                         'value'],
                                             body=actors.Expression(text='stringguard check: name.\r\nstringguard check: value.\r\nmake attribute',
                                                                    inner_map={'attribute': L453}),
                                             serial_id=0)])
L382 = actors.Actor(env=envs.Env(parent=L384),
                    script=L450)
L381 = actors.ActorEditor(actor=L382,
                          editable=True)
L508 = actors.Script(next_serial_id=0,
                     elements=[])
L511 = builtin.BoxMaker()
L510 = actors.ActorEditor(actor=L511,
                          editable=False)
L513 = builtin.Number(n=6.0)
L500 = builtin.Stamp()
L501 = builtin.StampGuard(stamp=L500)
L515 = actors.ActorEditor(actor=L501,
                          editable=False)
L418 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='show',
                                             parameters=[],
                                             body=actors.Expression(text="'<' + tag + (attributes foldr: showattr initially: '>')",
                                                                    inner_map={}),
                                             serial_id=0)])
L426 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='show',
                                             parameters=[],
                                             body=actors.Expression(text="'<' + tag + (attributes foldr: showattr initially: '>') + \r\n  (elements foldr: showattr initially: '') + \r\n  '</' + tag + '>'",
                                                                    inner_map={}),
                                             serial_id=0)])
L433 = actors.Script(next_serial_id=0,
                     elements=[])
L434 = actors.Script(next_serial_id=0,
                     elements=[])
L435 = actors.Script(next_serial_id=0,
                     elements=[])
L436 = actors.Script(next_serial_id=0,
                     elements=[])
L415 = actors.Script(next_serial_id=6,
                     elements=[actors.Method(selector='lonetag:attributes:',
                                             parameters=['tag',
                                                         'attributes'],
                                             body=actors.Expression(text='stringguard check: tag.\r\nlistguard check: attributes.\r\nhtmlstamp stamp: make element',
                                                                    inner_map={'element': L418}),
                                             serial_id=0),
                               actors.Text(body='XXX must check each attribute as well',
                                           serial_id=1),
                               actors.Method(selector='lonetag:',
                                             parameters=['tag'],
                                             body=actors.Expression(text='markup lonetag: tag attributes: []',
                                                                    inner_map={}),
                                             serial_id=2),
                               actors.Method(selector='tag:attributes:elements:',
                                             parameters=['tag',
                                                         'attributes',
                                                         'elements'],
                                             body=actors.Expression(text='stringguard check: tag.\r\nlistguard check: attributes.\r\nlistguard check: elements.\r\nhtmlstamp stamp: make element',
                                                                    inner_map={'element': L426}),
                                             serial_id=3),
                               actors.Method(selector='tag:elements:',
                                             parameters=['tag',
                                                         'elements'],
                                             body=actors.Expression(text='markup tag: tag attributes: [] elements: elements',
                                                                    inner_map={}),
                                             serial_id=4),
                               actors.Method(selector='coerce:',
                                             parameters=['object'],
                                             body=actors.Expression(text='if true: (htmlguard passes: object)\r\n   then: make onhtml\r\n   else: (if true: (listguard passes: object)\r\n               then: make onlist\r\n               else: (if true: (stringguard passes: object)\r\n                           then: make onstring\r\n                           else: make onerror))',
                                                                    inner_map={'onerror': L433,
                                                                               'onlist': L434,
                                                                               'onhtml': L435,
                                                                               'onstring': L436}),
                                             serial_id=5)])
L520 = builtin.Number(n=7.0)
L519 = actors.ActorEditor(actor=L520,
                          editable=False)
L251 = builtin.String(str='dog')
L522 = actors.ActorEditor(actor=L251,
                          editable=False)
L525 = builtin.Number(n=5.0)
L524 = actors.ActorEditor(actor=L525,
                          editable=False)
L276 = builtin.String(str='Does it meow?')
L529 = builtin.Number(n=25.0)
L528 = actors.ActorEditor(actor=L529,
                          editable=False)
L533 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L532 = builtin.Box(initial_value=L533)
L531 = actors.ActorEditor(actor=L532,
                          editable=False)
L541 = builtin.String(str='Hello, Alex!')
L540 = actors.ActorEditor(actor=L541,
                          editable=False)
L544 = builtin.String(str='Is it a dog?')
L543 = actors.ActorEditor(actor=L544,
                          editable=False)
L547 = builtin.Number(n=25.0)
L546 = actors.ActorEditor(actor=L547,
                          editable=False)
L550 = builtin.Number(n=5.0)
L549 = actors.ActorEditor(actor=L550,
                          editable=False)
L506 = actors.Script(next_serial_id=0,
                     elements=[])
L504 = actors.Actor(env=envs.Env(parent=L385),
                    script=L506)
L552 = actors.ActorEditor(actor=L504,
                          editable=True)
L558 = envs.Env(parent=None)
L557 = envs.Env(parent=L558)
L597 = actors.Script(next_serial_id=0,
                     elements=[])
L555 = actors.Actor(env=envs.Env(parent=L557),
                    script=L597)
L554 = actors.ActorEditor(actor=L555,
                          editable=True)
L603 = envs.Env(parent=None)
L602 = envs.Env(parent=L603)
L660 = actors.Script(next_serial_id=0,
                     elements=[])
L600 = actors.Actor(env=envs.Env(parent=L602),
                    script=L660)
L599 = actors.ActorEditor(actor=L600,
                          editable=True)
L119 = envs.Env(parent=L110)
L162 = envs.Env(parent=L119)
L161 = envs.Env(parent=L162)
L666 = envs.Env(parent=L161)
L126 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='question',
                                             parameters=[],
                                             body=actors.Expression(text='question',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='yes',
                                             parameters=[],
                                             body=actors.Expression(text='call on: yesbox',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='no',
                                             parameters=[],
                                             body=actors.Expression(text='call on: nobox',
                                                                    inner_map={}),
                                             serial_id=2)])
L664 = actors.Actor(env=envs.Env(parent=L666),
                    script=L126)
L663 = actors.ActorEditor(actor=L664,
                          editable=True)
L673 = envs.Env(parent=None)
L672 = envs.Env(parent=L673)
L725 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='greet',
                                             parameters=[],
                                             body=actors.Expression(text="'Hello, Alex! How are you?'",
                                                                    inner_map={}),
                                             serial_id=0)])
L670 = actors.Actor(env=envs.Env(parent=L672),
                    script=L725)
L669 = actors.ActorEditor(actor=L670,
                          editable=True)
L731 = envs.Env(parent=None)
L730 = actors.Actor(env=L731,
                    script=actors.Script(next_serial_id=0,
                                         elements=[]))
L729 = actors.ActorEditor(actor=L730,
                          editable=True)
L200 = envs.Env(parent=L181)
L199 = envs.Env(parent=L200)
L198 = actors.Actor(env=L199,
                    script=L148)
L763 = envs.Env(parent=None)
L762 = envs.Env(parent=L763)
L761 = envs.Env(parent=L762)
L783 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L759 = actors.Actor(env=envs.Env(parent=L761),
                    script=L783)
L758 = actors.ActorEditor(actor=L759,
                          editable=True)
L808 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L807 = actors.ActorEditor(actor=L808,
                          editable=False)
L816 = builtin.List(elements=(builtin.String(str='hello'),))
L815 = actors.ActorEditor(actor=L816,
                          editable=False)
L820 = builtin.Number(n=5.0)
L819 = actors.ActorEditor(actor=L820,
                          editable=False)
L227 = builtin.Box(initial_value=L79)
L822 = actors.ActorEditor(actor=L227,
                          editable=False)
L827 = envs.Env(parent=None)
L825 = builtin.MailDirectory(env=envs.Env(parent=L827))
L824 = actors.ActorEditor(actor=L825,
                          editable=False)
L764 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    body=actors.Expression(text='trueaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L851 = actors.ActorEditor(actor=L764,
                          editable=False)
L349 = builtin.Number(n=25.0)
L853 = actors.ActorEditor(actor=L349,
                          editable=False)
L178 = builtin.String(str='Does it meow?')
L336 = envs.Env(parent=L296)
L319 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L334 = actors.Actor(env=envs.Env(parent=L336),
                    script=L319)
L856 = actors.ActorEditor(actor=L334,
                          editable=True)
L862 = envs.Env(parent=L731)
L861 = envs.Env(parent=L862)
L871 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L859 = actors.Actor(env=envs.Env(parent=L861),
                    script=L871)
L858 = actors.ActorEditor(actor=L859,
                          editable=True)
L898 = builtin.Number(n=5.0)
L902 = envs.Env(parent=L827)
L926 = actors.Example(expression=actors.Expression(text='1 * 2 * 3 * 4 * 5',
                                                   inner_map={}),
                      serial_id=0)
L925 = actors.Script(next_serial_id=1,
                     elements=[L926])
L900 = actors.Actor(env=envs.Env(parent=L902),
                    script=L925)
L932 = builtin.List(elements=(builtin.String(str='hello'),))
L931 = actors.ActorEditor(actor=L932,
                          editable=False)
L908 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L911 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L904 = actors.Actor(env=L902,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L908,
                                                                                                   'mailbox': L911}),
                                                                 serial_id=0)]))
L935 = actors.ActorEditor(actor=L904,
                          editable=True)
L559 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    body=actors.Expression(text='falseaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L573 = builtin.Box(initial_value=L559)
L937 = actors.ActorEditor(actor=L573,
                          editable=False)
L942 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=1)
L945 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                   inner_map={}),
                      serial_id=2)
L31 = actors.Script(next_serial_id=0,
                    elements=[])
L949 = actors.Example(expression=actors.Expression(text='make Foo',
                                                   inner_map={'Foo': L31}),
                      serial_id=4)
L952 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                   inner_map={}),
                      serial_id=6)
L954 = actors.Example(expression=actors.Expression(text='box get',
                                                   inner_map={}),
                      serial_id=7)
L956 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                   inner_map={}),
                      serial_id=8)
L958 = actors.Example(expression=actors.Expression(text="['hello']",
                                                   inner_map={}),
                      serial_id=9)
L963 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                   inner_map={}),
                      serial_id=11)
L966 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                   inner_map={}),
                      serial_id=13)
L970 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                   inner_map={}),
                      serial_id=16)
L939 = actors.Actor(env=L4,
                    script=actors.Script(next_serial_id=17,
                                         elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                               serial_id=0),
                                                   L942,
                                                   L945,
                                                   actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                               serial_id=3),
                                                   L949,
                                                   actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                               serial_id=5),
                                                   L952,
                                                   L954,
                                                   L956,
                                                   L958,
                                                   actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                               serial_id=10),
                                                   L963,
                                                   actors.Text(body='You can create your own mailbox:',
                                                               serial_id=12),
                                                   L966,
                                                   actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                               serial_id=14),
                                                   actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                               serial_id=15),
                                                   L970]))
L113 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='run',
                                             parameters=[],
                                             body=actors.Expression(text='call on: root',
                                                                    inner_map={}),
                                             serial_id=0)])
L111 = actors.Actor(env=envs.Env(parent=L110),
                    script=L113)
L975 = actors.ActorEditor(actor=L111,
                          editable=True)
L978 = builtin.String(str='Is it a dog?')
L982 = envs.Env(parent=None)
L981 = actors.Actor(env=L982,
                    script=actors.Script(next_serial_id=0,
                                         elements=[]))
L980 = actors.ActorEditor(actor=L981,
                          editable=True)
L329 = actors.Actor(env=envs.Env(parent=L296),
                    script=L331)
L999 = actors.ActorEditor(actor=L329,
                          editable=True)
L1002 = builtin.String(str='Thanks, I will remember.')
L1001 = actors.ActorEditor(actor=L1002,
                           editable=False)
L1006 = builtin.String(str='hello world!')
L1005 = actors.ActorEditor(actor=L1006,
                           editable=False)
L960 = builtin.List(elements=(builtin.String(str='hello'),))
L1008 = actors.ActorEditor(actor=L960,
                           editable=False)
L212 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L215 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L208 = actors.Actor(env=L84,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L212,
                                                                                                   'mailbox': L215}),
                                                                 serial_id=0)]))
L1010 = actors.ActorEditor(actor=L208,
                           editable=True)
L1013 = actors.Actor(env=L603,
                     script=actors.Script(next_serial_id=0,
                                          elements=[]))
L839 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L1016 = actors.ActorEditor(actor=L839,
                           editable=False)
L492 = envs.Env(parent=L385)
L483 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L490 = actors.Actor(env=envs.Env(parent=L492),
                    script=L483)
L1018 = actors.ActorEditor(actor=L490,
                           editable=True)
L1020 = builtin.String(str='Is it a cat?')
L437 = actors.Actor(env=envs.Env(parent=L384),
                    script=L415)
L655 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='run',
                                             parameters=[],
                                             body=actors.Expression(text='let ballotbox = makebox holding: 0',
                                                                    inner_map={}),
                                             serial_id=0)])
L653 = actors.Actor(env=envs.Env(parent=L602),
                    script=L655)
L1023 = actors.ActorEditor(actor=L653,
                           editable=True)
L828 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L1025 = actors.ActorEditor(actor=L828,
                           editable=False)
L1027 = actors.ActorEditor(actor=L978,
                           editable=False)
L1030 = builtin.List(elements=(builtin.String(str='hello'),))
L1029 = actors.ActorEditor(actor=L1030,
                           editable=False)
L145 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='on:',
                                             parameters=['node'],
                                             body=actors.Expression(text='make guesser',
                                                                    inner_map={'guesser': L148}),
                                             serial_id=0)])
L180 = actors.Actor(env=L181,
                    script=L145)
L179 = builtin.Box(initial_value=L180)
L1033 = actors.ActorEditor(actor=L179,
                           editable=False)
L502 = actors.StampedActor(actor=builtin.String(str='hello'),
                           stamp=L500)
L1037 = builtin.String(str='Is it a dog?')
L1036 = actors.ActorEditor(actor=L1037,
                           editable=False)
L1040 = builtin.BoxMaker()
L1039 = actors.ActorEditor(actor=L1040,
                           editable=False)
L692 = envs.Env(parent=L672)
L695 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L693 = actors.Actor(env=envs.Env(parent=L692),
                    script=L695)
L1044 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                             elements=[actors.Method(selector='not',
                                                                     parameters=[],
                                                                     body=actors.Expression(text='false',
                                                                                            inner_map={}),
                                                                     serial_id=0),
                                                       actors.Method(selector='iftrue:iffalse:',
                                                                     parameters=['truevalue',
                                                                                 'falsevalue'],
                                                                     body=actors.Expression(text='truevalue',
                                                                                            inner_map={}),
                                                                     serial_id=1)]),
                        value=True)
L1043 = actors.ActorEditor(actor=L1044,
                           editable=False)
L400 = builtin.TypeGuard(sample_instance=())
L1051 = actors.ActorEditor(actor=L400,
                           editable=False)
L116 = actors.Actor(env=envs.Env(parent=L110),
                    script=L75)
L322 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L339 = actors.Actor(env=envs.Env(parent=L336),
                    script=L322)
L1054 = actors.ActorEditor(actor=L339,
                           editable=True)
L404 = actors.Example(expression=actors.Expression(text='let stamppair = makestamp run',
                                                   inner_map={}),
                      serial_id=0)
L409 = actors.Example(expression=actors.Expression(text='let htmlstamp = stamppair at: 1',
                                                   inner_map={}),
                      serial_id=1)
L411 = actors.Example(expression=actors.Expression(text='let htmlguard = stamppair at: 2',
                                                   inner_map={}),
                      serial_id=2)
L413 = actors.Example(expression=actors.Expression(text='make markup',
                                                   inner_map={'markup': L415}),
                      serial_id=4)
L441 = actors.Script(next_serial_id=2,
                     elements=[actors.Method(selector='p',
                                             parameters=[],
                                             body=actors.Expression(text="markup lonetag: 'p'",
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='blockquote:',
                                             parameters=['elements'],
                                             body=actors.Expression(text="markup tag: 'blockquote' elements: elements",
                                                                    inner_map={}),
                                             serial_id=1)])
L439 = actors.Example(expression=actors.Expression(text='make html',
                                                   inner_map={'html': L441}),
                      serial_id=5)
L448 = actors.Example(expression=actors.Expression(text='make makeattr',
                                                   inner_map={'makeattr': L450}),
                      serial_id=8)
L459 = actors.Script(next_serial_id=2,
                     elements=[actors.Method(selector='left:right:',
                                             parameters=['attribute',
                                                         'string'],
                                             body=actors.Expression(text="' ' + attribute show + string",
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Text(body='XXX rename this since it generically applies to html elements',
                                           serial_id=1)])
L457 = actors.Example(expression=actors.Expression(text='make showattr',
                                                   inner_map={'showattr': L459}),
                      serial_id=9)
L465 = actors.Example(expression=actors.Expression(text='html p show',
                                                   inner_map={}),
                      serial_id=12)
L468 = actors.Example(expression=actors.Expression(text='(html blockquote: []) show',
                                                   inner_map={}),
                      serial_id=14)
L471 = actors.Example(expression=actors.Expression(text='(html blockquote: [html p]) show',
                                                   inner_map={}),
                      serial_id=15)
L474 = actors.Example(expression=actors.Expression(text="(html blockquote: ['hello']) show",
                                                   inner_map={}),
                      serial_id=16)
L403 = actors.Script(next_serial_id=17,
                     elements=[L404,
                               L409,
                               L411,
                               L413,
                               L439,
                               L448,
                               L457,
                               L465,
                               L468,
                               L471,
                               L474])
L402 = actors.Actor(env=L384,
                    script=L403)
L406 = actors.ActorEditor(actor=L402,
                          editable=True)
L1064 = envs.Env(parent=None)
L1063 = envs.Env(parent=L1064)
L1062 = envs.Env(parent=L1063)
L1095 = actors.Script(next_serial_id=3,
                      elements=[actors.Method(selector='first',
                                              parameters=[],
                                              body=actors.Expression(text='inbox get at: 1',
                                                                     inner_map={}),
                                              serial_id=0),
                                actors.Method(selector='removefirst',
                                              parameters=[],
                                              body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                     inner_map={}),
                                              serial_id=1),
                                actors.Method(selector='sender',
                                              parameters=[],
                                              body=actors.Expression(text='sender',
                                                                     inner_map={}),
                                              serial_id=2)])
L1060 = actors.Actor(env=envs.Env(parent=L1062),
                     script=L1095)
L1059 = actors.ActorEditor(actor=L1060,
                           editable=True)
L1115 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1118 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L803 = actors.Script(next_serial_id=0,
                     elements=[])
L1121 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L803}),
                       serial_id=4)
L1124 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1126 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1128 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1130 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1135 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1138 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1142 = actors.Example(expression=actors.Expression(text='let tome = mailbox sender',
                                                    inner_map={}),
                       serial_id=16)
L799 = actors.Script(next_serial_id=1,
                     elements=[actors.Text(body='Hi me, how are me?\r\n',
                                           serial_id=0)])
L1144 = actors.Example(expression=actors.Expression(text='tome send: make message',
                                                    inner_map={'message': L799}),
                       serial_id=17)
L1163 = actors.Example(expression=actors.Expression(text='2 * 3',
                                                    inner_map={}),
                       serial_id=18)
L1166 = actors.Example(expression=actors.Expression(text='2 / 0',
                                                    inner_map={}),
                       serial_id=19)
L1168 = actors.Example(expression=actors.Expression(text='let pair = makestamp run',
                                                    inner_map={}),
                       serial_id=20)
L1112 = actors.Actor(env=L762,
                     script=actors.Script(next_serial_id=21,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1115,
                                                    L1118,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1121,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1124,
                                                    L1126,
                                                    L1128,
                                                    L1130,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1135,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1138,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1142,
                                                    L1144,
                                                    L1163,
                                                    L1166,
                                                    L1168]))
L1111 = actors.ActorEditor(actor=L1112,
                           editable=True)
L346 = builtin.Number(n=5.0)
L1173 = actors.ActorEditor(actor=L346,
                           editable=False)
L1176 = builtin.Number(n=42.0)
L1175 = builtin.Box(initial_value=L1176)
L1178 = actors.Actor(env=L673,
                     script=actors.Script(next_serial_id=0,
                                          elements=[]))
L36 = envs.Env(parent=L4)
L34 = actors.Actor(env=envs.Env(parent=L36),
                   script=L44)
L1181 = actors.ActorEditor(actor=L34,
                           editable=True)
L1184 = builtin.Number(n=5.0)
L1183 = actors.ActorEditor(actor=L1184,
                           editable=False)
L266 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='asking:ifyes:ifno:',
                                             parameters=['query',
                                                         'onyes',
                                                         'onno'],
                                             body=actors.Expression(text='make yesnoquestion\r\n',
                                                                    inner_map={'yesnoquestion': L269}),
                                             serial_id=2)])
L265 = actors.Actor(env=L82,
                    script=L266)
L123 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='on:',
                                             parameters=['node'],
                                             body=actors.Expression(text='make asker',
                                                                    inner_map={'asker': L126}),
                                             serial_id=0)])
L245 = envs.Env(parent=L83)
L250 = envs.Env(parent=L245)
L249 = envs.Env(parent=L250)
L240 = actors.Script(next_serial_id=2,
                     elements=[actors.Text(body="I'm out of guesses about your animal.  Please tell me its name and a new question I can ask, so that your animal has a yes answer.  Thanks!",
                                           serial_id=0),
                               actors.Method(selector='name:question:',
                                             parameters=['animal',
                                                         'question'],
                                             body=actors.Expression(text="box <- (makequestion asking: question ifyes: (makeguess name: animal parent: box) ifno: (box get)).\r\n'OK!'\r\n",
                                                                    inner_map={}),
                                             serial_id=1)])
L233 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='run',
                                             parameters=[],
                                             body=actors.Expression(text="'Is it a ' + animal + '?'\r\n",
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='yes',
                                             parameters=[],
                                             body=actors.Expression(text="'Thank you!'\r\n",
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='no',
                                             parameters=[],
                                             body=actors.Expression(text='make question',
                                                                    inner_map={'question': L240}),
                                             serial_id=2)])
L248 = actors.Actor(env=L249,
                    script=L233)
L1188 = actors.ActorEditor(actor=L248,
                           editable=True)
L920 = envs.Env(parent=L902)
L918 = actors.Actor(env=envs.Env(parent=L920),
                    script=L911)
L1190 = actors.ActorEditor(actor=L918,
                           editable=True)
L280 = builtin.String(str='cat')
L1192 = actors.ActorEditor(actor=L280,
                           editable=False)
L1195 = actors.ActorEditor(actor=L108,
                           editable=False)
L770 = builtin.BoxMaker()
L1198 = actors.ActorEditor(actor=L770,
                           editable=False)
L1202 = envs.Env(parent=L82)
L1205 = actors.Script(next_serial_id=0,
                      elements=[])
L1200 = actors.Actor(env=envs.Env(parent=L1202),
                     script=L1205)
L678 = builtin.BoxMaker()
L1207 = actors.ActorEditor(actor=L678,
                           editable=False)
L592 = envs.Env(parent=L557)
L581 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L590 = actors.Actor(env=envs.Env(parent=L592),
                    script=L581)
L1210 = actors.ActorEditor(actor=L590,
                           editable=True)
L743 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L1212 = actors.ActorEditor(actor=L743,
                           editable=False)
L888 = builtin.MailDirectory(env=envs.Env(parent=L731))
L1214 = actors.ActorEditor(actor=L888,
                           editable=False)
L893 = builtin.Box(initial_value=builtin.List(elements=()))
L1216 = actors.ActorEditor(actor=L893,
                           editable=False)
L1218 = actors.ActorEditor(actor=L437,
                           editable=True)
L463 = actors.Actor(env=envs.Env(parent=L384),
                    script=L459)
L1075 = builtin.BoxMaker()
L1222 = actors.ActorEditor(actor=L1075,
                           editable=False)
L37 = actors.Actor(env=envs.Env(parent=L36),
                   script=L39)
L1224 = actors.ActorEditor(actor=L37,
                           editable=True)
L1227 = builtin.Number(n=25.0)
L1226 = actors.ActorEditor(actor=L1227,
                           editable=False)
L1230 = builtin.Number(n=0.0)
L1232 = actors.ActorEditor(actor=L79,
                           editable=True)
L133 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='question',
                                             parameters=[],
                                             body=actors.Expression(text='question',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='yes',
                                             parameters=[],
                                             body=actors.Expression(text='call on: yesbox',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='no',
                                             parameters=[],
                                             body=actors.Expression(text='call on: nobox',
                                                                    inner_map={}),
                                             serial_id=2)])
L1238 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1242 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L892 = actors.Script(next_serial_id=0,
                     elements=[])
L1246 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L892}),
                       serial_id=4)
L1249 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1251 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1253 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1255 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1260 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1263 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L885 = actors.Script(next_serial_id=0,
                     elements=[])
L1267 = actors.Example(expression=actors.Expression(text='mailbox sender send: make message',
                                                    inner_map={'message': L885}),
                       serial_id=16)
L1235 = actors.Actor(env=L862,
                     script=actors.Script(next_serial_id=17,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1238,
                                                    L1242,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1246,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1249,
                                                    L1251,
                                                    L1253,
                                                    L1255,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1260,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1263,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1267]))
L1270 = builtin.String(str='hello')
L708 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L690 = actors.Actor(env=envs.Env(parent=L692),
                    script=L708)
L1272 = actors.ActorEditor(actor=L690,
                           editable=True)
L160 = actors.Actor(env=L161,
                    script=L123)
L159 = builtin.Box(initial_value=L160)
L1274 = actors.ActorEditor(actor=L159,
                           editable=False)
L1280 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1282 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1285 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L660}),
                       serial_id=4)
L1288 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1290 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1292 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1294 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1299 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1302 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L647 = actors.Script(next_serial_id=2,
                     elements=[actors.Text(body='Hi - time to vote on where to go out for lunch.  Pick a method for the restaurant you like and click it.',
                                           serial_id=0),
                               actors.Method(selector='voteforstarbucks',
                                             parameters=[],
                                             body=actors.Expression(text='',
                                                                    inner_map={}),
                                             serial_id=1)])
L1306 = actors.Example(expression=actors.Expression(text='mailbox sender send: make message',
                                                    inner_map={'message': L647}),
                       serial_id=16)
L1308 = actors.Example(expression=actors.Expression(text='makek makeballot',
                                                    inner_map={}),
                       serial_id=17)
L1310 = actors.Example(expression=actors.Expression(text='make makeballot',
                                                    inner_map={'makeballot': L655}),
                       serial_id=18)
L1277 = actors.Actor(env=L602,
                     script=actors.Script(next_serial_id=19,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1280,
                                                    L1282,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1285,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1288,
                                                    L1290,
                                                    L1292,
                                                    L1294,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1299,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1302,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1306,
                                                    L1308,
                                                    L1310]))
L1276 = actors.ActorEditor(actor=L1277,
                           editable=True)
L1316 = envs.Env(parent=L199)
L1314 = actors.Actor(env=envs.Env(parent=L1316),
                     script=L155)
L1313 = actors.ActorEditor(actor=L1314,
                           editable=True)
L679 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L1318 = actors.ActorEditor(actor=L679,
                           editable=False)
L868 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L895 = actors.Actor(env=envs.Env(parent=L861),
                    script=L868)
L1320 = actors.ActorEditor(actor=L895,
                           editable=True)
L890 = actors.Actor(env=envs.Env(parent=L862),
                    script=L892)
L1322 = actors.ActorEditor(actor=L890,
                           editable=True)
L176 = envs.Env(parent=L141)
L175 = envs.Env(parent=L176)
L1328 = envs.Env(parent=L175)
L1327 = envs.Env(parent=L1328)
L1326 = envs.Env(parent=L1327)
L1324 = actors.Actor(env=envs.Env(parent=L1326),
                     script=L155)
L658 = builtin.MailDirectory(env=envs.Env(parent=L603))
L1331 = actors.ActorEditor(actor=L658,
                           editable=False)
L1339 = envs.Env(parent=None)
L1338 = envs.Env(parent=L1339)
L1373 = actors.Script(next_serial_id=0,
                      elements=[])
L1336 = actors.Actor(env=envs.Env(parent=L1338),
                     script=L1373)
L1335 = actors.ActorEditor(actor=L1336,
                           editable=True)
L1378 = actors.Script(next_serial_id=0,
                      elements=[])
L1376 = actors.Actor(env=envs.Env(parent=L384),
                     script=L1378)
L1375 = actors.ActorEditor(actor=L1376,
                           editable=True)
L333 = envs.Env(parent=L297)
L332 = builtin.MailDirectory(env=L333)
L1380 = actors.ActorEditor(actor=L332,
                           editable=False)
L1383 = actors.ActorEditor(actor=L282,
                           editable=False)
L337 = builtin.Box(initial_value=builtin.List(elements=()))
L1385 = actors.ActorEditor(actor=L337,
                           editable=False)
L797 = actors.Actor(env=envs.Env(parent=L762),
                    script=L799)
L1387 = actors.ActorEditor(actor=L797,
                           editable=True)
L279 = envs.Env(parent=L245)
L278 = envs.Env(parent=L279)
L1391 = envs.Env(parent=L278)
L1389 = actors.Actor(env=envs.Env(parent=L1391),
                     script=L240)
L1393 = builtin.List(elements=(L1270,))
L473 = builtin.String(str='<blockquote> <p></blockquote>')
L1395 = actors.ActorEditor(actor=L473,
                           editable=False)
L185 = actors.Example(expression=actors.Expression(text='make call',
                                                   inner_map={'call': L75}),
                      serial_id=0)
L120 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='on:ifyes:ifno:',
                                             parameters=['question',
                                                         'yesbox',
                                                         'nobox'],
                                             body=actors.Expression(text='make askernode\r\n',
                                                                    inner_map={'askernode': L123,
                                                                               'asker': L133}),
                                             serial_id=0)])
L188 = actors.Example(expression=actors.Expression(text='make makebranch',
                                                   inner_map={'makebranch': L120}),
                      serial_id=1)
L142 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='for:',
                                             parameters=['animal'],
                                             body=actors.Expression(text='make guessernode',
                                                                    inner_map={'guesser': L58,
                                                                               'guessernode': L145}),
                                             serial_id=0)])
L190 = actors.Example(expression=actors.Expression(text='make makeguess',
                                                   inner_map={'makeguess': L142}),
                      serial_id=2)
L192 = actors.Example(expression=actors.Expression(text="let root = box holding: (makeguess for: 'dog')",
                                                   inner_map={}),
                      serial_id=3)
L194 = actors.Example(expression=actors.Expression(text="let root = makebox holding: (makeguess for: 'dog')",
                                                   inner_map={}),
                      serial_id=4)
L196 = actors.Example(expression=actors.Expression(text='call on: root',
                                                   inner_map={}),
                      serial_id=6)
L201 = actors.Example(expression=actors.Expression(text='call on: root',
                                                   inner_map={}),
                      serial_id=7)
L206 = actors.Example(expression=actors.Expression(text='make playgame',
                                                   inner_map={'playgame': L113}),
                      serial_id=8)
L184 = actors.Script(next_serial_id=9,
                     elements=[L185,
                               L188,
                               L190,
                               L192,
                               L194,
                               L196,
                               L201,
                               L206])
L1399 = builtin.String(str='Is it a dog?')
L1398 = actors.ActorEditor(actor=L1399,
                           editable=False)
L804 = builtin.Box(initial_value=builtin.List(elements=()))
L742 = builtin.BoxMaker()
L1402 = actors.ActorEditor(actor=L742,
                           editable=False)
L1117 = builtin.Number(n=5.0)
L1405 = actors.ActorEditor(actor=L1117,
                           editable=False)
L786 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L793 = actors.Actor(env=envs.Env(parent=L761),
                    script=L786)
L29 = actors.Actor(env=envs.Env(parent=L4),
                   script=L31)
L1408 = actors.ActorEditor(actor=L29,
                           editable=True)
L1065 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                             elements=[actors.Method(selector='not',
                                                                     parameters=[],
                                                                     body=actors.Expression(text='true',
                                                                                            inner_map={}),
                                                                     serial_id=0),
                                                       actors.Method(selector='iftrue:iffalse:',
                                                                     parameters=['truevalue',
                                                                                 'falsevalue'],
                                                                     body=actors.Expression(text='falsevalue',
                                                                                            inner_map={}),
                                                                     serial_id=1)]),
                        value=False)
L1410 = actors.ActorEditor(actor=L1065,
                           editable=False)
L1412 = actors.ActorEditor(actor=L559,
                           editable=False)
L630 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L633 = actors.Script(next_serial_id=3,
                     elements=[actors.Method(selector='first',
                                             parameters=[],
                                             body=actors.Expression(text='inbox get at: 1',
                                                                    inner_map={}),
                                             serial_id=0),
                               actors.Method(selector='removefirst',
                                             parameters=[],
                                             body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                    inner_map={}),
                                             serial_id=1),
                               actors.Method(selector='sender',
                                             parameters=[],
                                             body=actors.Expression(text='sender',
                                                                    inner_map={}),
                                             serial_id=2)])
L626 = actors.Actor(env=L602,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L630,
                                                                                                   'mailbox': L633}),
                                                                 serial_id=0)]))
L1414 = actors.ActorEditor(actor=L626,
                           editable=True)
L1420 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1424 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1428 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L725}),
                       serial_id=4)
L1431 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1433 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1435 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1437 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1442 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1445 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1449 = actors.Example(expression=actors.Expression(text="'hello alex' size",
                                                    inner_map={}),
                       serial_id=16)
L1451 = actors.Example(expression=actors.Expression(text="'hello alex' length",
                                                    inner_map={}),
                       serial_id=17)
L1454 = actors.Example(expression=actors.Expression(text='let sender = mailbox sender',
                                                    inner_map={}),
                       serial_id=18)
L706 = actors.Script(next_serial_id=1,
                     elements=[actors.Text(body='Hi, there.  ',
                                           serial_id=0)])
L1456 = actors.Example(expression=actors.Expression(text='sender send: make message',
                                                    inner_map={'message': L706}),
                       serial_id=19)
L720 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='votemcdonalds',
                                             parameters=[],
                                             body=actors.Expression(text='votesformcdonalds <- (votesformcdonalds get + 1)',
                                                                    inner_map={}),
                                             serial_id=0)])
L717 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='run',
                                             parameters=[],
                                             body=actors.Expression(text='let votesformcdonalds = makebox holding: 0.\r\nmake ballot',
                                                                    inner_map={'ballot': L720}),
                                             serial_id=0)])
L1458 = actors.Example(expression=actors.Expression(text='make makeballot',
                                                    inner_map={'makeballot': L717}),
                       serial_id=20)
L1417 = actors.Actor(env=L672,
                     script=actors.Script(next_serial_id=21,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1420,
                                                    L1424,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1428,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1431,
                                                    L1433,
                                                    L1435,
                                                    L1437,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1442,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1445,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1449,
                                                    L1451,
                                                    L1454,
                                                    L1456,
                                                    L1458]))
L1461 = actors.ActorEditor(actor=L180,
                           editable=True)
L470 = builtin.String(str='<blockquote></blockquote>')
L1464 = actors.ActorEditor(actor=L470,
                           editable=False)
L345 = actors.ActorEditor(actor=L295,
                          editable=True)
L1241 = builtin.Number(n=5.0)
L1467 = actors.ActorEditor(actor=L1241,
                           editable=False)
L1423 = builtin.Number(n=5.0)
L1475 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1478 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1482 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L506}),
                       serial_id=4)
L1485 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1487 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1489 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1491 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1494 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1497 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1501 = actors.Example(expression=actors.Expression(text='make htmlmodule',
                                                    inner_map={'htmlmodule': L403}),
                       serial_id=25)
L1472 = actors.Actor(env=L385,
                     script=actors.Script(next_serial_id=26,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1475,
                                                    L1478,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1482,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1485,
                                                    L1487,
                                                    L1489,
                                                    L1491,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1494,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1497,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1501]))
L1471 = actors.ActorEditor(actor=L1472,
                           editable=True)
L1505 = actors.ActorEditor(actor=L793,
                           editable=True)
L880 = envs.Env(parent=L862)
L878 = actors.Actor(env=envs.Env(parent=L880),
                    script=L871)
L1507 = actors.ActorEditor(actor=L878,
                           editable=True)
L118 = actors.Actor(env=L119,
                    script=L120)
L715 = actors.Actor(env=envs.Env(parent=L672),
                    script=L717)
L224 = actors.Example(expression=actors.Expression(text='let gamebox = makebox holding: 0',
                                                   inner_map={}),
                      serial_id=1)
L230 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='name:parent:',
                                             parameters=['animal',
                                                         'box'],
                                             body=actors.Expression(text='make guess\r\n',
                                                                    inner_map={'guess': L233}),
                                             serial_id=0)])
L228 = actors.Example(expression=actors.Expression(text='make makeguess',
                                                   inner_map={'makeguess': L230}),
                      serial_id=2)
L246 = actors.Example(expression=actors.Expression(text="makeguess name: 'dog' parent: gamebox",
                                                   inner_map={}),
                      serial_id=3)
L252 = actors.Example(expression=actors.Expression(text='gamebox get',
                                                   inner_map={}),
                      serial_id=4)
L223 = actors.Script(next_serial_id=5,
                     elements=[L224,
                               L228,
                               L246,
                               L252])
L222 = actors.Actor(env=L83,
                    script=L223)
L226 = actors.ActorEditor(actor=L222,
                          editable=True)
L314 = builtin.Box(initial_value=L68)
L1512 = actors.ActorEditor(actor=L314,
                           editable=False)
L704 = actors.Actor(env=envs.Env(parent=L672),
                    script=L706)
L109 = actors.Actor(env=L110,
                    script=L184)
L187 = actors.ActorEditor(actor=L109,
                          editable=True)
L6 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                          elements=[actors.Method(selector='not',
                                                                  parameters=[],
                                                                  body=actors.Expression(text='true',
                                                                                         inner_map={}),
                                                                  serial_id=0),
                                                    actors.Method(selector='iftrue:iffalse:',
                                                                  parameters=['truevalue',
                                                                              'falsevalue'],
                                                                  body=actors.Expression(text='falsevalue',
                                                                                         inner_map={}),
                                                                  serial_id=1)]),
                     value=False)
L1518 = actors.ActorEditor(actor=L6,
                           editable=False)
L923 = actors.Actor(env=envs.Env(parent=L920),
                    script=L908)
L1520 = actors.ActorEditor(actor=L923,
                           editable=True)
L97 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                           elements=[actors.Method(selector='not',
                                                                   parameters=[],
                                                                   body=actors.Expression(text='false',
                                                                                          inner_map={}),
                                                                   serial_id=0),
                                                     actors.Method(selector='iftrue:iffalse:',
                                                                   parameters=['truevalue',
                                                                               'falsevalue'],
                                                                   body=actors.Expression(text='truevalue',
                                                                                          inner_map={}),
                                                                   serial_id=1)]),
                      value=True)
L1522 = actors.ActorEditor(actor=L97,
                           editable=False)
L1528 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1530 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1533 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L597}),
                       serial_id=4)
L1536 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1538 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1540 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1542 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1545 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1548 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1552 = actors.Example(expression=actors.Expression(text='let pair = makestamp run',
                                                    inner_map={}),
                       serial_id=16)
L1525 = actors.Actor(env=L557,
                     script=actors.Script(next_serial_id=17,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1528,
                                                    L1530,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1533,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1536,
                                                    L1538,
                                                    L1540,
                                                    L1542,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1545,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1548,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1552]))
L1524 = actors.ActorEditor(actor=L1525,
                           editable=True)
L499 = builtin.List(elements=(L500,
                              L501))
L1556 = actors.ActorEditor(actor=L499,
                           editable=False)
L1560 = builtin.String(str='Thank you!')
L1559 = actors.ActorEditor(actor=L1560,
                           editable=False)
L1562 = builtin.String(str='hello world!hello world!')
L480 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L476 = actors.Actor(env=L385,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L480,
                                                                                                   'mailbox': L483}),
                                                                 serial_id=0)]))
L1564 = actors.ActorEditor(actor=L476,
                           editable=True)
L263 = actors.Actor(env=envs.Env(parent=L84),
                    script=L65)
L1566 = actors.ActorEditor(actor=L263,
                           editable=True)
L1571 = builtin.Number(n=25.0)
L1570 = actors.ActorEditor(actor=L1571,
                           editable=False)
L172 = builtin.String(str='Is it easily frightened?')
L1573 = actors.ActorEditor(actor=L172,
                           editable=False)
L1576 = actors.ActorEditor(actor=L1423,
                           editable=False)
L1581 = envs.Env(parent=L249)
L1579 = actors.Actor(env=envs.Env(parent=L1581),
                     script=L240)
L1578 = actors.ActorEditor(actor=L1579,
                           editable=True)
L1583 = actors.ActorEditor(actor=L502,
                           editable=False)
L205 = envs.Env(parent=L161)
L203 = actors.Actor(env=envs.Env(parent=L205),
                    script=L126)
L1585 = actors.ActorEditor(actor=L203,
                           editable=True)
L1588 = actors.ActorEditor(actor=L1393,
                           editable=False)
L261 = builtin.MailDirectory(env=envs.Env(parent=L85))
L1590 = actors.ActorEditor(actor=L261,
                           editable=False)
L1426 = builtin.Number(n=25.0)
L1592 = actors.ActorEditor(actor=L1426,
                           editable=False)
L1477 = builtin.Number(n=5.0)
L1594 = actors.ActorEditor(actor=L1477,
                           editable=False)
L166 = envs.Env(parent=L119)
L165 = envs.Env(parent=L166)
L164 = actors.Actor(env=L165,
                    script=L123)
L163 = builtin.Box(initial_value=L164)
L1599 = actors.ActorEditor(actor=L163,
                           editable=False)
L864 = actors.Actor(env=L862,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L868,
                                                                                                   'mailbox': L871}),
                                                                 serial_id=0)]))
L1601 = actors.ActorEditor(actor=L864,
                           editable=True)
L1603 = builtin.String(str='OK!')
L387 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    body=actors.Expression(text='falseaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L1607 = actors.ActorEditor(actor=L387,
                           editable=False)
L256 = envs.Env(parent=L84)
L254 = actors.Actor(env=envs.Env(parent=L256),
                    script=L215)
L1609 = actors.ActorEditor(actor=L254,
                           editable=True)
L497 = builtin.MailDirectory(env=envs.Env(parent=L386))
L1611 = actors.ActorEditor(actor=L497,
                           editable=False)
L1616 = envs.Env(parent=L165)
L1614 = actors.Actor(env=envs.Env(parent=L1616),
                     script=L126)
L1613 = actors.ActorEditor(actor=L1614,
                           editable=True)
L903 = builtin.Box(initial_value=L828)
L1618 = actors.ActorEditor(actor=L903,
                           editable=False)
L1620 = actors.ActorEditor(actor=L1324,
                           editable=True)
L1624 = envs.Env(parent=None)
L1623 = actors.Actor(env=L1624,
                     script=actors.Script(next_serial_id=0,
                                          elements=[]))
L1622 = actors.ActorEditor(actor=L1623,
                           editable=True)
L244 = actors.Actor(env=L245,
                    script=L230)
L1643 = actors.ActorEditor(actor=L1200,
                           editable=True)
L140 = actors.Actor(env=L141,
                    script=L142)
L315 = actors.Actor(env=L296,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L319,
                                                                                                   'mailbox': L322}),
                                                                 serial_id=0)]))
L1646 = actors.ActorEditor(actor=L315,
                           editable=True)
L302 = builtin.BoxMaker()
L1648 = actors.ActorEditor(actor=L302,
                           editable=False)
L604 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L1650 = actors.ActorEditor(actor=L604,
                           editable=False)
L1655 = envs.Env(parent=None)
L1654 = envs.Env(parent=L1655)
L1653 = actors.Actor(env=L1654,
                     script=actors.Script(next_serial_id=16,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    actors.Example(expression=actors.Expression(text='2 + 3',
                                                                                                inner_map={}),
                                                                   serial_id=1),
                                                    actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                                                                inner_map={}),
                                                                   serial_id=2),
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    actors.Example(expression=actors.Expression(text='make Foo',
                                                                                                inner_map={}),
                                                                   serial_id=4),
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                                                                inner_map={}),
                                                                   serial_id=6),
                                                    actors.Example(expression=actors.Expression(text='box get',
                                                                                                inner_map={}),
                                                                   serial_id=7),
                                                    actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                                                                inner_map={}),
                                                                   serial_id=8),
                                                    actors.Example(expression=actors.Expression(text="['hello']",
                                                                                                inner_map={}),
                                                                   serial_id=9),
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    actors.Example(expression=actors.Expression(text='maildirectory',
                                                                                                inner_map={}),
                                                                   serial_id=11),
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                                                                inner_map={}),
                                                                   serial_id=13),
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15)]))
L1652 = actors.ActorEditor(actor=L1653,
                           editable=True)
L1371 = builtin.MailDirectory(env=envs.Env(parent=L1339))
L1722 = actors.ActorEditor(actor=L1371,
                           editable=False)
L588 = builtin.MailDirectory(env=envs.Env(parent=L558))
L1726 = actors.ActorEditor(actor=L588,
                           editable=False)
L408 = builtin.StampGuard(stamp=L56)
L1728 = actors.ActorEditor(actor=L408,
                           editable=False)
L723 = builtin.MailDirectory(env=envs.Env(parent=L673))
L1730 = actors.ActorEditor(actor=L723,
                           editable=False)
L779 = actors.Actor(env=L762,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L783,
                                                                                                   'mailbox': L786}),
                                                                 serial_id=0)]))
L1732 = actors.ActorEditor(actor=L779,
                           editable=True)
L578 = actors.Script(next_serial_id=1,
                     elements=[actors.Method(selector='send:',
                                             parameters=['message'],
                                             body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                    inner_map={}),
                                             serial_id=0)])
L574 = actors.Actor(env=L557,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L578,
                                                                                                   'mailbox': L581}),
                                                                 serial_id=0)]))
L1735 = actors.ActorEditor(actor=L574,
                           editable=True)
L771 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    body=actors.Expression(text='falseaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L1737 = actors.ActorEditor(actor=L771,
                           editable=False)
L1087 = builtin.Box(initial_value=L1065)
L1742 = actors.ActorEditor(actor=L1087,
                           editable=False)
L1744 = actors.ActorEditor(actor=L704,
                           editable=True)
L1746 = actors.ActorEditor(actor=L463,
                           editable=True)
L1329 = actors.Actor(env=L1327,
                     script=L148)
L1748 = actors.ActorEditor(actor=L1329,
                           editable=True)
L1751 = actors.ActorEditor(actor=L1603,
                           editable=False)
L1439 = builtin.List(elements=(builtin.String(str='hello'),))
L1753 = actors.ActorEditor(actor=L1439,
                           editable=False)
L1422 = actors.ActorEditor(actor=L1417,
                           editable=True)
L1757 = actors.ActorEditor(actor=L500,
                           editable=False)
L277 = actors.Actor(env=L278,
                    script=L233)
L1765 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1768 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1772 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L925}),
                       serial_id=4)
L1775 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1777 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1779 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1781 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1784 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1787 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1762 = actors.Actor(env=L902,
                     script=actors.Script(next_serial_id=16,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1765,
                                                    L1768,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1772,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1775,
                                                    L1777,
                                                    L1779,
                                                    L1781,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1784,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1787,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15)]))
L1132 = builtin.List(elements=(builtin.String(str='hello'),))
L1792 = actors.ActorEditor(actor=L1132,
                           editable=False)
L1795 = builtin.Number(n=25.0)
L1794 = actors.ActorEditor(actor=L1795,
                           editable=False)
L1244 = builtin.Number(n=25.0)
L1797 = actors.ActorEditor(actor=L1244,
                           editable=False)
L446 = actors.Actor(env=envs.Env(parent=L384),
                    script=L441)
L1802 = actors.ActorEditor(actor=L1013,
                           editable=True)
L1104 = builtin.MailDirectory(env=envs.Env(parent=L1064))
L1805 = actors.ActorEditor(actor=L1104,
                           editable=False)
L947 = builtin.Number(n=25.0)
L1808 = actors.ActorEditor(actor=L947,
                           editable=False)
L1770 = builtin.Number(n=25.0)
L1811 = actors.ActorEditor(actor=L1770,
                           editable=False)
L795 = builtin.MailDirectory(env=envs.Env(parent=L763))
L1813 = actors.ActorEditor(actor=L795,
                           editable=False)
L1815 = actors.ActorEditor(actor=L265,
                           editable=True)
L1818 = builtin.Number(n=29.0)
L1817 = actors.ActorEditor(actor=L1818,
                           editable=False)
L1820 = actors.ActorEditor(actor=L1562,
                           editable=False)
L1823 = builtin.String(str='<p>')
L1822 = actors.ActorEditor(actor=L1823,
                           editable=False)
L1828 = builtin.List(elements=(builtin.String(str='hello'),))
L1827 = actors.ActorEditor(actor=L1828,
                           editable=False)
L1832 = builtin.String(str='<p/>')
L1831 = actors.ActorEditor(actor=L1832,
                           editable=False)
L362 = builtin.List(elements=(builtin.String(str='hello'),))
L1834 = actors.ActorEditor(actor=L362,
                           editable=False)
L1837 = actors.ActorEditor(actor=L898,
                           editable=False)
L625 = builtin.Box(initial_value=L604)
L1841 = actors.ActorEditor(actor=L625,
                           editable=False)
L1843 = actors.ActorEditor(actor=L276,
                           editable=False)
L407 = builtin.List(elements=(L56,
                              L408))
L1845 = actors.ActorEditor(actor=L407,
                           editable=False)
L1847 = actors.ActorEditor(actor=L1020,
                           editable=False)
L393 = builtin.StampMaker()
L1850 = actors.ActorEditor(actor=L393,
                           editable=False)
L944 = actors.ActorEditor(actor=L939,
                          editable=True)
L1864 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1867 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1871 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L65}),
                       serial_id=4)
L1874 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1876 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1878 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1880 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1883 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1886 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1890 = actors.Example(expression=actors.Expression(text='make animalgame',
                                                    inner_map={'animalgame': L223}),
                       serial_id=16)
L1892 = actors.Example(expression=actors.Expression(text='make newanimalgame',
                                                    inner_map={'newanimalgame': L184}),
                       serial_id=17)
L1861 = actors.Actor(env=L84,
                     script=actors.Script(next_serial_id=18,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1864,
                                                    L1867,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1871,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1874,
                                                    L1876,
                                                    L1878,
                                                    L1880,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1883,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1886,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1890,
                                                    L1892]))
L1860 = actors.ActorEditor(actor=L1861,
                           editable=True)
L43 = builtin.List(elements=())
L42 = builtin.Box(initial_value=L43)
L1895 = actors.ActorEditor(actor=L42,
                           editable=False)
L1480 = builtin.Number(n=25.0)
L1899 = actors.ActorEditor(actor=L1480,
                           editable=False)
L1905 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L1908 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L1911 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L508}),
                       serial_id=4)
L1914 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L1916 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L1918 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L1920 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L1923 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L1926 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L1930 = actors.Example(expression=actors.Expression(text='http://localhost:8080/id/5186614581370432354',
                                                    inner_map={}),
                       serial_id=16)
L1932 = actors.Example(expression=actors.Expression(text='8 * 5',
                                                    inner_map={}),
                       serial_id=17)
L1902 = actors.Actor(env=L1063,
                     script=actors.Script(next_serial_id=18,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L1905,
                                                    L1908,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L1911,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L1914,
                                                    L1916,
                                                    L1918,
                                                    L1920,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L1923,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L1926,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L1930,
                                                    L1932]))
L838 = builtin.BoxMaker()
L1936 = actors.ActorEditor(actor=L838,
                           editable=False)
L1938 = actors.ActorEditor(actor=L198,
                           editable=True)
L174 = actors.Actor(env=L175,
                    script=L145)
L1941 = actors.ActorEditor(actor=L174,
                           editable=True)
L1944 = builtin.String(str='Wavy!')
L1943 = actors.ActorEditor(actor=L1944,
                           editable=False)
L1946 = actors.ActorEditor(actor=L1389,
                           editable=True)
L1869 = builtin.Number(n=25.0)
L1948 = actors.ActorEditor(actor=L1869,
                           editable=False)
L778 = builtin.Box(initial_value=L771)
L1950 = actors.ActorEditor(actor=L778,
                           editable=False)
L1952 = actors.ActorEditor(actor=L446,
                           editable=True)
L929 = builtin.Number(n=120.0)
L1954 = actors.ActorEditor(actor=L929,
                           editable=False)
L1958 = actors.ActorEditor(actor=L1175,
                           editable=False)
L1961 = actors.ActorEditor(actor=L513,
                           editable=False)
L711 = actors.Actor(env=L672,
                    script=actors.Script(next_serial_id=1,
                                         elements=[actors.Method(selector='run',
                                                                 parameters=[],
                                                                 body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                        inner_map={'sender': L708,
                                                                                                   'mailbox': L695}),
                                                                 serial_id=0)]))
L1963 = actors.ActorEditor(actor=L711,
                           editable=True)
L401 = builtin.Box(initial_value=L387)
L1967 = actors.ActorEditor(actor=L401,
                           editable=False)
L972 = builtin.Number(n=5.0)
L394 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    body=actors.Expression(text='trueaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L1971 = actors.ActorEditor(actor=L394,
                           editable=False)
L1973 = actors.ActorEditor(actor=L244,
                           editable=True)
L1975 = actors.ActorEditor(actor=L715,
                           editable=True)
L1977 = actors.ActorEditor(actor=L140,
                           editable=True)
L1349 = builtin.Box(initial_value=L808)
L1979 = actors.ActorEditor(actor=L1349,
                           editable=False)
L1981 = actors.ActorEditor(actor=L118,
                           editable=True)
L702 = builtin.Box(initial_value=builtin.List(elements=(L704,)))
L1984 = actors.ActorEditor(actor=L702,
                           editable=False)
L1866 = builtin.Number(n=5.0)
L1988 = actors.ActorEditor(actor=L1866,
                           editable=False)
L1993 = envs.Env(parent=None)
L1992 = envs.Env(parent=L1993)
L1991 = actors.Actor(env=L1992,
                     script=actors.Script(next_serial_id=16,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    actors.Example(expression=actors.Expression(text='2 + 3',
                                                                                                inner_map={}),
                                                                   serial_id=1),
                                                    actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                                                                inner_map={}),
                                                                   serial_id=2),
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    actors.Example(expression=actors.Expression(text='make Foo',
                                                                                                inner_map={}),
                                                                   serial_id=4),
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                                                                inner_map={}),
                                                                   serial_id=6),
                                                    actors.Example(expression=actors.Expression(text='box get',
                                                                                                inner_map={}),
                                                                   serial_id=7),
                                                    actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                                                                inner_map={}),
                                                                   serial_id=8),
                                                    actors.Example(expression=actors.Expression(text="['hello']",
                                                                                                inner_map={}),
                                                                   serial_id=9),
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    actors.Example(expression=actors.Expression(text='maildirectory',
                                                                                                inner_map={}),
                                                                   serial_id=11),
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                                                                inner_map={}),
                                                                   serial_id=13),
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15)]))
L1990 = actors.ActorEditor(actor=L1991,
                           editable=True)
L1296 = builtin.List(elements=(builtin.String(str='hello'),))
L2059 = actors.ActorEditor(actor=L1296,
                           editable=False)
L1366 = envs.Env(parent=L1338)
L1357 = actors.Script(next_serial_id=3,
                      elements=[actors.Method(selector='first',
                                              parameters=[],
                                              body=actors.Expression(text='inbox get at: 1',
                                                                     inner_map={}),
                                              serial_id=0),
                                actors.Method(selector='removefirst',
                                              parameters=[],
                                              body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                     inner_map={}),
                                              serial_id=1),
                                actors.Method(selector='sender',
                                              parameters=[],
                                              body=actors.Expression(text='sender',
                                                                     inner_map={}),
                                              serial_id=2)])
L1364 = actors.Actor(env=envs.Env(parent=L1366),
                     script=L1357)
L2063 = actors.ActorEditor(actor=L1364,
                           editable=True)
L614 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L2065 = actors.ActorEditor(actor=L614,
                           editable=False)
L1147 = envs.Env(parent=None)
L1146 = actors.Actor(env=L1147,
                     script=actors.Script(next_serial_id=0,
                                          elements=[]))
L2067 = actors.ActorEditor(actor=L1146,
                           editable=True)
L1240 = actors.ActorEditor(actor=L1235,
                           editable=True)
L1257 = builtin.List(elements=(builtin.String(str='hello'),))
L2071 = actors.ActorEditor(actor=L1257,
                           editable=False)
L732 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='true',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='falsevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=False)
L863 = builtin.Box(initial_value=L732)
L2075 = actors.ActorEditor(actor=L863,
                           editable=False)
L2081 = actors.Example(expression=actors.Expression(text='2 + 3',
                                                    inner_map={}),
                       serial_id=1)
L2084 = actors.Example(expression=actors.Expression(text='(3*3) + (4*4)',
                                                    inner_map={}),
                       serial_id=2)
L2087 = actors.Example(expression=actors.Expression(text='make Foo',
                                                    inner_map={'Foo': L1373}),
                       serial_id=4)
L2090 = actors.Example(expression=actors.Expression(text='let box = makebox holding: true',
                                                    inner_map={}),
                       serial_id=6)
L2092 = actors.Example(expression=actors.Expression(text='box get',
                                                    inner_map={}),
                       serial_id=7)
L2094 = actors.Example(expression=actors.Expression(text='box <- false. box get',
                                                    inner_map={}),
                       serial_id=8)
L2096 = actors.Example(expression=actors.Expression(text="['hello']",
                                                    inner_map={}),
                       serial_id=9)
L2101 = actors.Example(expression=actors.Expression(text='maildirectory',
                                                    inner_map={}),
                       serial_id=11)
L2104 = actors.Example(expression=actors.Expression(text='let mailbox = makemailbox run',
                                                    inner_map={}),
                       serial_id=13)
L2108 = actors.Example(expression=actors.Expression(text='http://localhost:8080/id/5292533547202728044',
                                                    inner_map={}),
                       serial_id=16)
L2078 = actors.Actor(env=L1338,
                     script=actors.Script(next_serial_id=17,
                                          elements=[actors.Text(body='Welcome to your new account.  You should bookmark this page if you ever intend to return, because going back and clicking "Go!" again would create another new account with a different URI.\n\nIn Hmph, everything is an object, and every object has a page with a generated URI.  For example, the number 2 is an object.  Below, we send it the message "+ 3" and it adds 3 to itself, yielding 5:',
                                                                serial_id=0),
                                                    L2081,
                                                    L2084,
                                                    actors.Text(body='The syntax is related to Smalltalk, but not the same.  To make a new type of object, decide on what to call it in the local scope, such as Foo, and enter "make Foo":',
                                                                serial_id=3),
                                                    L2087,
                                                    actors.Text(body='You can also give a local name to any other object using "let name = expression". For example:',
                                                                serial_id=5),
                                                    L2090,
                                                    L2092,
                                                    L2094,
                                                    L2096,
                                                    actors.Text(body="There's a public directory of message boxes for other users, in maildirectory:",
                                                                serial_id=10),
                                                    L2101,
                                                    actors.Text(body='You can create your own mailbox:',
                                                                serial_id=12),
                                                    L2104,
                                                    actors.Text(body='To add it to the directory, enter "maildirectory at: \'alice\' put: mailbox sender" into the "Add example" field below, changing alice to some single-word identifier of your choice. (This will fail and return false if that identifier is already taken.)  Then inspect "mailbox" to see how to get your messages. A message can be any object, not just plain text.',
                                                                serial_id=14),
                                                    actors.Text(body="Have fun exploring!  Don't put much work into it, at least yet, because this account *will* get zapped during code upgrades; I'm not ready to commit to continuity yet.  There will be actual documentation real soon now.  Please send feedback to Darius Bacon <darius@accesscom.com>. Thanks!",
                                                                serial_id=15),
                                                    L2108]))
L2077 = actors.ActorEditor(actor=L2078,
                           editable=True)
L1907 = actors.ActorEditor(actor=L1902,
                           editable=True)
L2117 = envs.Env(parent=L249)
L2115 = actors.Actor(env=envs.Env(parent=L2117),
                     script=L240)
L2114 = actors.ActorEditor(actor=L2115,
                           editable=True)
L2119 = actors.ActorEditor(actor=L1176,
                           editable=False)
L566 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['trueaction',
                                                                                'falseaction'],
                                                                    body=actors.Expression(text='trueaction run',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L2121 = actors.ActorEditor(actor=L566,
                           editable=False)
L801 = actors.Actor(env=envs.Env(parent=L762),
                    script=L803)
L2123 = actors.ActorEditor(actor=L801,
                           editable=True)
L2128 = actors.ActorEditor(actor=L804,
                           editable=False)
L2130 = builtin.String(str='Is it a dog?')
L1102 = actors.Actor(env=envs.Env(parent=L1063),
                     script=L508)
L2132 = actors.ActorEditor(actor=L1102,
                           editable=True)
L2135 = builtin.List(elements=())
L2138 = actors.ActorEditor(actor=L693,
                           editable=True)
L2098 = builtin.List(elements=(builtin.String(str='hello'),))
L2140 = actors.ActorEditor(actor=L2098,
                           editable=False)
L1767 = actors.ActorEditor(actor=L1762,
                           editable=True)
L2145 = builtin.Number(n=0)
L2144 = actors.ActorEditor(actor=L2145,
                           editable=False)
L28 = builtin.Box(initial_value=L6)
L2148 = actors.ActorEditor(actor=L28,
                           editable=False)
L2152 = actors.ActorEditor(actor=L116,
                           editable=True)
L2156 = actors.ActorEditor(actor=L533,
                           editable=False)
L642 = envs.Env(parent=L602)
L640 = actors.Actor(env=envs.Env(parent=L642),
                    script=L633)
L2158 = actors.ActorEditor(actor=L640,
                           editable=True)
L1076 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                             elements=[actors.Method(selector='not',
                                                                     parameters=[],
                                                                     body=actors.Expression(text='false',
                                                                                            inner_map={}),
                                                                     serial_id=0),
                                                       actors.Method(selector='iftrue:iffalse:',
                                                                     parameters=['truevalue',
                                                                                 'falsevalue'],
                                                                     body=actors.Expression(text='truevalue',
                                                                                            inner_map={}),
                                                                     serial_id=1)]),
                        value=True)
L2160 = actors.ActorEditor(actor=L1076,
                           editable=False)
L921 = builtin.Box(initial_value=builtin.List(elements=()))
L2163 = actors.ActorEditor(actor=L921,
                           editable=False)
L928 = actors.ActorEditor(actor=L900,
                          editable=True)
L2167 = actors.ActorEditor(actor=L1230,
                           editable=False)
L177 = builtin.String(str='cat')
L2172 = actors.ActorEditor(actor=L177,
                           editable=False)
L565 = builtin.StampMaker()
L2174 = actors.ActorEditor(actor=L565,
                           editable=False)
L2178 = actors.ActorEditor(actor=L1178,
                           editable=True)
L467 = builtin.String(str='<p>')
L2180 = actors.ActorEditor(actor=L467,
                           editable=False)
L2182 = actors.ActorEditor(actor=L2135,
                           editable=False)
L2184 = actors.ActorEditor(actor=L86,
                           editable=False)
L1934 = builtin.Number(n=40.0)
L2186 = actors.ActorEditor(actor=L1934,
                           editable=False)
L2188 = actors.ActorEditor(actor=L1270,
                           editable=False)
L1354 = actors.Script(next_serial_id=1,
                      elements=[actors.Method(selector='send:',
                                              parameters=['message'],
                                              body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                     inner_map={}),
                                              serial_id=0)])
L1350 = actors.Actor(env=L1338,
                     script=actors.Script(next_serial_id=1,
                                          elements=[actors.Method(selector='run',
                                                                  parameters=[],
                                                                  body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                         inner_map={'sender': L1354,
                                                                                                    'mailbox': L1357}),
                                                                  serial_id=0)]))
L2192 = actors.ActorEditor(actor=L1350,
                           editable=True)
L2194 = actors.ActorEditor(actor=L2130,
                           editable=False)
L17 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                           elements=[actors.Method(selector='not',
                                                                   parameters=[],
                                                                   body=actors.Expression(text='false',
                                                                                          inner_map={}),
                                                                   serial_id=0),
                                                     actors.Method(selector='iftrue:iffalse:',
                                                                   parameters=['truevalue',
                                                                               'falsevalue'],
                                                                   body=actors.Expression(text='truevalue',
                                                                                          inner_map={}),
                                                                   serial_id=1)]),
                      value=True)
L2196 = actors.ActorEditor(actor=L17,
                           editable=False)
L2198 = actors.ActorEditor(actor=L732,
                           editable=False)
L1453 = builtin.Number(n=10)
L2200 = actors.ActorEditor(actor=L1453,
                           editable=False)
L2205 = actors.ActorEditor(actor=L178,
                           editable=False)
L183 = builtin.String(str='dog')
L2208 = actors.ActorEditor(actor=L183,
                           editable=False)
L2210 = actors.ActorEditor(actor=L277,
                           editable=True)
L1165 = builtin.Number(n=6.0)
L2212 = actors.ActorEditor(actor=L1165,
                           editable=False)
L2214 = actors.ActorEditor(actor=L972,
                           editable=False)
L1092 = actors.Script(next_serial_id=1,
                      elements=[actors.Method(selector='send:',
                                              parameters=['message'],
                                              body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                     inner_map={}),
                                              serial_id=0)])
L1088 = actors.Actor(env=L1063,
                     script=actors.Script(next_serial_id=1,
                                          elements=[actors.Method(selector='run',
                                                                  parameters=[],
                                                                  body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                         inner_map={'sender': L1092,
                                                                                                    'mailbox': L1095}),
                                                                  serial_id=0)]))
L2217 = actors.ActorEditor(actor=L1088,
                           editable=True)
L303 = builtin.Boolean(script=actors.Script(next_serial_id=2,
                                            elements=[actors.Method(selector='not',
                                                                    parameters=[],
                                                                    body=actors.Expression(text='false',
                                                                                           inner_map={}),
                                                                    serial_id=0),
                                                      actors.Method(selector='iftrue:iffalse:',
                                                                    parameters=['truevalue',
                                                                                'falsevalue'],
                                                                    body=actors.Expression(text='truevalue',
                                                                                           inner_map={}),
                                                                    serial_id=1)]),
                       value=True)
L2221 = actors.ActorEditor(actor=L303,
                           editable=False)
L2083 = builtin.Number(n=5.0)
L2224 = actors.ActorEditor(actor=L2083,
                           editable=False)
L0 = registry.HmphSystem(at_id={'ab0fef7f36dd3d6e5a6e': registry.Entry(actor=L2,
                                                                       timestamp=1208019537.386208),
                                '3852696174487011421': registry.Entry(actor=L55,
                                                                      timestamp=1104697525.0871),
                                'd0f449aa58533e36ea69': registry.Entry(actor=L58,
                                                                       timestamp=1109433966.39653),
                                '785dd82fa6b01f374f86': registry.Entry(actor=L60,
                                                                       timestamp=1208019245.832073),
                                '389f782794ad82bf42c2': registry.Entry(actor=L62,
                                                                       timestamp=1109435020.479353),
                                'fc1d1a3284d605538654': registry.Entry(actor=L65,
                                                                       timestamp=1109422775.098796),
                                '50c6025c3f7c1b17b359': registry.Entry(actor=L67,
                                                                       timestamp=1190664334.063704),
                                '92077dd35d38c54b1d7a': registry.Entry(actor=L75,
                                                                       timestamp=1109433506.802811),
                                'e0a19b1b2095e54a1a98': registry.Entry(actor=L79,
                                                                       timestamp=1109428828.339134),
                                '563ca179481499c18ab6': registry.Entry(actor=L282,
                                                                       timestamp=1109435048.102296),
                                '177af5534bd8e4a0efef': registry.Entry(actor=L284,
                                                                       timestamp=1109434948.988769),
                                '33e43cb0a69702868a1b': registry.Entry(actor=L286,
                                                                       timestamp=1109435117.511516),
                                'a9dd87deafb6771dc685': registry.Entry(actor=L108,
                                                                       timestamp=1109433538.641732),
                                '661509098043722411': registry.Entry(actor=L292,
                                                                     timestamp=1104650549.651986),
                                '9e4059674b42ebb77e80': registry.Entry(actor=L295,
                                                                       timestamp=1190664333.905583),
                                'db48f7ce53f52a1be8ef': registry.Entry(actor=L376,
                                                                       timestamp=1208019245.829556),
                                '2452790028842326399': registry.Entry(actor=L378,
                                                                      timestamp=1104650712.661585),
                                '244593790248987534': registry.Entry(actor=L381,
                                                                     timestamp=1104696067.74364),
                                '7733755804024661725': registry.Entry(actor=L508,
                                                                      timestamp=1104730507.793503),
                                'd3f069172de864d5ed94': registry.Entry(actor=L510,
                                                                       timestamp=1105921788.511422),
                                '585cf6e821add948341f': registry.Entry(actor=L513,
                                                                       timestamp=1108956454.268706),
                                '9923278975221135661': registry.Entry(actor=L515,
                                                                      timestamp=1104650760.298719),
                                '12946586331713097828': registry.Entry(actor=L500,
                                                                       timestamp=1104650753.210412),
                                '701718880621245410': registry.Entry(actor=L415,
                                                                     timestamp=1104689955.322702),
                                '2169573376375311512': registry.Entry(actor=L519,
                                                                      timestamp=1104732128.235605),
                                '425401d16cbbcb013414': registry.Entry(actor=L522,
                                                                       timestamp=1109424299.651423),
                                '7488614337481629366': registry.Entry(actor=L524,
                                                                      timestamp=1104732124.732973),
                                'b02f708094d7017ff9ca': registry.Entry(actor=L276,
                                                                       timestamp=1109428831.452741),
                                '4716280173295595176': registry.Entry(actor=L528,
                                                                      timestamp=1104632228.340987),
                                '6ea8e4e7c59015808866': registry.Entry(actor=L531,
                                                                       timestamp=1108956215.993707),
                                '809ca9a6a52e472c2232': registry.Entry(actor=L540,
                                                                       timestamp=1108956539.881407),
                                '2fe08bfff563b4be7b88': registry.Entry(actor=L543,
                                                                       timestamp=1109428875.280458),
                                '14f6bb412e4e8dba28e7': registry.Entry(actor=L546,
                                                                       timestamp=1105921513.453735),
                                '94c3545f0b71f518f49b': registry.Entry(actor=L549,
                                                                       timestamp=1208019245.82639),
                                '752780470375236548': registry.Entry(actor=L552,
                                                                     timestamp=1104650712.6552),
                                '13472432016877657261': registry.Entry(actor=L554,
                                                                       timestamp=1104650549.645519),
                                '86494131c70f31e05c76': registry.Entry(actor=L599,
                                                                       timestamp=1105921566.047498),
                                '95e56b4ad9bd4778155e': registry.Entry(actor=L63,
                                                                       timestamp=1109435020.482046),
                                'aeca121725efb320e1bd': registry.Entry(actor=L663,
                                                                       timestamp=1109435097.305729),
                                '10397032148789093459': registry.Entry(actor=L520,
                                                                       timestamp=1104732128.235873),
                                '6ad807ecfa9819fc5274': registry.Entry(actor=L669,
                                                                       timestamp=1108956554.296838),
                                '27a3eaafc2929449c2': registry.Entry(actor=L729,
                                                                     timestamp=1108412240.350591),
                                'f6599863150eeb0c6b2c': registry.Entry(actor=L198,
                                                                       timestamp=1109434795.847883),
                                '7773452571940476712': registry.Entry(actor=L56,
                                                                      timestamp=1104697525.087406),
                                '8260809509679861109': registry.Entry(actor=L758,
                                                                      timestamp=1104633042.413602),
                                '13289750248154104862': registry.Entry(actor=L807,
                                                                       timestamp=1104730109.325695),
                                '9876815513572400324': registry.Entry(actor=L815,
                                                                      timestamp=1104650549.662023),
                                '4023b3c507c036f50e56': registry.Entry(actor=L819,
                                                                       timestamp=1104797071.70976),
                                '4c09de69dcaeb7cc983c': registry.Entry(actor=L822,
                                                                       timestamp=1109428388.68279),
                                'afe0f8475c226480003e': registry.Entry(actor=L824,
                                                                       timestamp=1104797063.490594),
                                '14572783785176608328': registry.Entry(actor=L851,
                                                                       timestamp=1104632228.347634),
                                '2af0a890ec67be538d2e': registry.Entry(actor=L853,
                                                                       timestamp=1190664333.923369),
                                '3bc09d4543e10c13c0fd': registry.Entry(actor=L178,
                                                                       timestamp=1109435162.498421),
                                '744cd5a5607fb52901e3': registry.Entry(actor=L856,
                                                                       timestamp=1190665257.472483),
                                'dfdddcc9276b298ffa66': registry.Entry(actor=L858,
                                                                       timestamp=1108412173.816499),
                                '3221c3e44d26b6bbd5ad': registry.Entry(actor=L898,
                                                                       timestamp=1105921540.943424),
                                'e64afe24df26d799a9ac': registry.Entry(actor=L900,
                                                                       timestamp=1104807972.488673),
                                '17543361990980566375': registry.Entry(actor=L931,
                                                                       timestamp=1104650712.671244),
                                'aa59537f559184f9eca2': registry.Entry(actor=L935,
                                                                       timestamp=1104797063.503005),
                                '15235668337536127643': registry.Entry(actor=L937,
                                                                       timestamp=1104650549.649259),
                                '66910d75bb942953d69c': registry.Entry(actor=L939,
                                                                       timestamp=1208019245.825811),
                                '506e223cff60b5489e1b': registry.Entry(actor=L113,
                                                                       timestamp=1109435078.919728),
                                'bd4007d9b81ff6015fa': registry.Entry(actor=L975,
                                                                      timestamp=1109677352.059732),
                                '66e67041b7181b22690': registry.Entry(actor=L925,
                                                                      timestamp=1104797063.318946),
                                '9f783033e4c251e7aecd': registry.Entry(actor=L978,
                                                                       timestamp=1109435120.105415),
                                '1823737881735097641': registry.Entry(actor=L980,
                                                                      timestamp=1104633108.690904),
                                'd12f22d62909bfa38926': registry.Entry(actor=L999,
                                                                       timestamp=1190664334.043553),
                                '6231133fb36d5570d27a': registry.Entry(actor=L1001,
                                                                       timestamp=1109434995.110124),
                                '2291036927185731541': registry.Entry(actor=L506,
                                                                      timestamp=1104650712.656209),
                                '16832713526910606204': registry.Entry(actor=L1005,
                                                                       timestamp=1104732473.827361),
                                'e5adaa9b6e0a3d911e8c': registry.Entry(actor=L1008,
                                                                       timestamp=1208019245.831458),
                                '5ce1f20ddbfb0d7dbdc8': registry.Entry(actor=L1010,
                                                                       timestamp=1109422775.132426),
                                '10238622742572975996': registry.Entry(actor=L418,
                                                                       timestamp=1104696935.058783),
                                'feab0d101efa1eb7800c': registry.Entry(actor=L1013,
                                                                       timestamp=1105921822.377749),
                                '6368b3eb10785a7e39c3': registry.Entry(actor=L1016,
                                                                       timestamp=1104797063.330265),
                                '8635995105440979424': registry.Entry(actor=L1018,
                                                                      timestamp=1104650712.680698),
                                '9515dc91fc08cfc0dda0': registry.Entry(actor=L1020,
                                                                       timestamp=1109428838.224806),
                                '1955787528046718785': registry.Entry(actor=L437,
                                                                      timestamp=1104689968.784857),
                                '4b6ad410a34d5b6c16ee': registry.Entry(actor=L1023,
                                                                       timestamp=1105921803.839317),
                                '5b0ee41b18f3e75167a2': registry.Entry(actor=L1025,
                                                                       timestamp=1104797063.337943),
                                'd09a2d478bd604dc3907': registry.Entry(actor=L1027,
                                                                       timestamp=1109435120.102756),
                                '4eec14b8e7620b9cbbf6': registry.Entry(actor=L1029,
                                                                       timestamp=1104797063.345591),
                                '5f250d31a4b5ac2e53cb': registry.Entry(actor=L1033,
                                                                       timestamp=1109435010.016041),
                                '9360497806179331195': registry.Entry(actor=L502,
                                                                      timestamp=1104650930.792357),
                                'd56af1fc4e478d2676e4': registry.Entry(actor=L1036,
                                                                       timestamp=1109424447.451117),
                                '17127538032127337902': registry.Entry(actor=L1039,
                                                                       timestamp=1104730109.318953),
                                'f087d80a9309247b65a': registry.Entry(actor=L693,
                                                                      timestamp=1108956695.180273),
                                '844713905205980550': registry.Entry(actor=L1043,
                                                                     timestamp=1104730109.319428),
                                '17611950891294426261': registry.Entry(actor=L1051,
                                                                       timestamp=1104690171.623419),
                                'f58848882bb5b9bb3ac8': registry.Entry(actor=L116,
                                                                       timestamp=1109433508.581608),
                                '8cf176cfe796cd156975': registry.Entry(actor=L1054,
                                                                       timestamp=1190665181.345289),
                                '1d080e958d08e20c362b': registry.Entry(actor=L145,
                                                                       timestamp=1109434485.921203),
                                'f8ff73eb7cf1b9941a73': registry.Entry(actor=L227,
                                                                       timestamp=1109428388.685402),
                                '9057425907194955737': registry.Entry(actor=L406,
                                                                      timestamp=1105488351.887705),
                                '3518475730128674669': registry.Entry(actor=L1059,
                                                                      timestamp=1104730507.83989),
                                '4227047065147840205': registry.Entry(actor=L1111,
                                                                      timestamp=1104650529.884198),
                                '12634790733065757812': registry.Entry(actor=L803,
                                                                       timestamp=1104632228.343287),
                                '12685563122316055259': registry.Entry(actor=L433,
                                                                       timestamp=1104706912.387881),
                                'c4fbf97dd8919c749ca9': registry.Entry(actor=L1173,
                                                                       timestamp=1190664333.911598),
                                'fcceeb077cb614ca85f8': registry.Entry(actor=L1175,
                                                                       timestamp=1105921806.091142),
                                'a51f96a48acf383d67b6': registry.Entry(actor=L1178,
                                                                       timestamp=1108956747.618078),
                                '437ed8478e622b78736e': registry.Entry(actor=L1181,
                                                                       timestamp=1208019541.593823),
                                '3324730690425372007': registry.Entry(actor=L1183,
                                                                      timestamp=1104650549.631987),
                                'eaad67a6f405387e7f63': registry.Entry(actor=L265,
                                                                       timestamp=1109428392.426419),
                                '1f450f46787e5df1a832': registry.Entry(actor=L123,
                                                                       timestamp=1109433892.9025),
                                'f57378bfa8f1bda4717f': registry.Entry(actor=L1188,
                                                                       timestamp=1109428871.343946),
                                'e6e700e2d7e729e3e72': registry.Entry(actor=L1190,
                                                                      timestamp=1104807950.895449),
                                '2f63027d1e8f1c1a37fd': registry.Entry(actor=L1192,
                                                                       timestamp=1109428835.818986),
                                '9ffceadfb339bf0a37b7': registry.Entry(actor=L1002,
                                                                       timestamp=1109434995.112876),
                                '6c6ed31f12ce3e23a22a': registry.Entry(actor=L1195,
                                                                       timestamp=1109434683.425472),
                                '14138594607498135940': registry.Entry(actor=L501,
                                                                       timestamp=1104650760.299006),
                                '9638377965285201700': registry.Entry(actor=L1198,
                                                                      timestamp=1104632228.347318),
                                '1aa5ec03a965669b0022': registry.Entry(actor=L1200,
                                                                       timestamp=1109423781.764814),
                                '236d38760c6a183af6f8': registry.Entry(actor=L1207,
                                                                       timestamp=1108956215.996386),
                                '1546622807325074855': registry.Entry(actor=L453,
                                                                      timestamp=1104696117.332214),
                                '7936621921662856627': registry.Entry(actor=L1210,
                                                                      timestamp=1104650549.672792),
                                'e87eee5c7103444d365b': registry.Entry(actor=L1212,
                                                                       timestamp=1108412101.378515),
                                '941178e1441881defb2b': registry.Entry(actor=L1214,
                                                                       timestamp=1108412101.480884),
                                '97cdf671f963709d9eb3': registry.Entry(actor=L1216,
                                                                       timestamp=1108412173.822909),
                                '6817141969146993628': registry.Entry(actor=L1218,
                                                                      timestamp=1104708982.608636),
                                '12545444783397887118': registry.Entry(actor=L463,
                                                                       timestamp=1104693955.28495),
                                '7a19485e947469b48f5d': registry.Entry(actor=L1176,
                                                                       timestamp=1105921826.426072),
                                '13319024784900900893': registry.Entry(actor=L1222,
                                                                       timestamp=1104730507.798197),
                                'cc5e0eda4ea20f97f227': registry.Entry(actor=L1224,
                                                                       timestamp=1208019541.595728),
                                '3313777953666434324': registry.Entry(actor=L1226,
                                                                      timestamp=1104650549.639759),
                                '1061218531910574846': registry.Entry(actor=L434,
                                                                      timestamp=1104706912.387328),
                                '59366674524a8992ec57': registry.Entry(actor=L1230,
                                                                       timestamp=1105921808.808475),
                                '34874108ea81817dd45f': registry.Entry(actor=L1232,
                                                                       timestamp=1109428828.336385),
                                '620b2cb3deba6d946d89': registry.Entry(actor=L133,
                                                                       timestamp=1109433834.822554),
                                '12473ee71c96cd605738': registry.Entry(actor=L1235,
                                                                       timestamp=1108412101.331276),
                                '2496797421715521539': registry.Entry(actor=L1270,
                                                                      timestamp=1104732153.444034),
                                '4f4d746968439adc77f8': registry.Entry(actor=L1272,
                                                                       timestamp=1108956726.526049),
                                'fc67e57428a80e5c577': registry.Entry(actor=L1274,
                                                                      timestamp=1109434690.483549),
                                '959c6923ca073aa23ec2': registry.Entry(actor=L1276,
                                                                       timestamp=1105921745.740583),
                                '9e1868775012070da71': registry.Entry(actor=L1313,
                                                                      timestamp=1109434991.668722),
                                '479cbf4440b2fda712e3': registry.Entry(actor=L1318,
                                                                       timestamp=1108956215.996874),
                                '27642d37c9e93d88a9d3': registry.Entry(actor=L1320,
                                                                       timestamp=1108412173.830037),
                                '66d46b6a4c45495d85f': registry.Entry(actor=L1322,
                                                                      timestamp=1108412101.364145),
                                'c4491d62f5b2c77c1788': registry.Entry(actor=L1324,
                                                                       timestamp=1109435027.723671),
                                '9cab7b2aaf0861d72052': registry.Entry(actor=L1331,
                                                                       timestamp=1105921513.584868),
                                'b378f20f4218f5661db8': registry.Entry(actor=L233,
                                                                       timestamp=1109428186.780271),
                                '38674a8406c10d8acc66': registry.Entry(actor=L1277,
                                                                       timestamp=1105921513.413335),
                                '11497005180784433127': registry.Entry(actor=L1335,
                                                                       timestamp=1104730109.314078),
                                '11885770933734303644': registry.Entry(actor=L1375,
                                                                       timestamp=1104689888.176734),
                                '2909c2803333fa9763dd': registry.Entry(actor=L1380,
                                                                       timestamp=1190665226.653671),
                                'abd8c6c996e0bdee54ab': registry.Entry(actor=L511,
                                                                       timestamp=1105921788.513629),
                                '40318dd352f07bad2f32': registry.Entry(actor=L1383,
                                                                       timestamp=1109435048.090644),
                                'a3707eafba7f8c29438f': registry.Entry(actor=L1385,
                                                                       timestamp=1190665181.352079),
                                '7725879995356042119': registry.Entry(actor=L1387,
                                                                      timestamp=1104633105.533054),
                                'c28f00da84aabe9711f8': registry.Entry(actor=L1389,
                                                                       timestamp=1109428846.257795),
                                '8275236787514389161': registry.Entry(actor=L1393,
                                                                      timestamp=1104732146.039759),
                                '1049070116954587991': registry.Entry(actor=L1395,
                                                                      timestamp=1104697494.401659),
                                '211eb2ea127cce5956ea': registry.Entry(actor=L184,
                                                                       timestamp=1109433447.629179),
                                '6ae432c49f19b06e3dce': registry.Entry(actor=L1398,
                                                                       timestamp=1109424192.830728),
                                '6842470814180133769': registry.Entry(actor=L804,
                                                                      timestamp=1104632241.948518),
                                '3adc62bc55fb88be1f69': registry.Entry(actor=L1402,
                                                                       timestamp=1108412101.376064),
                                '5dc7e64e69d3a5a73189': registry.Entry(actor=L653,
                                                                       timestamp=1105921748.370198),
                                '1817218079521314969': registry.Entry(actor=L1405,
                                                                      timestamp=1104632228.331926),
                                '16897814623275256082': registry.Entry(actor=L793,
                                                                       timestamp=1104632239.255123),
                                '986b3d704ed99c37b1e2': registry.Entry(actor=L1408,
                                                                       timestamp=1208019254.894026),
                                '7984984827063085602': registry.Entry(actor=L1410,
                                                                      timestamp=1104730507.82483),
                                '10726820175615189179': registry.Entry(actor=L1412,
                                                                       timestamp=1104650549.657733),
                                '848b9113b67cd5bfccbc': registry.Entry(actor=L1414,
                                                                       timestamp=1105921513.603234),
                                'd368cd1b3e772c0dee3a': registry.Entry(actor=L142,
                                                                       timestamp=1109433734.279421),
                                'eea508d94e56f68e728b': registry.Entry(actor=L1417,
                                                                       timestamp=1108956215.955098),
                                'f675ab66721705423554': registry.Entry(actor=L1461,
                                                                       timestamp=1109434712.600971),
                                '15000248107523643647': registry.Entry(actor=L1006,
                                                                       timestamp=1104732488.300836),
                                '13176058059947371572': registry.Entry(actor=L1464,
                                                                       timestamp=1104697346.215501),
                                '6737ab2d99858d2cb98e': registry.Entry(actor=L345,
                                                                       timestamp=1190665221.273161),
                                'b25d5843447a0422c30a': registry.Entry(actor=L1467,
                                                                       timestamp=1108412101.337124),
                                '2a4f7a3dcd2f87a7532b': registry.Entry(actor=L647,
                                                                       timestamp=1105921690.904981),
                                'e20bc13b888334ad3537': registry.Entry(actor=L1423,
                                                                       timestamp=1108956448.854455),
                                '15354271914547105265': registry.Entry(actor=L1471,
                                                                       timestamp=1104689747.000292),
                                '9829540809193203453': registry.Entry(actor=L981,
                                                                      timestamp=1104633108.691174),
                                '11244828830854864470': registry.Entry(actor=L1505,
                                                                       timestamp=1104633047.078866),
                                '9e55068b582c80b9f474': registry.Entry(actor=L1507,
                                                                       timestamp=1108412101.489436),
                                'de5f81ed1b494d3519df': registry.Entry(actor=L118,
                                                                       timestamp=1109433597.629955),
                                '6aa8789df5ecc4190c79': registry.Entry(actor=L715,
                                                                       timestamp=1108956850.926143),
                                'f8670e226436fa73128f': registry.Entry(actor=L226,
                                                                       timestamp=1109428826.413799),
                                'def59007c148e24940ad': registry.Entry(actor=L1512,
                                                                       timestamp=1190664334.051161),
                                '35269d3b8f3f78114257': registry.Entry(actor=L704,
                                                                       timestamp=1108956796.855461),
                                'fa59d03a167a4c1b94ff': registry.Entry(actor=L148,
                                                                       timestamp=1109434755.246258),
                                '10330519763115726681': registry.Entry(actor=L1378,
                                                                       timestamp=1104689888.177563),
                                '93a74d12b66f1bf6d440': registry.Entry(actor=L187,
                                                                       timestamp=1109677336.731226),
                                '4a3c84658bd78b1029a1': registry.Entry(actor=L1518,
                                                                       timestamp=1208019245.830636),
                                '5d52906b91dc36916500': registry.Entry(actor=L1520,
                                                                       timestamp=1104807950.912137),
                                '54573033a0f923d876e0': registry.Entry(actor=L1522,
                                                                       timestamp=1109422775.108053),
                                '8511836882149982016': registry.Entry(actor=L1524,
                                                                      timestamp=1104650706.713083),
                                '120d37656e5a1a12158e': registry.Entry(actor=L240,
                                                                       timestamp=1109428443.654291),
                                '4667264518391135515': registry.Entry(actor=L1556,
                                                                      timestamp=1104650724.130875),
                                'e94c4dff11c20c4a0886': registry.Entry(actor=L820,
                                                                       timestamp=1104797071.712555),
                                '232be96254a60b1185f4': registry.Entry(actor=L1559,
                                                                       timestamp=1109428842.672349),
                                '5591050765793200711': registry.Entry(actor=L1562,
                                                                      timestamp=1104732505.688601),
                                '12051635174327115429': registry.Entry(actor=L1564,
                                                                       timestamp=1104650712.682002),
                                '9fe8821ff61c3fe3b77d': registry.Entry(actor=L1566,
                                                                       timestamp=1109422775.095513),
                                '56191cb3e8143011d87c': registry.Entry(actor=L339,
                                                                       timestamp=1190665181.347971),
                                '5274326361166066280': registry.Entry(actor=L382,
                                                                      timestamp=1104693745.099856),
                                '13270445787827545889': registry.Entry(actor=L1570,
                                                                       timestamp=1104730109.308865),
                                'c223f740d0189de07951': registry.Entry(actor=L1573,
                                                                       timestamp=1109435170.103392),
                                '9ed64c1f46f388ef377e': registry.Entry(actor=L730,
                                                                       timestamp=1108412240.352707),
                                '1a3edd7a42ba08472afd': registry.Entry(actor=L1576,
                                                                       timestamp=1108956448.852829),
                                '55786e30b2bf1b3ea69f': registry.Entry(actor=L1578,
                                                                       timestamp=1109428799.691737),
                                '4442827039649434997': registry.Entry(actor=L1583,
                                                                      timestamp=1104650930.792051),
                                '322fb4bc7605aa8653e2': registry.Entry(actor=L1585,
                                                                       timestamp=1109435009.982374),
                                '474b80e51e808fed1a99': registry.Entry(actor=L109,
                                                                       timestamp=1109433451.294275),
                                '12128037699416130148': registry.Entry(actor=L1588,
                                                                       timestamp=1104732146.039334),
                                '6f3a7f7d336523b08bd4': registry.Entry(actor=L1590,
                                                                       timestamp=1109422775.123138),
                                '22eb057b0621169328c9': registry.Entry(actor=L1592,
                                                                       timestamp=1108956215.977327),
                                '13387220976027820258': registry.Entry(actor=L1594,
                                                                       timestamp=1104650712.644146),
                                '7a89bcf8d307b258b3b4': registry.Entry(actor=L203,
                                                                       timestamp=1109435009.985155),
                                '672462e5d7d6c8606fe3': registry.Entry(actor=L96,
                                                                       timestamp=1109434948.992268),
                                'bb9c4f22765c549d20f1': registry.Entry(actor=L3,
                                                                       timestamp=1208019537.386277),
                                '708093d3f5efae9ceb81': registry.Entry(actor=L1599,
                                                                       timestamp=1109435009.994391),
                                '67eeb2429b63101a4ec7': registry.Entry(actor=L1601,
                                                                       timestamp=1108412161.574615),
                                'ca30c87e605ba765be06': registry.Entry(actor=L1603,
                                                                       timestamp=1109428804.820257),
                                '1679989706457713520': registry.Entry(actor=L436,
                                                                      timestamp=1104706912.387693),
                                'e18028cacd7efe69dfbb': registry.Entry(actor=L332,
                                                                       timestamp=1190665154.678051),
                                '6402116433048299654': registry.Entry(actor=L1607,
                                                                      timestamp=1104650712.667118),
                                '70ca891a948da6b4fd73': registry.Entry(actor=L1609,
                                                                       timestamp=1109422775.129649),
                                '15511116157062632786': registry.Entry(actor=L1611,
                                                                       timestamp=1104650712.674066),
                                'fff687e48591806e7d56': registry.Entry(actor=L1613,
                                                                       timestamp=1109435168.317849),
                                'b774260d0676ba628669': registry.Entry(actor=L1618,
                                                                       timestamp=1104797063.323903),
                                'b714558827a1934689eb': registry.Entry(actor=L1620,
                                                                       timestamp=1109435027.72104),
                                '16136617492328534660': registry.Entry(actor=L1622,
                                                                       timestamp=1104650949.250061),
                                'dee2d9a8289d27ac176a': registry.Entry(actor=L244,
                                                                       timestamp=1109424028.712737),
                                '804e5b1a3b2aadf7c001': registry.Entry(actor=L1643,
                                                                       timestamp=1109423781.762228),
                                'bd70c7c47be23dba293f': registry.Entry(actor=L140,
                                                                       timestamp=1109433735.957667),
                                '4cb50eebe02b70a0d71b': registry.Entry(actor=L1646,
                                                                       timestamp=1190664334.091352),
                                '9564f27dcab30da4c8d4': registry.Entry(actor=L1648,
                                                                       timestamp=1190664334.054083),
                                '25c2e6f96744ae60c374': registry.Entry(actor=L1650,
                                                                       timestamp=1105921513.572356),
                                'CCDF40493E712274L': registry.Entry(actor=L1652,
                                                                    timestamp=1104796672.150045),
                                '93ea785fea4a1506079a': registry.Entry(actor=L864,
                                                                       timestamp=1108412161.576831),
                                '10871997212631801029': registry.Entry(actor=L1722,
                                                                       timestamp=1104730109.333414),
                                '658c0f7cf8f1c49b6a69': registry.Entry(actor=L39,
                                                                       timestamp=1208019537.388222),
                                '73d4b6bd3504795305a1': registry.Entry(actor=L248,
                                                                       timestamp=1109424445.327506),
                                '8060076283853931247': registry.Entry(actor=L1726,
                                                                      timestamp=1104650549.665045),
                                '7472656884655288975': registry.Entry(actor=L1728,
                                                                      timestamp=1104689853.131622),
                                'fd0e0dcd73af9e72f597': registry.Entry(actor=L1730,
                                                                       timestamp=1108956216.009995),
                                '17980192334006365197': registry.Entry(actor=L1732,
                                                                       timestamp=1104632228.403507),
                                '7fd28421399c0260a1a0': registry.Entry(actor=L269,
                                                                       timestamp=1109428731.597176),
                                '4178227206424925539': registry.Entry(actor=L1735,
                                                                      timestamp=1104650549.674288),
                                '15250013233234179905': registry.Entry(actor=L1737,
                                                                       timestamp=1104632228.375059),
                                '6c85152f239871975017': registry.Entry(actor=L1205,
                                                                       timestamp=1109428208.878855),
                                '3cb26424481623ed41bc': registry.Entry(actor=L720,
                                                                       timestamp=1108956926.19813),
                                '1c4a4e54eec83f776e4a': registry.Entry(actor=L1399,
                                                                       timestamp=1109424192.83239),
                                '12946925928954107809': registry.Entry(actor=L1742,
                                                                       timestamp=1104730507.796433),
                                '92d4a78cea106df07c2c': registry.Entry(actor=L1744,
                                                                       timestamp=1108956796.853735),
                                '14095654525563810214': registry.Entry(actor=L1746,
                                                                       timestamp=1104694007.891321),
                                'a14d85d55467ffe04ee0': registry.Entry(actor=L1748,
                                                                       timestamp=1109435018.497181),
                                'c25353745b522913f4c2': registry.Entry(actor=L251,
                                                                       timestamp=1109424299.653085),
                                '659985c7578a877b07e3': registry.Entry(actor=L1751,
                                                                       timestamp=1109428804.817566),
                                '4f3f54f1d8db5a25f118': registry.Entry(actor=L1753,
                                                                       timestamp=1108956216.005373),
                                '13661059783025868973': registry.Entry(actor=L759,
                                                                       timestamp=1104633042.41388),
                                '7aa131ceb0eae191a3ed': registry.Entry(actor=L1422,
                                                                       timestamp=1108956833.114122),
                                '6055406963319936966': registry.Entry(actor=L1757,
                                                                      timestamp=1104650753.210143),
                                '354f3356b414dbdf6595': registry.Entry(actor=L111,
                                                                       timestamp=1109435083.837661),
                                '10927938414203847443': registry.Entry(actor=L441,
                                                                       timestamp=1104689958.530002),
                                '420e55efa0fb8d8f2ffd': registry.Entry(actor=L277,
                                                                       timestamp=1109428835.814178),
                                'fd6a40ab5331a449ac99': registry.Entry(actor=L1762,
                                                                       timestamp=1104797063.292553),
                                '1359982258694374825': registry.Entry(actor=L1792,
                                                                      timestamp=1104632228.379292),
                                '10593314374053890933': registry.Entry(actor=L1794,
                                                                       timestamp=1104730507.788162),
                                'ad509debf6bb51e095c9': registry.Entry(actor=L1797,
                                                                       timestamp=1108412101.357022),
                                'b33414f37886533390d2': registry.Entry(actor=L868,
                                                                       timestamp=1108412161.582691),
                                'f5a54a967633535bf134': registry.Entry(actor=L222,
                                                                       timestamp=1109422948.627283),
                                '10103513020179766570': registry.Entry(actor=L446,
                                                                       timestamp=1104690335.904788),
                                'c757003da8382520250d': registry.Entry(actor=L1802,
                                                                       timestamp=1105921822.375374),
                                '261ec3b86d5f1af30a43': registry.Entry(actor=L664,
                                                                       timestamp=1109435160.16693),
                                '14107852319538388771': registry.Entry(actor=L1805,
                                                                       timestamp=1104730507.833338),
                                '73f50a3f60d178768e5d': registry.Entry(actor=L918,
                                                                       timestamp=1104807950.897612),
                                'ef7b8185a1e8d3a1d99e': registry.Entry(actor=L1808,
                                                                       timestamp=1208019245.827675),
                                'f9ab36734295b51f1fb9': registry.Entry(actor=L172,
                                                                       timestamp=1109435170.100542),
                                '3ed58789fe9a7d9623fa': registry.Entry(actor=L1811,
                                                                       timestamp=1104797063.306871),
                                '11549355846312153998': registry.Entry(actor=L1813,
                                                                       timestamp=1104632228.3814),
                                '3191a13927a42a0aca34': registry.Entry(actor=L1815,
                                                                       timestamp=1109428764.749183),
                                '9ca23758d3e14b14e22f': registry.Entry(actor=L1817,
                                                                       timestamp=1105921548.349621),
                                '4138178436990957034': registry.Entry(actor=L1820,
                                                                      timestamp=1104732505.688319),
                                '6920636786683624616': registry.Entry(actor=L1822,
                                                                      timestamp=1104690523.13294),
                                '32b6411e86ed3305be63': registry.Entry(actor=L690,
                                                                       timestamp=1108956726.527702),
                                '14726587180619911525': registry.Entry(actor=L799,
                                                                       timestamp=1104633035.78582),
                                'a125bcaed7f5954b9150': registry.Entry(actor=L1827,
                                                                       timestamp=1109422775.11895),
                                '1564538181099476570': registry.Entry(actor=L1831,
                                                                      timestamp=1104690401.654279),
                                'ac567c51e8219e69ff16': registry.Entry(actor=L1834,
                                                                       timestamp=1190664334.070976),
                                'f4e883b36a48f3be4880': registry.Entry(actor=L223,
                                                                       timestamp=1109422945.68528),
                                'dfd2c79df992922d1acf': registry.Entry(actor=L1837,
                                                                       timestamp=1105921540.941346),
                                '12182569062741163979': registry.Entry(actor=L1373,
                                                                       timestamp=1104730109.314938),
                                'ca15ef2c3a7701c12458': registry.Entry(actor=L266,
                                                                       timestamp=1109423159.098862),
                                '1b5a49fb0fec6944ecc4': registry.Entry(actor=L1841,
                                                                       timestamp=1105921513.538332),
                                'a7bd903423cd5317bd7b': registry.Entry(actor=L1843,
                                                                       timestamp=1109428831.449992),
                                '17801320630458131755': registry.Entry(actor=L1845,
                                                                       timestamp=1104689816.700052),
                                '2d3ff26bf3a1ccdbda01': registry.Entry(actor=L1847,
                                                                       timestamp=1109428838.222214),
                                '3dda188fab7c5720065a': registry.Entry(actor=L31,
                                                                       timestamp=1208019245.828746),
                                '13838842964897476745': registry.Entry(actor=L1850,
                                                                       timestamp=1104650720.799705),
                                'f96001099601a04981f6': registry.Entry(actor=L670,
                                                                       timestamp=1108956537.787472),
                                '6461598025166001448': registry.Entry(actor=L402,
                                                                      timestamp=1104689796.40984),
                                'cea976a1318c7f6a6ec': registry.Entry(actor=L180,
                                                                      timestamp=1109434693.650279),
                                '7798158345955886274': registry.Entry(actor=L597,
                                                                      timestamp=1104650549.646416),
                                '3cadcfebb3425343d2ae': registry.Entry(actor=L159,
                                                                       timestamp=1109434660.001249),
                                '5b74f62f6857b7956095': registry.Entry(actor=L944,
                                                                       timestamp=1208019605.013859),
                                '2956948422716100561': registry.Entry(actor=L435,
                                                                      timestamp=1104706912.386812),
                                '4131740470354140357': registry.Entry(actor=L459,
                                                                      timestamp=1104697377.955356),
                                '740e543a73fba8ae453f': registry.Entry(actor=L1860,
                                                                       timestamp=1109677327.152944),
                                '8ceb80a0f5e5a7b0bbd6': registry.Entry(actor=L1895,
                                                                       timestamp=1208019554.739523),
                                'e568157c9501ba7cfc6a': registry.Entry(actor=L1579,
                                                                       timestamp=1109428462.781116),
                                'c700b53d7a40117bd126': registry.Entry(actor=L1614,
                                                                       timestamp=1109435168.315073),
                                '2805739992860418134': registry.Entry(actor=L1899,
                                                                      timestamp=1104650712.650219),
                                'a80d84152cb05bbf1286': registry.Entry(actor=L230,
                                                                       timestamp=1109424025.394774),
                                '8549478301856461533': registry.Entry(actor=L1902,
                                                                      timestamp=1104730507.77914),
                                '400632f1c4d59068aadc': registry.Entry(actor=L1936,
                                                                       timestamp=1104797063.32784),
                                '3bcc6e02355a4489272b': registry.Entry(actor=L1938,
                                                                       timestamp=1109434795.845222),
                                '12904228506947022660': registry.Entry(actor=L1112,
                                                                       timestamp=1104632228.327944),
                                'af6bc0bdd2da549d34ab': registry.Entry(actor=L1941,
                                                                       timestamp=1109435027.732684),
                                '978002a771fdb82dea39': registry.Entry(actor=L1943,
                                                                       timestamp=1109435124.705168),
                                '8ab96d54de6dae117484': registry.Entry(actor=L1946,
                                                                       timestamp=1109428846.255095),
                                '905b734d21990d905889': registry.Entry(actor=L1948,
                                                                       timestamp=1109422775.043208),
                                '8608183716299200486': registry.Entry(actor=L1950,
                                                                      timestamp=1104632228.348045),
                                '7436199748876259015': registry.Entry(actor=L1952,
                                                                      timestamp=1104696844.414509),
                                '63d95a5f3af1685a4628': registry.Entry(actor=L1954,
                                                                       timestamp=1104807978.857566),
                                '69de3657b02e113b0f93': registry.Entry(actor=L859,
                                                                       timestamp=1108412173.818725),
                                '14955675966070121265': registry.Entry(actor=L1472,
                                                                       timestamp=1104650712.641028),
                                'f607f8a7a922d909c959': registry.Entry(actor=L1958,
                                                                       timestamp=1105921825.245861),
                                '33f0080422fa3454881b': registry.Entry(actor=L29,
                                                                       timestamp=1208019263.446157),
                                '81ea31f2e40de4411915': registry.Entry(actor=L1961,
                                                                       timestamp=1108956454.267065),
                                'ea1042a44339a6b6299c': registry.Entry(actor=L1963,
                                                                       timestamp=1108956216.038376),
                                '4f7773f6e389793f5cff': registry.Entry(actor=L1560,
                                                                       timestamp=1109428842.674982),
                                '77c7ce5c863dd5a05a76': registry.Entry(actor=L1861,
                                                                       timestamp=1109422775.032875),
                                '1011012714027468268': registry.Entry(actor=L1967,
                                                                      timestamp=1104650712.65899),
                                'c171aaf4622a67eec25f': registry.Entry(actor=L655,
                                                                       timestamp=1105921745.787854),
                                '8238bb4120ed257048c5': registry.Entry(actor=L972,
                                                                       timestamp=1208019607.900213),
                                '13286087984584598130': registry.Entry(actor=L1971,
                                                                       timestamp=1104650712.661908),
                                '96f0ef4cbdcdc2586bf0': registry.Entry(actor=L1973,
                                                                       timestamp=1109428182.139416),
                                '40a8e69a8169b7a993b1': registry.Entry(actor=L1975,
                                                                       timestamp=1108956889.006049),
                                '10e10ac18640c6dd2364': registry.Entry(actor=L1977,
                                                                       timestamp=1109434627.705112),
                                '4939350837483695449': registry.Entry(actor=L1979,
                                                                      timestamp=1104730109.317359),
                                'daa4bbacf74bab652f0a': registry.Entry(actor=L1981,
                                                                       timestamp=1109434477.727283),
                                '7451b642c3dd07bfa37e': registry.Entry(actor=L43,
                                                                       timestamp=1208019554.739883),
                                'c6395c42b17dc6409a98': registry.Entry(actor=L1984,
                                                                       timestamp=1108956695.183551),
                                'ce21e0cc674c8dff1aa1': registry.Entry(actor=L544,
                                                                       timestamp=1109428875.283223),
                                'f1b64b96203dc1031e47': registry.Entry(actor=L120,
                                                                       timestamp=1109433805.358014),
                                'f2761198c8015e58297d': registry.Entry(actor=L1988,
                                                                       timestamp=1109422775.036537),
                                '987ba6d80c536ef72fd3': registry.Entry(actor=L1990,
                                                                       timestamp=1104796957.85256),
                                '112755c6b7b0197ca6bb': registry.Entry(actor=L2059,
                                                                       timestamp=1105921513.578842),
                                '335fd96b953d2239db53': registry.Entry(actor=L126,
                                                                       timestamp=1109433926.719766),
                                '2c4f6289354906ecf08': registry.Entry(actor=L1037,
                                                                      timestamp=1109424447.449366),
                                '11512313525346285370': registry.Entry(actor=L2063,
                                                                       timestamp=1104730109.340476),
                                '477d1d63d2661835065d': registry.Entry(actor=L2065,
                                                                       timestamp=1105921513.564682),
                                '14095783355500097386': registry.Entry(actor=L2067,
                                                                       timestamp=1104633023.253555),
                                '84af1be6f390fc4f0d92': registry.Entry(actor=L1240,
                                                                       timestamp=1108412234.059459),
                                '76105c3de42692569c7f': registry.Entry(actor=L334,
                                                                       timestamp=1190665257.473807),
                                'c97d9bb0c2aa5df61e6e': registry.Entry(actor=L2071,
                                                                       timestamp=1108412101.454735),
                                'dc10179ce6eb719eddec': registry.Entry(actor=L600,
                                                                       timestamp=1105921587.34643),
                                '132bd817a0e8acb0485e': registry.Entry(actor=L717,
                                                                       timestamp=1108956833.158008),
                                '40e51ffc174da6c81c4f': registry.Entry(actor=L2075,
                                                                       timestamp=1108412101.37217),
                                '5292533547202728044': registry.Entry(actor=L2077,
                                                                      timestamp=1104730442.789497),
                                'e5fb3e230d899e6a15ec': registry.Entry(actor=L44,
                                                                       timestamp=1208019537.388496),
                                'f84c449eddb7e174f514': registry.Entry(actor=L541,
                                                                       timestamp=1108956539.883023),
                                '16495268673511082035': registry.Entry(actor=L1907,
                                                                       timestamp=1104795314.047692),
                                '89b4ca205464b571e41e': registry.Entry(actor=L2114,
                                                                       timestamp=1109428157.539534),
                                '8a9f1ac419253f7817c7': registry.Entry(actor=L2119,
                                                                       timestamp=1105921826.428624),
                                '9462070805789713288': registry.Entry(actor=L2121,
                                                                      timestamp=1104650549.652365),
                                '15604201270503278878': registry.Entry(actor=L2123,
                                                                       timestamp=1104632228.343614),
                                '12079799893167868995': registry.Entry(actor=L450,
                                                                       timestamp=1104693742.130242),
                                'daf060d1d66ad487dee3': registry.Entry(actor=L287,
                                                                       timestamp=1109435117.514183),
                                'c88c9deae9a8bad90c4': registry.Entry(actor=L331,
                                                                      timestamp=1190664334.047466),
                                '5217137786238671049': registry.Entry(actor=L2128,
                                                                      timestamp=1104632241.948234),
                                '1f966172227f701d36a1': registry.Entry(actor=L2130,
                                                                       timestamp=1109434798.857053),
                                '7522505065968084182': registry.Entry(actor=L2132,
                                                                      timestamp=1104730507.792691),
                                '2ce2546b3a61d585544e': registry.Entry(actor=L871,
                                                                       timestamp=1108412161.584934),
                                '10579116576104148034': registry.Entry(actor=L2135,
                                                                       timestamp=1104632797.633367),
                                'bc6686a069873608f287': registry.Entry(actor=L155,
                                                                       timestamp=1109434503.006452),
                                'cac21146f6ccd1384dcb': registry.Entry(actor=L2138,
                                                                       timestamp=1108956794.639223),
                                '12427553908187455670': registry.Entry(actor=L2140,
                                                                       timestamp=1104730109.330364),
                                '4edd14e178ad0c694a5f': registry.Entry(actor=L1767,
                                                                       timestamp=1104807944.347418),
                                '1f894cedda7a5116c672': registry.Entry(actor=L86,
                                                                       timestamp=1109433555.511094),
                                '11346868527983282560': registry.Entry(actor=L2144,
                                                                       timestamp=1104632803.657857),
                                '5b87ae2914a9f9836ec7': registry.Entry(actor=L42,
                                                                       timestamp=1208019554.739634),
                                '7c9da28e49e64a268faa': registry.Entry(actor=L2148,
                                                                       timestamp=1208019245.829235),
                                '12280374078573952893': registry.Entry(actor=L403,
                                                                       timestamp=1104689747.038848),
                                '5186614581370432354': registry.Entry(actor=L525,
                                                                      timestamp=1104730776.194409),
                                'd3fa83e2175f56e2183f': registry.Entry(actor=L2152,
                                                                       timestamp=1109434779.069316),
                                '3719337025926476596': registry.Entry(actor=L1525,
                                                                      timestamp=1104650549.629279),
                                '7708682ba51a597e4483': registry.Entry(actor=L2115,
                                                                       timestamp=1109427882.698358),
                                '3d7fe3f0661198add7d2': registry.Entry(actor=L2156,
                                                                       timestamp=1108956216.001841),
                                'b6d022a6aab1a9c58c67': registry.Entry(actor=L2158,
                                                                       timestamp=1105921513.599361),
                                '7838193153830263651': registry.Entry(actor=L2160,
                                                                      timestamp=1104730507.7985),
                                '994f72d124ba4ab3e643': registry.Entry(actor=L1944,
                                                                       timestamp=1109435124.707993),
                                '5ee3a50d3351e3b67fd4': registry.Entry(actor=L2163,
                                                                       timestamp=1104807950.901929),
                                '10584963968992807980': registry.Entry(actor=L2078,
                                                                       timestamp=1104730109.300018),
                                '63af8fe6397a4ec62ec8': registry.Entry(actor=L928,
                                                                       timestamp=1104807978.85042),
                                '202f42bea33bd7dcb5c7': registry.Entry(actor=L2167,
                                                                       timestamp=1105921808.811406),
                                '129f5ab2812ebd35a6f3': registry.Entry(actor=L725,
                                                                       timestamp=1108956527.024495),
                                '8d2fd9ab021f90ee5c23': registry.Entry(actor=L34,
                                                                       timestamp=1208019541.593894),
                                '2737335135250149149': registry.Entry(actor=L499,
                                                                      timestamp=1104650724.131162),
                                'cf3306171571f5115689': registry.Entry(actor=L2172,
                                                                       timestamp=1109435018.505995),
                                '15550032082523474268': registry.Entry(actor=L2174,
                                                                       timestamp=1104650556.44932),
                                'a9cb48105a7013552f52': registry.Entry(actor=L885,
                                                                       timestamp=1108412234.392565),
                                '1245e3bda58496bdf7e7': registry.Entry(actor=L660,
                                                                       timestamp=1105921513.464356),
                                '1347a00d734365bfd85e': registry.Entry(actor=L2178,
                                                                       timestamp=1108956747.616488),
                                '3491372217552124879': registry.Entry(actor=L2180,
                                                                      timestamp=1104694604.203154),
                                '13101820419664547343': registry.Entry(actor=L2182,
                                                                       timestamp=1104632307.775392),
                                '48c31983ab36c2b93869': registry.Entry(actor=L2184,
                                                                       timestamp=1109422775.113838),
                                '2226060574216469791': registry.Entry(actor=L2186,
                                                                      timestamp=1104795314.147552),
                                '9191949582763768590': registry.Entry(actor=L2188,
                                                                      timestamp=1104732153.443767),
                                '11009507096081710421': registry.Entry(actor=L1623,
                                                                       timestamp=1104650949.250332),
                                'd6b5b4340e8822d2762c': registry.Entry(actor=L1314,
                                                                       timestamp=1109434804.450887),
                                '11031015219216838346': registry.Entry(actor=L2192,
                                                                       timestamp=1104730109.341886),
                                'bb790ac1a0ee7ed3ea5b': registry.Entry(actor=L2194,
                                                                       timestamp=1109434798.854404),
                                '1d9f30f9466014fd9845': registry.Entry(actor=L2196,
                                                                       timestamp=1208019245.829621),
                                'c136252aeda06b05ab25': registry.Entry(actor=L2198,
                                                                       timestamp=1108412101.447733),
                                'd81a12a2169de556f93d': registry.Entry(actor=L2200,
                                                                       timestamp=1108956488.748338),
                                '8096643624464055522': registry.Entry(actor=L797,
                                                                      timestamp=1104633049.924382),
                                '40e992d83eee6dfcc7a5': registry.Entry(actor=L892,
                                                                       timestamp=1108412101.367299),
                                'c16a270d21302658f53d': registry.Entry(actor=L706,
                                                                       timestamp=1108956776.0309),
                                '35b913d9f1a9ff04226a': registry.Entry(actor=L2205,
                                                                       timestamp=1109435098.701615),
                                '3112541654131017587': registry.Entry(actor=L1146,
                                                                      timestamp=1104633023.253822),
                                '310e5faab910f546eb10': registry.Entry(actor=L2208,
                                                                       timestamp=1109434795.853103),
                                '33c2fbb146d136f5d402': registry.Entry(actor=L2210,
                                                                       timestamp=1109428835.811226),
                                '14245085994013281857': registry.Entry(actor=L2212,
                                                                       timestamp=1104640325.666951),
                                '18d8a761281277ebaf47': registry.Entry(actor=L2214,
                                                                       timestamp=1208019607.90014),
                                '16622057499147950833': registry.Entry(actor=L426,
                                                                       timestamp=1104697074.970148),
                                '10084807298204554591': registry.Entry(actor=L2217,
                                                                       timestamp=1104730507.84133),
                                '2553436941368336606': registry.Entry(actor=L2145,
                                                                      timestamp=1104632803.657435),
                                '8343b425fd8ebf32117': registry.Entry(actor=L1818,
                                                                      timestamp=1105921548.351846),
                                '6752b9d510ea35cf88d9': registry.Entry(actor=L2221,
                                                                       timestamp=1190664334.057488),
                                '18af9ec7344533271914': registry.Entry(actor=L1329,
                                                                       timestamp=1109435018.501241),
                                '16060064330232869464': registry.Entry(actor=L2224,
                                                                       timestamp=1104730109.30314)},
                         editor_of_actor={L904: L935,
                                          L511: L510,
                                          L2115: L2114,
                                          L1117: L1405,
                                          L501: L515,
                                          L163: L1599,
                                          L678: L1207,
                                          L1623: L1622,
                                          L502: L1583,
                                          L1423: L1576,
                                          L97: L1522,
                                          L711: L1963,
                                          L490: L1018,
                                          L282: L1383,
                                          L1257: L2071,
                                          L923: L1520,
                                          L387: L1607,
                                          L547: L546,
                                          L1044: L1043,
                                          L118: L1981,
                                          L2130: L2194,
                                          L329: L999,
                                          L28: L2148,
                                          L693: L2138,
                                          L795: L1813,
                                          L764: L851,
                                          L929: L1954,
                                          L1088: L2217,
                                          L116: L2152,
                                          L640: L2158,
                                          L463: L1746,
                                          L315: L1646,
                                          L303: L2221,
                                          L265: L1815,
                                          L1393: L1588,
                                          L771: L1737,
                                          L742: L1402,
                                          L513: L1961,
                                          L778: L1950,
                                          L626: L1414,
                                          L1426: L1592,
                                          L520: L519,
                                          L978: L1027,
                                          L903: L1618,
                                          L177: L2172,
                                          L379: L378,
                                          L172: L1573,
                                          L476: L1564,
                                          L178: L2205,
                                          L3: L2,
                                          L1770: L1811,
                                          L17: L2196,
                                          L1417: L1422,
                                          L1314: L1313,
                                          L1991: L1990,
                                          L1472: L1471,
                                          L555: L554,
                                          L1571: L1570,
                                          L793: L1505,
                                          L302: L1648,
                                          L1065: L1410,
                                          L1560: L1559,
                                          L1112: L1111,
                                          L614: L2065,
                                          L276: L1843,
                                          L670: L669,
                                          L770: L1198,
                                          L1076: L2160,
                                          L1902: L1907,
                                          L972: L2214,
                                          L1040: L1039,
                                          L625: L1841,
                                          L293: L292,
                                          L960: L1008,
                                          L261: L1590,
                                          L743: L1212,
                                          L1132: L1792,
                                          L1329: L1748,
                                          L63: L62,
                                          L314: L1512,
                                          L402: L406,
                                          L198: L1938,
                                          L400: L1051,
                                          L1653: L1652,
                                          L382: L381,
                                          L981: L980,
                                          L34: L1181,
                                          L1934: L2186,
                                          L690: L1272,
                                          L346: L1173,
                                          L407: L1845,
                                          L541: L540,
                                          L715: L1975,
                                          L825: L824,
                                          L339: L1054,
                                          L1146: L2067,
                                          L932: L931,
                                          L679: L1318,
                                          L888: L1214,
                                          L895: L1320,
                                          L1480: L1899,
                                          L1828: L1827,
                                          L497: L1611,
                                          L1562: L1820,
                                          L470: L1464,
                                          L863: L2075,
                                          L2135: L2182,
                                          L801: L2123,
                                          L37: L1224,
                                          L732: L2198,
                                          L179: L1033,
                                          L277: L2210,
                                          L704: L1744,
                                          L263: L1566,
                                          L550: L549,
                                          L804: L2128,
                                          L29: L1408,
                                          L759: L758,
                                          L664: L663,
                                          L1277: L1276,
                                          L1176: L2119,
                                          L658: L1331,
                                          L797: L1387,
                                          L86: L2184,
                                          L401: L1967,
                                          L203: L1585,
                                          L499: L1556,
                                          L2145: L2144,
                                          L1227: L1226,
                                          L573: L937,
                                          L2078: L2077,
                                          L947: L1808,
                                          L334: L856,
                                          L159: L1274,
                                          L251: L522,
                                          L838: L1936,
                                          L394: L1971,
                                          L222: L226,
                                          L1324: L1620,
                                          L1270: L2188,
                                          L529: L528,
                                          L32: L60,
                                          L918: L1190,
                                          L473: L1395,
                                          L393: L1850,
                                          L1030: L1029,
                                          L248: L1188,
                                          L723: L1730,
                                          L1060: L1059,
                                          L1235: L1240,
                                          L878: L1507,
                                          L574: L1735,
                                          L1762: L1767,
                                          L730: L729,
                                          L808: L807,
                                          L864: L1601,
                                          L42: L1895,
                                          L565: L2174,
                                          L332: L1380,
                                          L140: L1977,
                                          L1376: L1375,
                                          L1861: L1860,
                                          L898: L1837,
                                          L437: L1218,
                                          L600: L599,
                                          L111: L975,
                                          L1944: L1943,
                                          L79: L1232,
                                          L1869: L1948,
                                          L408: L1728,
                                          L1020: L1847,
                                          L816: L815,
                                          L1818: L1817,
                                          L1165: L2212,
                                          L1364: L2063,
                                          L1075: L1222,
                                          L108: L1195,
                                          L1037: L1036,
                                          L1336: L1335,
                                          L244: L1973,
                                          L467: L2180,
                                          L1200: L1643,
                                          L1006: L1005,
                                          L500: L1757,
                                          L820: L819,
                                          L208: L1010,
                                          L446: L1952,
                                          L1371: L1722,
                                          L1795: L1794,
                                          L1178: L2178,
                                          L1349: L1979,
                                          L653: L1023,
                                          L1439: L1753,
                                          L939: L944,
                                          L287: L286,
                                          L337: L1385,
                                          L859: L858,
                                          L1477: L1594,
                                          L900: L928,
                                          L280: L1192,
                                          L180: L1461,
                                          L1832: L1831,
                                          L295: L345,
                                          L1866: L1988,
                                          L1603: L1751,
                                          L1102: L2132,
                                          L1579: L1578,
                                          L588: L1726,
                                          L56: L55,
                                          L890: L1322,
                                          L349: L853,
                                          L1453: L2200,
                                          L532: L531,
                                          L566: L2121,
                                          L893: L1216,
                                          L702: L1984,
                                          L2083: L2224,
                                          L1389: L1946,
                                          L1296: L2059,
                                          L525: L524,
                                          L1087: L1742,
                                          L1184: L1183,
                                          L183: L2208,
                                          L1244: L1797,
                                          L559: L1412,
                                          L533: L2156,
                                          L1013: L1802,
                                          L839: L1016,
                                          L1104: L1805,
                                          L1399: L1398,
                                          L362: L1834,
                                          L1823: L1822,
                                          L828: L1025,
                                          L921: L2163,
                                          L1002: L1001,
                                          L1614: L1613,
                                          L1230: L2167,
                                          L779: L1732,
                                          L227: L822,
                                          L1175: L1958,
                                          L254: L1609,
                                          L6: L1518,
                                          L604: L1650,
                                          L504: L552,
                                          L1241: L1467,
                                          L68: L67,
                                          L2098: L2140,
                                          L590: L1210,
                                          L544: L543,
                                          L109: L187,
                                          L174: L1941,
                                          L1525: L1524,
                                          L1350: L2192,
                                          L16: L376,
                                          L96: L284},
                         accounts=['4227047065147840205',
                                   '8511836882149982016',
                                   '15354271914547105265',
                                   '5292533547202728044',
                                   '16495268673511082035',
                                   'CCDF40493E712274L',
                                   '987ba6d80c536ef72fd3',
                                   '4edd14e178ad0c694a5f',
                                   '959c6923ca073aa23ec2',
                                   '84af1be6f390fc4f0d92',
                                   '7aa131ceb0eae191a3ed',
                                   '740e543a73fba8ae453f',
                                   '6737ab2d99858d2cb98e',
                                   '5b74f62f6857b7956095'])
L645 = actors.Actor(env=envs.Env(parent=L602),
                    script=L647)
L883 = actors.Actor(env=envs.Env(parent=L862),
                    script=L885)
L170 = envs.Env(parent=L141)
L168 = actors.Actor(env=envs.Env(parent=L170),
                    script=L145)

L4.define(var='box',
          value=L28)

L4.define(var='makemailbox',
           value=L3)

L4.define(var='Foo',
           value=L29)

L4.define(var='maildirectory',
           value=L32)

L4.define(var='mailbox',
           value=L34)

L5.define(var='false',
           value=L6)

L5.define(var='numberguard',
           value=builtin.TypeGuard(sample_instance=0))

L5.define(var='listguard',
           value=builtin.TypeGuard(sample_instance=()))

L5.define(var='makestamp',
           value=builtin.StampMaker())

L5.define(var='booleanguard',
           value=builtin.TypeGuard(sample_instance=True))

L5.define(var='makebox',
           value=L16)

L5.define(var='true',
           value=L17)

L5.define(var='stringguard',
           value=builtin.TypeGuard(sample_instance=''))

L5.define(var='if',
           value=actors.Actor(env=L5,
                              script=actors.Script(next_serial_id=1,
                                                   elements=[actors.Method(selector='true:then:else:',
                                                                           parameters=['test',
                                                                                       'yes',
                                                                                       'no'],
                                                                           body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                  inner_map={}),
                                                                           serial_id=0)])))

L81.define(var='query',
            value=L276)

L81.define(var='onyes',
            value=L277)

L81.define(var='onno',
            value=L265)

L81.define(var='yesnoquestion',
            value=L79)

L83.define(var='makequestion',
            value=L265)

L83.define(var='makeguess',
            value=L244)

L83.define(var='gamebox',
            value=L227)

L84.define(var='box',
            value=L108)

L84.define(var='newanimalgame',
            value=L109)

L84.define(var='makemailbox',
            value=L208)

L84.define(var='animalgame',
            value=L222)

L84.define(var='mailbox',
            value=L254)

L84.define(var='maildirectory',
            value=L261)

L84.define(var='Foo',
            value=L263)

L85.define(var='false',
            value=L86)

L85.define(var='numberguard',
            value=builtin.TypeGuard(sample_instance=0))

L85.define(var='listguard',
            value=builtin.TypeGuard(sample_instance=()))

L85.define(var='makestamp',
            value=builtin.StampMaker())

L85.define(var='booleanguard',
            value=builtin.TypeGuard(sample_instance=True))

L85.define(var='makebox',
            value=L96)

L85.define(var='true',
            value=L97)

L85.define(var='stringguard',
            value=builtin.TypeGuard(sample_instance=''))

L85.define(var='if',
            value=actors.Actor(env=L85,
                               script=actors.Script(next_serial_id=1,
                                                    elements=[actors.Method(selector='true:then:else:',
                                                                            parameters=['test',
                                                                                        'yes',
                                                                                        'no'],
                                                                            body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                   inner_map={}),
                                                                            serial_id=0)])))

L289.define(var='node',
             value=L179)

L289.define(var='guesser',
             value=L287)

L182.define(var='guessernode',
             value=L180)

L182.define(var='animal',
             value=L183)

L110.define(var='playgame',
             value=L111)

L110.define(var='call',
             value=L116)

L110.define(var='makebranch',
             value=L118)

L110.define(var='makeguess',
             value=L140)

L110.define(var='root',
             value=L159)

L296.define(var='box',
             value=L314)

L296.define(var='makemailbox',
             value=L315)

L296.define(var='Foo',
             value=L329)

L296.define(var='maildirectory',
             value=L332)

L296.define(var='mailbox',
             value=L339)

L297.define(var='false',
             value=L68)

L297.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L297.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L297.define(var='makestamp',
             value=builtin.StampMaker())

L297.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L297.define(var='makebox',
             value=L302)

L297.define(var='true',
             value=L303)

L297.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L297.define(var='if',
             value=actors.Actor(env=L297,
                                script=actors.Script(next_serial_id=1,
                                                     elements=[actors.Method(selector='true:then:else:',
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0)])))

L343._add_result(actor=L345,
                  result=L346)

L347._add_result(actor=L345,
                  result=L349)

L351._add_result(actor=L345,
                  result=L329)

L354._add_result(actor=L345,
                  result=L314)

L356._add_result(actor=L345,
                  result=L303)

L358._add_result(actor=L345,
                  result=L68)

L360._add_result(actor=L345,
                  result=L362)

L365._add_result(actor=L345,
                  result=L332)

L368._add_result(actor=L345,
                  result=L339)

L373._add_result(actor=L345,
                  result=L303)

L384.define(var='htmlguard',
             value=L408)

L384.define(var='markup',
             value=L437)

L384.define(var='html',
             value=L446)

L384.define(var='stamppair',
             value=L407)

L384.define(var='htmlstamp',
             value=L56)

L384.define(var='makeattr',
             value=L382)

L384.define(var='showattr',
             value=L463)

L385.define(var='box',
             value=L401)

L385.define(var='htmlmodule',
             value=L402)

L385.define(var='makemailbox',
             value=L476)

L385.define(var='mailbox',
             value=L490)

L385.define(var='maildirectory',
             value=L497)

L385.define(var='pair',
             value=L499)

L385.define(var='x',
             value=L502)

L385.define(var='Foo',
             value=L504)

L386.define(var='false',
             value=L387)

L386.define(var='makestamp',
             value=L393)

L386.define(var='true',
             value=L394)

L386.define(var='makebox',
             value=L379)

L386.define(var='listguard',
             value=L400)

L557.define(var='box',
             value=L573)

L557.define(var='makemailbox',
             value=L574)

L557.define(var='Foo',
             value=L555)

L557.define(var='maildirectory',
             value=L588)

L557.define(var='mailbox',
             value=L590)

L558.define(var='false',
             value=L559)

L558.define(var='makestamp',
             value=L565)

L558.define(var='true',
             value=L566)

L558.define(var='makebox',
             value=L293)

L558.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L602.define(var='box',
             value=L625)

L602.define(var='makemailbox',
             value=L626)

L602.define(var='mailbox',
             value=L640)

L602.define(var='makeballot',
             value=L653)

L602.define(var='maildirectory',
             value=L658)

L602.define(var='message',
             value=L645)

L602.define(var='Foo',
             value=L600)

L603.define(var='false',
             value=L604)

L603.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L603.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L603.define(var='makestamp',
             value=builtin.StampMaker())

L603.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L603.define(var='makebox',
             value=L511)

L603.define(var='true',
             value=L614)

L603.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L603.define(var='if',
             value=actors.Actor(env=L603,
                                script=actors.Script(next_serial_id=1,
                                                     elements=[actors.Method(selector='true:then:else:',
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0)])))

L666.define(var='node',
             value=L159)

L666.define(var='asker',
             value=L664)

L162.define(var='yesbox',
             value=L163)

L162.define(var='askernode',
             value=L160)

L162.define(var='question',
             value=L178)

L162.define(var='nobox',
             value=L179)

L672.define(var='box',
             value=L532)

L672.define(var='sender',
             value=L690)

L672.define(var='makemailbox',
             value=L711)

L672.define(var='mailbox',
             value=L693)

L672.define(var='makeballot',
             value=L715)

L672.define(var='maildirectory',
             value=L723)

L672.define(var='message',
             value=L704)

L672.define(var='Foo',
             value=L670)

L673.define(var='false',
             value=L533)

L673.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L673.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L673.define(var='makestamp',
             value=builtin.StampMaker())

L673.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L673.define(var='makebox',
             value=L678)

L673.define(var='true',
             value=L679)

L673.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L673.define(var='if',
             value=actors.Actor(env=L673,
                                script=actors.Script(next_serial_id=1,
                                                     elements=[actors.Method(selector='true:then:else:',
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0)])))

L731.define(var='false',
             value=L732)

L731.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L731.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L731.define(var='makestamp',
             value=builtin.StampMaker())

L731.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L731.define(var='makebox',
             value=L742)

L731.define(var='true',
             value=L743)

L731.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L731.define(var='if',
             value=actors.Actor(env=L731,
                                script=actors.Script(next_serial_id=1,
                                                     elements=[actors.Method(selector='true:then:else:',
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0)])))

L200.define(var='node',
             value=L159)

L200.define(var='guesser',
             value=L198)

L761.define(var='sender',
             value=L759)

L761.define(var='inbox',
             value=L804)

L761.define(var='mailbox',
             value=L793)

L762.define(var='box',
             value=L778)

L762.define(var='makemailbox',
             value=L779)

L762.define(var='mailbox',
             value=L793)

L762.define(var='maildirectory',
             value=L795)

L762.define(var='message',
             value=L797)

L762.define(var='Foo',
             value=L801)

L762.define(var='tome',
             value=L759)

L763.define(var='true',
             value=L764)

L763.define(var='makebox',
             value=L770)

L763.define(var='false',
             value=L771)

L763.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L827.define(var='false',
             value=L828)

L827.define(var='numberguard',
             value=builtin.TypeGuard(sample_instance=0))

L827.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L827.define(var='makestamp',
             value=builtin.StampMaker())

L827.define(var='booleanguard',
             value=builtin.TypeGuard(sample_instance=True))

L827.define(var='makebox',
             value=L838)

L827.define(var='true',
             value=L839)

L827.define(var='stringguard',
             value=builtin.TypeGuard(sample_instance=''))

L827.define(var='if',
             value=actors.Actor(env=L827,
                                script=actors.Script(next_serial_id=1,
                                                     elements=[actors.Method(selector='true:then:else:',
                                                                             parameters=['test',
                                                                                         'yes',
                                                                                         'no'],
                                                                             body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                    inner_map={}),
                                                                             serial_id=0)])))

L336.define(var='inbox',
             value=L337)

L336.define(var='sender',
             value=L334)

L336.define(var='mailbox',
             value=L339)

L861.define(var='inbox',
             value=L893)

L861.define(var='sender',
             value=L895)

L861.define(var='mailbox',
             value=L859)

L862.define(var='box',
             value=L863)

L862.define(var='makemailbox',
             value=L864)

L862.define(var='mailbox',
             value=L878)

L862.define(var='maildirectory',
             value=L888)

L862.define(var='message',
             value=L883)

L862.define(var='Foo',
             value=L890)

L902.define(var='box',
             value=L903)

L902.define(var='makemailbox',
             value=L904)

L902.define(var='Foo',
             value=L900)

L902.define(var='mailbox',
             value=L918)

L902.define(var='maildirectory',
             value=L825)

L926._add_result(actor=L928,
                  result=L929)

L942._add_result(actor=L944,
                  result=L550)

L945._add_result(actor=L944,
                  result=L947)

L949._add_result(actor=L944,
                  result=L29)

L952._add_result(actor=L944,
                  result=L28)

L954._add_result(actor=L944,
                  result=L17)

L956._add_result(actor=L944,
                  result=L6)

L958._add_result(actor=L944,
                  result=L960)

L963._add_result(actor=L944,
                  result=L32)

L966._add_result(actor=L944,
                  result=L34)

L970._add_result(actor=L944,
                  result=L972)

L982.define(var='true',
             value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                        elements=[actors.Method(selector='not',
                                                                                parameters=[],
                                                                                body=actors.Expression(text='false',
                                                                                                       inner_map={}),
                                                                                serial_id=0),
                                                                  actors.Method(selector='iftrue:iffalse:',
                                                                                parameters=['trueaction',
                                                                                            'falseaction'],
                                                                                body=actors.Expression(text='trueaction run',
                                                                                                       inner_map={}),
                                                                                serial_id=1)]),
                                   value=True))

L982.define(var='makebox',
             value=builtin.BoxMaker())

L982.define(var='false',
             value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                        elements=[actors.Method(selector='not',
                                                                                parameters=[],
                                                                                body=actors.Expression(text='true',
                                                                                                       inner_map={}),
                                                                                serial_id=0),
                                                                  actors.Method(selector='iftrue:iffalse:',
                                                                                parameters=['trueaction',
                                                                                            'falseaction'],
                                                                                body=actors.Expression(text='falseaction run',
                                                                                                       inner_map={}),
                                                                                serial_id=1)]),
                                   value=False))

L982.define(var='listguard',
             value=builtin.TypeGuard(sample_instance=()))

L492.define(var='mailbox',
             value=L490)

L492.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L492),
                                script=L480))

L492.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L692.define(var='mailbox',
             value=L693)

L692.define(var='sender',
             value=L690)

L692.define(var='inbox',
             value=L702)

L404._add_result(actor=L406,
                  result=L407)

L409._add_result(actor=L406,
                  result=L56)

L411._add_result(actor=L406,
                  result=L408)

L413._add_result(actor=L406,
                  result=L437)

L439._add_result(actor=L406,
                  result=L446)

L448._add_result(actor=L406,
                  result=L382)

L457._add_result(actor=L406,
                  result=L463)

L465._add_result(actor=L406,
                  result=L467)

L468._add_result(actor=L406,
                  result=L470)

L471._add_result(actor=L406,
                  result=L473)

L474._add_result(actor=L406,
                  result='Error: No matching method: show')

L1062.define(var='sender',
              value=actors.Actor(env=envs.Env(parent=L1062),
                                 script=L1092))

L1062.define(var='inbox',
              value=builtin.Box(initial_value=builtin.List(elements=())))

L1062.define(var='mailbox',
              value=L1060)

L1063.define(var='box',
              value=L1087)

L1063.define(var='makemailbox',
              value=L1088)

L1063.define(var='Foo',
              value=L1102)

L1063.define(var='maildirectory',
              value=L1104)

L1063.define(var='mailbox',
              value=L1060)

L1064.define(var='false',
              value=L1065)

L1064.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1064.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1064.define(var='makestamp',
              value=builtin.StampMaker())

L1064.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1064.define(var='makebox',
              value=L1075)

L1064.define(var='true',
              value=L1076)

L1064.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1064.define(var='if',
              value=actors.Actor(env=L1064,
                                 script=actors.Script(next_serial_id=1,
                                                      elements=[actors.Method(selector='true:then:else:',
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0)])))

L1115._add_result(actor=L1111,
                   result=L1117)

L1118._add_result(actor=L1111,
                   result=L529)

L1121._add_result(actor=L1111,
                   result=L801)

L1124._add_result(actor=L1111,
                   result=L778)

L1126._add_result(actor=L1111,
                   result=L764)

L1128._add_result(actor=L1111,
                   result=L771)

L1130._add_result(actor=L1111,
                   result=L1132)

L1135._add_result(actor=L1111,
                   result=L795)

L1138._add_result(actor=L1111,
                   result=L793)

L1142._add_result(actor=L1111,
                   result=L759)

L1144._add_result(actor=L1111,
                   result=L1146)

L1163._add_result(actor=L1111,
                   result=L1165)

L1166._add_result(actor=L1111,
                   result='Error: exceptions.ZeroDivisionError: float division')

L1168._add_result(actor=L1111,
                   result='Error: Unbound: makestamp')

L36.define(var='sender',
            value=L37)

L36.define(var='inbox',
            value=L42)

L36.define(var='mailbox',
            value=L34)

L250.define(var='box',
             value=L227)

L250.define(var='guess',
             value=L248)

L250.define(var='animal',
             value=L251)

L920.define(var='mailbox',
             value=L918)

L920.define(var='inbox',
             value=L921)

L920.define(var='sender',
             value=L923)

L1202.define(var='query',
              value=builtin.String(str='Does it bark?'))

L1202.define(var='question',
              value=L1200)

L1202.define(var='animal',
              value=builtin.String(str='dog'))

L592.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L592.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L592),
                                script=L578))

L592.define(var='mailbox',
             value=L590)

L1238._add_result(actor=L1240,
                   result=L1241)

L1242._add_result(actor=L1240,
                   result=L1244)

L1246._add_result(actor=L1240,
                   result=L890)

L1249._add_result(actor=L1240,
                   result=L863)

L1251._add_result(actor=L1240,
                   result=L743)

L1253._add_result(actor=L1240,
                   result=L732)

L1255._add_result(actor=L1240,
                   result=L1257)

L1260._add_result(actor=L1240,
                   result=L888)

L1263._add_result(actor=L1240,
                   result=L878)

L1267._add_result(actor=L1240,
                   result=L730)

L1280._add_result(actor=L1276,
                   result=L898)

L1282._add_result(actor=L1276,
                   result=L547)

L1285._add_result(actor=L1276,
                   result=L600)

L1288._add_result(actor=L1276,
                   result=L625)

L1290._add_result(actor=L1276,
                   result=L614)

L1292._add_result(actor=L1276,
                   result=L604)

L1294._add_result(actor=L1276,
                   result=L1296)

L1299._add_result(actor=L1276,
                   result=L658)

L1302._add_result(actor=L1276,
                   result=L640)

L1306._add_result(actor=L1276,
                   result=L1013)

L1308._add_result(actor=L1276,
                   result='Error: Unbound: makek')

L1310._add_result(actor=L1276,
                   result=L653)

L1316.define(var='terminus',
              value=L1314)

L1326.define(var='terminus',
              value=L1324)

L1328.define(var='node',
              value=L163)

L1328.define(var='guesser',
              value=L1329)

L176.define(var='guessernode',
             value=L174)

L176.define(var='animal',
             value=L177)

L1338.define(var='box',
              value=L1349)

L1338.define(var='makemailbox',
              value=L1350)

L1338.define(var='Foo',
              value=L1336)

L1338.define(var='mailbox',
              value=L1364)

L1338.define(var='maildirectory',
              value=L1371)

L1339.define(var='false',
              value=L808)

L1339.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1339.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1339.define(var='makestamp',
              value=builtin.StampMaker())

L1339.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1339.define(var='makebox',
              value=L1040)

L1339.define(var='true',
              value=L1044)

L1339.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1339.define(var='if',
              value=actors.Actor(env=L1339,
                                 script=actors.Script(next_serial_id=1,
                                                      elements=[actors.Method(selector='true:then:else:',
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0)])))

L333.define(var='alice',
             value=L334)

L1391.define(var='question',
              value=L1389)

L279.define(var='box',
             value=L227)

L279.define(var='guess',
             value=L277)

L279.define(var='animal',
             value=L280)

L185._add_result(actor=L187,
                  result=L116)

L188._add_result(actor=L187,
                  result=L118)

L190._add_result(actor=L187,
                  result=L140)

L192._add_result(actor=L187,
                  result='Error: No matching method: holding:')

L194._add_result(actor=L187,
                  result=L159)

L196._add_result(actor=L187,
                  result=L198)

L201._add_result(actor=L187,
                  result=L203)

L206._add_result(actor=L187,
                  result=L111)

L1420._add_result(actor=L1422,
                   result=L1423)

L1424._add_result(actor=L1422,
                   result=L1426)

L1428._add_result(actor=L1422,
                   result=L670)

L1431._add_result(actor=L1422,
                   result=L532)

L1433._add_result(actor=L1422,
                   result=L679)

L1435._add_result(actor=L1422,
                   result=L533)

L1437._add_result(actor=L1422,
                   result=L1439)

L1442._add_result(actor=L1422,
                   result=L723)

L1445._add_result(actor=L1422,
                   result=L693)

L1449._add_result(actor=L1422,
                   result='Error: No matching method: size')

L1451._add_result(actor=L1422,
                   result=L1453)

L1454._add_result(actor=L1422,
                   result=L690)

L1456._add_result(actor=L1422,
                   result=L1178)

L1458._add_result(actor=L1422,
                   result=L715)

L1475._add_result(actor=L1471,
                   result=L1477)

L1478._add_result(actor=L1471,
                   result=L1480)

L1482._add_result(actor=L1471,
                   result=L504)

L1485._add_result(actor=L1471,
                   result=L401)

L1487._add_result(actor=L1471,
                   result=L394)

L1489._add_result(actor=L1471,
                   result=L387)

L1491._add_result(actor=L1471,
                   result=L932)

L1494._add_result(actor=L1471,
                   result=L497)

L1497._add_result(actor=L1471,
                   result=L490)

L1501._add_result(actor=L1471,
                   result=L402)

L880.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=(L883,))))

L880.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L880),
                                script=L868))

L880.define(var='mailbox',
             value=L878)

L224._add_result(actor=L226,
                  result=L227)

L228._add_result(actor=L226,
                  result=L244)

L246._add_result(actor=L226,
                  result=L248)

L252._add_result(actor=L226,
                  result=L79)

L1528._add_result(actor=L1524,
                   result=L1184)

L1530._add_result(actor=L1524,
                   result=L1227)

L1533._add_result(actor=L1524,
                   result=L555)

L1536._add_result(actor=L1524,
                   result=L573)

L1538._add_result(actor=L1524,
                   result=L566)

L1540._add_result(actor=L1524,
                   result=L559)

L1542._add_result(actor=L1524,
                   result=L816)

L1545._add_result(actor=L1524,
                   result=L588)

L1548._add_result(actor=L1524,
                   result=L590)

L1552._add_result(actor=L1524,
                   result='Error: exceptions.TypeError: unbound method __init__() must be called with Actor instance as first argument (got Stamp instance instead)')

L1581.define(var='question',
              value=L1579)

L205.define(var='node',
             value=L159)

L205.define(var='asker',
             value=L203)

L166.define(var='yesbox',
             value=builtin.Box(initial_value=L168))

L166.define(var='askernode',
             value=L164)

L166.define(var='question',
             value=L172)

L166.define(var='nobox',
             value=builtin.Box(initial_value=L174))

L256.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L256),
                                script=L212))

L256.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=())))

L256.define(var='mailbox',
             value=L254)

L1616.define(var='node',
              value=L163)

L1616.define(var='asker',
              value=L1614)

L1624.define(var='false',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 body=actors.Expression(text='falseaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=False))

L1624.define(var='makestamp',
              value=builtin.StampMaker())

L1624.define(var='true',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 body=actors.Expression(text='trueaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=True))

L1624.define(var='makebox',
              value=builtin.BoxMaker())

L1624.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1654.define(var='makemailbox',
              value=actors.Actor(env=L1654,
                                 script=actors.Script(next_serial_id=1,
                                                      elements=[actors.Method(selector='run',
                                                                              parameters=[],
                                                                              body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                                     inner_map={'sender': actors.Script(next_serial_id=1,
                                                                                                                                        elements=[actors.Method(selector='send:',
                                                                                                                                                                parameters=['message'],
                                                                                                                                                                body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                                                                                                                                       inner_map={}),
                                                                                                                                                                serial_id=0)]),
                                                                                                                'mailbox': actors.Script(next_serial_id=3,
                                                                                                                                         elements=[actors.Method(selector='first',
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 body=actors.Expression(text='inbox get at: 1',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=0),
                                                                                                                                                   actors.Method(selector='removefirst',
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=1),
                                                                                                                                                   actors.Method(selector='sender',
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 body=actors.Expression(text='sender',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=2)])}),
                                                                              serial_id=0)])))

L1654.define(var='maildirectory',
              value=builtin.MailDirectory(env=envs.Env(parent=L1655)))

L1655.define(var='false',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 body=actors.Expression(text='falsevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=False))

L1655.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1655.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1655.define(var='makestamp',
              value=builtin.StampMaker())

L1655.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1655.define(var='makebox',
              value=builtin.BoxMaker())

L1655.define(var='true',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 body=actors.Expression(text='truevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=True))

L1655.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1655.define(var='if',
              value=actors.Actor(env=L1655,
                                 script=actors.Script(next_serial_id=1,
                                                      elements=[actors.Method(selector='true:then:else:',
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0)])))

L1765._add_result(actor=L1767,
                   result=L820)

L1768._add_result(actor=L1767,
                   result=L1770)

L1772._add_result(actor=L1767,
                   result=L900)

L1775._add_result(actor=L1767,
                   result=L903)

L1777._add_result(actor=L1767,
                   result=L839)

L1779._add_result(actor=L1767,
                   result=L828)

L1781._add_result(actor=L1767,
                   result=L1030)

L1784._add_result(actor=L1767,
                   result=L825)

L1787._add_result(actor=L1767,
                   result=L918)

L1864._add_result(actor=L1860,
                   result=L1866)

L1867._add_result(actor=L1860,
                   result=L1869)

L1871._add_result(actor=L1860,
                   result=L263)

L1874._add_result(actor=L1860,
                   result=L108)

L1876._add_result(actor=L1860,
                   result=L97)

L1878._add_result(actor=L1860,
                   result=L86)

L1880._add_result(actor=L1860,
                   result=L1828)

L1883._add_result(actor=L1860,
                   result=L261)

L1886._add_result(actor=L1860,
                   result=L254)

L1890._add_result(actor=L1860,
                   result=L222)

L1892._add_result(actor=L1860,
                   result=L109)

L1905._add_result(actor=L1907,
                   result=L525)

L1908._add_result(actor=L1907,
                   result=L1795)

L1911._add_result(actor=L1907,
                   result=L1102)

L1914._add_result(actor=L1907,
                   result=L1087)

L1916._add_result(actor=L1907,
                   result=L1076)

L1918._add_result(actor=L1907,
                   result=L1065)

L1920._add_result(actor=L1907,
                   result=L1393)

L1923._add_result(actor=L1907,
                   result=L1104)

L1926._add_result(actor=L1907,
                   result=L1060)

L1930._add_result(actor=L1907,
                   result=L525)

L1932._add_result(actor=L1907,
                   result=L1934)

L1992.define(var='makemailbox',
              value=actors.Actor(env=L1992,
                                 script=actors.Script(next_serial_id=1,
                                                      elements=[actors.Method(selector='run',
                                                                              parameters=[],
                                                                              body=actors.Expression(text='let inbox = makebox holding: []. make sender. make mailbox',
                                                                                                     inner_map={'sender': actors.Script(next_serial_id=1,
                                                                                                                                        elements=[actors.Method(selector='send:',
                                                                                                                                                                parameters=['message'],
                                                                                                                                                                body=actors.Expression(text='inbox <- ([message] + inbox get)',
                                                                                                                                                                                       inner_map={}),
                                                                                                                                                                serial_id=0)]),
                                                                                                                'mailbox': actors.Script(next_serial_id=3,
                                                                                                                                         elements=[actors.Method(selector='first',
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 body=actors.Expression(text='inbox get at: 1',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=0),
                                                                                                                                                   actors.Method(selector='removefirst',
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 body=actors.Expression(text='inbox <- (inbox get from: 2)',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=1),
                                                                                                                                                   actors.Method(selector='sender',
                                                                                                                                                                 parameters=[],
                                                                                                                                                                 body=actors.Expression(text='sender',
                                                                                                                                                                                        inner_map={}),
                                                                                                                                                                 serial_id=2)])}),
                                                                              serial_id=0)])))

L1992.define(var='maildirectory',
              value=builtin.MailDirectory(env=envs.Env(parent=L1993)))

L1993.define(var='false',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 body=actors.Expression(text='falsevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=False))

L1993.define(var='numberguard',
              value=builtin.TypeGuard(sample_instance=0))

L1993.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L1993.define(var='makestamp',
              value=builtin.StampMaker())

L1993.define(var='booleanguard',
              value=builtin.TypeGuard(sample_instance=True))

L1993.define(var='makebox',
              value=builtin.BoxMaker())

L1993.define(var='true',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['truevalue',
                                                                                             'falsevalue'],
                                                                                 body=actors.Expression(text='truevalue',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=True))

L1993.define(var='stringguard',
              value=builtin.TypeGuard(sample_instance=''))

L1993.define(var='if',
              value=actors.Actor(env=L1993,
                                 script=actors.Script(next_serial_id=1,
                                                      elements=[actors.Method(selector='true:then:else:',
                                                                              parameters=['test',
                                                                                          'yes',
                                                                                          'no'],
                                                                              body=actors.Expression(text='booleanguard check: test. (test iftrue: yes iffalse: no) run',
                                                                                                     inner_map={}),
                                                                              serial_id=0)])))

L1366.define(var='mailbox',
              value=L1364)

L1366.define(var='sender',
              value=actors.Actor(env=envs.Env(parent=L1366),
                                 script=L1354))

L1366.define(var='inbox',
              value=builtin.Box(initial_value=builtin.List(elements=())))

L1147.define(var='false',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='true',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 body=actors.Expression(text='falseaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=False))

L1147.define(var='makebox',
              value=builtin.BoxMaker())

L1147.define(var='true',
              value=builtin.Boolean(script=actors.Script(next_serial_id=2,
                                                         elements=[actors.Method(selector='not',
                                                                                 parameters=[],
                                                                                 body=actors.Expression(text='false',
                                                                                                        inner_map={}),
                                                                                 serial_id=0),
                                                                   actors.Method(selector='iftrue:iffalse:',
                                                                                 parameters=['trueaction',
                                                                                             'falseaction'],
                                                                                 body=actors.Expression(text='trueaction run',
                                                                                                        inner_map={}),
                                                                                 serial_id=1)]),
                                    value=True))

L1147.define(var='listguard',
              value=builtin.TypeGuard(sample_instance=()))

L2081._add_result(actor=L2077,
                   result=L2083)

L2084._add_result(actor=L2077,
                   result=L1571)

L2087._add_result(actor=L2077,
                   result=L1336)

L2090._add_result(actor=L2077,
                   result=L1349)

L2092._add_result(actor=L2077,
                   result=L1044)

L2094._add_result(actor=L2077,
                   result=L808)

L2096._add_result(actor=L2077,
                   result=L2098)

L2101._add_result(actor=L2077,
                   result=L1371)

L2104._add_result(actor=L2077,
                   result=L1364)

L2108._add_result(actor=L2077,
                   result=L2077)

L2117.define(var='question',
              value=L2115)

L642.define(var='mailbox',
             value=L640)

L642.define(var='inbox',
             value=builtin.Box(initial_value=builtin.List(elements=(L645,))))

L642.define(var='sender',
             value=actors.Actor(env=envs.Env(parent=L642),
                                script=L630))

L170.define(var='guessernode',
             value=L168)

L170.define(var='animal',
             value=builtin.String(str='fraidycat'))

L0
root = L0
