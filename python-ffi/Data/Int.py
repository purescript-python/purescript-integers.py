import math


def fromNumberImpl(just):
    def nothing_(nothing):
        def n_(n):
            if isinstance(n, int):
                return just(n)
            else:
                return nothing
        return n_
    return nothing_


# exports.fromNumberImpl = function (just) {
#   return function (nothing) {
#     return function (n) {
#       /* jshint bitwise: false */
#       return (n | 0) === n ? just(n) : nothing;
#     };
#   };
# };


def toNumber(n):
    return n


def fromStringAsImpl(just):
    def nothing_(nothing):
        def radix_(radix):
            def s_(s):
                try:
                    return just(int(s, radix))
                except ValueError as e:
                    return nothing
            return s_
        return radix_
    return nothing_


# exports.fromStringAsImpl = function (just) {
#   return function (nothing) {
#     return function (radix) {
#       var digits;
#       if (radix < 11) {
#         digits = "[0-" + (radix - 1).toString() + "]";
#       } else if (radix === 11) {
#         digits = "[0-9a]";
#       } else {
#         digits = "[0-9a-" + String.fromCharCode(86 + radix) + "]";
#       }
#       var pattern = new RegExp("^[\\+\\-]?" + digits + "+$", "i");

#       return function (s) {
#         /* jshint bitwise: false */
#         if (pattern.test(s)) {
#           var i = parseInt(s, radix);
#           return (i | 0) === i ? just(i) : nothing;
#         } else {
#           return nothing;
#         }
#       };
#     };
#   };
# };


def toStringAs(radix):
    def ap(i):
        BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while i:
            result+=BS[i%radix]
            i//= radix
        return result[::-1] or "0"
    return ap


# exports.toStringAs = function (radix) {
#   return function (i) {
#     return i.toString(radix);
#   };
# };

quot = lambda x: lambda y: x / y

# exports.quot = function (x) {
#   return function (y) {
#     /* jshint bitwise: false */
#     return x / y | 0;
#   };
# };

rem = lambda x: lambda y: x % y

# exports.rem = function (x) {
#   return function (y) {
#     return x % y;
#   };
# };


pow = lambda x: lambda y: math.pow(x, y)

# exports.pow = function (x) {
#   return function (y) {
#     /* jshint bitwise: false */
#     return Math.pow(x,y) | 0;
#   };
# };
