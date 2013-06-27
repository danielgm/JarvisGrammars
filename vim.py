#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

"""
    This module is a simple example of Dragonfly use.

"""

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text, Alternative, IntegerRef, RuleRef, Function, Repetition)


esc = Key('escape')

grammar_context = AppContext(executable='vim')
grammar = Grammar('vim', context=grammar_context)

class LetterRule(MappingRule):
	exported = True
	mapping = {
			'alpha': Key('a', static=True),
			'bravo': Key('b', static=True),
			'charlie': Key('c', static=True),
			'dixie': Key('d', static=True),
			'echo': Key('e', static=True),
			'foxtrot': Key('f', static=True),
			'golf': Key('g', static=True),
			'hotel': Key('h', static=True),
			'india': Key('i', static=True),
			'juliet': Key('j', static=True),
			'kilo': Key('k', static=True),
			'lima': Key('l', static=True),
			'mike': Key('m', static=True),
			'november': Key('n', static=True),
			'oscar': Key('o', static=True),
			'papa': Key('p', static=True),
			'quebec': Key('q', static=True),
			'romeo': Key('r', static=True),
			'sierra': Key('s', static=True),
			'tango': Key('t', static=True),
			'uniform': Key('u', static=True),
			'victor': Key('v', static=True),
			'whiskey': Key('w', static=True),
			'x-ray': Key('x', static=True),
			'yankee': Key('y', static=True),
			'zulu': Key('z', static=True),

			'upper alpha': Key('A', static=True),
			'upper bravo': Key('B', static=True),
			'upper charlie': Key('C', static=True),
			'upper dixie': Key('D', static=True),
			'upper echo': Key('E', static=True),
			'upper foxtrot': Key('F', static=True),
			'upper golf': Key('G', static=True),
			'upper hotel': Key('H', static=True),
			'upper india': Key('I', static=True),
			'upper juliet': Key('J', static=True),
			'upper kilo': Key('K', static=True),
			'upper lima': Key('L', static=True),
			'upper mike': Key('M', static=True),
			'upper november': Key('N', static=True),
			'upper oscar': Key('O', static=True),
			'upper papa': Key('P', static=True),
			'upper quebec': Key('Q', static=True),
			'upper romeo': Key('R', static=True),
			'upper sierra': Key('S', static=True),
			'upper tango': Key('T', static=True),
			'upper uniform': Key('U', static=True),
			'upper victor': Key('V', static=True),
			'upper whiskey': Key('W', static=True),
			'upper x-ray': Key('X', static=True),
			'upper yankee': Key('Y', static=True),
			'upper zulu': Key('Z', static=True),

			'0': Key('0'),
			'1': Key('1'),
			'2': Key('2'),
			'3': Key('3'),
			'4': Key('4'),
			'5': Key('5'),
			'6': Key('6'),
			'7': Key('7'),
			'8': Key('8'),
			'9': Key('9'),

			'space': Key('space'),
			'tab': Key('tab'),

			'ampersand': Key('ampersand'),
			'apostrophe': Key('apostrophe'),
			'asterisk': Key('asterisk'),
			'at': Key('at'),
			'backslash': Key('backslash'),
			'backtick': Key('backtick'),
			'bar': Key('bar'),
			'caret': Key('caret'),
			'colon': Key('colon'),
			'comma': Key('comma'),
			'dollar': Key('dollar'),
			'dot': Key('dot'),
			'double quote': Key('dquote'),
			'equal': Key('equal'),
			'exclamation': Key('exclamation'),
			'hash': Key('hash'),
			'hyphen': Key('hyphen'),
			'minus': Key('minus'),
			'percent': Key('percent'),
			'plus': Key('plus'),
			'question': Key('question'),
			#'semicolon': Key('semicolon'), # Getting Invalid key name: 'semicolon'
			'slash': Key('slash'),
			'[single] quote': Key('squote'),
			'tilde': Key('tilde'),
			'underscore | score': Key('underscore'),

			'angle left': Key('langle'),
			'brace left': Key('lbrace'),
			'bracket left': Key('lbracket'),
			'paren left': Key('lparen'),
			'angle right': Key('rangle'),
			'brace right': Key('rbrace'),
	 		'bracket right': Key('rbracket'),
			'paren right': Key('rparen'),
			}

