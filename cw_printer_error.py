##In a factory a printer prints labels for boxes.
##For one kind of boxes the printer has to use colors which,
##for the sake of simplicity, are named with letters from a to m.
##
##The colors used by the printer are recorded in a control string.
##For example a "good" control string would be aaabbbbhaijjjm meaning
##that the printer used three times color a, four times color b,
##then one time color a...
##
##Sometimes there are problems: lack of colors, technical malfunction
##and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.
##
##You have to write a function printer_error which given a string
##will output the error rate of the printer as a string representing
##a rational whose numerator is the number of errors and the denominator the
##length of the control string. Don't reduce this fraction to a simpler
##expression.
##
##The string has a length greater or equal to one and contains only
##letters from ato z.


def printer_error(s):
    # your code
    den=len(s)
    num=0
    for i in s:
        if i not in "abcdefghijklm":
            num+=1
    return str(num)+'/'+str(den)


st="aaaxbbbbyyhwawiwjjjwwm"
print printer_error(st)   # => "8/22"
