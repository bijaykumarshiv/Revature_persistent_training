Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5>6 and 3<7
False
5>3
True
5>6 or 3<7
True
not 6
False
not 0
True
not5
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    not5
NameError: name 'not5' is not defined
not 4
False
7&9
1
7|9
15
7^9
14
5<<3
40
5<<4
80
5>>2
1
5>>>2
SyntaxError: invalid syntax
5<<<2
SyntaxError: invalid syntax
num1 = 10
type(num)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(num)
NameError: name 'num' is not defined. Did you mean: 'num1'?
type(num1)
<class 'int'>
num1 is int
False
5 is int
False
type(5) is int
True

print('hi')
hi
'hi'
'hi'
print('hi'+"hello")
hihello
print(num1+10)
20
print(hi+'hii')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(hi+'hii')
NameError: name 'hi' is not defined
print('hi'+'10')
hi10
print('sum : '+ '\n' ,num1+10)
sum : 
 20
input ()
input()
'input()'
input()
5
'5'
input('Enter anumber')
Enter anumber6
'6'
>>> int(input('Enter a num'))
Enter a num5
5
>>> boolean(input('Enter a num'))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    boolean(input('Enter a num'))
NameError: name 'boolean' is not defined
>>> bool(input('Enter a num'))
Enter a num4
True
>>> Truebool(input('Enter a num'))
... Enter a num4
... 
SyntaxError: multiple statements found while compiling a single statement
>>> bool(input('Enter a num'))
... Enter a num
SyntaxError: multiple statements found while compiling a single statement
>>> bool(input('Enter a num'))
... Enter a num
SyntaxError: multiple statements found while compiling a single statement
>>> ""
''
>>> bool(input('Enter a num'))
... Enter a num
SyntaxError: multiple statements found while compiling a single statement
>>> bool(input('enter a  number'))
enter a  number
False
>>> 'hi'
'hi'
>>> "hi"
'hi'
>>> "Bijay's house"
"Bijay's house"
>>> 'bijay's house'
SyntaxError: unterminated string literal (detected at line 1)
>>> 'bijay"s house'
'bijay"s house'