letter = RuleRef(rule=LetterRule(), name='letter')
letter_sequence = Repetition(letter, min=1, max=32, name='letter_sequence')

# Is there a better way to do this?
def executeLetter(letter):
	letter.execute()

# Is there a better way to do this?
def executeLetterSequence(letter_sequence):
	for letter in letter_sequence:
		letter.execute()

def find(letter, n):
	f = Key('f')
	for i in range(n):
		f.execute()
		letter.execute()


example_rule = MappingRule(
    name='example',
    mapping={
		 'again | repeat | marra thani': esc + Key('dot'),
		 'append': esc + Key('a'),
		 'insert': esc + Key('i'),
		 'replace': esc + Key('R'),
		 'escape | out | done | khalas | finito': esc,

		 'swap <letter>': Key('r') + Function(executeLetter),
		 'spell <letter_sequence>': Function(executeLetterSequence),

		 '[go to] line <n>': esc + Text('%(n)d') + Key('G'),
		 '[go to [the]] first line': esc + Key('1') + Key('G'),
		 '[go to [the]] last line': esc + Key('G'),
		 
		 'find <letter> [<n> times]': esc + Function(find),
		 'find <letter> twice': esc + Function(find) + Function(find),

		 'drop letter': esc + Key('x'),
		 'drop left [letter]': esc + Key('X'),
		 'drop word': esc + Key('d, w'),
		 'drop find <letter> [<n> times]': esc + Key('d') + Function(find),
		 'drop to home': esc + Key('d, caret'),
		 'drop to end': esc + Key('d, dollar'),

		 'search <text> nocase': esc + Text('/%(text)s\c\n'),
		 'search <text>': esc + Text('/%(text)s\n'),
		 'clear search': esc + Text(':let @/ = ""\n'),
		 'previous': esc + Key('N'),
		 'next': esc + Key('n'),

		 'drop line': esc + Text('dd'),
		 'drop <n> lines': esc + Text('d%(n)dd'),
		 'drop line above': esc + Text('kdd'),
		 'drop line below': esc + Text('jdd'),
		 'drop line <n>': esc + Text('%(n)dGdd'),
		 'drop to line <n>': esc + Text(':,%(n)dd\n'),

		 'blank line [below]': esc + Key('o'),
		 'open line [below]': esc + Key('o'),
		 'open line above': esc + Key('O'),

		 'yank line': esc + Key('Y'),
		 'yank word': esc + Key('y, w'),
		 'yank find <letter> [<n> times]': esc + Key('y') + Function(find),
		 'yank find <letter> twice': esc + Key('y') + Function(find) + Function(find),
		 'put [(text | lines)] [after]': esc + Key('p'),
		 'put [(text | lines)] before': esc + Key('P'),

		 'save [file]': esc + Text(':w\n'),

		 'undo | back | oops': esc + Key('u'),
		 'redo': esc + Key('c-r'),

		 'indent [<n> times]': esc + Key('rangle%(n)d, rangle%(n)d'),
		 'outdent [<n> times]': esc + Key('langle:%(n)d, langle:%(nd)d'),
		 'indent block': esc + Key('rangle, i, rbrace'),
		 'outdent block': esc + Key('langle, i, rbrace'),
		},
    extras=[           # Special elements in the specs of the mapping.
						letter,
						letter_sequence,
            Dictation('text'),
            Dictation('text2'),
						IntegerRef('n', 1, 10000),
           ],
		defaults={
					 'n': 1
					 }
    )

grammar.add_rule(example_rule)

grammar.load()
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

