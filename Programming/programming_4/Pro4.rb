#!/usr/bin/ruby
a = "612251df69aa19ac0054cc284bd0daa840abd1";
b = "2361059912f229de5f03ed5c238fa8dd22f2ac";
c = (a.to_i(16) ^ b.to_i(16)).to_s(16);
print c;