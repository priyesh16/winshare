# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interacting with Git
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key
from aenea import Text
import dragonfly

git_context = aenea.ProxyPlatformContext('linux')
grammar = dragonfly.Grammar('git', context=git_context)

git_mapping = aenea.configuration.make_grammar_commands('git', {
    'git': Text("git"),

    'git amend': Text("git commit --amend") + Key("enter"),
    'switch': Key("a-tab"),
    'chain mode': Text("./mods i2c.js -board sunstreaker.js -ctrl 1 -slave 0x55 -offset 0x0 -run 1 -offsetWidth 16 -mode 0 -dmaChain -packetNo 2 -packetSize 4") + Key("enter"),
    'edit chain': Text("./mods i2c.js -board sunstreaker.js -ctrl 1 -slave 0x55 -offset 0x0 -run 1 -offsetWidth 16 -mode 0 -dmaChain -packetNo 2 -packetSize 4"),
    
    'terminator left': Key("a-left"),
    'terminator right': Key("a-right"),
    'terminator up': Key("a-up"),
    'terminator down': Key("a-down"),
    'push mods': Text("adb push runspace/mods /home/mods") + Key("enter"),
    'push javascript': Text("adb push runspace/i2c.js /home/i2c.js") + Key("enter"),
    'compile': Text("make build_all -j12") + Key("enter"),
    
    'sublime find': Key("c-p"),
    'sublime escape': Key("esc"),
    'git commit': Text("git commit") + Key("enter"),
    'git pull': Text("git pull") + Key("enter"),
    'git branches': Text("git branch -l") + Key("enter"),
    'git status': Text("git status") + Key("enter"),
    'git stat': Text("git show --stat") + Key("enter"),
    'git log': Text("git log") + Key("enter"),
    'git push': Text("git push") + Key("enter"),
    'git diff': Text("git diff") + Key("enter"),

    'left': Key("left"),
    'right': Key("right"),
    'up': Key("up"),
    'down': Key("down"),
    'enter': Key("enter"),
    'cancel': Key("c-c"),
    'page up': Key("up"),
    'page down': Key("down"),
    

    'undo': Key("c-z"),
    'redo': Key("c-y"),
    'cut': Key("c-x"),
    'copy': Key("c-c"),
    'paste': Key("c-v"),
    'find': Key("c-f"),
    'search': Key("c-f"),
    'reverse search': Key("c-r"),
    'replace': Key("c-h"),
    'save': Key("c-s"),

    'shell reload': Key("c-c") + Text("zsh") + Key("enter");,
    
    'windows copy': Key("c-c"),
    'windows paste': Key("c-v"),
    'linux copy': Key("c-insert"),
    'linux paste': Key("c-v"),

    'line delete' : Key("s-down, delete"), 
    'line select' : Key("s-down, c-c"), 
         
    


    'alpha': Text("a"),
    'bravo': Text("b"),
    'charlie': Text("c"),
    'delta': Text("d"),
    'echo': Text("e"),
    'foxtrot': Text("f"),
    'golf': Text("g"),
    'hotel': Text("h"),
    'india': Text("i"),
    'juliett': Text("j"),
    'kilo': Text("k"),
    'lima': Text("l"),
    'mike': Text("m"),
    'november': Text("n"),
    'oscar': Text("o"),
    'papa': Text("p"),
    'quebec': Text("q"),
    'romeo': Text("r"),
    'sierra': Text("s"),
    'tango': Text("t"),
    'uniform': Text("u"),
    'victor': Text("v"),
    'whiskey': Text("w"),
    'x ray': Text("x"),
    'yankee': Text("y"),
    'zulu': Text("z"),
    

    # https://github.com/tgrosinger/dotfiles/blob/master/.gitconfig#L15
    'git hist': Text("git hist") + Key("enter"),

    # Incomplete Commands
    'git add': Text("git add "),
    'git checkout': Text("git checkout "),
    'git interactive rebase': Text("git rebase -i "),
    'git rebase': Text("git rebase "),
    'git push to': Text("git push"),

    # SVN Commands
    'git trunk': Text("git checkout trunk-svn") + Key("enter"),
    'git SVN pull': Text("git svn rebase") + Key("enter"),
    'git SVN rebase interactive': Text("git rebase -i trunk-svn") + Key("enter"),
    'git SVN rebase': Text("git rebase trunk-svn") + Key("enter"),
})


class Mapping(dragonfly.MappingRule):
    mapping = git_mapping

grammar.add_rule(Mapping())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None